 

#FIXME: Binding for uniform buffer block: Need to look at binding= line

import traceback
from math2801 import *
import ctypes
import array
import re
import inspect
import os.path
import typing

import gl
from glconstants import *
from gl import *

__all__ = ["ShaderError", "UniformTypeMismatchError",
    "ShaderStageMismatchError", "NoSuchUniformError",
    "UninitializedUniformError", "NoActiveProgramError",
    "Program"
]

class _ShaderData:
    def __init__(self,filename,data):
        self.filename=filename
        self.data=data
        
class ShaderError(RuntimeError):
    pass
    
class UniformTypeMismatchError(ShaderError):
    pass
    
class ShaderStageMismatchError(ShaderError):
    pass
    
class NoSuchUniformError(ShaderError):
    pass
    
class UninitializedUniformError(ShaderError):
    pass

class NoActiveProgramError(ShaderError):
    pass
     
    
def _shaderError(filename, line, msg):
    m = "Shader error: File {}, line {}: {}".format(filename,line,msg)
    # ~ print(m)
    raise ShaderError(m)


def _stringRangeReplace(st,s,e):
    return st[:s]+(' '*(e-s))+st[e:]
    
    
class _Token:
    def __init__(self,sym,lexeme,line,index):
        self.sym=sym
        self.lexeme=lexeme
        self.line=line
        self.startIndex=index
        self.endIndex = self.startIndex + len(lexeme)
    def __str__(self):
        return "[Token: {} {} {}]".format(self.sym,self.line,self.lexeme)
    def __repr__(self):
        return str(self)
        
class _Terminal:
    def __init__(self,s,rx):
        self.sym = s
        self.rex = rx
  
_terminals = [
    ( "VERSION",        re.compile("#version\\b")                       ),
    ( "IN",             re.compile("\\bin\\b")                          ),
    ( "OUT",            re.compile("\\bout\\b")                         ),
    ( "SEMI",           re.compile(";")                                 ),
    ( "NUM",            re.compile("\\d+")                              ),
    ( "WHITESPACE",     re.compile("\\s+")                              ),
    ( "COMMENT",        re.compile("/[*](.|\n)*?\\*/|//[^\n]*\n")       ),
    ( "LAYOUT",         re.compile("\\blayout\\b")                      ),
    ( "UNIFORM",        re.compile("\\buniform\\b")                     ),
    ( "BUFFER",         re.compile("\\bbuffer\\b")                      ),
    ( "LP",             re.compile("[(]")                               ),
    ( "RP",             re.compile("[)]")                               ),
    ( "LOCATION",       re.compile("\\blocation\\b")                    ),
    ( "BINDING",        re.compile("\\bbinding\\b")                     ),
    ( "EQ",             re.compile("=")                                 ),
    ( "SAMPLERTYPE",    re.compile("\\b[iu]?(sampler|image)"  
                        "("
                            "[123]D(Array)?|"
                            "Cube(Array)?|"
                            "2DRect"
                            "[12]DShadow|"
                            "2DRectShadow|"
                            "[12]DArray(Shadow)?|"
                            "Buffer|"
                            "2DMS(Array)?|"
                        ")\\b")                                         ),
    #must be after all keywords
    ( "ID",             re.compile("\\b[A-Za-z_]\\w*\\b")               ),
    #must be last
    ( "ANYTHING",       re.compile(".")                                 )
]     

 
_uboBuffer=None
_uboBackingMemory=None
_uboBackingAddress=None
_bufferDirty=True
_hookAdded=False
_SHADER_FILE_MAGIC_NUMBER = "31337"
_UNIFORM_FILE_MAGIC_NUMBER = "31338"
 

# 0(123): Text
# 0:123(456): Text
# 0:123: Text
_errorRex = re.compile( 
    "^\\b"
    f"({_SHADER_FILE_MAGIC_NUMBER}|{_UNIFORM_FILE_MAGIC_NUMBER})" 
    "[(:]"
    r"(\d+)"
)
   

class _ShaderVariable:
    def __init__(self,*, type,name,binding,bindingClass,location,sourceStartChar,sourceEndChar,
                        layoutStartChar,layoutEndChar,lineNumber):
        self.type = type
        self.name=name
        self.binding=binding
        self.bindingClass=bindingClass
        self.location=location
        self.sourceStartChar=sourceStartChar
        self.sourceEndChar=sourceEndChar
        self.layoutStartChar=layoutStartChar
        self.layoutEndChar=layoutEndChar
        self.lineNumber=lineNumber
        self.matched=False



class _UniformSetter:
    def __init__(self, name, offset, location, numBytes, typ, arraySize):
        self.name = name
        self.offset = offset
        self.location = location
        self.numBytes = numBytes
        self.type = typ
        self.arraySize = arraySize
        self.hasBeenSet = False
        self.hasBeenWarned = False
        
        self.setDict = {
            float: lambda x: self.setFloat(x),
            int: lambda x: self.setInt(x),
            vec2: lambda x: self.setVec2(x),
            ivec2: lambda x: self.setIVec2(x),
            vec3: lambda x: self.setVec3(x),
            vec4: lambda x: self.setVec4(x),
            mat2: lambda x: self.setMat2(x),
            mat3: lambda x: self.setMat3(x),
            mat4: lambda x: self.setMat4(x),
            list: lambda x: self.setList(x),
            tuple: lambda x: self.setList(x)
        }
        self.listDict = {
            int: lambda x: self.setListFloat(x),        #we only support lists of floats
            float: lambda x: self.setListFloat(x),
            vec2: lambda x: self.setListVec2(x),
            vec3: lambda x: self.setListVec3(x),
            vec4: lambda x: self.setListVec4(x),
            mat4: lambda x: self.setListMat4(x)
        }
            
        
    def getTypeName(self):
        assert 0
     
    def listToBytes(self,L,expectedType,paddingSize):
        tmp = bytearray()
        P=bytearray(paddingSize)
        for item in L:
            if type(item) != expectedType:
                raise RuntimeError("Bad object in list: It's of type "+str(type(item))+" but it should have been "+str(expectedType) )
            tmp += item.tobytes()
            tmp += P
        return tmp
        
    def set(self,f):
        t = type(f)
        if t not in self.setDict:
             raise RuntimeError("Bad type ({}) for setting uniform".format(t))
        else:
            self.setDict[t](f)
            
    def setFloat(self,f: float): 
        raise UniformTypeMismatchError("Bad type when setting uniform "+self.name+": got float; expected "+self.getTypeName() )
    
    def setInt(self,f: float): 
        raise UniformTypeMismatchError("Bad type when setting uniform "+self.name+": got int; expected "+self.getTypeName() )
    
    def setVec2(self,f: vec2): 
        raise UniformTypeMismatchError("Bad type when setting uniform "+self.name+": got vec2; expected "+self.getTypeName() )

    def setIVec2(self,f: ivec2): 
        raise UniformTypeMismatchError("Bad type when setting uniform "+self.name+": got vec2; expected "+self.getTypeName() )
    
    def setVec3(self,f: vec3): 
        raise UniformTypeMismatchError("Bad type when setting uniform "+self.name+": got vec3; expected "+self.getTypeName() )
    
    def setVec4(self,f: vec4): 
        raise UniformTypeMismatchError("Bad type when setting uniform "+self.name+": got vec4; expected "+self.getTypeName() )
    
    def setMat2(self,f: mat2): 
        raise UniformTypeMismatchError("Bad type when setting uniform "+self.name+": got mat2; expected "+self.getTypeName() )

    def setMat3(self,f: mat3): 
        raise UniformTypeMismatchError("Bad type when setting uniform "+self.name+": got mat3; expected "+self.getTypeName() )

    def setMat4(self,f: mat4): 
        raise UniformTypeMismatchError("Bad type when setting uniform "+self.name+": got mat4; expected "+self.getTypeName() )
    
    def setList(self,L):
        if len(L) == 0 :
            raise RuntimeError("Empty list")
        t = type(L[0])
        if t not in self.listDict:
            raise RuntimeError("Bad type in list for setting uniform")
        self.listDict[t](L)
            
    def setListFloat(self, L):
        raise UniformTypeMismatchError("Bad type when setting uniform "+self.name+": got list of float; expected "+self.getTypeName() )

    def setListVec2(self, L):
        raise UniformTypeMismatchError("Bad type when setting uniform "+self.name+": got list of float; expected "+self.getTypeName() )

    def setListVec3(self, L):
        raise UniformTypeMismatchError("Bad type when setting uniform "+self.name+": got list of float; expected "+self.getTypeName() )

    def setListVec4(self, L):
        raise UniformTypeMismatchError("Bad type when setting uniform "+self.name+": got list of float; expected "+self.getTypeName() )

    def setListMat4(self, L):
        raise UniformTypeMismatchError("Bad type when setting uniform "+self.name+": got list of float; expected "+self.getTypeName() )

    def sizeCheck(self,v):
        if len(v) != self.arraySize:
            raise UniformTypeMismatchError("Array size mismatch when setting uniform "+self.name+": List has "+str(len(v))+" elements but shader expects "+str(self.arraySize)+" elements")
        
    def doSet(self, byteBuff):
        global _bufferDirty
        assert type(byteBuff) == bytes or type(byteBuff) == bytearray
        byteSize = len(byteBuff)
        if  self.numBytes != byteSize :
            raise RuntimeError("Expected "+str(self.numBytes)+" bytes but got "+str(byteSize)+" bytes for "+name)
        assert self.offset != -1
        dst = ctypes.c_void_p( _uboBackingAddress + self.offset )
        ctypes.memmove( dst, bytes(byteBuff), self.numBytes )
        _bufferDirty = True
        self.hasBeenSet=True
#end _UniformSetter class



class _FloatSetter(_UniformSetter):
    def __init__(self,name,offset,location,typ,size):
        super().__init__(name,offset,location,4,typ,size)

    def getTypeName(self):
        return "float"
    
    def setFloat(self,f):
        if self.location != -1:
            glUniform1f( self.location, f )
            self.hasBeenSet=True
        else:
            self.doSet( array.array("f",[f]).tobytes() )
    def setInt(self,f):
        self.setFloat(float(f))

class _IntSetter(_UniformSetter):
    def __init__(self,name,offset,location,typ,size):
        super().__init__(name,offset,location,4,typ,size)

    def getTypeName(self):
        return "int"
    
    def setInt(self,f):
        if self.location != -1:
            print(__file__,": setInt:",self.name,"to",f)
            glUniform1i( self.location, f )
            self.hasBeenSet=True
        else:
            self.doSet( array.array("i",[f]).tobytes()  )
    def setFloat(self,f):
        self.setInt(int(f))

class _Vec2Setter(_UniformSetter):
    def __init__(self,name,offset,location,typ,size):
        super().__init__(name,offset,location,8,typ,size)

    def getTypeName(self):
        return "vec2"
    
    def setVec2(self,f):
        if self.location != -1:
            glUniform2f( self.location, f.x, f.y )
            self.hasBeenSet=True
        else:
            self.doSet( f.tobytes() )

class _IVec2Setter(_UniformSetter):
    def __init__(self,name,offset,location,typ,size):
        super().__init__(name,offset,location,8,typ,size)

    def getTypeName(self):
        return "ivec2"
    
    def setIVec2(self,f):
        if self.location != -1:
            glUniform2i( self.location, f.x, f.y )
            self.hasBeenSet=True
        else:
            self.doSet( f.tobytes() )


class _Vec3Setter(_UniformSetter):
    def __init__(self,name,offset,location,typ,size):
        super().__init__(name,offset,location,12,typ,size)

    def getTypeName(self):
        return "vec3"
    
    def setVec3(self,f):
        if self.location != -1:
            glUniform3f( self.location, f.x, f.y, f.z )
            self.hasBeenSet=True
        else:
            self.doSet( f.tobytes() )

class _Vec4Setter(_UniformSetter):
    def __init__(self,name,offset,location,typ,size):
        super().__init__(name,offset,location,16,typ,size)

    def getTypeName(self):
        return "vec4"
    
    def setVec4(self,f):
        if self.location != -1:
            glUniform3f( self.location, f.x, f.y, f.z, f.w )
            self.hasBeenSet=True
        else:
            self.doSet( f.tobytes() )
            
class _Mat2Setter(_UniformSetter):
    def __init__(self,name,offset,location,typ,size):
        super().__init__(name,offset,location,2*16,typ,size)        #2*16 because one vec4 per row

    def getTypeName(self):
        return "mat2"
    
    def setMat2(self,f):
        if self.location != -1:
            glUniformMatrix2fv( self.location, 1, True, f.tobytes() )
            self.hasBeenSet=True
        else:
            self.doSet( f.tobytes() )

class _Mat3Setter(_UniformSetter):
    def __init__(self,name,offset,location,typ,size):
        super().__init__(name,offset,location,3*16,typ,size)        #3*16 because one vec4 per row

    def getTypeName(self):
        return "mat3"
    
    def setMat3(self,f):
        if self.location != -1:
            glUniformMatrix3fv( self.location, 1, True, f.tobytes() )
            self.hasBeenSet=True
        else:
            self.doSet( f.tobytes() )

class _Mat4Setter(_UniformSetter):
    def __init__(self,name,offset,location,typ,size):
        super().__init__(name,offset,location,4*16,typ,size)        

    def getTypeName(self):
        return "mat4"
    
    def setMat4(self,f):
        if self.location != -1:
            glUniformMatrix4fv( self.location, 1, True, f.tobytes() )
            self.hasBeenSet=True
        else:
            self.doSet( f.tobytes() )

class _Mat4ArraySetter(_UniformSetter):
    def __init__(self,name,offset,location,typ,size):
        super().__init__(name,offset,location,size*4*16,typ,size)        

    def getTypeName(self):
        return "list of mat4"
    
    def setListMat4(self,v):
        self.sizeCheck(v)
        tmp = self.listToBytes(v,mat4,0)
        if self.location != -1 :
            glUniformMatrix4fv( self.location, self.arraySize, True, tmp )
            self.hasBeenSet=True
        else:
            self.doSet( tmp )

class _Vec4ArraySetter(_UniformSetter):
    def __init__(self,name,offset,location,typ,size):
        super().__init__(name,offset,location,size*16,typ,size)       

    def getTypeName(self):
        return "list of vec4"

    def setListVec4(self,v):
        self.sizeCheck(v)
        tmp = self.listToBytes(v,vec4,0)
        if self.location != -1:
            glUniform4fv( self.location, self.arraySize, tmp )
            self.hasBeenSet=True;
        else:
            self.doSet( tmp )

class _Vec3ArraySetter(_UniformSetter):
    def __init__(self,name,offset,location,typ,size):
        super().__init__(name,offset,location,size*16,typ,size)      

    def getTypeName(self):
        return "list of vec3"

    def setListVec3(self,v):
        self.sizeCheck(v)
        if self.location != -1:
            tmp = self.listToBytes(v,vec3,0)
            glUniform3fv( self.location, self.arraySize, tmp )
            self.hasBeenSet=True;
        else:
            tmp = self.listToBytes(v,vec3,4)
            self.doSet( tmp )
            
class _Vec2ArraySetter(_UniformSetter):
    def __init__(self,name,offset,location,typ,size):
        super().__init__(name,offset,location,size*16,typ,size)       

    def getTypeName(self):
        return "list of vec2"

    def setListVec2(self,v):
        self.sizeCheck(v)
        if self.location != -1:
            tmp = self.listToBytes(v,vec2,0)
            glUniform2fv( self.location, self.arraySize, tmp )
            self.hasBeenSet=True
        else:
            tmp = self.listToBytes(v,vec2,8)
            self.doSet( tmp )

class _FloatArraySetter(_UniformSetter):
    def __init__(self,name,offset,location,typ,size):
        super().__init__(name,offset,location,size*16,typ,size)       

    def getTypeName(self):
        return "list of floats"

    def setListFloat(self,v):
        self.sizeCheck(v)
        if self.location != -1:
            tmp = array.array("f",v)
            glUniform2fv( self.location, self.arraySize, tmp.tobytes() )
            self.hasBeenSet=True
        else:
            tmp = array.array("f",[0]*self.arraySize*4)
            j=0
            for x in v:
               tmp[j] = x
               j+=4
            self.doSet( tmp.tobytes() )

class _Tokenizer:
    
    def __init__(self,inp,filename):
        assert inp != None
        self.input = inp
        self.filename = filename
        self.line = 1
        self.idx=0
        
    def next(self):
        if self.idx >= len(self.input):
            return _Token("$","",self.line,len(self.input))
            
        for i in range(len(_terminals)):
            sym,rex = _terminals[i]
            M = rex.match( self.input, self.idx )
            if M:
                T = _Token( sym, M.group(0), self.line, self.idx )
                for c in T.lexeme:
                    if c == '\n':
                        self.line += 1
                self.idx += len(T.lexeme)
                if sym == "WHITESPACE" or  sym == "COMMENT":
                    return self.next()
                else:
                    return T
        _shaderError(self.filename, self.line, "Cannot tokenize")
    
    def expect(self,sym):
        T = self.next()
        if  T.sym == sym:
            return T
        _shaderError(self.filename,T.line, "Expected to find '(' but found '"+T.lexeme+"'")


def _getLog(sourceFile,uniformFile,msg,func,identifier):
    blob = bytearray(4096)
    tmp = array.array("I",[0])
    func( identifier, len(blob), tmp, blob )
    length = tmp[0]
    if length > 0 :
        blobstr = blob[:length].decode()
    
    if length > 0:
        lines = blobstr.split("\n")
        for i in range(len(lines)):
            
            M = _errorRex.search(lines[i])
            if M:
                filenum = M.group(1)
                
                if  filenum == "0" or filenum == _SHADER_FILE_MAGIC_NUMBER  or  filenum == _UNIFORM_FILE_MAGIC_NUMBER :
                    linestring = M.group(2)
                    if filenum == "0" or filenum == _SHADER_FILE_MAGIC_NUMBER:
                        F = sourceFile
                    else:
                        F = uniformFile
                        
                    lines[i] = "{} File '{}', line {}: {}".format(
                        lines[i][0:M.start()],
                        F,
                        linestring,
                        lines[i][M.end(1):]
                    )
                    lines[i] = lines[i].strip()
                
        print(msg)
        for l in lines:
            print(l)

        return "\n".join(lines)
        
    return ""

def _readFile(fname, missingOK=False):

    possibilities=[]
    
    for c in [  os.path.abspath(fname),
                os.path.abspath(os.path.join(os.path.dirname(__file__),"shaders",fname)),
                os.path.abspath(os.path.join(os.path.dirname(__file__),fname))
    ]:
        if c not in possibilities:
            possibilities.append(c)
            
    disfavoredpossibilities=[]
    i = fname.rfind(".")
    if i != -1:
        suffix = fname[i:]
        for p in possibilities:
            disfavoredpossibilities.append( p+suffix)
            
    found=[]
    shaderdata = None
    for f in possibilities:
        if not os.access(f,os.F_OK):
            d = os.path.dirname(f)
            if d == "":
                d="."
            b = os.path.basename(f)
            if os.access(d,os.F_OK):
                for x in os.listdir(d):
                    if x.lower() == b.lower():
                        f=os.path.join(d,x)
                        break
        if os.access(f,os.F_OK):
            found.append(f)
            with open(f) as fp:
                shaderdata = fp.read()
                
    extramessage=[]
    for f in disfavoredpossibilities:
        if os.access(f,os.F_OK):
            extramessage.append("This filename looks suspicious: "+f)
    extramessage = "\n".join(extramessage)
    
    if len(found) > 1:
        raise RuntimeError("Found {} in several places; I don't know which one to use:\n{}".format(
            fname, "\n".join(found)))
      
    if shaderdata != None:
        return shaderdata
        
    if missingOK:
        return ""

    raise RuntimeError("Cannot find {} in any of these locations:\n{}\n{}".format(
            fname, "\n".join(possibilities),extramessage))
        



def _compile(S,shaderType,prog):
 
    shaderdata = S.data
    
    if len(shaderdata) == 0:
        _shaderError(S.filename,0,"File is empty!")
        
    tok = _Tokenizer(shaderdata,S.filename)
    T = tok.next()
    if  T.sym != "VERSION":
        _shaderError(S.filename,1,"Expected to find #version specification as first line of shader")
    
    lineEnd = shaderdata.find("\n")
    if lineEnd == -1:
        _shaderError(S.filename,1,"No newline in shader file")
    
    uniformdata = _readFile("uniforms.txt",True)
    
    
    shaderdata = ( 
            shaderdata[0:lineEnd+1] + "\n"
            "//begin uniforms.txt\n"
            "#line 1 "+_UNIFORM_FILE_MAGIC_NUMBER+"\n" + 
            uniformdata + "\n"
            "//end uniforms.txt\n"
            "#line 2 "+_SHADER_FILE_MAGIC_NUMBER+"\n" +
            shaderdata[lineEnd+1:]
    )
    
    if shaderType == GL_VERTEX_SHADER:
        shaderTypeString = "vertex shader"
    elif shaderType == GL_FRAGMENT_SHADER:
        shaderTypeString = "fragment shader"
    elif shaderType == GL_GEOMETRY_SHADER:
        shaderTypeString = "geometry shader"
    elif shaderType == GL_TESS_CONTROL_SHADER:
        shaderTypeString = "tesselation control shader"
    elif shaderType == GL_TESS_EVALUATION_SHADER:
        shaderTypeString = "tesselation evaluation shader"
    elif shaderType == GL_COMPUTE_SHADER:
        shaderTypeString = "compute shader"
    else:
        shaderTypeString = "unknown type of shader"
    
    s = glCreateShader(shaderType)
    
    
    shaderdata = shaderdata.replace("\r\n","\n").replace("\r","\n")
    
    if 0:
        print("SHADER SOURCE:")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~")
        xx = shaderdata.split()
        for iii,ll in enumerate(shaderdata.split("\n")):
            print("{:4d} - {}".format(iii+1,ll))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    
    glShaderSource( s, 1, [shaderdata], None )
    glCompileShader(s)
    logtxt = _getLog( S.filename, "uniforms.txt", "Compiling "+shaderTypeString+" "+S.filename+": ",
        glGetShaderInfoLog, s)
        
    if uniformdata != "" and not uniformdata.strip().endswith(";"):
        logtxt += "\nWARNING: uniform declaration does not end with a semicolon"
 
    tmp = array.array("I",[0])
    glGetShaderiv( s, GL_COMPILE_STATUS, tmp )
    if not tmp[0]:
        raise ShaderError(f"Cannot compile!\n{logtxt}")
    glAttachShader(prog,s)
    glDeleteShader(s)



def _queryUniforms( prog, uniforms, privateOnly):
    tmp = array.array("I",[0])
    glGetProgramiv(prog,GL_ACTIVE_UNIFORMS,tmp)
    numuniforms = tmp[0]
    if numuniforms > 0:
        uniformsToQuery = array.array("I",list(range(numuniforms)))
        offsets = array.array("i",[0]*numuniforms)
        sizes = array.array("i",[0]*numuniforms)
        types = array.array("I",[0]*numuniforms)
        blocks = array.array("I",[0]*numuniforms)
        glGetActiveUniformsiv(prog, numuniforms, uniformsToQuery, GL_UNIFORM_OFFSET, offsets )
        glGetActiveUniformsiv(prog, numuniforms, uniformsToQuery, GL_UNIFORM_SIZE, sizes)
        glGetActiveUniformsiv(prog, numuniforms, uniformsToQuery, GL_UNIFORM_TYPE, types)
        glGetActiveUniformsiv(prog, numuniforms, uniformsToQuery, GL_UNIFORM_BLOCK_INDEX, blocks)
    
    nameBytes = bytearray(256)
    totalUniformBytes = 0
    for i in range(numuniforms):

        glGetActiveUniformName(prog, i, len(nameBytes), tmp, nameBytes )
        nameLen = tmp[0]
        name = nameBytes[0:nameLen].decode()

        # ~ print("i=",i)
        # ~ print("name=",name)
        # ~ print("blocks[i]=",blocks[i])
        if blocks[i] == -1 or blocks[i] == 0xffffffff or blocks[i] == 0xffffffffffffffff:
            blockbinding = -1
        else:
            glGetActiveUniformBlockiv( prog, blocks[i], GL_UNIFORM_BLOCK_BINDING, tmp )
            blockbinding = tmp[0]
        # ~ print("binding=",blockbinding)
        
        if blockbinding != 0 and blockbinding != -1:
            print("Info: Skipping uniform",name,"in uniform bound at",blockbinding)
            continue
            
        if offsets[i] == -1 or offsets[i] == 0xffffffff or offsets[i] == 0xffffffffffffffff:
            isPrivate = True
        else:
            isPrivate = False
            
        if privateOnly  and  not isPrivate:
            continue
        if not privateOnly  and  isPrivate:
            continue
        
        
        if False:
            print("Found (private={}) uniform {}".format(isPrivate,name))
        
        
        if isPrivate:
            location = glGetUniformLocation(prog,name)
        else:
            location = -1
        
        if sizes[i] == 1:
            if   types[i] == GL_FLOAT_VEC4:                     u = _Vec4Setter (name, offsets[i], location,  types[i], sizes[i] )
            elif types[i] == GL_FLOAT_VEC3:                     u = _Vec3Setter (name, offsets[i], location,  types[i], sizes[i] )
            elif types[i] == GL_FLOAT_VEC2:                     u = _Vec2Setter (name, offsets[i], location,  types[i], sizes[i] )
            elif types[i] == GL_INT_VEC2:                       u = _IVec2Setter (name, offsets[i], location,  types[i], sizes[i] )
            elif types[i] == GL_FLOAT_MAT4:                     u = _Mat4Setter (name, offsets[i], location,  types[i], sizes[i] )
            elif types[i] == GL_FLOAT_MAT3:                     u = _Mat3Setter (name, offsets[i], location,  types[i], sizes[i] )
            elif types[i] == GL_FLOAT_MAT2:                     u = _Mat2Setter (name, offsets[i], location,  types[i], sizes[i] )
            elif types[i] == GL_FLOAT:                          u = _FloatSetter(name, offsets[i], location,  types[i], sizes[i] )
            elif types[i] == GL_INT:                            u = _IntSetter  (name, offsets[i], location,  types[i], sizes[i] )
            elif types[i] == GL_UNSIGNED_INT:                   u = _UintSetter (name, offsets[i], location,  types[i], sizes[i] )
            elif types[i] == GL_SAMPLER_1D:                     u = _IntSetter  (name, offsets[i], location,  types[i], sizes[i] )
            elif types[i] == GL_SAMPLER_1D_ARRAY:               u = _IntSetter  (name, offsets[i], location,  types[i], sizes[i] )
            elif types[i] == GL_SAMPLER_2D:                     u = _IntSetter  (name, offsets[i], location,  types[i], sizes[i] )
            elif types[i] == GL_SAMPLER_2D_ARRAY:               u = _IntSetter  (name, offsets[i], location,  types[i], sizes[i] )
            elif types[i] == GL_SAMPLER_3D:                     u = _IntSetter  (name, offsets[i], location,  types[i], sizes[i] )
            elif types[i] == GL_SAMPLER_CUBE:                   u = _IntSetter  (name, offsets[i], location,  types[i], sizes[i] )
            elif types[i] == GL_INT_SAMPLER_1D:                 u = _IntSetter  (name, offsets[i], location,  types[i], sizes[i] )
            elif types[i] == GL_INT_SAMPLER_1D_ARRAY:           u = _IntSetter  (name, offsets[i], location,  types[i], sizes[i] )
            elif types[i] == GL_INT_SAMPLER_2D:                 u = _IntSetter  (name, offsets[i], location,  types[i], sizes[i] )
            elif types[i] == GL_INT_SAMPLER_2D_ARRAY:           u = _IntSetter  (name, offsets[i], location,  types[i], sizes[i] )
            elif types[i] == GL_INT_SAMPLER_3D:                 u = _IntSetter  (name, offsets[i], location,  types[i], sizes[i] )
            elif types[i] == GL_INT_SAMPLER_CUBE:               u = _IntSetter  (name, offsets[i], location,  types[i], sizes[i] )
            elif types[i] == GL_UNSIGNED_INT_SAMPLER_1D:        u = _IntSetter  (name, offsets[i], location,  types[i], sizes[i] )
            elif types[i] == GL_UNSIGNED_INT_SAMPLER_1D_ARRAY:  u = _IntSetter  (name, offsets[i], location,  types[i], sizes[i] )
            elif types[i] == GL_UNSIGNED_INT_SAMPLER_2D:        u = _IntSetter  (name, offsets[i], location,  types[i], sizes[i] )
            elif types[i] == GL_UNSIGNED_INT_SAMPLER_2D_ARRAY:  u = _IntSetter  (name, offsets[i], location,  types[i], sizes[i] )
            elif types[i] == GL_UNSIGNED_INT_SAMPLER_3D:        u = _IntSetter  (name, offsets[i], location,  types[i], sizes[i] )
            elif types[i] == GL_UNSIGNED_INT_SAMPLER_CUBE:      u = _IntSetter  (name, offsets[i], location,  types[i], sizes[i] )
            elif types[i] == GL_SAMPLER_1D_SHADOW:              u = _IntSetter  (name, offsets[i], location,  types[i], sizes[i] )
            elif types[i] == GL_SAMPLER_2D_SHADOW:              u = _IntSetter  (name, offsets[i], location,  types[i], sizes[i] )
            elif types[i] == GL_SAMPLER_2D_ARRAY_SHADOW:        u = _IntSetter  (name, offsets[i], location,  types[i], sizes[i] )
            elif types[i] == GL_SAMPLER_CUBE_SHADOW:            u = _IntSetter  (name, offsets[i], location,  types[i], sizes[i] )
            elif types[i] == GL_SAMPLER_BUFFER:                 u = _IntSetter  (name, offsets[i], location,  types[i], sizes[i] )
            elif types[i] == GL_SAMPLER_2D_MULTISAMPLE:         u = _IntSetter  (name, offsets[i], location,  types[i], sizes[i] )
            elif types[i] == GL_SAMPLER_2D_MULTISAMPLE_ARRAY:   u = _IntSetter  (name, offsets[i], location,  types[i], sizes[i] )
            elif types[i] == GL_SAMPLER_CUBE_MAP_ARRAY:         u = _IntSetter  (name, offsets[i], location,  types[i], sizes[i] )
            elif types[i] == GL_SAMPLER_CUBE_MAP_ARRAY_SHADOW:  u = _IntSetter  (name, offsets[i], location,  types[i], sizes[i] )
            elif types[i] == GL_IMAGE_BUFFER:                   u = _IntSetter  (name, offsets[i], location,  types[i], sizes[i] )
            elif types[i] == GL_IMAGE_2D_ARRAY:                 u = _IntSetter  (name, offsets[i], location,  types[i], sizes[i] )
            elif types[i] == GL_IMAGE_2D:                       u = _IntSetter  (name, offsets[i], location,  types[i], sizes[i] )
            else: raise ShaderError("Uniform "+name+": Unsupported type")
        else:
            if   types[i] == GL_FLOAT_MAT4:  u = _Mat4ArraySetter  (name, offsets[i], location,  types[i], sizes[i] )
            elif types[i] == GL_FLOAT_VEC4:  u = _Vec4ArraySetter  (name, offsets[i], location,  types[i], sizes[i] )
            elif types[i] == GL_FLOAT_VEC3:  u = _Vec3ArraySetter  (name, offsets[i], location,  types[i], sizes[i] )
            elif types[i] == GL_FLOAT_VEC2:  u = _Vec2ArraySetter  (name, offsets[i], location,  types[i], sizes[i] )
            elif types[i] == GL_FLOAT:       u = _FloatArraySetter (name, offsets[i], location,  types[i], sizes[i] )
            else: raise ShaderError("Uniform "+name+": Unsupported type (arrays must be vecN or float or mat4)")
        
        uniforms[name] = u
        
        if offsets[i] != -1:
            end = offsets[i] + u.numBytes
            if end > totalUniformBytes:
                totalUniformBytes = end
    
    rv = array.array("I",[0])
    glGetProgramiv( prog, GL_ACTIVE_UNIFORM_BLOCKS, rv )
    if  rv[0] != 0 :
        glGetActiveUniformBlockiv( prog, 0, GL_UNIFORM_BLOCK_DATA_SIZE, rv )
        return rv[0]
    else:
        return 0
       

def _getShaderInputsAndOutputs( S, shaderType, inputs, uniforms, outputs ):
    del inputs[0:len(inputs)]
    del outputs[0:len(outputs)]

    tok = _Tokenizer(S.data,S.filename)
    filename=S.filename
    tokens = []
    
    toDelete=[]
    
    while(True):
        T = tok.next()
        # ~ print("next:",T)
        if  T.sym == "$" :
            break
        if  T.sym == "LAYOUT" :
            # ~ print("-"*20,"layout")
            #layout(local_size_x=32,local_size_y=1,local_size_z=1) in;
            #layout(location=0) in vec3 foo;
            #layout(binding=0) uniform sampler2DArray tex;
            #layout(location=0) out vec4 foo;
            #layout(binding=0,rgba) uniform image2DArray img;
            
            #take everything between parens
            binding=-1
            location=-1
            toKeep=[]
            
            #layout(foo,location=x)     -> layout(foo)
            #layout(location=x,foo)     -> layout(foo)
            #layout(foo,bar)            -> layout(foo,bar)
            #layout(location=x)         -> [nothing]
            #layout(foo,location=x,bar) -> layout(foo,bar)
            
            maybeDelete=[]


            lp = tok.expect("LP")
            while True:
                attr = tok.next()
                if attr.sym == "RP":
                    rp = attr
                    break
                elif attr.sym == "$":
                    #syntax error
                    _shaderError(filename, lp.line, "Unclosed '('")
                elif attr.sym == "BINDING":
                    maybeDelete.append(attr)
                    maybeDelete.append(tok.expect("EQ"))
                    num = tok.expect("NUM")
                    maybeDelete.append(num)
                    binding = int(num.lexeme)
                elif attr.sym == "LOCATION" :
                    maybeDelete.append(attr)
                    maybeDelete.append(tok.expect("EQ"))
                    num = tok.expect("NUM")
                    maybeDelete.append(num)
                    location = int(num.lexeme)
                else:
                    toKeep.append(attr)



            # ~ print("tokeep=",toKeep)
            #delete consecutive commas from toKeep
            
            
            ci=0
            while ci < len(toKeep)-1:
                if toKeep[ci].lexeme == "," and toKeep[ci+1].lexeme == ",":
                    maybeDelete.append(toKeep[ci])
                    del toKeep[ci]
                else:
                    ci+=1
            if len(toKeep) > 0 and toKeep[0].lexeme == ",":
                maybeDelete.append(toKeep[0])
                del toKeep[0]
            if len(toKeep) > 0 and toKeep[-1].lexeme == ",":
                maybeDelete.append(toKeep[-1])
                del toKeep[-1]
                

            if len(toKeep) == 0:
                #delete layout specifier too
                maybeDelete.append(T)  #layout
                maybeDelete.append(lp)
                maybeDelete.append(rp)
                
            itemType = tok.next()     #in, uniform, buffer, out
            if itemType.sym != "IN"  and  itemType.sym != "OUT"  and  itemType.sym != "UNIFORM" and itemType.sym != "BUFFER" :
                _shaderError(filename, itemType.line, "Expected 'in', 'out', 'uniform', or 'buffer' but got '"+itemType.lexeme+"'")
                
            varType = tok.next()        #variable type OR block name (if uniform or buffer block)
            
            if varType.sym == "SEMI":
                #apparently a cs local_size specifier. Ignore.
                #don't add maybeDelete to toDelete
                pass
            else:
                varName = tok.next()
                semi = tok.next()
                
                
                if itemType.sym in ["UNIFORM","BUFFER"] and varName.lexeme == "{" :
                    #it's a uniform block. Ignore it.
                    #FIXME: Won't handle nested uniform blocks!
                    tmp = tok.next()
                    while tmp.sym != "$" and tmp.lexeme != "}":
                        tmp = tok.next()
                    #don't add maybeDelete to toDelete
                else:
                    
                    toDelete += maybeDelete
                    
                    # ~ print("itemType=",itemType)
                    # ~ print("varType:",varType)
                    # ~ print("semi:",semi)
                    
                    if semi.sym != "SEMI":
                        _shaderError(filename,semi.line,"Expected semicolon but got "+semi.lexeme)
                    
                    if itemType.sym == "IN" :
                        if shaderType != GL_VERTEX_SHADER:
                            _shaderError(filename,itemType.line,"'layout' is only valid for 'in' variables in the vertex shader")
                        if  binding != -1 :
                            _shaderError(filename,itemType.line,"'binding' is not valid for 'in' variables (did you mean 'location'?)")
                        inputs.append( _ShaderVariable( type=varType.lexeme, 
                                                        name=varName.lexeme,
                                                        location=location,
                                                        binding=binding,
                                                        bindingClass=None,
                                                        sourceStartChar=T.startIndex, sourceEndChar=semi.endIndex,
                                                        layoutStartChar=T.startIndex,layoutEndChar=rp.endIndex,
                                                        lineNumber=varName.line))
                            #T.startIndex, semi.endIndex, T.startIndex, rp.endIndex, varName.line ))
                    elif itemType.sym == "UNIFORM" :
                        if varType.sym == "SAMPLERTYPE"  and  location != -1:
                            _shaderError(filename,itemType.line,"'location' is not valid for sampler variables (did you mean 'binding'?)")
                        if varType.sym != "SAMPLERTYPE":
                            _shaderError(filename, varType.line, "Can only specify layout for a sampler uniform; this one is of type "+varType.lexeme)
                        if "sampler" in varType.lexeme:
                            bindingClass = "sampler"
                        elif "image" in varType.lexeme:
                            bindingClass="image"
                        else:
                            bindingClass="unknown"
                        for u in uniforms:
                            if u.binding != -1 and u.binding == binding and u.bindingClass == bindingClass:
                                _shaderError(filename,varType.line,"More than one sampler with the same binding")
                        uniforms.append( _ShaderVariable( type=varType.lexeme, name=varName.lexeme,
                                                        location=location,binding=binding,bindingClass=bindingClass,
                                                        sourceStartChar=T.startIndex, sourceEndChar=semi.endIndex, 
                                                        layoutStartChar=T.startIndex, layoutEndChar=rp.endIndex, 
                                                        lineNumber=varName.line))
                    elif itemType.sym == "OUT" :
                        if  shaderType != GL_FRAGMENT_SHADER :
                            _shaderError(filename,itemType.line,"'layout' is only valid for 'out' variables in the fragment shader")
                        if  binding != -1 :
                            _shaderError(filename,itemType.line,"'binding' is not valid for 'out' variables (did you mean 'layout'?)")
                        outputs.append( _ShaderVariable( type=varType.lexeme, name=varName.lexeme,location=location,
                            binding=binding,bindingClass=None,
                            sourceStartChar=T.startIndex, sourceEndChar=semi.endIndex, 
                            layoutStartChar=T.startIndex, layoutEndChar=rp.endIndex, lineNumber=varName.line))
                    else:
                        _shaderError(filename,itemType.line,"Expected 'in', 'out', or 'uniform'")
        elif T.sym == "IN"  or  T.sym == "OUT" :
            #layout (...) out;
            #in vec3 foo;
            #out float bar;
            varType = tok.expect("ID")
            varName = tok.expect("ID")
            t = tok.next()
            if t.sym == "SEMI":
                semi = t
            elif t.sym == "ANYTHING" and t.lexeme == "[":
                t = tok.expect("ANYTHING")
                semi = tok.expect("SEMI")
            else:
                _shaderError(filename,itemType.line,"Expected ';' or '[]'")

            #FIXME: Won't work for TCS, TES, or GS if we have array inputs.
            #semi = tok.expect("SEMI")
            if T.sym == "IN" :
                inputs.append( _ShaderVariable( type=varType.lexeme, name=varName.lexeme,
                    binding=-1,bindingClass=None, location=-1,
                    sourceStartChar=T.startIndex, sourceEndChar=semi.endIndex, 
                    layoutStartChar=-1, layoutEndChar=-1, lineNumber=varName.line))
            elif T.sym == "OUT" :
                outputs.append( _ShaderVariable( type=varType.lexeme, name=varName.lexeme,
                    binding=-1,bindingClass=None, location=-1,
                    sourceStartChar=T.startIndex, sourceEndChar=semi.endIndex,
                    layoutStartChar=-1, layoutEndChar=-1, lineNumber=varName.line))
            else:
                #FIXME: Probably part of a GS input specification. 
                #Should skip it.
                pass
        else:
            pass
            #~ std.cout << "? wat ? " << T.lexeme << "\n";


    for deltoken in toDelete:
        S.data = _stringRangeReplace( S.data, deltoken.startIndex, deltoken.endIndex )
        
# ~ for sv in inputs:
                # ~ if sv.layoutStartChar!= -1 :
                    # ~ S[si].data = _stringRangeReplace( S[si].data, sv.layoutStartChar, sv.layoutEndChar )
                    
            # ~ for sv in outputs:
                # ~ if sv.layoutStartChar!= -1 :
                    # ~ S[si].data = _stringRangeReplace( S[si].data, sv.layoutStartChar, sv.layoutEndChar )
                    
            # ~ for sv in uniforms:
                # ~ if sv.layoutStartChar!= -1 :
                    # ~ S[si].data = _stringRangeReplace( S[si].data, sv.layoutStartChar, sv.layoutEndChar )
 
 
def __checkUninitializedUniforms():
    if not Program.current:
        raise NoActiveProgramError("No program is active")
    for name in Program.commonUniforms:
        it = Program.commonUniforms[name]
        if  not it.hasBeenSet  and  not it.hasBeenWarned:
            it.hasBeenWarned=True
            raise UninitializedUniformError( "Uniform '{}' has not been initialized".format(it.name))
    for name in Program.current.privateUniforms:
        it = Program.current.privateUniforms[name]
        if  not it.hasBeenSet  and  not it.hasBeenWarned:
            it.hasBeenWarned=True
            raise UninitializedUniformError( "Uniform '{}' has not been initialized".format(it.name))

def __updateUniforms():
    global _bufferDirty
    if _bufferDirty :
        glBindBufferBase(GL_UNIFORM_BUFFER,0,_uboBuffer)
        glBufferSubData(GL_UNIFORM_BUFFER,0,
            len(_uboBackingMemory),
            _uboBackingMemory )
        _bufferDirty = False

  
def _initialize(progObj,vs,tcs,tes,gs,fs,cs,paramsAreData):
    progObj.prog = glCreateProgram()
    
    plist=[vs,tcs,tes,gs,fs,cs]
    types = [GL_VERTEX_SHADER,GL_TESS_CONTROL_SHADER,GL_TESS_EVALUATION_SHADER,
            GL_GEOMETRY_SHADER, GL_FRAGMENT_SHADER, GL_COMPUTE_SHADER ]
    stageNames = [ "vertex shader", "tesselation control shader",
            "tesselation evaluation shader", "geometry shader",
            "fragment shader", "compute shader" ]

    previousStage=-1
    previousOutputs = []
    
    allStageUniforms = []
    S=[]
    
    fromFile=False
    for si in range(6):
        shaderType = types[si]
        if paramsAreData:
            filename=None
            data=plist[si]
        else:
            filename=plist[si]
            data=None
             
        S.append( _ShaderData(filename,data) )
        
        if not filename and not data:
            continue
            
        
        if filename:
            fromFile=True
            S[si].data = _readFile(S[si].filename)
        
        
        inputs=[]
        outputs=[]
        uniforms=[]
         
        if progObj.identifier != "":
            progObj.identifier += "+"
        progObj.identifier += filename

        _getShaderInputsAndOutputs( S[si], shaderType, inputs, uniforms, outputs )
        
        if previousStage == -1 :
            for p in inputs:
                p.matched=True
        else:
            for psout in previousOutputs:
                for psin in inputs:
                    if psout.name == psin.name :
                        if psout.type != psin.type :
                            msg = (
                                "ERROR: {} '{}' produces output '{}' of type {} but {} '{}' expects it to be of type {}.".format(
                                    stageNames[previousStage],  S[previousStage].filename,
                                    psout.name, psout.type, stageNames[si], S[si].filename, psin.type ))
                            # ~ print(msg)
                            raise ShaderStageMismatchError(msg)
                        else:
                            psout.matched=True
                            psin.matched=True
                            break
       
        for psin in inputs:
            if  not psin.matched:
                msg = "ERROR: {} '{}' reads input '{}' but {} '{}' does not output it.".format(
                        stageNames[si], S[si].filename, psin.name, stageNames[previousStage], S[previousStage].filename)
                # ~ print(msg)
                raise ShaderStageMismatchError(msg)
        for psout in previousOutputs :
            if  not psout.matched :
                msg = "ERROR: {} '{}' outputs '{}' but {} '{}' does not read it".format(
                        stageNames[previousStage], S[previousStage].filename,
                        psout.name, stageNames[si], S[si].filename )
                # ~ print(msg)
                raise ShaderStageMismatchError(msg)
         
        _compile(S[si], shaderType, progObj.prog)


        if  shaderType == GL_VERTEX_SHADER :
            used=set()
            for vsin in inputs :
                if  vsin.location != -1 :
                    __log("{}: Setting VS input '{}' to location {}".format(
                        S[si].filename,
                        vsin.name,vsin.location)) 
                    glBindAttribLocation( progObj.prog, vsin.location, vsin.name )
                    if  vsin.location in used:
                        _shaderError(S[si].filename,vsin.lineNumber,"More than one VS input uses the same location")
                    used.add(vsin.location)
            for vsin in inputs :
                if  vsin.location == -1 :
                    for i in range(256):
                        if  i not in used:
                            __log("{}: Setting VS input '{}' to location {}".format(
                                S[si].filename,vsin.name,i)) 
                            glBindAttribLocation( progObj.prog, vsin.location, vsin.name )
                            used.add(vsin.location)
                            break
                    if  i == 256 :
                        _shaderError(S[si].filename,vsin.lineNumber,"Too many VS inputs")

        if  shaderType == GL_FRAGMENT_SHADER :
            used=set()
            for fsout in outputs :
                if  fsout.location != -1 :
                    __log("{}: Setting FS output '{}' to location {}".format(
                        S[si].filename,fsout.name,fsout.location))
                    glBindFragDataLocation( progObj.prog, fsout.location, fsout.name )
                    if fsout.location in used:
                        _shaderError(S[si].filename,fsout.lineNumber,"More than one FS output uses the same location")
                    used.add(fsout.location)
            for fsout in outputs:
                if  fsout.location == -1 :
                    for i in range(256):
                        if  i not in used:
                            __log("{}: Setting FS output '{}' to location {}".format(
                                S[si].filename,fsout.name,i))
                            glBindFragDataLocation( progObj.prog, i, fsout.name )
                            used.add(fsout.location)
                            break
                    if  i == 256 :
                        _shaderError(S[si].filename,fsout.lineNumber,"Too many FS outputs")
        
        previousOutputs = outputs
        allStageUniforms.append(uniforms)
        previousStage = si
   
    glLinkProgram(progObj.prog)
    _getLog( "","","Linking "+progObj.identifier+":", glGetProgramInfoLog, progObj.prog)
    tmp = array.array("I",[0])
    glGetProgramiv( progObj.prog, GL_LINK_STATUS, tmp )
    if not tmp[0]:
        raise ShaderError("Cannot link")
        
        
    progObj.privateUniforms = {}
    _queryUniforms( progObj.prog, progObj.privateUniforms, True  )

    if  fromFile :
        __setupCommonUniforms(progObj.prog)
        
    old = Program.current
    progObj.use()
    for U in allStageUniforms :
        for unif in U:
            if  unif.binding != -1:
                #unused uniforms might be missing
                #so we skip them
                __log("{}: Setting uniform '{}' to {}".format(progObj.identifier,unif.name,unif.binding))
                Program.setUniform(unif.name,unif.binding,True)

    if old :
        old.use()
    else:
        Program.current = None
        glUseProgram(0)

    global _hookAdded
    if not _hookAdded :
        L=[]
        for X in ["glDrawArrays","glDrawElements","glMultiDrawElements","glMultiDrawArrays"]:
            for Y in ["","Instanced","InstancedBaseInstance","Indirect"]:
                L.append(X+Y)
        L.append("glDrawRangeElements")
        L.append("glDrawRangeElementsBaseVertex")
        L.append("glDrawElementsBaseVertex")
        L.append("glMultiDrawElementsBaseVertex")
        L.append("glDrawElementsInstancedBaseVertex")
        L.append("glDrawElementsInstancedBaseVertexBaseInstance")
        L.append("glDispatchCompute")
        L.append("glDispatchComputeIndirect")
        
        for f in L:
            gl.addGLHook( f, lambda *args: __updateUniforms() )
            gl.addGLHook( f, lambda *args: __checkUninitializedUniforms() )
        _hookAdded=True

def _getSetter(name,missingOK):
    if  Program.current :
        it = Program.current.privateUniforms.get(name,None)
        if it != None:
            return it
    
    it = Program.commonUniforms.get(name,None)
    if it != None:
        return it

    if  missingOK:
        return None
        
    if(  name+"[0]" in Program.commonUniforms or
        (Program.current  and  name+"[0]" in Program.current.privateUniforms)):
        msg = "No such uniform "+name+" (maybe you meant '"+name+"[0]'?)"
        # ~ print(msg)
        raise NoSuchUniformError(msg)
    else:
        msg = "No such uniform "+name
        # ~ print(msg)
        raise NoSuchUniformError(msg)   

def __log(fmt,*args):
    if type(fmt) != str:
        tmp = [fmt] + args
        output = " ".join([ str(q) for q in tmp ])
    else:
        output = fmt.format(*args)
    fr = inspect.getouterframes(inspect.currentframe())[1]
    #print(fr)
    #filename,lineno,func,context,index = fr #inspect.getframeinfo(fr)
    print("{} ({}): {}".format(
        os.path.basename(fr.filename), 
        fr.lineno,
        output
    ))
    
def __setupCommonUniforms(prog):
    global _uboBackingMemory, _uboBuffer, _uboBackingAddress
    if  _uboBuffer != None:
        return
    totalUniformBytes = _queryUniforms( prog, Program.commonUniforms, False )
    __log("{} bytes = {} vec4 slots for common uniforms",
        totalUniformBytes,totalUniformBytes//4//4)
    _uboBackingMemory = ctypes.create_string_buffer(totalUniformBytes)
    _uboBackingAddress = ctypes.addressof( _uboBackingMemory )
    tmp = array.array("I",[0])
    glGenBuffers(1,tmp)
    _uboBuffer = tmp[0]
    glBindBuffer(GL_UNIFORM_BUFFER,_uboBuffer)
    glBufferData(GL_UNIFORM_BUFFER, totalUniformBytes, None, GL_DYNAMIC_DRAW )
    glBindBufferBase(GL_UNIFORM_BUFFER, 0, _uboBuffer )


class Program:

    commonUniforms : typing.Any = {}
    current = None
    
    def __init__(self,*,vs:str=None,tcs:str=None,tes:str=None,gs:str=None,fs:str=None,cs:str=None,
                    paramsAreSource=False):
                        
        self.prog = None
        self.identifier=""
        _initialize(self,vs,tcs,tes,gs,fs,cs,paramsAreSource)
        
    def dispatch(self,xs:int,ys:int,zs:int):
        if Program.current != self:
            self.use()
        if xs <= 0 or ys <= 0 or zs <= 0:
            raise RuntimeError("Bad dispatch count")
        glDispatchCompute(xs,ys,zs)
     
    
    @staticmethod
    def setUniform(name:str,value:typing.Any,missingOK=False):
        u = _getSetter(name,missingOK)
        if u:
            u.set(value)

    def use(self):
        glUseProgram(self.prog)
        Program.current = self

