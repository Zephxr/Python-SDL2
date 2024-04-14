#Data from gl.xml, which has this copyright:

#Copyright (c) 2013-2016 The Khronos Group Inc.
#
#Permission is hereby granted, free of charge, to any person obtaining a
#copy of this software and/or associated documentation files (the
#"Materials"), to deal in the Materials without restriction, including
#without limitation the rights to use, copy, modify, merge, publish,
#distribute, sublicense, and/or sell copies of the Materials, and to
#permit persons to whom the Materials are furnished to do so, subject to
#the following conditions:
#
#The above copyright notice and this permission notice shall be included
#in all copies or substantial portions of the Materials.
#
#THE MATERIALS ARE PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
#CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
#TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#MATERIALS OR THE USE OR OTHER DEALINGS IN THE MATERIALS.
#
#------------------------------------------------------------------------
#
#This file, gl.xml, is the OpenGL and OpenGL API Registry. The older
#".spec" file format has been retired and will no longer be updated with
#new extensions and API versions. The canonical version of the registry,
#together with documentation, schema, and Python generator scripts used
#to generate C header files for OpenGL and OpenGL ES, can always be found
#in the Khronos Registry at
#        http://www.opengl.org/registry/
#    

import sys
from ctypes import *
import array
import os
import glconstants
import typing


_hookable=set(["glTexImage2D","glDrawElementsInstancedBaseVertexBaseInstance","glDispatchComputeIndirect","glDrawElementsIndirect","glDrawElements","glBufferData","glMultiDrawElementsInstanced","glMultiDrawArraysIndirect","glDrawArrays","glDispatchCompute","glMultiDrawElementsInstancedBaseInstance","glMultiDrawArraysInstanced","glMultiDrawArrays","glDrawArraysInstanced","glDrawElementsInstancedBaseVertex","glTexImage1D","glDrawArraysIndirect","glDrawArraysInstancedBaseInstance","glDrawRangeElements","glGenBuffers","glMultiDrawElementsIndirect","glMultiDrawArraysInstancedBaseInstance","glMultiDrawElementsBaseVertex","glMultiDrawElements","glDrawRangeElementsBaseVertex","glGenTextures","glDrawElementsBaseVertex","glClear","glTexImage3D","glDrawElementsInstancedBaseInstance","glDrawElementsInstanced" ])


def __pyglMakeCallback(fname):
    def tmp(*args):
        raise RuntimeError("The function "+fname+" is not implemented")
    return tmp
       
  
def isHookable(funcname):
    if _hookable == None:
        return True     #all functions may be hooked
    else:
        return funcname in _hookable

if typing.TYPE_CHECKING:
    WINFUNCTYPE = typing.cast(typing.Any, [] )
    windll = typing.cast(typing.Any, [] )
    
#http://stackoverflow.com/questions/279561/what-is-the-python-equivalent-of-static-variables-inside-a-function
def __pyglGetFuncAddress(funcname):
    if sys.platform.lower().find("win32") != -1:
        if "kernel32" not in __pyglGetFuncAddress.__dict__:

            __pyglGetFuncAddress.kernel32 = windll.kernel32

            __pyglGetFuncAddress.LoadLibraryA = __pyglGetFuncAddress.kernel32.LoadLibraryA
            __pyglGetFuncAddress.LoadLibraryA.argtypes=[c_char_p]
            __pyglGetFuncAddress.LoadLibraryA.restype = c_void_p


            __pyglGetFuncAddress.GetProcAddress = __pyglGetFuncAddress.kernel32.GetProcAddress
            __pyglGetFuncAddress.GetProcAddress.argtypes = [c_void_p,c_char_p]
            __pyglGetFuncAddress.GetProcAddress.restype = c_void_p

            __pyglGetFuncAddress.opengl32 = __pyglGetFuncAddress.LoadLibraryA(b"opengl32.dll")
            tmp = __pyglGetFuncAddress.GetProcAddress(__pyglGetFuncAddress.opengl32,b"wglGetProcAddress")
            __pyglGetFuncAddress.wglGetProcAddress = WINFUNCTYPE(c_void_p,c_char_p)(tmp)    

        x = __pyglGetFuncAddress.wglGetProcAddress(funcname.encode())
        if not x or x == None or x == 0 or x == 1 or x == 2 or x == 3 or x == -1 or x == 0xffffffff or x == 0xffffffffffffffff:
            x = __pyglGetFuncAddress.GetProcAddress(__pyglGetFuncAddress.opengl32,funcname.encode())
    else:
        if "dlopen" not in __pyglGetFuncAddress.__dict__:
            __pyglGetFuncAddress.dlopen = cdll.LoadLibrary("libdl.so").dlopen
            __pyglGetFuncAddress.dlopen.argtypes = [c_char_p,c_int]
            __pyglGetFuncAddress.dlopen.restype = c_void_p
            #2 = RTLD_NOW
            __pyglGetFuncAddress.libgl = __pyglGetFuncAddress.dlopen(b"libGL.so",2)
            __pyglGetFuncAddress.dlsym = cdll.LoadLibrary("libdl.so").dlsym
            __pyglGetFuncAddress.dlsym.argtypes = [c_void_p,c_char_p]
            __pyglGetFuncAddress.dlsym.restype = c_void_p
        x = __pyglGetFuncAddress.dlsym(__pyglGetFuncAddress.libgl,funcname.encode())
    #endif
    return x
            
if sys.platform.lower().find('win32') != -1:
    __PYGL_FUNC_TYPE = WINFUNCTYPE
else:
    __PYGL_FUNC_TYPE = CFUNCTYPE
      
__hooks = {}
__posthooks = {}
__universal_hooks=[]
__universal_posthooks=[]

def addGLHook( funcname, func ):
    assert callable(func)
    if funcname =="*":
        __universal_hooks.append(func)
        return
    if not isHookable(funcname):
        raise Exception("The function "+funcname+" cannot be hooked")
    if funcname not in __hooks:
        __hooks[funcname] = []
    __hooks[funcname].append(func)
 
def removeGLHook( funcname, func ):
    if funcname =="*":
        __universal_hooks.remove(func)
        return
    if not isHookable(funcname):
        raise Exception("The function "+str(func)+" cannot be unhooked")
    if funcname not in __hooks:
        return
    __hooks[funcname].remove(func)
    if len(__hooks[funcname]) == 0:
        del __hooks[funcname]

def addGLPostHook( funcname, func ):
    assert callable(func)
    if funcname =="*":
        __universal_posthooks.append(func)
        return
    if not isHookable(funcname):
        raise Exception("The function "+str(func)+" cannot be hooked")
    if funcname not in __posthooks:
        __posthooks[funcname] = []
    __posthooks[funcname].append(func)
 
def removeGLPostHook( funcname, func ):
    if funcname =="*":
        __universal_posthooks.remove(func)
        return
    if not isHookable(funcname):
        raise Exception("The function "+str(func)+" cannot be unhooked")
    if funcname not in __posthooks:
        return
    __posthooks[funcname].remove(func)
    if len(__posthooks[funcname]) == 0:
        del __posthooks[funcname]

def __pyglGetAsConstVoidPointer(v):
    if v == None:
        a= c_void_p(None)
    elif isinstance(v,bytes):
        a= c_char_p(v)
    elif isinstance(v,bytearray):
        a= (c_uint8*len(v)).from_buffer(v)
    elif isinstance(v,array.array):
        a= c_void_p(v.buffer_info()[0])
    elif isinstance(v, c_void_p):
        a = v
    elif isinstance(v, memoryview):
        a = v.tobytes()
    else:
        a = byref(v) #raise TypeError("Invalid type:"+str(type(v)))
    return a  
    
    

__glActiveShaderProgram_impl = None
def glActiveShaderProgram ( pipeline:int,program:int ) -> None :
    global __glActiveShaderProgram_impl
    if not __glActiveShaderProgram_impl:
        fptr = __pyglGetFuncAddress('glActiveShaderProgram')
        if not fptr:
            raise RuntimeError('The function glActiveShaderProgram is not available (maybe GL has not been initialized yet?)')
        __glActiveShaderProgram_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint )(fptr)
        global glActiveShaderProgram
        glActiveShaderProgram =__glActiveShaderProgram_impl
    return __glActiveShaderProgram_impl(pipeline,program)

__glActiveTexture_impl = None
def glActiveTexture ( texture:int ) -> None :
    global __glActiveTexture_impl
    if not __glActiveTexture_impl:
        fptr = __pyglGetFuncAddress('glActiveTexture')
        if not fptr:
            raise RuntimeError('The function glActiveTexture is not available (maybe GL has not been initialized yet?)')
        __glActiveTexture_impl = __PYGL_FUNC_TYPE( None,c_uint )(fptr)
        global glActiveTexture
        glActiveTexture =__glActiveTexture_impl
    return __glActiveTexture_impl(texture)

__glAttachShader_impl = None
def glAttachShader ( program:int,shader:int ) -> None :
    global __glAttachShader_impl
    if not __glAttachShader_impl:
        fptr = __pyglGetFuncAddress('glAttachShader')
        if not fptr:
            raise RuntimeError('The function glAttachShader is not available (maybe GL has not been initialized yet?)')
        __glAttachShader_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint )(fptr)
        global glAttachShader
        glAttachShader =__glAttachShader_impl
    return __glAttachShader_impl(program,shader)

__glBeginConditionalRender_impl = None
def glBeginConditionalRender ( id:int,mode:int ) -> None :
    global __glBeginConditionalRender_impl
    if not __glBeginConditionalRender_impl:
        fptr = __pyglGetFuncAddress('glBeginConditionalRender')
        if not fptr:
            raise RuntimeError('The function glBeginConditionalRender is not available (maybe GL has not been initialized yet?)')
        __glBeginConditionalRender_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint )(fptr)
        global glBeginConditionalRender
        glBeginConditionalRender =__glBeginConditionalRender_impl
    return __glBeginConditionalRender_impl(id,mode)

__glBeginQuery_impl = None
def glBeginQuery ( target:int,id:int ) -> None :
    global __glBeginQuery_impl
    if not __glBeginQuery_impl:
        fptr = __pyglGetFuncAddress('glBeginQuery')
        if not fptr:
            raise RuntimeError('The function glBeginQuery is not available (maybe GL has not been initialized yet?)')
        __glBeginQuery_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint )(fptr)
        global glBeginQuery
        glBeginQuery =__glBeginQuery_impl
    return __glBeginQuery_impl(target,id)

__glBeginQueryIndexed_impl = None
def glBeginQueryIndexed ( target:int,index:int,id:int ) -> None :
    global __glBeginQueryIndexed_impl
    if not __glBeginQueryIndexed_impl:
        fptr = __pyglGetFuncAddress('glBeginQueryIndexed')
        if not fptr:
            raise RuntimeError('The function glBeginQueryIndexed is not available (maybe GL has not been initialized yet?)')
        __glBeginQueryIndexed_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint )(fptr)
        global glBeginQueryIndexed
        glBeginQueryIndexed =__glBeginQueryIndexed_impl
    return __glBeginQueryIndexed_impl(target,index,id)

__glBeginTransformFeedback_impl = None
def glBeginTransformFeedback ( primitiveMode:int ) -> None :
    global __glBeginTransformFeedback_impl
    if not __glBeginTransformFeedback_impl:
        fptr = __pyglGetFuncAddress('glBeginTransformFeedback')
        if not fptr:
            raise RuntimeError('The function glBeginTransformFeedback is not available (maybe GL has not been initialized yet?)')
        __glBeginTransformFeedback_impl = __PYGL_FUNC_TYPE( None,c_uint )(fptr)
        global glBeginTransformFeedback
        glBeginTransformFeedback =__glBeginTransformFeedback_impl
    return __glBeginTransformFeedback_impl(primitiveMode)

__glBindAttribLocation_impl = None
def glBindAttribLocation ( program:int,index:int,name:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glBindAttribLocation_impl
    if not __glBindAttribLocation_impl:
        fptr = __pyglGetFuncAddress('glBindAttribLocation')
        if not fptr:
            raise RuntimeError('The function glBindAttribLocation is not available (maybe GL has not been initialized yet?)')
        __glBindAttribLocation_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glBindAttribLocation_impl
        __glBindAttribLocation_impl = (lambda program,index,name: tmp(program,index,c_char_p(name.encode())))
        global glBindAttribLocation
        glBindAttribLocation =__glBindAttribLocation_impl
    return __glBindAttribLocation_impl(program,index,name)

__glBindBuffer_impl = None
def glBindBuffer ( target:int,buffer:int ) -> None :
    global __glBindBuffer_impl
    if not __glBindBuffer_impl:
        fptr = __pyglGetFuncAddress('glBindBuffer')
        if not fptr:
            raise RuntimeError('The function glBindBuffer is not available (maybe GL has not been initialized yet?)')
        __glBindBuffer_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint )(fptr)
        global glBindBuffer
        glBindBuffer =__glBindBuffer_impl
    return __glBindBuffer_impl(target,buffer)

__glBindBufferBase_impl = None
def glBindBufferBase ( target:int,index:int,buffer:int ) -> None :
    global __glBindBufferBase_impl
    if not __glBindBufferBase_impl:
        fptr = __pyglGetFuncAddress('glBindBufferBase')
        if not fptr:
            raise RuntimeError('The function glBindBufferBase is not available (maybe GL has not been initialized yet?)')
        __glBindBufferBase_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint )(fptr)
        global glBindBufferBase
        glBindBufferBase =__glBindBufferBase_impl
    return __glBindBufferBase_impl(target,index,buffer)

__glBindBufferRange_impl = None
def glBindBufferRange ( target:int,index:int,buffer:int,offset:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],size:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glBindBufferRange_impl
    if not __glBindBufferRange_impl:
        fptr = __pyglGetFuncAddress('glBindBufferRange')
        if not fptr:
            raise RuntimeError('The function glBindBufferRange is not available (maybe GL has not been initialized yet?)')
        __glBindBufferRange_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint,c_size_t,c_void_p )(fptr)
        global glBindBufferRange
        glBindBufferRange =__glBindBufferRange_impl
    return __glBindBufferRange_impl(target,index,buffer,offset,size)

__glBindBuffersBase_impl = None
def glBindBuffersBase ( target:int,first:int,count:int,buffers:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glBindBuffersBase_impl
    if not __glBindBuffersBase_impl:
        fptr = __pyglGetFuncAddress('glBindBuffersBase')
        if not fptr:
            raise RuntimeError('The function glBindBuffersBase is not available (maybe GL has not been initialized yet?)')
        __glBindBuffersBase_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_int,c_void_p )(fptr)
        tmp = __glBindBuffersBase_impl
        __glBindBuffersBase_impl = (lambda target,first,count,buffers: tmp(target,first,count,__pyglGetAsConstVoidPointer(buffers)))
        global glBindBuffersBase
        glBindBuffersBase =__glBindBuffersBase_impl
    return __glBindBuffersBase_impl(target,first,count,buffers)

__glBindBuffersRange_impl = None
def glBindBuffersRange ( target:int,first:int,count:int,buffers:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],offsets:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],sizes:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glBindBuffersRange_impl
    if not __glBindBuffersRange_impl:
        fptr = __pyglGetFuncAddress('glBindBuffersRange')
        if not fptr:
            raise RuntimeError('The function glBindBuffersRange is not available (maybe GL has not been initialized yet?)')
        __glBindBuffersRange_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_int,c_void_p,c_void_p,c_void_p )(fptr)
        tmp = __glBindBuffersRange_impl
        __glBindBuffersRange_impl = (lambda target,first,count,buffers,offsets,sizes: tmp(target,first,count,__pyglGetAsConstVoidPointer(buffers),__pyglGetAsConstVoidPointer(offsets),__pyglGetAsConstVoidPointer(sizes)))
        global glBindBuffersRange
        glBindBuffersRange =__glBindBuffersRange_impl
    return __glBindBuffersRange_impl(target,first,count,buffers,offsets,sizes)

__glBindFragDataLocation_impl = None
def glBindFragDataLocation ( program:int,color:int,name:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glBindFragDataLocation_impl
    if not __glBindFragDataLocation_impl:
        fptr = __pyglGetFuncAddress('glBindFragDataLocation')
        if not fptr:
            raise RuntimeError('The function glBindFragDataLocation is not available (maybe GL has not been initialized yet?)')
        __glBindFragDataLocation_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glBindFragDataLocation_impl
        __glBindFragDataLocation_impl = (lambda program,color,name: tmp(program,color,c_char_p(name.encode())))
        global glBindFragDataLocation
        glBindFragDataLocation =__glBindFragDataLocation_impl
    return __glBindFragDataLocation_impl(program,color,name)

__glBindFragDataLocationIndexed_impl = None
def glBindFragDataLocationIndexed ( program:int,colorNumber:int,index:int,name:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glBindFragDataLocationIndexed_impl
    if not __glBindFragDataLocationIndexed_impl:
        fptr = __pyglGetFuncAddress('glBindFragDataLocationIndexed')
        if not fptr:
            raise RuntimeError('The function glBindFragDataLocationIndexed is not available (maybe GL has not been initialized yet?)')
        __glBindFragDataLocationIndexed_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glBindFragDataLocationIndexed_impl
        __glBindFragDataLocationIndexed_impl = (lambda program,colorNumber,index,name: tmp(program,colorNumber,index,c_char_p(name.encode())))
        global glBindFragDataLocationIndexed
        glBindFragDataLocationIndexed =__glBindFragDataLocationIndexed_impl
    return __glBindFragDataLocationIndexed_impl(program,colorNumber,index,name)

__glBindFramebuffer_impl = None
def glBindFramebuffer ( target:int,framebuffer:int ) -> None :
    global __glBindFramebuffer_impl
    if not __glBindFramebuffer_impl:
        fptr = __pyglGetFuncAddress('glBindFramebuffer')
        if not fptr:
            raise RuntimeError('The function glBindFramebuffer is not available (maybe GL has not been initialized yet?)')
        __glBindFramebuffer_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint )(fptr)
        global glBindFramebuffer
        glBindFramebuffer =__glBindFramebuffer_impl
    return __glBindFramebuffer_impl(target,framebuffer)

__glBindImageTexture_impl = None
def glBindImageTexture ( unit:int,texture:int,level:int,layered:bool,layer:int,access:int,format:int ) -> None :
    global __glBindImageTexture_impl
    if not __glBindImageTexture_impl:
        fptr = __pyglGetFuncAddress('glBindImageTexture')
        if not fptr:
            raise RuntimeError('The function glBindImageTexture is not available (maybe GL has not been initialized yet?)')
        __glBindImageTexture_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_int,c_char,c_int,c_uint,c_uint )(fptr)
        global glBindImageTexture
        glBindImageTexture =__glBindImageTexture_impl
    return __glBindImageTexture_impl(unit,texture,level,layered,layer,access,format)

__glBindImageTextures_impl = None
def glBindImageTextures ( first:int,count:int,textures:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glBindImageTextures_impl
    if not __glBindImageTextures_impl:
        fptr = __pyglGetFuncAddress('glBindImageTextures')
        if not fptr:
            raise RuntimeError('The function glBindImageTextures is not available (maybe GL has not been initialized yet?)')
        __glBindImageTextures_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_void_p )(fptr)
        tmp = __glBindImageTextures_impl
        __glBindImageTextures_impl = (lambda first,count,textures: tmp(first,count,__pyglGetAsConstVoidPointer(textures)))
        global glBindImageTextures
        glBindImageTextures =__glBindImageTextures_impl
    return __glBindImageTextures_impl(first,count,textures)

__glBindProgramPipeline_impl = None
def glBindProgramPipeline ( pipeline:int ) -> None :
    global __glBindProgramPipeline_impl
    if not __glBindProgramPipeline_impl:
        fptr = __pyglGetFuncAddress('glBindProgramPipeline')
        if not fptr:
            raise RuntimeError('The function glBindProgramPipeline is not available (maybe GL has not been initialized yet?)')
        __glBindProgramPipeline_impl = __PYGL_FUNC_TYPE( None,c_uint )(fptr)
        global glBindProgramPipeline
        glBindProgramPipeline =__glBindProgramPipeline_impl
    return __glBindProgramPipeline_impl(pipeline)

__glBindRenderbuffer_impl = None
def glBindRenderbuffer ( target:int,renderbuffer:int ) -> None :
    global __glBindRenderbuffer_impl
    if not __glBindRenderbuffer_impl:
        fptr = __pyglGetFuncAddress('glBindRenderbuffer')
        if not fptr:
            raise RuntimeError('The function glBindRenderbuffer is not available (maybe GL has not been initialized yet?)')
        __glBindRenderbuffer_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint )(fptr)
        global glBindRenderbuffer
        glBindRenderbuffer =__glBindRenderbuffer_impl
    return __glBindRenderbuffer_impl(target,renderbuffer)

__glBindSampler_impl = None
def glBindSampler ( unit:int,sampler:int ) -> None :
    global __glBindSampler_impl
    if not __glBindSampler_impl:
        fptr = __pyglGetFuncAddress('glBindSampler')
        if not fptr:
            raise RuntimeError('The function glBindSampler is not available (maybe GL has not been initialized yet?)')
        __glBindSampler_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint )(fptr)
        global glBindSampler
        glBindSampler =__glBindSampler_impl
    return __glBindSampler_impl(unit,sampler)

__glBindSamplers_impl = None
def glBindSamplers ( first:int,count:int,samplers:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glBindSamplers_impl
    if not __glBindSamplers_impl:
        fptr = __pyglGetFuncAddress('glBindSamplers')
        if not fptr:
            raise RuntimeError('The function glBindSamplers is not available (maybe GL has not been initialized yet?)')
        __glBindSamplers_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_void_p )(fptr)
        tmp = __glBindSamplers_impl
        __glBindSamplers_impl = (lambda first,count,samplers: tmp(first,count,__pyglGetAsConstVoidPointer(samplers)))
        global glBindSamplers
        glBindSamplers =__glBindSamplers_impl
    return __glBindSamplers_impl(first,count,samplers)

__glBindTexture_impl = None
def glBindTexture ( target:int,texture:int ) -> None :
    global __glBindTexture_impl
    if not __glBindTexture_impl:
        fptr = __pyglGetFuncAddress('glBindTexture')
        if not fptr:
            raise RuntimeError('The function glBindTexture is not available (maybe GL has not been initialized yet?)')
        __glBindTexture_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint )(fptr)
        global glBindTexture
        glBindTexture =__glBindTexture_impl
    return __glBindTexture_impl(target,texture)

__glBindTextureUnit_impl = None
def glBindTextureUnit ( unit:int,texture:int ) -> None :
    global __glBindTextureUnit_impl
    if not __glBindTextureUnit_impl:
        fptr = __pyglGetFuncAddress('glBindTextureUnit')
        if not fptr:
            raise RuntimeError('The function glBindTextureUnit is not available (maybe GL has not been initialized yet?)')
        __glBindTextureUnit_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint )(fptr)
        global glBindTextureUnit
        glBindTextureUnit =__glBindTextureUnit_impl
    return __glBindTextureUnit_impl(unit,texture)

__glBindTextures_impl = None
def glBindTextures ( first:int,count:int,textures:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glBindTextures_impl
    if not __glBindTextures_impl:
        fptr = __pyglGetFuncAddress('glBindTextures')
        if not fptr:
            raise RuntimeError('The function glBindTextures is not available (maybe GL has not been initialized yet?)')
        __glBindTextures_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_void_p )(fptr)
        tmp = __glBindTextures_impl
        __glBindTextures_impl = (lambda first,count,textures: tmp(first,count,__pyglGetAsConstVoidPointer(textures)))
        global glBindTextures
        glBindTextures =__glBindTextures_impl
    return __glBindTextures_impl(first,count,textures)

__glBindTransformFeedback_impl = None
def glBindTransformFeedback ( target:int,id:int ) -> None :
    global __glBindTransformFeedback_impl
    if not __glBindTransformFeedback_impl:
        fptr = __pyglGetFuncAddress('glBindTransformFeedback')
        if not fptr:
            raise RuntimeError('The function glBindTransformFeedback is not available (maybe GL has not been initialized yet?)')
        __glBindTransformFeedback_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint )(fptr)
        global glBindTransformFeedback
        glBindTransformFeedback =__glBindTransformFeedback_impl
    return __glBindTransformFeedback_impl(target,id)

__glBindVertexArray_impl = None
def glBindVertexArray ( array:int ) -> None :
    global __glBindVertexArray_impl
    if not __glBindVertexArray_impl:
        fptr = __pyglGetFuncAddress('glBindVertexArray')
        if not fptr:
            raise RuntimeError('The function glBindVertexArray is not available (maybe GL has not been initialized yet?)')
        __glBindVertexArray_impl = __PYGL_FUNC_TYPE( None,c_uint )(fptr)
        global glBindVertexArray
        glBindVertexArray =__glBindVertexArray_impl
    return __glBindVertexArray_impl(array)

__glBindVertexBuffer_impl = None
def glBindVertexBuffer ( bindingindex:int,buffer:int,offset:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],stride:int ) -> None :
    global __glBindVertexBuffer_impl
    if not __glBindVertexBuffer_impl:
        fptr = __pyglGetFuncAddress('glBindVertexBuffer')
        if not fptr:
            raise RuntimeError('The function glBindVertexBuffer is not available (maybe GL has not been initialized yet?)')
        __glBindVertexBuffer_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_size_t,c_int )(fptr)
        global glBindVertexBuffer
        glBindVertexBuffer =__glBindVertexBuffer_impl
    return __glBindVertexBuffer_impl(bindingindex,buffer,offset,stride)

__glBindVertexBuffers_impl = None
def glBindVertexBuffers ( first:int,count:int,buffers:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],offsets:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],strides:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glBindVertexBuffers_impl
    if not __glBindVertexBuffers_impl:
        fptr = __pyglGetFuncAddress('glBindVertexBuffers')
        if not fptr:
            raise RuntimeError('The function glBindVertexBuffers is not available (maybe GL has not been initialized yet?)')
        __glBindVertexBuffers_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_void_p,c_void_p,c_void_p )(fptr)
        tmp = __glBindVertexBuffers_impl
        __glBindVertexBuffers_impl = (lambda first,count,buffers,offsets,strides: tmp(first,count,__pyglGetAsConstVoidPointer(buffers),__pyglGetAsConstVoidPointer(offsets),__pyglGetAsConstVoidPointer(strides)))
        global glBindVertexBuffers
        glBindVertexBuffers =__glBindVertexBuffers_impl
    return __glBindVertexBuffers_impl(first,count,buffers,offsets,strides)

__glBlendColor_impl = None
def glBlendColor ( red:float,green:float,blue:float,alpha:float ) -> None :
    global __glBlendColor_impl
    if not __glBlendColor_impl:
        fptr = __pyglGetFuncAddress('glBlendColor')
        if not fptr:
            raise RuntimeError('The function glBlendColor is not available (maybe GL has not been initialized yet?)')
        __glBlendColor_impl = __PYGL_FUNC_TYPE( None,c_float,c_float,c_float,c_float )(fptr)
        global glBlendColor
        glBlendColor =__glBlendColor_impl
    return __glBlendColor_impl(red,green,blue,alpha)

__glBlendEquation_impl = None
def glBlendEquation ( mode:int ) -> None :
    global __glBlendEquation_impl
    if not __glBlendEquation_impl:
        fptr = __pyglGetFuncAddress('glBlendEquation')
        if not fptr:
            raise RuntimeError('The function glBlendEquation is not available (maybe GL has not been initialized yet?)')
        __glBlendEquation_impl = __PYGL_FUNC_TYPE( None,c_uint )(fptr)
        global glBlendEquation
        glBlendEquation =__glBlendEquation_impl
    return __glBlendEquation_impl(mode)

__glBlendEquationSeparate_impl = None
def glBlendEquationSeparate ( modeRGB:int,modeAlpha:int ) -> None :
    global __glBlendEquationSeparate_impl
    if not __glBlendEquationSeparate_impl:
        fptr = __pyglGetFuncAddress('glBlendEquationSeparate')
        if not fptr:
            raise RuntimeError('The function glBlendEquationSeparate is not available (maybe GL has not been initialized yet?)')
        __glBlendEquationSeparate_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint )(fptr)
        global glBlendEquationSeparate
        glBlendEquationSeparate =__glBlendEquationSeparate_impl
    return __glBlendEquationSeparate_impl(modeRGB,modeAlpha)

__glBlendEquationSeparatei_impl = None
def glBlendEquationSeparatei ( buf:int,modeRGB:int,modeAlpha:int ) -> None :
    global __glBlendEquationSeparatei_impl
    if not __glBlendEquationSeparatei_impl:
        fptr = __pyglGetFuncAddress('glBlendEquationSeparatei')
        if not fptr:
            raise RuntimeError('The function glBlendEquationSeparatei is not available (maybe GL has not been initialized yet?)')
        __glBlendEquationSeparatei_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint )(fptr)
        global glBlendEquationSeparatei
        glBlendEquationSeparatei =__glBlendEquationSeparatei_impl
    return __glBlendEquationSeparatei_impl(buf,modeRGB,modeAlpha)

__glBlendEquationi_impl = None
def glBlendEquationi ( buf:int,mode:int ) -> None :
    global __glBlendEquationi_impl
    if not __glBlendEquationi_impl:
        fptr = __pyglGetFuncAddress('glBlendEquationi')
        if not fptr:
            raise RuntimeError('The function glBlendEquationi is not available (maybe GL has not been initialized yet?)')
        __glBlendEquationi_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint )(fptr)
        global glBlendEquationi
        glBlendEquationi =__glBlendEquationi_impl
    return __glBlendEquationi_impl(buf,mode)

__glBlendFunc_impl = None
def glBlendFunc ( sfactor:int,dfactor:int ) -> None :
    global __glBlendFunc_impl
    if not __glBlendFunc_impl:
        fptr = __pyglGetFuncAddress('glBlendFunc')
        if not fptr:
            raise RuntimeError('The function glBlendFunc is not available (maybe GL has not been initialized yet?)')
        __glBlendFunc_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint )(fptr)
        global glBlendFunc
        glBlendFunc =__glBlendFunc_impl
    return __glBlendFunc_impl(sfactor,dfactor)

__glBlendFuncSeparate_impl = None
def glBlendFuncSeparate ( sfactorRGB:int,dfactorRGB:int,sfactorAlpha:int,dfactorAlpha:int ) -> None :
    global __glBlendFuncSeparate_impl
    if not __glBlendFuncSeparate_impl:
        fptr = __pyglGetFuncAddress('glBlendFuncSeparate')
        if not fptr:
            raise RuntimeError('The function glBlendFuncSeparate is not available (maybe GL has not been initialized yet?)')
        __glBlendFuncSeparate_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint,c_uint )(fptr)
        global glBlendFuncSeparate
        glBlendFuncSeparate =__glBlendFuncSeparate_impl
    return __glBlendFuncSeparate_impl(sfactorRGB,dfactorRGB,sfactorAlpha,dfactorAlpha)

__glBlendFuncSeparatei_impl = None
def glBlendFuncSeparatei ( buf:int,srcRGB:int,dstRGB:int,srcAlpha:int,dstAlpha:int ) -> None :
    global __glBlendFuncSeparatei_impl
    if not __glBlendFuncSeparatei_impl:
        fptr = __pyglGetFuncAddress('glBlendFuncSeparatei')
        if not fptr:
            raise RuntimeError('The function glBlendFuncSeparatei is not available (maybe GL has not been initialized yet?)')
        __glBlendFuncSeparatei_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint,c_uint,c_uint )(fptr)
        global glBlendFuncSeparatei
        glBlendFuncSeparatei =__glBlendFuncSeparatei_impl
    return __glBlendFuncSeparatei_impl(buf,srcRGB,dstRGB,srcAlpha,dstAlpha)

__glBlendFunci_impl = None
def glBlendFunci ( buf:int,src:int,dst:int ) -> None :
    global __glBlendFunci_impl
    if not __glBlendFunci_impl:
        fptr = __pyglGetFuncAddress('glBlendFunci')
        if not fptr:
            raise RuntimeError('The function glBlendFunci is not available (maybe GL has not been initialized yet?)')
        __glBlendFunci_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint )(fptr)
        global glBlendFunci
        glBlendFunci =__glBlendFunci_impl
    return __glBlendFunci_impl(buf,src,dst)

__glBlitFramebuffer_impl = None
def glBlitFramebuffer ( srcX0:int,srcY0:int,srcX1:int,srcY1:int,dstX0:int,dstY0:int,dstX1:int,dstY1:int,mask:int,filter:int ) -> None :
    global __glBlitFramebuffer_impl
    if not __glBlitFramebuffer_impl:
        fptr = __pyglGetFuncAddress('glBlitFramebuffer')
        if not fptr:
            raise RuntimeError('The function glBlitFramebuffer is not available (maybe GL has not been initialized yet?)')
        __glBlitFramebuffer_impl = __PYGL_FUNC_TYPE( None,c_int,c_int,c_int,c_int,c_int,c_int,c_int,c_int,c_uint,c_uint )(fptr)
        global glBlitFramebuffer
        glBlitFramebuffer =__glBlitFramebuffer_impl
    return __glBlitFramebuffer_impl(srcX0,srcY0,srcX1,srcY1,dstX0,dstY0,dstX1,dstY1,mask,filter)

__glBlitNamedFramebuffer_impl = None
def glBlitNamedFramebuffer ( readFramebuffer:int,drawFramebuffer:int,srcX0:int,srcY0:int,srcX1:int,srcY1:int,dstX0:int,dstY0:int,dstX1:int,dstY1:int,mask:int,filter:int ) -> None :
    global __glBlitNamedFramebuffer_impl
    if not __glBlitNamedFramebuffer_impl:
        fptr = __pyglGetFuncAddress('glBlitNamedFramebuffer')
        if not fptr:
            raise RuntimeError('The function glBlitNamedFramebuffer is not available (maybe GL has not been initialized yet?)')
        __glBlitNamedFramebuffer_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_int,c_int,c_int,c_int,c_int,c_int,c_int,c_int,c_uint,c_uint )(fptr)
        global glBlitNamedFramebuffer
        glBlitNamedFramebuffer =__glBlitNamedFramebuffer_impl
    return __glBlitNamedFramebuffer_impl(readFramebuffer,drawFramebuffer,srcX0,srcY0,srcX1,srcY1,dstX0,dstY0,dstX1,dstY1,mask,filter)

__glBufferData_impl = None
def glBufferData ( target:int,size:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],data:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],usage:int ) -> None :
    global __glBufferData_impl
    if not __glBufferData_impl:
        fptr = __pyglGetFuncAddress('glBufferData')
        if not fptr:
            raise RuntimeError('The function glBufferData is not available (maybe GL has not been initialized yet?)')
        __glBufferData_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p,c_void_p,c_uint )(fptr)
        tmp = __glBufferData_impl
        __glBufferData_impl = (lambda target,size,data,usage: tmp(target,size,__pyglGetAsConstVoidPointer(data),usage))
    for _f in __universal_hooks:
        _f("glBufferData",glBufferData,target,size,data,usage)
    if 'glBufferData' in __hooks:
        for _f in __hooks['glBufferData']:
            _f("glBufferData",glBufferData,target,size,data,usage)
    rv = __glBufferData_impl(target,size,data,usage)
    if 'glBufferData' in __posthooks:
        for _f in __posthooks['glBufferData']:
            _f(rv,"glBufferData",glBufferData,target,size,data,usage)
    for _f in __universal_posthooks:
        _f(rv,"glBufferData",glBufferData,target,size,data,usage)
    return rv

__glBufferStorage_impl = None
def glBufferStorage ( target:int,size:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],data:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],flags:int ) -> None :
    global __glBufferStorage_impl
    if not __glBufferStorage_impl:
        fptr = __pyglGetFuncAddress('glBufferStorage')
        if not fptr:
            raise RuntimeError('The function glBufferStorage is not available (maybe GL has not been initialized yet?)')
        __glBufferStorage_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p,c_void_p,c_uint )(fptr)
        tmp = __glBufferStorage_impl
        __glBufferStorage_impl = (lambda target,size,data,flags: tmp(target,size,__pyglGetAsConstVoidPointer(data),flags))
        global glBufferStorage
        glBufferStorage =__glBufferStorage_impl
    return __glBufferStorage_impl(target,size,data,flags)

__glBufferSubData_impl = None
def glBufferSubData ( target:int,offset:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],size:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],data:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glBufferSubData_impl
    if not __glBufferSubData_impl:
        fptr = __pyglGetFuncAddress('glBufferSubData')
        if not fptr:
            raise RuntimeError('The function glBufferSubData is not available (maybe GL has not been initialized yet?)')
        __glBufferSubData_impl = __PYGL_FUNC_TYPE( None,c_uint,c_size_t,c_void_p,c_void_p )(fptr)
        tmp = __glBufferSubData_impl
        __glBufferSubData_impl = (lambda target,offset,size,data: tmp(target,offset,size,__pyglGetAsConstVoidPointer(data)))
        global glBufferSubData
        glBufferSubData =__glBufferSubData_impl
    return __glBufferSubData_impl(target,offset,size,data)

__glCheckFramebufferStatus_impl = None
def glCheckFramebufferStatus ( target:int ) -> int :
    global __glCheckFramebufferStatus_impl
    if not __glCheckFramebufferStatus_impl:
        fptr = __pyglGetFuncAddress('glCheckFramebufferStatus')
        if not fptr:
            raise RuntimeError('The function glCheckFramebufferStatus is not available (maybe GL has not been initialized yet?)')
        __glCheckFramebufferStatus_impl = __PYGL_FUNC_TYPE( c_uint,c_uint )(fptr)
        global glCheckFramebufferStatus
        glCheckFramebufferStatus =__glCheckFramebufferStatus_impl
    return __glCheckFramebufferStatus_impl(target)

__glCheckNamedFramebufferStatus_impl = None
def glCheckNamedFramebufferStatus ( framebuffer:int,target:int ) -> int :
    global __glCheckNamedFramebufferStatus_impl
    if not __glCheckNamedFramebufferStatus_impl:
        fptr = __pyglGetFuncAddress('glCheckNamedFramebufferStatus')
        if not fptr:
            raise RuntimeError('The function glCheckNamedFramebufferStatus is not available (maybe GL has not been initialized yet?)')
        __glCheckNamedFramebufferStatus_impl = __PYGL_FUNC_TYPE( c_uint,c_uint,c_uint )(fptr)
        global glCheckNamedFramebufferStatus
        glCheckNamedFramebufferStatus =__glCheckNamedFramebufferStatus_impl
    return __glCheckNamedFramebufferStatus_impl(framebuffer,target)

__glClampColor_impl = None
def glClampColor ( target:int,clamp:int ) -> None :
    global __glClampColor_impl
    if not __glClampColor_impl:
        fptr = __pyglGetFuncAddress('glClampColor')
        if not fptr:
            raise RuntimeError('The function glClampColor is not available (maybe GL has not been initialized yet?)')
        __glClampColor_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint )(fptr)
        global glClampColor
        glClampColor =__glClampColor_impl
    return __glClampColor_impl(target,clamp)

__glClear_impl = None
def glClear ( mask:int ) -> None :
    global __glClear_impl
    if not __glClear_impl:
        fptr = __pyglGetFuncAddress('glClear')
        if not fptr:
            raise RuntimeError('The function glClear is not available (maybe GL has not been initialized yet?)')
        __glClear_impl = __PYGL_FUNC_TYPE( None,c_uint )(fptr)
    for _f in __universal_hooks:
        _f("glClear",glClear,mask)
    if 'glClear' in __hooks:
        for _f in __hooks['glClear']:
            _f("glClear",glClear,mask)
    rv = __glClear_impl(mask)
    if 'glClear' in __posthooks:
        for _f in __posthooks['glClear']:
            _f(rv,"glClear",glClear,mask)
    for _f in __universal_posthooks:
        _f(rv,"glClear",glClear,mask)
    return rv

__glClearBufferData_impl = None
def glClearBufferData ( target:int,internalformat:int,format:int,type:int,data:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glClearBufferData_impl
    if not __glClearBufferData_impl:
        fptr = __pyglGetFuncAddress('glClearBufferData')
        if not fptr:
            raise RuntimeError('The function glClearBufferData is not available (maybe GL has not been initialized yet?)')
        __glClearBufferData_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glClearBufferData_impl
        __glClearBufferData_impl = (lambda target,internalformat,format,type,data: tmp(target,internalformat,format,type,__pyglGetAsConstVoidPointer(data)))
        global glClearBufferData
        glClearBufferData =__glClearBufferData_impl
    return __glClearBufferData_impl(target,internalformat,format,type,data)

__glClearBufferSubData_impl = None
def glClearBufferSubData ( target:int,internalformat:int,offset:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],size:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],format:int,type:int,data:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glClearBufferSubData_impl
    if not __glClearBufferSubData_impl:
        fptr = __pyglGetFuncAddress('glClearBufferSubData')
        if not fptr:
            raise RuntimeError('The function glClearBufferSubData is not available (maybe GL has not been initialized yet?)')
        __glClearBufferSubData_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_size_t,c_void_p,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glClearBufferSubData_impl
        __glClearBufferSubData_impl = (lambda target,internalformat,offset,size,format,type,data: tmp(target,internalformat,offset,size,format,type,__pyglGetAsConstVoidPointer(data)))
        global glClearBufferSubData
        glClearBufferSubData =__glClearBufferSubData_impl
    return __glClearBufferSubData_impl(target,internalformat,offset,size,format,type,data)

__glClearBufferfi_impl = None
def glClearBufferfi ( buffer:int,drawbuffer:int,depth:float,stencil:int ) -> None :
    global __glClearBufferfi_impl
    if not __glClearBufferfi_impl:
        fptr = __pyglGetFuncAddress('glClearBufferfi')
        if not fptr:
            raise RuntimeError('The function glClearBufferfi is not available (maybe GL has not been initialized yet?)')
        __glClearBufferfi_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_float,c_int )(fptr)
        global glClearBufferfi
        glClearBufferfi =__glClearBufferfi_impl
    return __glClearBufferfi_impl(buffer,drawbuffer,depth,stencil)

__glClearBufferfv_impl = None
def glClearBufferfv ( buffer:int,drawbuffer:int,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glClearBufferfv_impl
    if not __glClearBufferfv_impl:
        fptr = __pyglGetFuncAddress('glClearBufferfv')
        if not fptr:
            raise RuntimeError('The function glClearBufferfv is not available (maybe GL has not been initialized yet?)')
        __glClearBufferfv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_void_p )(fptr)
        tmp = __glClearBufferfv_impl
        __glClearBufferfv_impl = (lambda buffer,drawbuffer,value: tmp(buffer,drawbuffer,__pyglGetAsConstVoidPointer(value)))
        global glClearBufferfv
        glClearBufferfv =__glClearBufferfv_impl
    return __glClearBufferfv_impl(buffer,drawbuffer,value)

__glClearBufferiv_impl = None
def glClearBufferiv ( buffer:int,drawbuffer:int,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glClearBufferiv_impl
    if not __glClearBufferiv_impl:
        fptr = __pyglGetFuncAddress('glClearBufferiv')
        if not fptr:
            raise RuntimeError('The function glClearBufferiv is not available (maybe GL has not been initialized yet?)')
        __glClearBufferiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_void_p )(fptr)
        tmp = __glClearBufferiv_impl
        __glClearBufferiv_impl = (lambda buffer,drawbuffer,value: tmp(buffer,drawbuffer,__pyglGetAsConstVoidPointer(value)))
        global glClearBufferiv
        glClearBufferiv =__glClearBufferiv_impl
    return __glClearBufferiv_impl(buffer,drawbuffer,value)

__glClearBufferuiv_impl = None
def glClearBufferuiv ( buffer:int,drawbuffer:int,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glClearBufferuiv_impl
    if not __glClearBufferuiv_impl:
        fptr = __pyglGetFuncAddress('glClearBufferuiv')
        if not fptr:
            raise RuntimeError('The function glClearBufferuiv is not available (maybe GL has not been initialized yet?)')
        __glClearBufferuiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_void_p )(fptr)
        tmp = __glClearBufferuiv_impl
        __glClearBufferuiv_impl = (lambda buffer,drawbuffer,value: tmp(buffer,drawbuffer,__pyglGetAsConstVoidPointer(value)))
        global glClearBufferuiv
        glClearBufferuiv =__glClearBufferuiv_impl
    return __glClearBufferuiv_impl(buffer,drawbuffer,value)

__glClearColor_impl = None
def glClearColor ( red:float,green:float,blue:float,alpha:float ) -> None :
    global __glClearColor_impl
    if not __glClearColor_impl:
        fptr = __pyglGetFuncAddress('glClearColor')
        if not fptr:
            raise RuntimeError('The function glClearColor is not available (maybe GL has not been initialized yet?)')
        __glClearColor_impl = __PYGL_FUNC_TYPE( None,c_float,c_float,c_float,c_float )(fptr)
        global glClearColor
        glClearColor =__glClearColor_impl
    return __glClearColor_impl(red,green,blue,alpha)

__glClearDepth_impl = None
def glClearDepth ( depth:float ) -> None :
    global __glClearDepth_impl
    if not __glClearDepth_impl:
        fptr = __pyglGetFuncAddress('glClearDepth')
        if not fptr:
            raise RuntimeError('The function glClearDepth is not available (maybe GL has not been initialized yet?)')
        __glClearDepth_impl = __PYGL_FUNC_TYPE( None,c_double )(fptr)
        global glClearDepth
        glClearDepth =__glClearDepth_impl
    return __glClearDepth_impl(depth)

__glClearDepthf_impl = None
def glClearDepthf ( d:float ) -> None :
    global __glClearDepthf_impl
    if not __glClearDepthf_impl:
        fptr = __pyglGetFuncAddress('glClearDepthf')
        if not fptr:
            raise RuntimeError('The function glClearDepthf is not available (maybe GL has not been initialized yet?)')
        __glClearDepthf_impl = __PYGL_FUNC_TYPE( None,c_float )(fptr)
        global glClearDepthf
        glClearDepthf =__glClearDepthf_impl
    return __glClearDepthf_impl(d)

__glClearNamedBufferData_impl = None
def glClearNamedBufferData ( buffer:int,internalformat:int,format:int,type:int,data:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glClearNamedBufferData_impl
    if not __glClearNamedBufferData_impl:
        fptr = __pyglGetFuncAddress('glClearNamedBufferData')
        if not fptr:
            raise RuntimeError('The function glClearNamedBufferData is not available (maybe GL has not been initialized yet?)')
        __glClearNamedBufferData_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glClearNamedBufferData_impl
        __glClearNamedBufferData_impl = (lambda buffer,internalformat,format,type,data: tmp(buffer,internalformat,format,type,__pyglGetAsConstVoidPointer(data)))
        global glClearNamedBufferData
        glClearNamedBufferData =__glClearNamedBufferData_impl
    return __glClearNamedBufferData_impl(buffer,internalformat,format,type,data)

__glClearNamedBufferSubData_impl = None
def glClearNamedBufferSubData ( buffer:int,internalformat:int,offset:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],size:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],format:int,type:int,data:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glClearNamedBufferSubData_impl
    if not __glClearNamedBufferSubData_impl:
        fptr = __pyglGetFuncAddress('glClearNamedBufferSubData')
        if not fptr:
            raise RuntimeError('The function glClearNamedBufferSubData is not available (maybe GL has not been initialized yet?)')
        __glClearNamedBufferSubData_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_size_t,c_void_p,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glClearNamedBufferSubData_impl
        __glClearNamedBufferSubData_impl = (lambda buffer,internalformat,offset,size,format,type,data: tmp(buffer,internalformat,offset,size,format,type,__pyglGetAsConstVoidPointer(data)))
        global glClearNamedBufferSubData
        glClearNamedBufferSubData =__glClearNamedBufferSubData_impl
    return __glClearNamedBufferSubData_impl(buffer,internalformat,offset,size,format,type,data)

__glClearNamedFramebufferfi_impl = None
def glClearNamedFramebufferfi ( framebuffer:int,buffer:int,drawbuffer:int,depth:float,stencil:int ) -> None :
    global __glClearNamedFramebufferfi_impl
    if not __glClearNamedFramebufferfi_impl:
        fptr = __pyglGetFuncAddress('glClearNamedFramebufferfi')
        if not fptr:
            raise RuntimeError('The function glClearNamedFramebufferfi is not available (maybe GL has not been initialized yet?)')
        __glClearNamedFramebufferfi_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_int,c_float,c_int )(fptr)
        global glClearNamedFramebufferfi
        glClearNamedFramebufferfi =__glClearNamedFramebufferfi_impl
    return __glClearNamedFramebufferfi_impl(framebuffer,buffer,drawbuffer,depth,stencil)

__glClearNamedFramebufferfv_impl = None
def glClearNamedFramebufferfv ( framebuffer:int,buffer:int,drawbuffer:int,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glClearNamedFramebufferfv_impl
    if not __glClearNamedFramebufferfv_impl:
        fptr = __pyglGetFuncAddress('glClearNamedFramebufferfv')
        if not fptr:
            raise RuntimeError('The function glClearNamedFramebufferfv is not available (maybe GL has not been initialized yet?)')
        __glClearNamedFramebufferfv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_int,c_void_p )(fptr)
        tmp = __glClearNamedFramebufferfv_impl
        __glClearNamedFramebufferfv_impl = (lambda framebuffer,buffer,drawbuffer,value: tmp(framebuffer,buffer,drawbuffer,__pyglGetAsConstVoidPointer(value)))
        global glClearNamedFramebufferfv
        glClearNamedFramebufferfv =__glClearNamedFramebufferfv_impl
    return __glClearNamedFramebufferfv_impl(framebuffer,buffer,drawbuffer,value)

__glClearNamedFramebufferiv_impl = None
def glClearNamedFramebufferiv ( framebuffer:int,buffer:int,drawbuffer:int,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glClearNamedFramebufferiv_impl
    if not __glClearNamedFramebufferiv_impl:
        fptr = __pyglGetFuncAddress('glClearNamedFramebufferiv')
        if not fptr:
            raise RuntimeError('The function glClearNamedFramebufferiv is not available (maybe GL has not been initialized yet?)')
        __glClearNamedFramebufferiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_int,c_void_p )(fptr)
        tmp = __glClearNamedFramebufferiv_impl
        __glClearNamedFramebufferiv_impl = (lambda framebuffer,buffer,drawbuffer,value: tmp(framebuffer,buffer,drawbuffer,__pyglGetAsConstVoidPointer(value)))
        global glClearNamedFramebufferiv
        glClearNamedFramebufferiv =__glClearNamedFramebufferiv_impl
    return __glClearNamedFramebufferiv_impl(framebuffer,buffer,drawbuffer,value)

__glClearNamedFramebufferuiv_impl = None
def glClearNamedFramebufferuiv ( framebuffer:int,buffer:int,drawbuffer:int,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glClearNamedFramebufferuiv_impl
    if not __glClearNamedFramebufferuiv_impl:
        fptr = __pyglGetFuncAddress('glClearNamedFramebufferuiv')
        if not fptr:
            raise RuntimeError('The function glClearNamedFramebufferuiv is not available (maybe GL has not been initialized yet?)')
        __glClearNamedFramebufferuiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_int,c_void_p )(fptr)
        tmp = __glClearNamedFramebufferuiv_impl
        __glClearNamedFramebufferuiv_impl = (lambda framebuffer,buffer,drawbuffer,value: tmp(framebuffer,buffer,drawbuffer,__pyglGetAsConstVoidPointer(value)))
        global glClearNamedFramebufferuiv
        glClearNamedFramebufferuiv =__glClearNamedFramebufferuiv_impl
    return __glClearNamedFramebufferuiv_impl(framebuffer,buffer,drawbuffer,value)

__glClearStencil_impl = None
def glClearStencil ( s:int ) -> None :
    global __glClearStencil_impl
    if not __glClearStencil_impl:
        fptr = __pyglGetFuncAddress('glClearStencil')
        if not fptr:
            raise RuntimeError('The function glClearStencil is not available (maybe GL has not been initialized yet?)')
        __glClearStencil_impl = __PYGL_FUNC_TYPE( None,c_int )(fptr)
        global glClearStencil
        glClearStencil =__glClearStencil_impl
    return __glClearStencil_impl(s)

__glClearTexImage_impl = None
def glClearTexImage ( texture:int,level:int,format:int,type:int,data:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glClearTexImage_impl
    if not __glClearTexImage_impl:
        fptr = __pyglGetFuncAddress('glClearTexImage')
        if not fptr:
            raise RuntimeError('The function glClearTexImage is not available (maybe GL has not been initialized yet?)')
        __glClearTexImage_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glClearTexImage_impl
        __glClearTexImage_impl = (lambda texture,level,format,type,data: tmp(texture,level,format,type,__pyglGetAsConstVoidPointer(data)))
        global glClearTexImage
        glClearTexImage =__glClearTexImage_impl
    return __glClearTexImage_impl(texture,level,format,type,data)

__glClearTexSubImage_impl = None
def glClearTexSubImage ( texture:int,level:int,xoffset:int,yoffset:int,zoffset:int,width:int,height:int,depth:int,format:int,type:int,data:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glClearTexSubImage_impl
    if not __glClearTexSubImage_impl:
        fptr = __pyglGetFuncAddress('glClearTexSubImage')
        if not fptr:
            raise RuntimeError('The function glClearTexSubImage is not available (maybe GL has not been initialized yet?)')
        __glClearTexSubImage_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_int,c_int,c_int,c_int,c_int,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glClearTexSubImage_impl
        __glClearTexSubImage_impl = (lambda texture,level,xoffset,yoffset,zoffset,width,height,depth,format,type,data: tmp(texture,level,xoffset,yoffset,zoffset,width,height,depth,format,type,__pyglGetAsConstVoidPointer(data)))
        global glClearTexSubImage
        glClearTexSubImage =__glClearTexSubImage_impl
    return __glClearTexSubImage_impl(texture,level,xoffset,yoffset,zoffset,width,height,depth,format,type,data)

__glClientWaitSync_impl = None
def glClientWaitSync ( sync:typing.Any,flags:int,timeout:int ) -> int :
    global __glClientWaitSync_impl
    if not __glClientWaitSync_impl:
        fptr = __pyglGetFuncAddress('glClientWaitSync')
        if not fptr:
            raise RuntimeError('The function glClientWaitSync is not available (maybe GL has not been initialized yet?)')
        __glClientWaitSync_impl = __PYGL_FUNC_TYPE( c_uint,c_void_p,c_uint,c_ulonglong )(fptr)
        global glClientWaitSync
        glClientWaitSync =__glClientWaitSync_impl
    return __glClientWaitSync_impl(sync,flags,timeout)

__glClipControl_impl = None
def glClipControl ( origin:int,depth:int ) -> None :
    global __glClipControl_impl
    if not __glClipControl_impl:
        fptr = __pyglGetFuncAddress('glClipControl')
        if not fptr:
            raise RuntimeError('The function glClipControl is not available (maybe GL has not been initialized yet?)')
        __glClipControl_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint )(fptr)
        global glClipControl
        glClipControl =__glClipControl_impl
    return __glClipControl_impl(origin,depth)

__glColorMask_impl = None
def glColorMask ( red:bool,green:bool,blue:bool,alpha:bool ) -> None :
    global __glColorMask_impl
    if not __glColorMask_impl:
        fptr = __pyglGetFuncAddress('glColorMask')
        if not fptr:
            raise RuntimeError('The function glColorMask is not available (maybe GL has not been initialized yet?)')
        __glColorMask_impl = __PYGL_FUNC_TYPE( None,c_char,c_char,c_char,c_char )(fptr)
        global glColorMask
        glColorMask =__glColorMask_impl
    return __glColorMask_impl(red,green,blue,alpha)

__glColorMaski_impl = None
def glColorMaski ( index:int,r:bool,g:bool,b:bool,a:bool ) -> None :
    global __glColorMaski_impl
    if not __glColorMaski_impl:
        fptr = __pyglGetFuncAddress('glColorMaski')
        if not fptr:
            raise RuntimeError('The function glColorMaski is not available (maybe GL has not been initialized yet?)')
        __glColorMaski_impl = __PYGL_FUNC_TYPE( None,c_uint,c_char,c_char,c_char,c_char )(fptr)
        global glColorMaski
        glColorMaski =__glColorMaski_impl
    return __glColorMaski_impl(index,r,g,b,a)

__glCompileShader_impl = None
def glCompileShader ( shader:int ) -> None :
    global __glCompileShader_impl
    if not __glCompileShader_impl:
        fptr = __pyglGetFuncAddress('glCompileShader')
        if not fptr:
            raise RuntimeError('The function glCompileShader is not available (maybe GL has not been initialized yet?)')
        __glCompileShader_impl = __PYGL_FUNC_TYPE( None,c_uint )(fptr)
        global glCompileShader
        glCompileShader =__glCompileShader_impl
    return __glCompileShader_impl(shader)

__glCompressedTexImage1D_impl = None
def glCompressedTexImage1D ( target:int,level:int,internalformat:int,width:int,border:int,imageSize:int,data:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glCompressedTexImage1D_impl
    if not __glCompressedTexImage1D_impl:
        fptr = __pyglGetFuncAddress('glCompressedTexImage1D')
        if not fptr:
            raise RuntimeError('The function glCompressedTexImage1D is not available (maybe GL has not been initialized yet?)')
        __glCompressedTexImage1D_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_uint,c_int,c_int,c_int,c_void_p )(fptr)
        tmp = __glCompressedTexImage1D_impl
        __glCompressedTexImage1D_impl = (lambda target,level,internalformat,width,border,imageSize,data: tmp(target,level,internalformat,width,border,imageSize,__pyglGetAsConstVoidPointer(data)))
        global glCompressedTexImage1D
        glCompressedTexImage1D =__glCompressedTexImage1D_impl
    return __glCompressedTexImage1D_impl(target,level,internalformat,width,border,imageSize,data)

__glCompressedTexImage2D_impl = None
def glCompressedTexImage2D ( target:int,level:int,internalformat:int,width:int,height:int,border:int,imageSize:int,data:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glCompressedTexImage2D_impl
    if not __glCompressedTexImage2D_impl:
        fptr = __pyglGetFuncAddress('glCompressedTexImage2D')
        if not fptr:
            raise RuntimeError('The function glCompressedTexImage2D is not available (maybe GL has not been initialized yet?)')
        __glCompressedTexImage2D_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_uint,c_int,c_int,c_int,c_int,c_void_p )(fptr)
        tmp = __glCompressedTexImage2D_impl
        __glCompressedTexImage2D_impl = (lambda target,level,internalformat,width,height,border,imageSize,data: tmp(target,level,internalformat,width,height,border,imageSize,__pyglGetAsConstVoidPointer(data)))
        global glCompressedTexImage2D
        glCompressedTexImage2D =__glCompressedTexImage2D_impl
    return __glCompressedTexImage2D_impl(target,level,internalformat,width,height,border,imageSize,data)

__glCompressedTexImage3D_impl = None
def glCompressedTexImage3D ( target:int,level:int,internalformat:int,width:int,height:int,depth:int,border:int,imageSize:int,data:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glCompressedTexImage3D_impl
    if not __glCompressedTexImage3D_impl:
        fptr = __pyglGetFuncAddress('glCompressedTexImage3D')
        if not fptr:
            raise RuntimeError('The function glCompressedTexImage3D is not available (maybe GL has not been initialized yet?)')
        __glCompressedTexImage3D_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_uint,c_int,c_int,c_int,c_int,c_int,c_void_p )(fptr)
        tmp = __glCompressedTexImage3D_impl
        __glCompressedTexImage3D_impl = (lambda target,level,internalformat,width,height,depth,border,imageSize,data: tmp(target,level,internalformat,width,height,depth,border,imageSize,__pyglGetAsConstVoidPointer(data)))
        global glCompressedTexImage3D
        glCompressedTexImage3D =__glCompressedTexImage3D_impl
    return __glCompressedTexImage3D_impl(target,level,internalformat,width,height,depth,border,imageSize,data)

__glCompressedTexSubImage1D_impl = None
def glCompressedTexSubImage1D ( target:int,level:int,xoffset:int,width:int,format:int,imageSize:int,data:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glCompressedTexSubImage1D_impl
    if not __glCompressedTexSubImage1D_impl:
        fptr = __pyglGetFuncAddress('glCompressedTexSubImage1D')
        if not fptr:
            raise RuntimeError('The function glCompressedTexSubImage1D is not available (maybe GL has not been initialized yet?)')
        __glCompressedTexSubImage1D_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_int,c_uint,c_int,c_void_p )(fptr)
        tmp = __glCompressedTexSubImage1D_impl
        __glCompressedTexSubImage1D_impl = (lambda target,level,xoffset,width,format,imageSize,data: tmp(target,level,xoffset,width,format,imageSize,__pyglGetAsConstVoidPointer(data)))
        global glCompressedTexSubImage1D
        glCompressedTexSubImage1D =__glCompressedTexSubImage1D_impl
    return __glCompressedTexSubImage1D_impl(target,level,xoffset,width,format,imageSize,data)

__glCompressedTexSubImage2D_impl = None
def glCompressedTexSubImage2D ( target:int,level:int,xoffset:int,yoffset:int,width:int,height:int,format:int,imageSize:int,data:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glCompressedTexSubImage2D_impl
    if not __glCompressedTexSubImage2D_impl:
        fptr = __pyglGetFuncAddress('glCompressedTexSubImage2D')
        if not fptr:
            raise RuntimeError('The function glCompressedTexSubImage2D is not available (maybe GL has not been initialized yet?)')
        __glCompressedTexSubImage2D_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_int,c_int,c_int,c_uint,c_int,c_void_p )(fptr)
        tmp = __glCompressedTexSubImage2D_impl
        __glCompressedTexSubImage2D_impl = (lambda target,level,xoffset,yoffset,width,height,format,imageSize,data: tmp(target,level,xoffset,yoffset,width,height,format,imageSize,__pyglGetAsConstVoidPointer(data)))
        global glCompressedTexSubImage2D
        glCompressedTexSubImage2D =__glCompressedTexSubImage2D_impl
    return __glCompressedTexSubImage2D_impl(target,level,xoffset,yoffset,width,height,format,imageSize,data)

__glCompressedTexSubImage3D_impl = None
def glCompressedTexSubImage3D ( target:int,level:int,xoffset:int,yoffset:int,zoffset:int,width:int,height:int,depth:int,format:int,imageSize:int,data:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glCompressedTexSubImage3D_impl
    if not __glCompressedTexSubImage3D_impl:
        fptr = __pyglGetFuncAddress('glCompressedTexSubImage3D')
        if not fptr:
            raise RuntimeError('The function glCompressedTexSubImage3D is not available (maybe GL has not been initialized yet?)')
        __glCompressedTexSubImage3D_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_int,c_int,c_int,c_int,c_int,c_uint,c_int,c_void_p )(fptr)
        tmp = __glCompressedTexSubImage3D_impl
        __glCompressedTexSubImage3D_impl = (lambda target,level,xoffset,yoffset,zoffset,width,height,depth,format,imageSize,data: tmp(target,level,xoffset,yoffset,zoffset,width,height,depth,format,imageSize,__pyglGetAsConstVoidPointer(data)))
        global glCompressedTexSubImage3D
        glCompressedTexSubImage3D =__glCompressedTexSubImage3D_impl
    return __glCompressedTexSubImage3D_impl(target,level,xoffset,yoffset,zoffset,width,height,depth,format,imageSize,data)

__glCompressedTextureSubImage1D_impl = None
def glCompressedTextureSubImage1D ( texture:int,level:int,xoffset:int,width:int,format:int,imageSize:int,data:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glCompressedTextureSubImage1D_impl
    if not __glCompressedTextureSubImage1D_impl:
        fptr = __pyglGetFuncAddress('glCompressedTextureSubImage1D')
        if not fptr:
            raise RuntimeError('The function glCompressedTextureSubImage1D is not available (maybe GL has not been initialized yet?)')
        __glCompressedTextureSubImage1D_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_int,c_uint,c_int,c_void_p )(fptr)
        tmp = __glCompressedTextureSubImage1D_impl
        __glCompressedTextureSubImage1D_impl = (lambda texture,level,xoffset,width,format,imageSize,data: tmp(texture,level,xoffset,width,format,imageSize,__pyglGetAsConstVoidPointer(data)))
        global glCompressedTextureSubImage1D
        glCompressedTextureSubImage1D =__glCompressedTextureSubImage1D_impl
    return __glCompressedTextureSubImage1D_impl(texture,level,xoffset,width,format,imageSize,data)

__glCompressedTextureSubImage2D_impl = None
def glCompressedTextureSubImage2D ( texture:int,level:int,xoffset:int,yoffset:int,width:int,height:int,format:int,imageSize:int,data:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glCompressedTextureSubImage2D_impl
    if not __glCompressedTextureSubImage2D_impl:
        fptr = __pyglGetFuncAddress('glCompressedTextureSubImage2D')
        if not fptr:
            raise RuntimeError('The function glCompressedTextureSubImage2D is not available (maybe GL has not been initialized yet?)')
        __glCompressedTextureSubImage2D_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_int,c_int,c_int,c_uint,c_int,c_void_p )(fptr)
        tmp = __glCompressedTextureSubImage2D_impl
        __glCompressedTextureSubImage2D_impl = (lambda texture,level,xoffset,yoffset,width,height,format,imageSize,data: tmp(texture,level,xoffset,yoffset,width,height,format,imageSize,__pyglGetAsConstVoidPointer(data)))
        global glCompressedTextureSubImage2D
        glCompressedTextureSubImage2D =__glCompressedTextureSubImage2D_impl
    return __glCompressedTextureSubImage2D_impl(texture,level,xoffset,yoffset,width,height,format,imageSize,data)

__glCompressedTextureSubImage3D_impl = None
def glCompressedTextureSubImage3D ( texture:int,level:int,xoffset:int,yoffset:int,zoffset:int,width:int,height:int,depth:int,format:int,imageSize:int,data:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glCompressedTextureSubImage3D_impl
    if not __glCompressedTextureSubImage3D_impl:
        fptr = __pyglGetFuncAddress('glCompressedTextureSubImage3D')
        if not fptr:
            raise RuntimeError('The function glCompressedTextureSubImage3D is not available (maybe GL has not been initialized yet?)')
        __glCompressedTextureSubImage3D_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_int,c_int,c_int,c_int,c_int,c_uint,c_int,c_void_p )(fptr)
        tmp = __glCompressedTextureSubImage3D_impl
        __glCompressedTextureSubImage3D_impl = (lambda texture,level,xoffset,yoffset,zoffset,width,height,depth,format,imageSize,data: tmp(texture,level,xoffset,yoffset,zoffset,width,height,depth,format,imageSize,__pyglGetAsConstVoidPointer(data)))
        global glCompressedTextureSubImage3D
        glCompressedTextureSubImage3D =__glCompressedTextureSubImage3D_impl
    return __glCompressedTextureSubImage3D_impl(texture,level,xoffset,yoffset,zoffset,width,height,depth,format,imageSize,data)

__glCopyBufferSubData_impl = None
def glCopyBufferSubData ( readTarget:int,writeTarget:int,readOffset:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],writeOffset:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],size:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glCopyBufferSubData_impl
    if not __glCopyBufferSubData_impl:
        fptr = __pyglGetFuncAddress('glCopyBufferSubData')
        if not fptr:
            raise RuntimeError('The function glCopyBufferSubData is not available (maybe GL has not been initialized yet?)')
        __glCopyBufferSubData_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_size_t,c_size_t,c_void_p )(fptr)
        global glCopyBufferSubData
        glCopyBufferSubData =__glCopyBufferSubData_impl
    return __glCopyBufferSubData_impl(readTarget,writeTarget,readOffset,writeOffset,size)

__glCopyImageSubData_impl = None
def glCopyImageSubData ( srcName:int,srcTarget:int,srcLevel:int,srcX:int,srcY:int,srcZ:int,dstName:int,dstTarget:int,dstLevel:int,dstX:int,dstY:int,dstZ:int,srcWidth:int,srcHeight:int,srcDepth:int ) -> None :
    global __glCopyImageSubData_impl
    if not __glCopyImageSubData_impl:
        fptr = __pyglGetFuncAddress('glCopyImageSubData')
        if not fptr:
            raise RuntimeError('The function glCopyImageSubData is not available (maybe GL has not been initialized yet?)')
        __glCopyImageSubData_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_int,c_int,c_int,c_int,c_uint,c_uint,c_int,c_int,c_int,c_int,c_int,c_int,c_int )(fptr)
        global glCopyImageSubData
        glCopyImageSubData =__glCopyImageSubData_impl
    return __glCopyImageSubData_impl(srcName,srcTarget,srcLevel,srcX,srcY,srcZ,dstName,dstTarget,dstLevel,dstX,dstY,dstZ,srcWidth,srcHeight,srcDepth)

__glCopyNamedBufferSubData_impl = None
def glCopyNamedBufferSubData ( readBuffer:int,writeBuffer:int,readOffset:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],writeOffset:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],size:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glCopyNamedBufferSubData_impl
    if not __glCopyNamedBufferSubData_impl:
        fptr = __pyglGetFuncAddress('glCopyNamedBufferSubData')
        if not fptr:
            raise RuntimeError('The function glCopyNamedBufferSubData is not available (maybe GL has not been initialized yet?)')
        __glCopyNamedBufferSubData_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_size_t,c_size_t,c_void_p )(fptr)
        global glCopyNamedBufferSubData
        glCopyNamedBufferSubData =__glCopyNamedBufferSubData_impl
    return __glCopyNamedBufferSubData_impl(readBuffer,writeBuffer,readOffset,writeOffset,size)

__glCopyTexImage1D_impl = None
def glCopyTexImage1D ( target:int,level:int,internalformat:int,x:int,y:int,width:int,border:int ) -> None :
    global __glCopyTexImage1D_impl
    if not __glCopyTexImage1D_impl:
        fptr = __pyglGetFuncAddress('glCopyTexImage1D')
        if not fptr:
            raise RuntimeError('The function glCopyTexImage1D is not available (maybe GL has not been initialized yet?)')
        __glCopyTexImage1D_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_uint,c_int,c_int,c_int,c_int )(fptr)
        global glCopyTexImage1D
        glCopyTexImage1D =__glCopyTexImage1D_impl
    return __glCopyTexImage1D_impl(target,level,internalformat,x,y,width,border)

__glCopyTexImage2D_impl = None
def glCopyTexImage2D ( target:int,level:int,internalformat:int,x:int,y:int,width:int,height:int,border:int ) -> None :
    global __glCopyTexImage2D_impl
    if not __glCopyTexImage2D_impl:
        fptr = __pyglGetFuncAddress('glCopyTexImage2D')
        if not fptr:
            raise RuntimeError('The function glCopyTexImage2D is not available (maybe GL has not been initialized yet?)')
        __glCopyTexImage2D_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_uint,c_int,c_int,c_int,c_int,c_int )(fptr)
        global glCopyTexImage2D
        glCopyTexImage2D =__glCopyTexImage2D_impl
    return __glCopyTexImage2D_impl(target,level,internalformat,x,y,width,height,border)

__glCopyTexSubImage1D_impl = None
def glCopyTexSubImage1D ( target:int,level:int,xoffset:int,x:int,y:int,width:int ) -> None :
    global __glCopyTexSubImage1D_impl
    if not __glCopyTexSubImage1D_impl:
        fptr = __pyglGetFuncAddress('glCopyTexSubImage1D')
        if not fptr:
            raise RuntimeError('The function glCopyTexSubImage1D is not available (maybe GL has not been initialized yet?)')
        __glCopyTexSubImage1D_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_int,c_int,c_int )(fptr)
        global glCopyTexSubImage1D
        glCopyTexSubImage1D =__glCopyTexSubImage1D_impl
    return __glCopyTexSubImage1D_impl(target,level,xoffset,x,y,width)

__glCopyTexSubImage2D_impl = None
def glCopyTexSubImage2D ( target:int,level:int,xoffset:int,yoffset:int,x:int,y:int,width:int,height:int ) -> None :
    global __glCopyTexSubImage2D_impl
    if not __glCopyTexSubImage2D_impl:
        fptr = __pyglGetFuncAddress('glCopyTexSubImage2D')
        if not fptr:
            raise RuntimeError('The function glCopyTexSubImage2D is not available (maybe GL has not been initialized yet?)')
        __glCopyTexSubImage2D_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_int,c_int,c_int,c_int,c_int )(fptr)
        global glCopyTexSubImage2D
        glCopyTexSubImage2D =__glCopyTexSubImage2D_impl
    return __glCopyTexSubImage2D_impl(target,level,xoffset,yoffset,x,y,width,height)

__glCopyTexSubImage3D_impl = None
def glCopyTexSubImage3D ( target:int,level:int,xoffset:int,yoffset:int,zoffset:int,x:int,y:int,width:int,height:int ) -> None :
    global __glCopyTexSubImage3D_impl
    if not __glCopyTexSubImage3D_impl:
        fptr = __pyglGetFuncAddress('glCopyTexSubImage3D')
        if not fptr:
            raise RuntimeError('The function glCopyTexSubImage3D is not available (maybe GL has not been initialized yet?)')
        __glCopyTexSubImage3D_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_int,c_int,c_int,c_int,c_int,c_int )(fptr)
        global glCopyTexSubImage3D
        glCopyTexSubImage3D =__glCopyTexSubImage3D_impl
    return __glCopyTexSubImage3D_impl(target,level,xoffset,yoffset,zoffset,x,y,width,height)

__glCopyTextureSubImage1D_impl = None
def glCopyTextureSubImage1D ( texture:int,level:int,xoffset:int,x:int,y:int,width:int ) -> None :
    global __glCopyTextureSubImage1D_impl
    if not __glCopyTextureSubImage1D_impl:
        fptr = __pyglGetFuncAddress('glCopyTextureSubImage1D')
        if not fptr:
            raise RuntimeError('The function glCopyTextureSubImage1D is not available (maybe GL has not been initialized yet?)')
        __glCopyTextureSubImage1D_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_int,c_int,c_int )(fptr)
        global glCopyTextureSubImage1D
        glCopyTextureSubImage1D =__glCopyTextureSubImage1D_impl
    return __glCopyTextureSubImage1D_impl(texture,level,xoffset,x,y,width)

__glCopyTextureSubImage2D_impl = None
def glCopyTextureSubImage2D ( texture:int,level:int,xoffset:int,yoffset:int,x:int,y:int,width:int,height:int ) -> None :
    global __glCopyTextureSubImage2D_impl
    if not __glCopyTextureSubImage2D_impl:
        fptr = __pyglGetFuncAddress('glCopyTextureSubImage2D')
        if not fptr:
            raise RuntimeError('The function glCopyTextureSubImage2D is not available (maybe GL has not been initialized yet?)')
        __glCopyTextureSubImage2D_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_int,c_int,c_int,c_int,c_int )(fptr)
        global glCopyTextureSubImage2D
        glCopyTextureSubImage2D =__glCopyTextureSubImage2D_impl
    return __glCopyTextureSubImage2D_impl(texture,level,xoffset,yoffset,x,y,width,height)

__glCopyTextureSubImage3D_impl = None
def glCopyTextureSubImage3D ( texture:int,level:int,xoffset:int,yoffset:int,zoffset:int,x:int,y:int,width:int,height:int ) -> None :
    global __glCopyTextureSubImage3D_impl
    if not __glCopyTextureSubImage3D_impl:
        fptr = __pyglGetFuncAddress('glCopyTextureSubImage3D')
        if not fptr:
            raise RuntimeError('The function glCopyTextureSubImage3D is not available (maybe GL has not been initialized yet?)')
        __glCopyTextureSubImage3D_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_int,c_int,c_int,c_int,c_int,c_int )(fptr)
        global glCopyTextureSubImage3D
        glCopyTextureSubImage3D =__glCopyTextureSubImage3D_impl
    return __glCopyTextureSubImage3D_impl(texture,level,xoffset,yoffset,zoffset,x,y,width,height)

__glCreateBuffers_impl = None
def glCreateBuffers ( n:int,buffers:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glCreateBuffers_impl
    if not __glCreateBuffers_impl:
        fptr = __pyglGetFuncAddress('glCreateBuffers')
        if not fptr:
            raise RuntimeError('The function glCreateBuffers is not available (maybe GL has not been initialized yet?)')
        __glCreateBuffers_impl = __PYGL_FUNC_TYPE( None,c_int,c_void_p )(fptr)
        tmp = __glCreateBuffers_impl
        __glCreateBuffers_impl = (lambda n,buffers: tmp(n,(c_uint8*len(buffers)).from_buffer(buffers)))
        global glCreateBuffers
        glCreateBuffers =__glCreateBuffers_impl
    return __glCreateBuffers_impl(n,buffers)

__glCreateFramebuffers_impl = None
def glCreateFramebuffers ( n:int,framebuffers:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glCreateFramebuffers_impl
    if not __glCreateFramebuffers_impl:
        fptr = __pyglGetFuncAddress('glCreateFramebuffers')
        if not fptr:
            raise RuntimeError('The function glCreateFramebuffers is not available (maybe GL has not been initialized yet?)')
        __glCreateFramebuffers_impl = __PYGL_FUNC_TYPE( None,c_int,c_void_p )(fptr)
        tmp = __glCreateFramebuffers_impl
        __glCreateFramebuffers_impl = (lambda n,framebuffers: tmp(n,(c_uint8*len(framebuffers)).from_buffer(framebuffers)))
        global glCreateFramebuffers
        glCreateFramebuffers =__glCreateFramebuffers_impl
    return __glCreateFramebuffers_impl(n,framebuffers)

__glCreateProgram_impl = None
def glCreateProgram (  ) -> int :
    global __glCreateProgram_impl
    if not __glCreateProgram_impl:
        fptr = __pyglGetFuncAddress('glCreateProgram')
        if not fptr:
            raise RuntimeError('The function glCreateProgram is not available (maybe GL has not been initialized yet?)')
        __glCreateProgram_impl = __PYGL_FUNC_TYPE( c_uint )(fptr)
        global glCreateProgram
        glCreateProgram =__glCreateProgram_impl
    return __glCreateProgram_impl()

__glCreateProgramPipelines_impl = None
def glCreateProgramPipelines ( n:int,pipelines:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glCreateProgramPipelines_impl
    if not __glCreateProgramPipelines_impl:
        fptr = __pyglGetFuncAddress('glCreateProgramPipelines')
        if not fptr:
            raise RuntimeError('The function glCreateProgramPipelines is not available (maybe GL has not been initialized yet?)')
        __glCreateProgramPipelines_impl = __PYGL_FUNC_TYPE( None,c_int,c_void_p )(fptr)
        tmp = __glCreateProgramPipelines_impl
        __glCreateProgramPipelines_impl = (lambda n,pipelines: tmp(n,(c_uint8*len(pipelines)).from_buffer(pipelines)))
        global glCreateProgramPipelines
        glCreateProgramPipelines =__glCreateProgramPipelines_impl
    return __glCreateProgramPipelines_impl(n,pipelines)

__glCreateQueries_impl = None
def glCreateQueries ( target:int,n:int,ids:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glCreateQueries_impl
    if not __glCreateQueries_impl:
        fptr = __pyglGetFuncAddress('glCreateQueries')
        if not fptr:
            raise RuntimeError('The function glCreateQueries is not available (maybe GL has not been initialized yet?)')
        __glCreateQueries_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_void_p )(fptr)
        tmp = __glCreateQueries_impl
        __glCreateQueries_impl = (lambda target,n,ids: tmp(target,n,(c_uint8*len(ids)).from_buffer(ids)))
        global glCreateQueries
        glCreateQueries =__glCreateQueries_impl
    return __glCreateQueries_impl(target,n,ids)

__glCreateRenderbuffers_impl = None
def glCreateRenderbuffers ( n:int,renderbuffers:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glCreateRenderbuffers_impl
    if not __glCreateRenderbuffers_impl:
        fptr = __pyglGetFuncAddress('glCreateRenderbuffers')
        if not fptr:
            raise RuntimeError('The function glCreateRenderbuffers is not available (maybe GL has not been initialized yet?)')
        __glCreateRenderbuffers_impl = __PYGL_FUNC_TYPE( None,c_int,c_void_p )(fptr)
        tmp = __glCreateRenderbuffers_impl
        __glCreateRenderbuffers_impl = (lambda n,renderbuffers: tmp(n,(c_uint8*len(renderbuffers)).from_buffer(renderbuffers)))
        global glCreateRenderbuffers
        glCreateRenderbuffers =__glCreateRenderbuffers_impl
    return __glCreateRenderbuffers_impl(n,renderbuffers)

__glCreateSamplers_impl = None
def glCreateSamplers ( n:int,samplers:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glCreateSamplers_impl
    if not __glCreateSamplers_impl:
        fptr = __pyglGetFuncAddress('glCreateSamplers')
        if not fptr:
            raise RuntimeError('The function glCreateSamplers is not available (maybe GL has not been initialized yet?)')
        __glCreateSamplers_impl = __PYGL_FUNC_TYPE( None,c_int,c_void_p )(fptr)
        tmp = __glCreateSamplers_impl
        __glCreateSamplers_impl = (lambda n,samplers: tmp(n,(c_uint8*len(samplers)).from_buffer(samplers)))
        global glCreateSamplers
        glCreateSamplers =__glCreateSamplers_impl
    return __glCreateSamplers_impl(n,samplers)

__glCreateShader_impl = None
def glCreateShader ( type:int ) -> int :
    global __glCreateShader_impl
    if not __glCreateShader_impl:
        fptr = __pyglGetFuncAddress('glCreateShader')
        if not fptr:
            raise RuntimeError('The function glCreateShader is not available (maybe GL has not been initialized yet?)')
        __glCreateShader_impl = __PYGL_FUNC_TYPE( c_uint,c_uint )(fptr)
        global glCreateShader
        glCreateShader =__glCreateShader_impl
    return __glCreateShader_impl(type)

__glCreateShaderProgramv_impl = None
def glCreateShaderProgramv ( type:int,count:int,strings:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> int :
    global __glCreateShaderProgramv_impl
    if not __glCreateShaderProgramv_impl:
        fptr = __pyglGetFuncAddress('glCreateShaderProgramv')
        if not fptr:
            raise RuntimeError('The function glCreateShaderProgramv is not available (maybe GL has not been initialized yet?)')
        __glCreateShaderProgramv_impl = __PYGL_FUNC_TYPE( c_uint,c_uint,c_int,c_void_p )(fptr)
        tmp = __glCreateShaderProgramv_impl
        __glCreateShaderProgramv_impl = (lambda type,count,strings: tmp(type,count,c_char_p(strings.encode())))
        global glCreateShaderProgramv
        glCreateShaderProgramv =__glCreateShaderProgramv_impl
    return __glCreateShaderProgramv_impl(type,count,strings)

__glCreateTextures_impl = None
def glCreateTextures ( target:int,n:int,textures:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glCreateTextures_impl
    if not __glCreateTextures_impl:
        fptr = __pyglGetFuncAddress('glCreateTextures')
        if not fptr:
            raise RuntimeError('The function glCreateTextures is not available (maybe GL has not been initialized yet?)')
        __glCreateTextures_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_void_p )(fptr)
        tmp = __glCreateTextures_impl
        __glCreateTextures_impl = (lambda target,n,textures: tmp(target,n,(c_uint8*len(textures)).from_buffer(textures)))
        global glCreateTextures
        glCreateTextures =__glCreateTextures_impl
    return __glCreateTextures_impl(target,n,textures)

__glCreateTransformFeedbacks_impl = None
def glCreateTransformFeedbacks ( n:int,ids:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glCreateTransformFeedbacks_impl
    if not __glCreateTransformFeedbacks_impl:
        fptr = __pyglGetFuncAddress('glCreateTransformFeedbacks')
        if not fptr:
            raise RuntimeError('The function glCreateTransformFeedbacks is not available (maybe GL has not been initialized yet?)')
        __glCreateTransformFeedbacks_impl = __PYGL_FUNC_TYPE( None,c_int,c_void_p )(fptr)
        tmp = __glCreateTransformFeedbacks_impl
        __glCreateTransformFeedbacks_impl = (lambda n,ids: tmp(n,(c_uint8*len(ids)).from_buffer(ids)))
        global glCreateTransformFeedbacks
        glCreateTransformFeedbacks =__glCreateTransformFeedbacks_impl
    return __glCreateTransformFeedbacks_impl(n,ids)

__glCreateVertexArrays_impl = None
def glCreateVertexArrays ( n:int,arrays:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glCreateVertexArrays_impl
    if not __glCreateVertexArrays_impl:
        fptr = __pyglGetFuncAddress('glCreateVertexArrays')
        if not fptr:
            raise RuntimeError('The function glCreateVertexArrays is not available (maybe GL has not been initialized yet?)')
        __glCreateVertexArrays_impl = __PYGL_FUNC_TYPE( None,c_int,c_void_p )(fptr)
        tmp = __glCreateVertexArrays_impl
        __glCreateVertexArrays_impl = (lambda n,arrays: tmp(n,(c_uint8*len(arrays)).from_buffer(arrays)))
        global glCreateVertexArrays
        glCreateVertexArrays =__glCreateVertexArrays_impl
    return __glCreateVertexArrays_impl(n,arrays)

__glCullFace_impl = None
def glCullFace ( mode:int ) -> None :
    global __glCullFace_impl
    if not __glCullFace_impl:
        fptr = __pyglGetFuncAddress('glCullFace')
        if not fptr:
            raise RuntimeError('The function glCullFace is not available (maybe GL has not been initialized yet?)')
        __glCullFace_impl = __PYGL_FUNC_TYPE( None,c_uint )(fptr)
        global glCullFace
        glCullFace =__glCullFace_impl
    return __glCullFace_impl(mode)

__glDebugMessageControl_impl = None
def glDebugMessageControl ( source:int,type:int,severity:int,count:int,ids:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],enabled:bool ) -> None :
    global __glDebugMessageControl_impl
    if not __glDebugMessageControl_impl:
        fptr = __pyglGetFuncAddress('glDebugMessageControl')
        if not fptr:
            raise RuntimeError('The function glDebugMessageControl is not available (maybe GL has not been initialized yet?)')
        __glDebugMessageControl_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint,c_int,c_void_p,c_char )(fptr)
        tmp = __glDebugMessageControl_impl
        __glDebugMessageControl_impl = (lambda source,type,severity,count,ids,enabled: tmp(source,type,severity,count,__pyglGetAsConstVoidPointer(ids),enabled))
        global glDebugMessageControl
        glDebugMessageControl =__glDebugMessageControl_impl
    return __glDebugMessageControl_impl(source,type,severity,count,ids,enabled)

__glDebugMessageInsert_impl = None
def glDebugMessageInsert ( source:int,type:int,id:int,severity:int,length:int,buf:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glDebugMessageInsert_impl
    if not __glDebugMessageInsert_impl:
        fptr = __pyglGetFuncAddress('glDebugMessageInsert')
        if not fptr:
            raise RuntimeError('The function glDebugMessageInsert is not available (maybe GL has not been initialized yet?)')
        __glDebugMessageInsert_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint,c_uint,c_int,c_void_p )(fptr)
        tmp = __glDebugMessageInsert_impl
        __glDebugMessageInsert_impl = (lambda source,type,id,severity,length,buf: tmp(source,type,id,severity,length,c_char_p(buf.encode())))
        global glDebugMessageInsert
        glDebugMessageInsert =__glDebugMessageInsert_impl
    return __glDebugMessageInsert_impl(source,type,id,severity,length,buf)

__glDeleteBuffers_impl = None
def glDeleteBuffers ( n:int,buffers:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glDeleteBuffers_impl
    if not __glDeleteBuffers_impl:
        fptr = __pyglGetFuncAddress('glDeleteBuffers')
        if not fptr:
            raise RuntimeError('The function glDeleteBuffers is not available (maybe GL has not been initialized yet?)')
        __glDeleteBuffers_impl = __PYGL_FUNC_TYPE( None,c_int,c_void_p )(fptr)
        tmp = __glDeleteBuffers_impl
        __glDeleteBuffers_impl = (lambda n,buffers: tmp(n,__pyglGetAsConstVoidPointer(buffers)))
        global glDeleteBuffers
        glDeleteBuffers =__glDeleteBuffers_impl
    return __glDeleteBuffers_impl(n,buffers)

__glDeleteFramebuffers_impl = None
def glDeleteFramebuffers ( n:int,framebuffers:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glDeleteFramebuffers_impl
    if not __glDeleteFramebuffers_impl:
        fptr = __pyglGetFuncAddress('glDeleteFramebuffers')
        if not fptr:
            raise RuntimeError('The function glDeleteFramebuffers is not available (maybe GL has not been initialized yet?)')
        __glDeleteFramebuffers_impl = __PYGL_FUNC_TYPE( None,c_int,c_void_p )(fptr)
        tmp = __glDeleteFramebuffers_impl
        __glDeleteFramebuffers_impl = (lambda n,framebuffers: tmp(n,__pyglGetAsConstVoidPointer(framebuffers)))
        global glDeleteFramebuffers
        glDeleteFramebuffers =__glDeleteFramebuffers_impl
    return __glDeleteFramebuffers_impl(n,framebuffers)

__glDeleteProgram_impl = None
def glDeleteProgram ( program:int ) -> None :
    global __glDeleteProgram_impl
    if not __glDeleteProgram_impl:
        fptr = __pyglGetFuncAddress('glDeleteProgram')
        if not fptr:
            raise RuntimeError('The function glDeleteProgram is not available (maybe GL has not been initialized yet?)')
        __glDeleteProgram_impl = __PYGL_FUNC_TYPE( None,c_uint )(fptr)
        global glDeleteProgram
        glDeleteProgram =__glDeleteProgram_impl
    return __glDeleteProgram_impl(program)

__glDeleteProgramPipelines_impl = None
def glDeleteProgramPipelines ( n:int,pipelines:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glDeleteProgramPipelines_impl
    if not __glDeleteProgramPipelines_impl:
        fptr = __pyglGetFuncAddress('glDeleteProgramPipelines')
        if not fptr:
            raise RuntimeError('The function glDeleteProgramPipelines is not available (maybe GL has not been initialized yet?)')
        __glDeleteProgramPipelines_impl = __PYGL_FUNC_TYPE( None,c_int,c_void_p )(fptr)
        tmp = __glDeleteProgramPipelines_impl
        __glDeleteProgramPipelines_impl = (lambda n,pipelines: tmp(n,__pyglGetAsConstVoidPointer(pipelines)))
        global glDeleteProgramPipelines
        glDeleteProgramPipelines =__glDeleteProgramPipelines_impl
    return __glDeleteProgramPipelines_impl(n,pipelines)

__glDeleteQueries_impl = None
def glDeleteQueries ( n:int,ids:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glDeleteQueries_impl
    if not __glDeleteQueries_impl:
        fptr = __pyglGetFuncAddress('glDeleteQueries')
        if not fptr:
            raise RuntimeError('The function glDeleteQueries is not available (maybe GL has not been initialized yet?)')
        __glDeleteQueries_impl = __PYGL_FUNC_TYPE( None,c_int,c_void_p )(fptr)
        tmp = __glDeleteQueries_impl
        __glDeleteQueries_impl = (lambda n,ids: tmp(n,__pyglGetAsConstVoidPointer(ids)))
        global glDeleteQueries
        glDeleteQueries =__glDeleteQueries_impl
    return __glDeleteQueries_impl(n,ids)

__glDeleteRenderbuffers_impl = None
def glDeleteRenderbuffers ( n:int,renderbuffers:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glDeleteRenderbuffers_impl
    if not __glDeleteRenderbuffers_impl:
        fptr = __pyglGetFuncAddress('glDeleteRenderbuffers')
        if not fptr:
            raise RuntimeError('The function glDeleteRenderbuffers is not available (maybe GL has not been initialized yet?)')
        __glDeleteRenderbuffers_impl = __PYGL_FUNC_TYPE( None,c_int,c_void_p )(fptr)
        tmp = __glDeleteRenderbuffers_impl
        __glDeleteRenderbuffers_impl = (lambda n,renderbuffers: tmp(n,__pyglGetAsConstVoidPointer(renderbuffers)))
        global glDeleteRenderbuffers
        glDeleteRenderbuffers =__glDeleteRenderbuffers_impl
    return __glDeleteRenderbuffers_impl(n,renderbuffers)

__glDeleteSamplers_impl = None
def glDeleteSamplers ( count:int,samplers:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glDeleteSamplers_impl
    if not __glDeleteSamplers_impl:
        fptr = __pyglGetFuncAddress('glDeleteSamplers')
        if not fptr:
            raise RuntimeError('The function glDeleteSamplers is not available (maybe GL has not been initialized yet?)')
        __glDeleteSamplers_impl = __PYGL_FUNC_TYPE( None,c_int,c_void_p )(fptr)
        tmp = __glDeleteSamplers_impl
        __glDeleteSamplers_impl = (lambda count,samplers: tmp(count,__pyglGetAsConstVoidPointer(samplers)))
        global glDeleteSamplers
        glDeleteSamplers =__glDeleteSamplers_impl
    return __glDeleteSamplers_impl(count,samplers)

__glDeleteShader_impl = None
def glDeleteShader ( shader:int ) -> None :
    global __glDeleteShader_impl
    if not __glDeleteShader_impl:
        fptr = __pyglGetFuncAddress('glDeleteShader')
        if not fptr:
            raise RuntimeError('The function glDeleteShader is not available (maybe GL has not been initialized yet?)')
        __glDeleteShader_impl = __PYGL_FUNC_TYPE( None,c_uint )(fptr)
        global glDeleteShader
        glDeleteShader =__glDeleteShader_impl
    return __glDeleteShader_impl(shader)

__glDeleteSync_impl = None
def glDeleteSync ( sync:typing.Any ) -> None :
    global __glDeleteSync_impl
    if not __glDeleteSync_impl:
        fptr = __pyglGetFuncAddress('glDeleteSync')
        if not fptr:
            raise RuntimeError('The function glDeleteSync is not available (maybe GL has not been initialized yet?)')
        __glDeleteSync_impl = __PYGL_FUNC_TYPE( None,c_void_p )(fptr)
        global glDeleteSync
        glDeleteSync =__glDeleteSync_impl
    return __glDeleteSync_impl(sync)

__glDeleteTextures_impl = None
def glDeleteTextures ( n:int,textures:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glDeleteTextures_impl
    if not __glDeleteTextures_impl:
        fptr = __pyglGetFuncAddress('glDeleteTextures')
        if not fptr:
            raise RuntimeError('The function glDeleteTextures is not available (maybe GL has not been initialized yet?)')
        __glDeleteTextures_impl = __PYGL_FUNC_TYPE( None,c_int,c_void_p )(fptr)
        tmp = __glDeleteTextures_impl
        __glDeleteTextures_impl = (lambda n,textures: tmp(n,__pyglGetAsConstVoidPointer(textures)))
        global glDeleteTextures
        glDeleteTextures =__glDeleteTextures_impl
    return __glDeleteTextures_impl(n,textures)

__glDeleteTransformFeedbacks_impl = None
def glDeleteTransformFeedbacks ( n:int,ids:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glDeleteTransformFeedbacks_impl
    if not __glDeleteTransformFeedbacks_impl:
        fptr = __pyglGetFuncAddress('glDeleteTransformFeedbacks')
        if not fptr:
            raise RuntimeError('The function glDeleteTransformFeedbacks is not available (maybe GL has not been initialized yet?)')
        __glDeleteTransformFeedbacks_impl = __PYGL_FUNC_TYPE( None,c_int,c_void_p )(fptr)
        tmp = __glDeleteTransformFeedbacks_impl
        __glDeleteTransformFeedbacks_impl = (lambda n,ids: tmp(n,__pyglGetAsConstVoidPointer(ids)))
        global glDeleteTransformFeedbacks
        glDeleteTransformFeedbacks =__glDeleteTransformFeedbacks_impl
    return __glDeleteTransformFeedbacks_impl(n,ids)

__glDeleteVertexArrays_impl = None
def glDeleteVertexArrays ( n:int,arrays:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glDeleteVertexArrays_impl
    if not __glDeleteVertexArrays_impl:
        fptr = __pyglGetFuncAddress('glDeleteVertexArrays')
        if not fptr:
            raise RuntimeError('The function glDeleteVertexArrays is not available (maybe GL has not been initialized yet?)')
        __glDeleteVertexArrays_impl = __PYGL_FUNC_TYPE( None,c_int,c_void_p )(fptr)
        tmp = __glDeleteVertexArrays_impl
        __glDeleteVertexArrays_impl = (lambda n,arrays: tmp(n,__pyglGetAsConstVoidPointer(arrays)))
        global glDeleteVertexArrays
        glDeleteVertexArrays =__glDeleteVertexArrays_impl
    return __glDeleteVertexArrays_impl(n,arrays)

__glDepthFunc_impl = None
def glDepthFunc ( func:int ) -> None :
    global __glDepthFunc_impl
    if not __glDepthFunc_impl:
        fptr = __pyglGetFuncAddress('glDepthFunc')
        if not fptr:
            raise RuntimeError('The function glDepthFunc is not available (maybe GL has not been initialized yet?)')
        __glDepthFunc_impl = __PYGL_FUNC_TYPE( None,c_uint )(fptr)
        global glDepthFunc
        glDepthFunc =__glDepthFunc_impl
    return __glDepthFunc_impl(func)

__glDepthMask_impl = None
def glDepthMask ( flag:bool ) -> None :
    global __glDepthMask_impl
    if not __glDepthMask_impl:
        fptr = __pyglGetFuncAddress('glDepthMask')
        if not fptr:
            raise RuntimeError('The function glDepthMask is not available (maybe GL has not been initialized yet?)')
        __glDepthMask_impl = __PYGL_FUNC_TYPE( None,c_char )(fptr)
        global glDepthMask
        glDepthMask =__glDepthMask_impl
    return __glDepthMask_impl(flag)

__glDepthRange_impl = None
def glDepthRange ( near:float,far:float ) -> None :
    global __glDepthRange_impl
    if not __glDepthRange_impl:
        fptr = __pyglGetFuncAddress('glDepthRange')
        if not fptr:
            raise RuntimeError('The function glDepthRange is not available (maybe GL has not been initialized yet?)')
        __glDepthRange_impl = __PYGL_FUNC_TYPE( None,c_double,c_double )(fptr)
        global glDepthRange
        glDepthRange =__glDepthRange_impl
    return __glDepthRange_impl(near,far)

__glDepthRangeArrayv_impl = None
def glDepthRangeArrayv ( first:int,count:int,v:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glDepthRangeArrayv_impl
    if not __glDepthRangeArrayv_impl:
        fptr = __pyglGetFuncAddress('glDepthRangeArrayv')
        if not fptr:
            raise RuntimeError('The function glDepthRangeArrayv is not available (maybe GL has not been initialized yet?)')
        __glDepthRangeArrayv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_void_p )(fptr)
        tmp = __glDepthRangeArrayv_impl
        __glDepthRangeArrayv_impl = (lambda first,count,v: tmp(first,count,__pyglGetAsConstVoidPointer(v)))
        global glDepthRangeArrayv
        glDepthRangeArrayv =__glDepthRangeArrayv_impl
    return __glDepthRangeArrayv_impl(first,count,v)

__glDepthRangeIndexed_impl = None
def glDepthRangeIndexed ( index:int,n:float,f:float ) -> None :
    global __glDepthRangeIndexed_impl
    if not __glDepthRangeIndexed_impl:
        fptr = __pyglGetFuncAddress('glDepthRangeIndexed')
        if not fptr:
            raise RuntimeError('The function glDepthRangeIndexed is not available (maybe GL has not been initialized yet?)')
        __glDepthRangeIndexed_impl = __PYGL_FUNC_TYPE( None,c_uint,c_double,c_double )(fptr)
        global glDepthRangeIndexed
        glDepthRangeIndexed =__glDepthRangeIndexed_impl
    return __glDepthRangeIndexed_impl(index,n,f)

__glDepthRangef_impl = None
def glDepthRangef ( n:float,f:float ) -> None :
    global __glDepthRangef_impl
    if not __glDepthRangef_impl:
        fptr = __pyglGetFuncAddress('glDepthRangef')
        if not fptr:
            raise RuntimeError('The function glDepthRangef is not available (maybe GL has not been initialized yet?)')
        __glDepthRangef_impl = __PYGL_FUNC_TYPE( None,c_float,c_float )(fptr)
        global glDepthRangef
        glDepthRangef =__glDepthRangef_impl
    return __glDepthRangef_impl(n,f)

__glDetachShader_impl = None
def glDetachShader ( program:int,shader:int ) -> None :
    global __glDetachShader_impl
    if not __glDetachShader_impl:
        fptr = __pyglGetFuncAddress('glDetachShader')
        if not fptr:
            raise RuntimeError('The function glDetachShader is not available (maybe GL has not been initialized yet?)')
        __glDetachShader_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint )(fptr)
        global glDetachShader
        glDetachShader =__glDetachShader_impl
    return __glDetachShader_impl(program,shader)

__glDisable_impl = None
def glDisable ( cap:int ) -> None :
    global __glDisable_impl
    if not __glDisable_impl:
        fptr = __pyglGetFuncAddress('glDisable')
        if not fptr:
            raise RuntimeError('The function glDisable is not available (maybe GL has not been initialized yet?)')
        __glDisable_impl = __PYGL_FUNC_TYPE( None,c_uint )(fptr)
        global glDisable
        glDisable =__glDisable_impl
    return __glDisable_impl(cap)

__glDisableVertexArrayAttrib_impl = None
def glDisableVertexArrayAttrib ( vaobj:int,index:int ) -> None :
    global __glDisableVertexArrayAttrib_impl
    if not __glDisableVertexArrayAttrib_impl:
        fptr = __pyglGetFuncAddress('glDisableVertexArrayAttrib')
        if not fptr:
            raise RuntimeError('The function glDisableVertexArrayAttrib is not available (maybe GL has not been initialized yet?)')
        __glDisableVertexArrayAttrib_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint )(fptr)
        global glDisableVertexArrayAttrib
        glDisableVertexArrayAttrib =__glDisableVertexArrayAttrib_impl
    return __glDisableVertexArrayAttrib_impl(vaobj,index)

__glDisableVertexAttribArray_impl = None
def glDisableVertexAttribArray ( index:int ) -> None :
    global __glDisableVertexAttribArray_impl
    if not __glDisableVertexAttribArray_impl:
        fptr = __pyglGetFuncAddress('glDisableVertexAttribArray')
        if not fptr:
            raise RuntimeError('The function glDisableVertexAttribArray is not available (maybe GL has not been initialized yet?)')
        __glDisableVertexAttribArray_impl = __PYGL_FUNC_TYPE( None,c_uint )(fptr)
        global glDisableVertexAttribArray
        glDisableVertexAttribArray =__glDisableVertexAttribArray_impl
    return __glDisableVertexAttribArray_impl(index)

__glDisablei_impl = None
def glDisablei ( target:int,index:int ) -> None :
    global __glDisablei_impl
    if not __glDisablei_impl:
        fptr = __pyglGetFuncAddress('glDisablei')
        if not fptr:
            raise RuntimeError('The function glDisablei is not available (maybe GL has not been initialized yet?)')
        __glDisablei_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint )(fptr)
        global glDisablei
        glDisablei =__glDisablei_impl
    return __glDisablei_impl(target,index)

__glDispatchCompute_impl = None
def glDispatchCompute ( num_groups_x:int,num_groups_y:int,num_groups_z:int ) -> None :
    global __glDispatchCompute_impl
    if not __glDispatchCompute_impl:
        fptr = __pyglGetFuncAddress('glDispatchCompute')
        if not fptr:
            raise RuntimeError('The function glDispatchCompute is not available (maybe GL has not been initialized yet?)')
        __glDispatchCompute_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint )(fptr)
    for _f in __universal_hooks:
        _f("glDispatchCompute",glDispatchCompute,num_groups_x,num_groups_y,num_groups_z)
    if 'glDispatchCompute' in __hooks:
        for _f in __hooks['glDispatchCompute']:
            _f("glDispatchCompute",glDispatchCompute,num_groups_x,num_groups_y,num_groups_z)
    rv = __glDispatchCompute_impl(num_groups_x,num_groups_y,num_groups_z)
    if 'glDispatchCompute' in __posthooks:
        for _f in __posthooks['glDispatchCompute']:
            _f(rv,"glDispatchCompute",glDispatchCompute,num_groups_x,num_groups_y,num_groups_z)
    for _f in __universal_posthooks:
        _f(rv,"glDispatchCompute",glDispatchCompute,num_groups_x,num_groups_y,num_groups_z)
    return rv

__glDispatchComputeIndirect_impl = None
def glDispatchComputeIndirect ( indirect:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glDispatchComputeIndirect_impl
    if not __glDispatchComputeIndirect_impl:
        fptr = __pyglGetFuncAddress('glDispatchComputeIndirect')
        if not fptr:
            raise RuntimeError('The function glDispatchComputeIndirect is not available (maybe GL has not been initialized yet?)')
        __glDispatchComputeIndirect_impl = __PYGL_FUNC_TYPE( None,c_size_t )(fptr)
    for _f in __universal_hooks:
        _f("glDispatchComputeIndirect",glDispatchComputeIndirect,indirect)
    if 'glDispatchComputeIndirect' in __hooks:
        for _f in __hooks['glDispatchComputeIndirect']:
            _f("glDispatchComputeIndirect",glDispatchComputeIndirect,indirect)
    rv = __glDispatchComputeIndirect_impl(indirect)
    if 'glDispatchComputeIndirect' in __posthooks:
        for _f in __posthooks['glDispatchComputeIndirect']:
            _f(rv,"glDispatchComputeIndirect",glDispatchComputeIndirect,indirect)
    for _f in __universal_posthooks:
        _f(rv,"glDispatchComputeIndirect",glDispatchComputeIndirect,indirect)
    return rv

__glDrawArrays_impl = None
def glDrawArrays ( mode:int,first:int,count:int ) -> None :
    global __glDrawArrays_impl
    if not __glDrawArrays_impl:
        fptr = __pyglGetFuncAddress('glDrawArrays')
        if not fptr:
            raise RuntimeError('The function glDrawArrays is not available (maybe GL has not been initialized yet?)')
        __glDrawArrays_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int )(fptr)
    for _f in __universal_hooks:
        _f("glDrawArrays",glDrawArrays,mode,first,count)
    if 'glDrawArrays' in __hooks:
        for _f in __hooks['glDrawArrays']:
            _f("glDrawArrays",glDrawArrays,mode,first,count)
    rv = __glDrawArrays_impl(mode,first,count)
    if 'glDrawArrays' in __posthooks:
        for _f in __posthooks['glDrawArrays']:
            _f(rv,"glDrawArrays",glDrawArrays,mode,first,count)
    for _f in __universal_posthooks:
        _f(rv,"glDrawArrays",glDrawArrays,mode,first,count)
    return rv

__glDrawArraysIndirect_impl = None
def glDrawArraysIndirect ( mode:int,indirect:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glDrawArraysIndirect_impl
    if not __glDrawArraysIndirect_impl:
        fptr = __pyglGetFuncAddress('glDrawArraysIndirect')
        if not fptr:
            raise RuntimeError('The function glDrawArraysIndirect is not available (maybe GL has not been initialized yet?)')
        __glDrawArraysIndirect_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p )(fptr)
        tmp = __glDrawArraysIndirect_impl
        __glDrawArraysIndirect_impl = (lambda mode,indirect: tmp(mode,__pyglGetAsConstVoidPointer(indirect)))
    for _f in __universal_hooks:
        _f("glDrawArraysIndirect",glDrawArraysIndirect,mode,indirect)
    if 'glDrawArraysIndirect' in __hooks:
        for _f in __hooks['glDrawArraysIndirect']:
            _f("glDrawArraysIndirect",glDrawArraysIndirect,mode,indirect)
    rv = __glDrawArraysIndirect_impl(mode,indirect)
    if 'glDrawArraysIndirect' in __posthooks:
        for _f in __posthooks['glDrawArraysIndirect']:
            _f(rv,"glDrawArraysIndirect",glDrawArraysIndirect,mode,indirect)
    for _f in __universal_posthooks:
        _f(rv,"glDrawArraysIndirect",glDrawArraysIndirect,mode,indirect)
    return rv

__glDrawArraysInstanced_impl = None
def glDrawArraysInstanced ( mode:int,first:int,count:int,instancecount:int ) -> None :
    global __glDrawArraysInstanced_impl
    if not __glDrawArraysInstanced_impl:
        fptr = __pyglGetFuncAddress('glDrawArraysInstanced')
        if not fptr:
            raise RuntimeError('The function glDrawArraysInstanced is not available (maybe GL has not been initialized yet?)')
        __glDrawArraysInstanced_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_int )(fptr)
    for _f in __universal_hooks:
        _f("glDrawArraysInstanced",glDrawArraysInstanced,mode,first,count,instancecount)
    if 'glDrawArraysInstanced' in __hooks:
        for _f in __hooks['glDrawArraysInstanced']:
            _f("glDrawArraysInstanced",glDrawArraysInstanced,mode,first,count,instancecount)
    rv = __glDrawArraysInstanced_impl(mode,first,count,instancecount)
    if 'glDrawArraysInstanced' in __posthooks:
        for _f in __posthooks['glDrawArraysInstanced']:
            _f(rv,"glDrawArraysInstanced",glDrawArraysInstanced,mode,first,count,instancecount)
    for _f in __universal_posthooks:
        _f(rv,"glDrawArraysInstanced",glDrawArraysInstanced,mode,first,count,instancecount)
    return rv

__glDrawArraysInstancedBaseInstance_impl = None
def glDrawArraysInstancedBaseInstance ( mode:int,first:int,count:int,instancecount:int,baseinstance:int ) -> None :
    global __glDrawArraysInstancedBaseInstance_impl
    if not __glDrawArraysInstancedBaseInstance_impl:
        fptr = __pyglGetFuncAddress('glDrawArraysInstancedBaseInstance')
        if not fptr:
            raise RuntimeError('The function glDrawArraysInstancedBaseInstance is not available (maybe GL has not been initialized yet?)')
        __glDrawArraysInstancedBaseInstance_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_int,c_uint )(fptr)
    for _f in __universal_hooks:
        _f("glDrawArraysInstancedBaseInstance",glDrawArraysInstancedBaseInstance,mode,first,count,instancecount,baseinstance)
    if 'glDrawArraysInstancedBaseInstance' in __hooks:
        for _f in __hooks['glDrawArraysInstancedBaseInstance']:
            _f("glDrawArraysInstancedBaseInstance",glDrawArraysInstancedBaseInstance,mode,first,count,instancecount,baseinstance)
    rv = __glDrawArraysInstancedBaseInstance_impl(mode,first,count,instancecount,baseinstance)
    if 'glDrawArraysInstancedBaseInstance' in __posthooks:
        for _f in __posthooks['glDrawArraysInstancedBaseInstance']:
            _f(rv,"glDrawArraysInstancedBaseInstance",glDrawArraysInstancedBaseInstance,mode,first,count,instancecount,baseinstance)
    for _f in __universal_posthooks:
        _f(rv,"glDrawArraysInstancedBaseInstance",glDrawArraysInstancedBaseInstance,mode,first,count,instancecount,baseinstance)
    return rv

__glDrawBuffer_impl = None
def glDrawBuffer ( buf:int ) -> None :
    global __glDrawBuffer_impl
    if not __glDrawBuffer_impl:
        fptr = __pyglGetFuncAddress('glDrawBuffer')
        if not fptr:
            raise RuntimeError('The function glDrawBuffer is not available (maybe GL has not been initialized yet?)')
        __glDrawBuffer_impl = __PYGL_FUNC_TYPE( None,c_uint )(fptr)
        global glDrawBuffer
        glDrawBuffer =__glDrawBuffer_impl
    return __glDrawBuffer_impl(buf)

__glDrawBuffers_impl = None
def glDrawBuffers ( n:int,bufs:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glDrawBuffers_impl
    if not __glDrawBuffers_impl:
        fptr = __pyglGetFuncAddress('glDrawBuffers')
        if not fptr:
            raise RuntimeError('The function glDrawBuffers is not available (maybe GL has not been initialized yet?)')
        __glDrawBuffers_impl = __PYGL_FUNC_TYPE( None,c_int,c_void_p )(fptr)
        tmp = __glDrawBuffers_impl
        __glDrawBuffers_impl = (lambda n,bufs: tmp(n,__pyglGetAsConstVoidPointer(bufs)))
        global glDrawBuffers
        glDrawBuffers =__glDrawBuffers_impl
    return __glDrawBuffers_impl(n,bufs)

__glDrawElements_impl = None
def glDrawElements ( mode:int,count:int,type:int,indices:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glDrawElements_impl
    if not __glDrawElements_impl:
        fptr = __pyglGetFuncAddress('glDrawElements')
        if not fptr:
            raise RuntimeError('The function glDrawElements is not available (maybe GL has not been initialized yet?)')
        __glDrawElements_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_uint,c_void_p )(fptr)
    for _f in __universal_hooks:
        _f("glDrawElements",glDrawElements,mode,count,type,indices)
    if 'glDrawElements' in __hooks:
        for _f in __hooks['glDrawElements']:
            _f("glDrawElements",glDrawElements,mode,count,type,indices)
    rv = __glDrawElements_impl(mode,count,type,indices)
    if 'glDrawElements' in __posthooks:
        for _f in __posthooks['glDrawElements']:
            _f(rv,"glDrawElements",glDrawElements,mode,count,type,indices)
    for _f in __universal_posthooks:
        _f(rv,"glDrawElements",glDrawElements,mode,count,type,indices)
    return rv

__glDrawElementsBaseVertex_impl = None
def glDrawElementsBaseVertex ( mode:int,count:int,type:int,indices:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],basevertex:int ) -> None :
    global __glDrawElementsBaseVertex_impl
    if not __glDrawElementsBaseVertex_impl:
        fptr = __pyglGetFuncAddress('glDrawElementsBaseVertex')
        if not fptr:
            raise RuntimeError('The function glDrawElementsBaseVertex is not available (maybe GL has not been initialized yet?)')
        __glDrawElementsBaseVertex_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_uint,c_void_p,c_int )(fptr)
    for _f in __universal_hooks:
        _f("glDrawElementsBaseVertex",glDrawElementsBaseVertex,mode,count,type,indices,basevertex)
    if 'glDrawElementsBaseVertex' in __hooks:
        for _f in __hooks['glDrawElementsBaseVertex']:
            _f("glDrawElementsBaseVertex",glDrawElementsBaseVertex,mode,count,type,indices,basevertex)
    rv = __glDrawElementsBaseVertex_impl(mode,count,type,indices,basevertex)
    if 'glDrawElementsBaseVertex' in __posthooks:
        for _f in __posthooks['glDrawElementsBaseVertex']:
            _f(rv,"glDrawElementsBaseVertex",glDrawElementsBaseVertex,mode,count,type,indices,basevertex)
    for _f in __universal_posthooks:
        _f(rv,"glDrawElementsBaseVertex",glDrawElementsBaseVertex,mode,count,type,indices,basevertex)
    return rv

__glDrawElementsIndirect_impl = None
def glDrawElementsIndirect ( mode:int,type:int,indirect:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glDrawElementsIndirect_impl
    if not __glDrawElementsIndirect_impl:
        fptr = __pyglGetFuncAddress('glDrawElementsIndirect')
        if not fptr:
            raise RuntimeError('The function glDrawElementsIndirect is not available (maybe GL has not been initialized yet?)')
        __glDrawElementsIndirect_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glDrawElementsIndirect_impl
        __glDrawElementsIndirect_impl = (lambda mode,type,indirect: tmp(mode,type,__pyglGetAsConstVoidPointer(indirect)))
    for _f in __universal_hooks:
        _f("glDrawElementsIndirect",glDrawElementsIndirect,mode,type,indirect)
    if 'glDrawElementsIndirect' in __hooks:
        for _f in __hooks['glDrawElementsIndirect']:
            _f("glDrawElementsIndirect",glDrawElementsIndirect,mode,type,indirect)
    rv = __glDrawElementsIndirect_impl(mode,type,indirect)
    if 'glDrawElementsIndirect' in __posthooks:
        for _f in __posthooks['glDrawElementsIndirect']:
            _f(rv,"glDrawElementsIndirect",glDrawElementsIndirect,mode,type,indirect)
    for _f in __universal_posthooks:
        _f(rv,"glDrawElementsIndirect",glDrawElementsIndirect,mode,type,indirect)
    return rv

__glDrawElementsInstanced_impl = None
def glDrawElementsInstanced ( mode:int,count:int,type:int,indices:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],instancecount:int ) -> None :
    global __glDrawElementsInstanced_impl
    if not __glDrawElementsInstanced_impl:
        fptr = __pyglGetFuncAddress('glDrawElementsInstanced')
        if not fptr:
            raise RuntimeError('The function glDrawElementsInstanced is not available (maybe GL has not been initialized yet?)')
        __glDrawElementsInstanced_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_uint,c_void_p,c_int )(fptr)
    for _f in __universal_hooks:
        _f("glDrawElementsInstanced",glDrawElementsInstanced,mode,count,type,indices,instancecount)
    if 'glDrawElementsInstanced' in __hooks:
        for _f in __hooks['glDrawElementsInstanced']:
            _f("glDrawElementsInstanced",glDrawElementsInstanced,mode,count,type,indices,instancecount)
    rv = __glDrawElementsInstanced_impl(mode,count,type,indices,instancecount)
    if 'glDrawElementsInstanced' in __posthooks:
        for _f in __posthooks['glDrawElementsInstanced']:
            _f(rv,"glDrawElementsInstanced",glDrawElementsInstanced,mode,count,type,indices,instancecount)
    for _f in __universal_posthooks:
        _f(rv,"glDrawElementsInstanced",glDrawElementsInstanced,mode,count,type,indices,instancecount)
    return rv

__glDrawElementsInstancedBaseInstance_impl = None
def glDrawElementsInstancedBaseInstance ( mode:int,count:int,type:int,indices:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],instancecount:int,baseinstance:int ) -> None :
    global __glDrawElementsInstancedBaseInstance_impl
    if not __glDrawElementsInstancedBaseInstance_impl:
        fptr = __pyglGetFuncAddress('glDrawElementsInstancedBaseInstance')
        if not fptr:
            raise RuntimeError('The function glDrawElementsInstancedBaseInstance is not available (maybe GL has not been initialized yet?)')
        __glDrawElementsInstancedBaseInstance_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_uint,c_void_p,c_int,c_uint )(fptr)
    for _f in __universal_hooks:
        _f("glDrawElementsInstancedBaseInstance",glDrawElementsInstancedBaseInstance,mode,count,type,indices,instancecount,baseinstance)
    if 'glDrawElementsInstancedBaseInstance' in __hooks:
        for _f in __hooks['glDrawElementsInstancedBaseInstance']:
            _f("glDrawElementsInstancedBaseInstance",glDrawElementsInstancedBaseInstance,mode,count,type,indices,instancecount,baseinstance)
    rv = __glDrawElementsInstancedBaseInstance_impl(mode,count,type,indices,instancecount,baseinstance)
    if 'glDrawElementsInstancedBaseInstance' in __posthooks:
        for _f in __posthooks['glDrawElementsInstancedBaseInstance']:
            _f(rv,"glDrawElementsInstancedBaseInstance",glDrawElementsInstancedBaseInstance,mode,count,type,indices,instancecount,baseinstance)
    for _f in __universal_posthooks:
        _f(rv,"glDrawElementsInstancedBaseInstance",glDrawElementsInstancedBaseInstance,mode,count,type,indices,instancecount,baseinstance)
    return rv

__glDrawElementsInstancedBaseVertex_impl = None
def glDrawElementsInstancedBaseVertex ( mode:int,count:int,type:int,indices:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],instancecount:int,basevertex:int ) -> None :
    global __glDrawElementsInstancedBaseVertex_impl
    if not __glDrawElementsInstancedBaseVertex_impl:
        fptr = __pyglGetFuncAddress('glDrawElementsInstancedBaseVertex')
        if not fptr:
            raise RuntimeError('The function glDrawElementsInstancedBaseVertex is not available (maybe GL has not been initialized yet?)')
        __glDrawElementsInstancedBaseVertex_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_uint,c_void_p,c_int,c_int )(fptr)
    for _f in __universal_hooks:
        _f("glDrawElementsInstancedBaseVertex",glDrawElementsInstancedBaseVertex,mode,count,type,indices,instancecount,basevertex)
    if 'glDrawElementsInstancedBaseVertex' in __hooks:
        for _f in __hooks['glDrawElementsInstancedBaseVertex']:
            _f("glDrawElementsInstancedBaseVertex",glDrawElementsInstancedBaseVertex,mode,count,type,indices,instancecount,basevertex)
    rv = __glDrawElementsInstancedBaseVertex_impl(mode,count,type,indices,instancecount,basevertex)
    if 'glDrawElementsInstancedBaseVertex' in __posthooks:
        for _f in __posthooks['glDrawElementsInstancedBaseVertex']:
            _f(rv,"glDrawElementsInstancedBaseVertex",glDrawElementsInstancedBaseVertex,mode,count,type,indices,instancecount,basevertex)
    for _f in __universal_posthooks:
        _f(rv,"glDrawElementsInstancedBaseVertex",glDrawElementsInstancedBaseVertex,mode,count,type,indices,instancecount,basevertex)
    return rv

__glDrawElementsInstancedBaseVertexBaseInstance_impl = None
def glDrawElementsInstancedBaseVertexBaseInstance ( mode:int,count:int,type:int,indices:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],instancecount:int,basevertex:int,baseinstance:int ) -> None :
    global __glDrawElementsInstancedBaseVertexBaseInstance_impl
    if not __glDrawElementsInstancedBaseVertexBaseInstance_impl:
        fptr = __pyglGetFuncAddress('glDrawElementsInstancedBaseVertexBaseInstance')
        if not fptr:
            raise RuntimeError('The function glDrawElementsInstancedBaseVertexBaseInstance is not available (maybe GL has not been initialized yet?)')
        __glDrawElementsInstancedBaseVertexBaseInstance_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_uint,c_void_p,c_int,c_int,c_uint )(fptr)
    for _f in __universal_hooks:
        _f("glDrawElementsInstancedBaseVertexBaseInstance",glDrawElementsInstancedBaseVertexBaseInstance,mode,count,type,indices,instancecount,basevertex,baseinstance)
    if 'glDrawElementsInstancedBaseVertexBaseInstance' in __hooks:
        for _f in __hooks['glDrawElementsInstancedBaseVertexBaseInstance']:
            _f("glDrawElementsInstancedBaseVertexBaseInstance",glDrawElementsInstancedBaseVertexBaseInstance,mode,count,type,indices,instancecount,basevertex,baseinstance)
    rv = __glDrawElementsInstancedBaseVertexBaseInstance_impl(mode,count,type,indices,instancecount,basevertex,baseinstance)
    if 'glDrawElementsInstancedBaseVertexBaseInstance' in __posthooks:
        for _f in __posthooks['glDrawElementsInstancedBaseVertexBaseInstance']:
            _f(rv,"glDrawElementsInstancedBaseVertexBaseInstance",glDrawElementsInstancedBaseVertexBaseInstance,mode,count,type,indices,instancecount,basevertex,baseinstance)
    for _f in __universal_posthooks:
        _f(rv,"glDrawElementsInstancedBaseVertexBaseInstance",glDrawElementsInstancedBaseVertexBaseInstance,mode,count,type,indices,instancecount,basevertex,baseinstance)
    return rv

__glDrawRangeElements_impl = None
def glDrawRangeElements ( mode:int,start:int,end:int,count:int,type:int,indices:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glDrawRangeElements_impl
    if not __glDrawRangeElements_impl:
        fptr = __pyglGetFuncAddress('glDrawRangeElements')
        if not fptr:
            raise RuntimeError('The function glDrawRangeElements is not available (maybe GL has not been initialized yet?)')
        __glDrawRangeElements_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint,c_int,c_uint,c_void_p )(fptr)
    for _f in __universal_hooks:
        _f("glDrawRangeElements",glDrawRangeElements,mode,start,end,count,type,indices)
    if 'glDrawRangeElements' in __hooks:
        for _f in __hooks['glDrawRangeElements']:
            _f("glDrawRangeElements",glDrawRangeElements,mode,start,end,count,type,indices)
    rv = __glDrawRangeElements_impl(mode,start,end,count,type,indices)
    if 'glDrawRangeElements' in __posthooks:
        for _f in __posthooks['glDrawRangeElements']:
            _f(rv,"glDrawRangeElements",glDrawRangeElements,mode,start,end,count,type,indices)
    for _f in __universal_posthooks:
        _f(rv,"glDrawRangeElements",glDrawRangeElements,mode,start,end,count,type,indices)
    return rv

__glDrawRangeElementsBaseVertex_impl = None
def glDrawRangeElementsBaseVertex ( mode:int,start:int,end:int,count:int,type:int,indices:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],basevertex:int ) -> None :
    global __glDrawRangeElementsBaseVertex_impl
    if not __glDrawRangeElementsBaseVertex_impl:
        fptr = __pyglGetFuncAddress('glDrawRangeElementsBaseVertex')
        if not fptr:
            raise RuntimeError('The function glDrawRangeElementsBaseVertex is not available (maybe GL has not been initialized yet?)')
        __glDrawRangeElementsBaseVertex_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint,c_int,c_uint,c_void_p,c_int )(fptr)
        tmp = __glDrawRangeElementsBaseVertex_impl
        __glDrawRangeElementsBaseVertex_impl = (lambda mode,start,end,count,type,indices,basevertex: tmp(mode,start,end,count,type,__pyglGetAsConstVoidPointer(indices),basevertex))
    for _f in __universal_hooks:
        _f("glDrawRangeElementsBaseVertex",glDrawRangeElementsBaseVertex,mode,start,end,count,type,indices,basevertex)
    if 'glDrawRangeElementsBaseVertex' in __hooks:
        for _f in __hooks['glDrawRangeElementsBaseVertex']:
            _f("glDrawRangeElementsBaseVertex",glDrawRangeElementsBaseVertex,mode,start,end,count,type,indices,basevertex)
    rv = __glDrawRangeElementsBaseVertex_impl(mode,start,end,count,type,indices,basevertex)
    if 'glDrawRangeElementsBaseVertex' in __posthooks:
        for _f in __posthooks['glDrawRangeElementsBaseVertex']:
            _f(rv,"glDrawRangeElementsBaseVertex",glDrawRangeElementsBaseVertex,mode,start,end,count,type,indices,basevertex)
    for _f in __universal_posthooks:
        _f(rv,"glDrawRangeElementsBaseVertex",glDrawRangeElementsBaseVertex,mode,start,end,count,type,indices,basevertex)
    return rv

__glDrawTransformFeedback_impl = None
def glDrawTransformFeedback ( mode:int,id:int ) -> None :
    global __glDrawTransformFeedback_impl
    if not __glDrawTransformFeedback_impl:
        fptr = __pyglGetFuncAddress('glDrawTransformFeedback')
        if not fptr:
            raise RuntimeError('The function glDrawTransformFeedback is not available (maybe GL has not been initialized yet?)')
        __glDrawTransformFeedback_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint )(fptr)
        global glDrawTransformFeedback
        glDrawTransformFeedback =__glDrawTransformFeedback_impl
    return __glDrawTransformFeedback_impl(mode,id)

__glDrawTransformFeedbackInstanced_impl = None
def glDrawTransformFeedbackInstanced ( mode:int,id:int,instancecount:int ) -> None :
    global __glDrawTransformFeedbackInstanced_impl
    if not __glDrawTransformFeedbackInstanced_impl:
        fptr = __pyglGetFuncAddress('glDrawTransformFeedbackInstanced')
        if not fptr:
            raise RuntimeError('The function glDrawTransformFeedbackInstanced is not available (maybe GL has not been initialized yet?)')
        __glDrawTransformFeedbackInstanced_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_int )(fptr)
        global glDrawTransformFeedbackInstanced
        glDrawTransformFeedbackInstanced =__glDrawTransformFeedbackInstanced_impl
    return __glDrawTransformFeedbackInstanced_impl(mode,id,instancecount)

__glDrawTransformFeedbackStream_impl = None
def glDrawTransformFeedbackStream ( mode:int,id:int,stream:int ) -> None :
    global __glDrawTransformFeedbackStream_impl
    if not __glDrawTransformFeedbackStream_impl:
        fptr = __pyglGetFuncAddress('glDrawTransformFeedbackStream')
        if not fptr:
            raise RuntimeError('The function glDrawTransformFeedbackStream is not available (maybe GL has not been initialized yet?)')
        __glDrawTransformFeedbackStream_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint )(fptr)
        global glDrawTransformFeedbackStream
        glDrawTransformFeedbackStream =__glDrawTransformFeedbackStream_impl
    return __glDrawTransformFeedbackStream_impl(mode,id,stream)

__glDrawTransformFeedbackStreamInstanced_impl = None
def glDrawTransformFeedbackStreamInstanced ( mode:int,id:int,stream:int,instancecount:int ) -> None :
    global __glDrawTransformFeedbackStreamInstanced_impl
    if not __glDrawTransformFeedbackStreamInstanced_impl:
        fptr = __pyglGetFuncAddress('glDrawTransformFeedbackStreamInstanced')
        if not fptr:
            raise RuntimeError('The function glDrawTransformFeedbackStreamInstanced is not available (maybe GL has not been initialized yet?)')
        __glDrawTransformFeedbackStreamInstanced_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint,c_int )(fptr)
        global glDrawTransformFeedbackStreamInstanced
        glDrawTransformFeedbackStreamInstanced =__glDrawTransformFeedbackStreamInstanced_impl
    return __glDrawTransformFeedbackStreamInstanced_impl(mode,id,stream,instancecount)

__glEnable_impl = None
def glEnable ( cap:int ) -> None :
    global __glEnable_impl
    if not __glEnable_impl:
        fptr = __pyglGetFuncAddress('glEnable')
        if not fptr:
            raise RuntimeError('The function glEnable is not available (maybe GL has not been initialized yet?)')
        __glEnable_impl = __PYGL_FUNC_TYPE( None,c_uint )(fptr)
        global glEnable
        glEnable =__glEnable_impl
    return __glEnable_impl(cap)

__glEnableVertexArrayAttrib_impl = None
def glEnableVertexArrayAttrib ( vaobj:int,index:int ) -> None :
    global __glEnableVertexArrayAttrib_impl
    if not __glEnableVertexArrayAttrib_impl:
        fptr = __pyglGetFuncAddress('glEnableVertexArrayAttrib')
        if not fptr:
            raise RuntimeError('The function glEnableVertexArrayAttrib is not available (maybe GL has not been initialized yet?)')
        __glEnableVertexArrayAttrib_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint )(fptr)
        global glEnableVertexArrayAttrib
        glEnableVertexArrayAttrib =__glEnableVertexArrayAttrib_impl
    return __glEnableVertexArrayAttrib_impl(vaobj,index)

__glEnableVertexAttribArray_impl = None
def glEnableVertexAttribArray ( index:int ) -> None :
    global __glEnableVertexAttribArray_impl
    if not __glEnableVertexAttribArray_impl:
        fptr = __pyglGetFuncAddress('glEnableVertexAttribArray')
        if not fptr:
            raise RuntimeError('The function glEnableVertexAttribArray is not available (maybe GL has not been initialized yet?)')
        __glEnableVertexAttribArray_impl = __PYGL_FUNC_TYPE( None,c_uint )(fptr)
        global glEnableVertexAttribArray
        glEnableVertexAttribArray =__glEnableVertexAttribArray_impl
    return __glEnableVertexAttribArray_impl(index)

__glEnablei_impl = None
def glEnablei ( target:int,index:int ) -> None :
    global __glEnablei_impl
    if not __glEnablei_impl:
        fptr = __pyglGetFuncAddress('glEnablei')
        if not fptr:
            raise RuntimeError('The function glEnablei is not available (maybe GL has not been initialized yet?)')
        __glEnablei_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint )(fptr)
        global glEnablei
        glEnablei =__glEnablei_impl
    return __glEnablei_impl(target,index)

__glEndConditionalRender_impl = None
def glEndConditionalRender (  ) -> None :
    global __glEndConditionalRender_impl
    if not __glEndConditionalRender_impl:
        fptr = __pyglGetFuncAddress('glEndConditionalRender')
        if not fptr:
            raise RuntimeError('The function glEndConditionalRender is not available (maybe GL has not been initialized yet?)')
        __glEndConditionalRender_impl = __PYGL_FUNC_TYPE( None )(fptr)
        global glEndConditionalRender
        glEndConditionalRender =__glEndConditionalRender_impl
    return __glEndConditionalRender_impl()

__glEndQuery_impl = None
def glEndQuery ( target:int ) -> None :
    global __glEndQuery_impl
    if not __glEndQuery_impl:
        fptr = __pyglGetFuncAddress('glEndQuery')
        if not fptr:
            raise RuntimeError('The function glEndQuery is not available (maybe GL has not been initialized yet?)')
        __glEndQuery_impl = __PYGL_FUNC_TYPE( None,c_uint )(fptr)
        global glEndQuery
        glEndQuery =__glEndQuery_impl
    return __glEndQuery_impl(target)

__glEndQueryIndexed_impl = None
def glEndQueryIndexed ( target:int,index:int ) -> None :
    global __glEndQueryIndexed_impl
    if not __glEndQueryIndexed_impl:
        fptr = __pyglGetFuncAddress('glEndQueryIndexed')
        if not fptr:
            raise RuntimeError('The function glEndQueryIndexed is not available (maybe GL has not been initialized yet?)')
        __glEndQueryIndexed_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint )(fptr)
        global glEndQueryIndexed
        glEndQueryIndexed =__glEndQueryIndexed_impl
    return __glEndQueryIndexed_impl(target,index)

__glEndTransformFeedback_impl = None
def glEndTransformFeedback (  ) -> None :
    global __glEndTransformFeedback_impl
    if not __glEndTransformFeedback_impl:
        fptr = __pyglGetFuncAddress('glEndTransformFeedback')
        if not fptr:
            raise RuntimeError('The function glEndTransformFeedback is not available (maybe GL has not been initialized yet?)')
        __glEndTransformFeedback_impl = __PYGL_FUNC_TYPE( None )(fptr)
        global glEndTransformFeedback
        glEndTransformFeedback =__glEndTransformFeedback_impl
    return __glEndTransformFeedback_impl()

__glFenceSync_impl = None
def glFenceSync ( condition:int,flags:int ) -> typing.Any :
    global __glFenceSync_impl
    if not __glFenceSync_impl:
        fptr = __pyglGetFuncAddress('glFenceSync')
        if not fptr:
            raise RuntimeError('The function glFenceSync is not available (maybe GL has not been initialized yet?)')
        __glFenceSync_impl = __PYGL_FUNC_TYPE( c_void_p,c_uint,c_uint )(fptr)
        global glFenceSync
        glFenceSync =__glFenceSync_impl
    return __glFenceSync_impl(condition,flags)

__glFinish_impl = None
def glFinish (  ) -> None :
    global __glFinish_impl
    if not __glFinish_impl:
        fptr = __pyglGetFuncAddress('glFinish')
        if not fptr:
            raise RuntimeError('The function glFinish is not available (maybe GL has not been initialized yet?)')
        __glFinish_impl = __PYGL_FUNC_TYPE( None )(fptr)
        global glFinish
        glFinish =__glFinish_impl
    return __glFinish_impl()

__glFlush_impl = None
def glFlush (  ) -> None :
    global __glFlush_impl
    if not __glFlush_impl:
        fptr = __pyglGetFuncAddress('glFlush')
        if not fptr:
            raise RuntimeError('The function glFlush is not available (maybe GL has not been initialized yet?)')
        __glFlush_impl = __PYGL_FUNC_TYPE( None )(fptr)
        global glFlush
        glFlush =__glFlush_impl
    return __glFlush_impl()

__glFlushMappedBufferRange_impl = None
def glFlushMappedBufferRange ( target:int,offset:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],length:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glFlushMappedBufferRange_impl
    if not __glFlushMappedBufferRange_impl:
        fptr = __pyglGetFuncAddress('glFlushMappedBufferRange')
        if not fptr:
            raise RuntimeError('The function glFlushMappedBufferRange is not available (maybe GL has not been initialized yet?)')
        __glFlushMappedBufferRange_impl = __PYGL_FUNC_TYPE( None,c_uint,c_size_t,c_void_p )(fptr)
        global glFlushMappedBufferRange
        glFlushMappedBufferRange =__glFlushMappedBufferRange_impl
    return __glFlushMappedBufferRange_impl(target,offset,length)

__glFlushMappedNamedBufferRange_impl = None
def glFlushMappedNamedBufferRange ( buffer:int,offset:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],length:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glFlushMappedNamedBufferRange_impl
    if not __glFlushMappedNamedBufferRange_impl:
        fptr = __pyglGetFuncAddress('glFlushMappedNamedBufferRange')
        if not fptr:
            raise RuntimeError('The function glFlushMappedNamedBufferRange is not available (maybe GL has not been initialized yet?)')
        __glFlushMappedNamedBufferRange_impl = __PYGL_FUNC_TYPE( None,c_uint,c_size_t,c_void_p )(fptr)
        global glFlushMappedNamedBufferRange
        glFlushMappedNamedBufferRange =__glFlushMappedNamedBufferRange_impl
    return __glFlushMappedNamedBufferRange_impl(buffer,offset,length)

__glFramebufferParameteri_impl = None
def glFramebufferParameteri ( target:int,pname:int,param:int ) -> None :
    global __glFramebufferParameteri_impl
    if not __glFramebufferParameteri_impl:
        fptr = __pyglGetFuncAddress('glFramebufferParameteri')
        if not fptr:
            raise RuntimeError('The function glFramebufferParameteri is not available (maybe GL has not been initialized yet?)')
        __glFramebufferParameteri_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_int )(fptr)
        global glFramebufferParameteri
        glFramebufferParameteri =__glFramebufferParameteri_impl
    return __glFramebufferParameteri_impl(target,pname,param)

__glFramebufferRenderbuffer_impl = None
def glFramebufferRenderbuffer ( target:int,attachment:int,renderbuffertarget:int,renderbuffer:int ) -> None :
    global __glFramebufferRenderbuffer_impl
    if not __glFramebufferRenderbuffer_impl:
        fptr = __pyglGetFuncAddress('glFramebufferRenderbuffer')
        if not fptr:
            raise RuntimeError('The function glFramebufferRenderbuffer is not available (maybe GL has not been initialized yet?)')
        __glFramebufferRenderbuffer_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint,c_uint )(fptr)
        global glFramebufferRenderbuffer
        glFramebufferRenderbuffer =__glFramebufferRenderbuffer_impl
    return __glFramebufferRenderbuffer_impl(target,attachment,renderbuffertarget,renderbuffer)

__glFramebufferTexture_impl = None
def glFramebufferTexture ( target:int,attachment:int,texture:int,level:int ) -> None :
    global __glFramebufferTexture_impl
    if not __glFramebufferTexture_impl:
        fptr = __pyglGetFuncAddress('glFramebufferTexture')
        if not fptr:
            raise RuntimeError('The function glFramebufferTexture is not available (maybe GL has not been initialized yet?)')
        __glFramebufferTexture_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint,c_int )(fptr)
        global glFramebufferTexture
        glFramebufferTexture =__glFramebufferTexture_impl
    return __glFramebufferTexture_impl(target,attachment,texture,level)

__glFramebufferTexture1D_impl = None
def glFramebufferTexture1D ( target:int,attachment:int,textarget:int,texture:int,level:int ) -> None :
    global __glFramebufferTexture1D_impl
    if not __glFramebufferTexture1D_impl:
        fptr = __pyglGetFuncAddress('glFramebufferTexture1D')
        if not fptr:
            raise RuntimeError('The function glFramebufferTexture1D is not available (maybe GL has not been initialized yet?)')
        __glFramebufferTexture1D_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint,c_uint,c_int )(fptr)
        global glFramebufferTexture1D
        glFramebufferTexture1D =__glFramebufferTexture1D_impl
    return __glFramebufferTexture1D_impl(target,attachment,textarget,texture,level)

__glFramebufferTexture2D_impl = None
def glFramebufferTexture2D ( target:int,attachment:int,textarget:int,texture:int,level:int ) -> None :
    global __glFramebufferTexture2D_impl
    if not __glFramebufferTexture2D_impl:
        fptr = __pyglGetFuncAddress('glFramebufferTexture2D')
        if not fptr:
            raise RuntimeError('The function glFramebufferTexture2D is not available (maybe GL has not been initialized yet?)')
        __glFramebufferTexture2D_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint,c_uint,c_int )(fptr)
        global glFramebufferTexture2D
        glFramebufferTexture2D =__glFramebufferTexture2D_impl
    return __glFramebufferTexture2D_impl(target,attachment,textarget,texture,level)

__glFramebufferTexture3D_impl = None
def glFramebufferTexture3D ( target:int,attachment:int,textarget:int,texture:int,level:int,zoffset:int ) -> None :
    global __glFramebufferTexture3D_impl
    if not __glFramebufferTexture3D_impl:
        fptr = __pyglGetFuncAddress('glFramebufferTexture3D')
        if not fptr:
            raise RuntimeError('The function glFramebufferTexture3D is not available (maybe GL has not been initialized yet?)')
        __glFramebufferTexture3D_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint,c_uint,c_int,c_int )(fptr)
        global glFramebufferTexture3D
        glFramebufferTexture3D =__glFramebufferTexture3D_impl
    return __glFramebufferTexture3D_impl(target,attachment,textarget,texture,level,zoffset)

__glFramebufferTextureLayer_impl = None
def glFramebufferTextureLayer ( target:int,attachment:int,texture:int,level:int,layer:int ) -> None :
    global __glFramebufferTextureLayer_impl
    if not __glFramebufferTextureLayer_impl:
        fptr = __pyglGetFuncAddress('glFramebufferTextureLayer')
        if not fptr:
            raise RuntimeError('The function glFramebufferTextureLayer is not available (maybe GL has not been initialized yet?)')
        __glFramebufferTextureLayer_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint,c_int,c_int )(fptr)
        global glFramebufferTextureLayer
        glFramebufferTextureLayer =__glFramebufferTextureLayer_impl
    return __glFramebufferTextureLayer_impl(target,attachment,texture,level,layer)

__glFrontFace_impl = None
def glFrontFace ( mode:int ) -> None :
    global __glFrontFace_impl
    if not __glFrontFace_impl:
        fptr = __pyglGetFuncAddress('glFrontFace')
        if not fptr:
            raise RuntimeError('The function glFrontFace is not available (maybe GL has not been initialized yet?)')
        __glFrontFace_impl = __PYGL_FUNC_TYPE( None,c_uint )(fptr)
        global glFrontFace
        glFrontFace =__glFrontFace_impl
    return __glFrontFace_impl(mode)

__glGenBuffers_impl = None
def glGenBuffers ( n:int,buffers:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGenBuffers_impl
    if not __glGenBuffers_impl:
        fptr = __pyglGetFuncAddress('glGenBuffers')
        if not fptr:
            raise RuntimeError('The function glGenBuffers is not available (maybe GL has not been initialized yet?)')
        __glGenBuffers_impl = __PYGL_FUNC_TYPE( None,c_int,c_void_p )(fptr)
        tmp = __glGenBuffers_impl
        __glGenBuffers_impl = (lambda n,buffers: tmp(n,(c_uint8*len(buffers)).from_buffer(buffers)))
    for _f in __universal_hooks:
        _f("glGenBuffers",glGenBuffers,n,buffers)
    if 'glGenBuffers' in __hooks:
        for _f in __hooks['glGenBuffers']:
            _f("glGenBuffers",glGenBuffers,n,buffers)
    rv = __glGenBuffers_impl(n,buffers)
    if 'glGenBuffers' in __posthooks:
        for _f in __posthooks['glGenBuffers']:
            _f(rv,"glGenBuffers",glGenBuffers,n,buffers)
    for _f in __universal_posthooks:
        _f(rv,"glGenBuffers",glGenBuffers,n,buffers)
    return rv

__glGenFramebuffers_impl = None
def glGenFramebuffers ( n:int,framebuffers:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGenFramebuffers_impl
    if not __glGenFramebuffers_impl:
        fptr = __pyglGetFuncAddress('glGenFramebuffers')
        if not fptr:
            raise RuntimeError('The function glGenFramebuffers is not available (maybe GL has not been initialized yet?)')
        __glGenFramebuffers_impl = __PYGL_FUNC_TYPE( None,c_int,c_void_p )(fptr)
        tmp = __glGenFramebuffers_impl
        __glGenFramebuffers_impl = (lambda n,framebuffers: tmp(n,(c_uint8*len(framebuffers)).from_buffer(framebuffers)))
        global glGenFramebuffers
        glGenFramebuffers =__glGenFramebuffers_impl
    return __glGenFramebuffers_impl(n,framebuffers)

__glGenProgramPipelines_impl = None
def glGenProgramPipelines ( n:int,pipelines:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGenProgramPipelines_impl
    if not __glGenProgramPipelines_impl:
        fptr = __pyglGetFuncAddress('glGenProgramPipelines')
        if not fptr:
            raise RuntimeError('The function glGenProgramPipelines is not available (maybe GL has not been initialized yet?)')
        __glGenProgramPipelines_impl = __PYGL_FUNC_TYPE( None,c_int,c_void_p )(fptr)
        tmp = __glGenProgramPipelines_impl
        __glGenProgramPipelines_impl = (lambda n,pipelines: tmp(n,(c_uint8*len(pipelines)).from_buffer(pipelines)))
        global glGenProgramPipelines
        glGenProgramPipelines =__glGenProgramPipelines_impl
    return __glGenProgramPipelines_impl(n,pipelines)

__glGenQueries_impl = None
def glGenQueries ( n:int,ids:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGenQueries_impl
    if not __glGenQueries_impl:
        fptr = __pyglGetFuncAddress('glGenQueries')
        if not fptr:
            raise RuntimeError('The function glGenQueries is not available (maybe GL has not been initialized yet?)')
        __glGenQueries_impl = __PYGL_FUNC_TYPE( None,c_int,c_void_p )(fptr)
        tmp = __glGenQueries_impl
        __glGenQueries_impl = (lambda n,ids: tmp(n,(c_uint8*len(ids)).from_buffer(ids)))
        global glGenQueries
        glGenQueries =__glGenQueries_impl
    return __glGenQueries_impl(n,ids)

__glGenRenderbuffers_impl = None
def glGenRenderbuffers ( n:int,renderbuffers:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGenRenderbuffers_impl
    if not __glGenRenderbuffers_impl:
        fptr = __pyglGetFuncAddress('glGenRenderbuffers')
        if not fptr:
            raise RuntimeError('The function glGenRenderbuffers is not available (maybe GL has not been initialized yet?)')
        __glGenRenderbuffers_impl = __PYGL_FUNC_TYPE( None,c_int,c_void_p )(fptr)
        tmp = __glGenRenderbuffers_impl
        __glGenRenderbuffers_impl = (lambda n,renderbuffers: tmp(n,(c_uint8*len(renderbuffers)).from_buffer(renderbuffers)))
        global glGenRenderbuffers
        glGenRenderbuffers =__glGenRenderbuffers_impl
    return __glGenRenderbuffers_impl(n,renderbuffers)

__glGenSamplers_impl = None
def glGenSamplers ( count:int,samplers:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGenSamplers_impl
    if not __glGenSamplers_impl:
        fptr = __pyglGetFuncAddress('glGenSamplers')
        if not fptr:
            raise RuntimeError('The function glGenSamplers is not available (maybe GL has not been initialized yet?)')
        __glGenSamplers_impl = __PYGL_FUNC_TYPE( None,c_int,c_void_p )(fptr)
        tmp = __glGenSamplers_impl
        __glGenSamplers_impl = (lambda count,samplers: tmp(count,(c_uint8*len(samplers)).from_buffer(samplers)))
        global glGenSamplers
        glGenSamplers =__glGenSamplers_impl
    return __glGenSamplers_impl(count,samplers)

__glGenTextures_impl = None
def glGenTextures ( n:int,textures:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGenTextures_impl
    if not __glGenTextures_impl:
        fptr = __pyglGetFuncAddress('glGenTextures')
        if not fptr:
            raise RuntimeError('The function glGenTextures is not available (maybe GL has not been initialized yet?)')
        __glGenTextures_impl = __PYGL_FUNC_TYPE( None,c_int,c_void_p )(fptr)
        tmp = __glGenTextures_impl
        __glGenTextures_impl = (lambda n,textures: tmp(n,(c_uint8*len(textures)).from_buffer(textures)))
    for _f in __universal_hooks:
        _f("glGenTextures",glGenTextures,n,textures)
    if 'glGenTextures' in __hooks:
        for _f in __hooks['glGenTextures']:
            _f("glGenTextures",glGenTextures,n,textures)
    rv = __glGenTextures_impl(n,textures)
    if 'glGenTextures' in __posthooks:
        for _f in __posthooks['glGenTextures']:
            _f(rv,"glGenTextures",glGenTextures,n,textures)
    for _f in __universal_posthooks:
        _f(rv,"glGenTextures",glGenTextures,n,textures)
    return rv

__glGenTransformFeedbacks_impl = None
def glGenTransformFeedbacks ( n:int,ids:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGenTransformFeedbacks_impl
    if not __glGenTransformFeedbacks_impl:
        fptr = __pyglGetFuncAddress('glGenTransformFeedbacks')
        if not fptr:
            raise RuntimeError('The function glGenTransformFeedbacks is not available (maybe GL has not been initialized yet?)')
        __glGenTransformFeedbacks_impl = __PYGL_FUNC_TYPE( None,c_int,c_void_p )(fptr)
        tmp = __glGenTransformFeedbacks_impl
        __glGenTransformFeedbacks_impl = (lambda n,ids: tmp(n,(c_uint8*len(ids)).from_buffer(ids)))
        global glGenTransformFeedbacks
        glGenTransformFeedbacks =__glGenTransformFeedbacks_impl
    return __glGenTransformFeedbacks_impl(n,ids)

__glGenVertexArrays_impl = None
def glGenVertexArrays ( n:int,arrays:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGenVertexArrays_impl
    if not __glGenVertexArrays_impl:
        fptr = __pyglGetFuncAddress('glGenVertexArrays')
        if not fptr:
            raise RuntimeError('The function glGenVertexArrays is not available (maybe GL has not been initialized yet?)')
        __glGenVertexArrays_impl = __PYGL_FUNC_TYPE( None,c_int,c_void_p )(fptr)
        tmp = __glGenVertexArrays_impl
        __glGenVertexArrays_impl = (lambda n,arrays: tmp(n,(c_uint8*len(arrays)).from_buffer(arrays)))
        global glGenVertexArrays
        glGenVertexArrays =__glGenVertexArrays_impl
    return __glGenVertexArrays_impl(n,arrays)

__glGenerateMipmap_impl = None
def glGenerateMipmap ( target:int ) -> None :
    global __glGenerateMipmap_impl
    if not __glGenerateMipmap_impl:
        fptr = __pyglGetFuncAddress('glGenerateMipmap')
        if not fptr:
            raise RuntimeError('The function glGenerateMipmap is not available (maybe GL has not been initialized yet?)')
        __glGenerateMipmap_impl = __PYGL_FUNC_TYPE( None,c_uint )(fptr)
        global glGenerateMipmap
        glGenerateMipmap =__glGenerateMipmap_impl
    return __glGenerateMipmap_impl(target)

__glGenerateTextureMipmap_impl = None
def glGenerateTextureMipmap ( texture:int ) -> None :
    global __glGenerateTextureMipmap_impl
    if not __glGenerateTextureMipmap_impl:
        fptr = __pyglGetFuncAddress('glGenerateTextureMipmap')
        if not fptr:
            raise RuntimeError('The function glGenerateTextureMipmap is not available (maybe GL has not been initialized yet?)')
        __glGenerateTextureMipmap_impl = __PYGL_FUNC_TYPE( None,c_uint )(fptr)
        global glGenerateTextureMipmap
        glGenerateTextureMipmap =__glGenerateTextureMipmap_impl
    return __glGenerateTextureMipmap_impl(texture)

__glGetActiveAtomicCounterBufferiv_impl = None
def glGetActiveAtomicCounterBufferiv ( program:int,bufferIndex:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetActiveAtomicCounterBufferiv_impl
    if not __glGetActiveAtomicCounterBufferiv_impl:
        fptr = __pyglGetFuncAddress('glGetActiveAtomicCounterBufferiv')
        if not fptr:
            raise RuntimeError('The function glGetActiveAtomicCounterBufferiv is not available (maybe GL has not been initialized yet?)')
        __glGetActiveAtomicCounterBufferiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetActiveAtomicCounterBufferiv_impl
        __glGetActiveAtomicCounterBufferiv_impl = (lambda program,bufferIndex,pname,params: tmp(program,bufferIndex,pname,(c_uint8*len(params)).from_buffer(params)))
        global glGetActiveAtomicCounterBufferiv
        glGetActiveAtomicCounterBufferiv =__glGetActiveAtomicCounterBufferiv_impl
    return __glGetActiveAtomicCounterBufferiv_impl(program,bufferIndex,pname,params)

__glGetActiveAttrib_impl = None
def glGetActiveAttrib ( program:int,index:int,bufSize:int,length:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],size:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],type:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],name:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetActiveAttrib_impl
    if not __glGetActiveAttrib_impl:
        fptr = __pyglGetFuncAddress('glGetActiveAttrib')
        if not fptr:
            raise RuntimeError('The function glGetActiveAttrib is not available (maybe GL has not been initialized yet?)')
        __glGetActiveAttrib_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_int,c_void_p,c_void_p,c_void_p,c_void_p )(fptr)
        tmp = __glGetActiveAttrib_impl
        __glGetActiveAttrib_impl = (lambda program,index,bufSize,length,size,type,name: tmp(program,index,bufSize,(c_uint8*len(length)).from_buffer(length),(c_uint8*len(size)).from_buffer(size),(c_uint8*len(type)).from_buffer(type),(c_uint8*len(name)).from_buffer(name)))
        global glGetActiveAttrib
        glGetActiveAttrib =__glGetActiveAttrib_impl
    return __glGetActiveAttrib_impl(program,index,bufSize,length,size,type,name)

__glGetActiveSubroutineName_impl = None
def glGetActiveSubroutineName ( program:int,shadertype:int,index:int,bufsize:int,length:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],name:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetActiveSubroutineName_impl
    if not __glGetActiveSubroutineName_impl:
        fptr = __pyglGetFuncAddress('glGetActiveSubroutineName')
        if not fptr:
            raise RuntimeError('The function glGetActiveSubroutineName is not available (maybe GL has not been initialized yet?)')
        __glGetActiveSubroutineName_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint,c_int,c_void_p,c_void_p )(fptr)
        tmp = __glGetActiveSubroutineName_impl
        __glGetActiveSubroutineName_impl = (lambda program,shadertype,index,bufsize,length,name: tmp(program,shadertype,index,bufsize,(c_uint8*len(length)).from_buffer(length),(c_uint8*len(name)).from_buffer(name)))
        global glGetActiveSubroutineName
        glGetActiveSubroutineName =__glGetActiveSubroutineName_impl
    return __glGetActiveSubroutineName_impl(program,shadertype,index,bufsize,length,name)

__glGetActiveSubroutineUniformName_impl = None
def glGetActiveSubroutineUniformName ( program:int,shadertype:int,index:int,bufsize:int,length:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],name:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetActiveSubroutineUniformName_impl
    if not __glGetActiveSubroutineUniformName_impl:
        fptr = __pyglGetFuncAddress('glGetActiveSubroutineUniformName')
        if not fptr:
            raise RuntimeError('The function glGetActiveSubroutineUniformName is not available (maybe GL has not been initialized yet?)')
        __glGetActiveSubroutineUniformName_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint,c_int,c_void_p,c_void_p )(fptr)
        tmp = __glGetActiveSubroutineUniformName_impl
        __glGetActiveSubroutineUniformName_impl = (lambda program,shadertype,index,bufsize,length,name: tmp(program,shadertype,index,bufsize,(c_uint8*len(length)).from_buffer(length),(c_uint8*len(name)).from_buffer(name)))
        global glGetActiveSubroutineUniformName
        glGetActiveSubroutineUniformName =__glGetActiveSubroutineUniformName_impl
    return __glGetActiveSubroutineUniformName_impl(program,shadertype,index,bufsize,length,name)

__glGetActiveSubroutineUniformiv_impl = None
def glGetActiveSubroutineUniformiv ( program:int,shadertype:int,index:int,pname:int,values:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetActiveSubroutineUniformiv_impl
    if not __glGetActiveSubroutineUniformiv_impl:
        fptr = __pyglGetFuncAddress('glGetActiveSubroutineUniformiv')
        if not fptr:
            raise RuntimeError('The function glGetActiveSubroutineUniformiv is not available (maybe GL has not been initialized yet?)')
        __glGetActiveSubroutineUniformiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetActiveSubroutineUniformiv_impl
        __glGetActiveSubroutineUniformiv_impl = (lambda program,shadertype,index,pname,values: tmp(program,shadertype,index,pname,(c_uint8*len(values)).from_buffer(values)))
        global glGetActiveSubroutineUniformiv
        glGetActiveSubroutineUniformiv =__glGetActiveSubroutineUniformiv_impl
    return __glGetActiveSubroutineUniformiv_impl(program,shadertype,index,pname,values)

__glGetActiveUniform_impl = None
def glGetActiveUniform ( program:int,index:int,bufSize:int,length:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],size:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],type:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],name:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetActiveUniform_impl
    if not __glGetActiveUniform_impl:
        fptr = __pyglGetFuncAddress('glGetActiveUniform')
        if not fptr:
            raise RuntimeError('The function glGetActiveUniform is not available (maybe GL has not been initialized yet?)')
        __glGetActiveUniform_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_int,c_void_p,c_void_p,c_void_p,c_void_p )(fptr)
        tmp = __glGetActiveUniform_impl
        __glGetActiveUniform_impl = (lambda program,index,bufSize,length,size,type,name: tmp(program,index,bufSize,(c_uint8*len(length)).from_buffer(length),(c_uint8*len(size)).from_buffer(size),(c_uint8*len(type)).from_buffer(type),(c_uint8*len(name)).from_buffer(name)))
        global glGetActiveUniform
        glGetActiveUniform =__glGetActiveUniform_impl
    return __glGetActiveUniform_impl(program,index,bufSize,length,size,type,name)

__glGetActiveUniformBlockName_impl = None
def glGetActiveUniformBlockName ( program:int,uniformBlockIndex:int,bufSize:int,length:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],uniformBlockName:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetActiveUniformBlockName_impl
    if not __glGetActiveUniformBlockName_impl:
        fptr = __pyglGetFuncAddress('glGetActiveUniformBlockName')
        if not fptr:
            raise RuntimeError('The function glGetActiveUniformBlockName is not available (maybe GL has not been initialized yet?)')
        __glGetActiveUniformBlockName_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_int,c_void_p,c_void_p )(fptr)
        tmp = __glGetActiveUniformBlockName_impl
        __glGetActiveUniformBlockName_impl = (lambda program,uniformBlockIndex,bufSize,length,uniformBlockName: tmp(program,uniformBlockIndex,bufSize,(c_uint8*len(length)).from_buffer(length),(c_uint8*len(uniformBlockName)).from_buffer(uniformBlockName)))
        global glGetActiveUniformBlockName
        glGetActiveUniformBlockName =__glGetActiveUniformBlockName_impl
    return __glGetActiveUniformBlockName_impl(program,uniformBlockIndex,bufSize,length,uniformBlockName)

__glGetActiveUniformBlockiv_impl = None
def glGetActiveUniformBlockiv ( program:int,uniformBlockIndex:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetActiveUniformBlockiv_impl
    if not __glGetActiveUniformBlockiv_impl:
        fptr = __pyglGetFuncAddress('glGetActiveUniformBlockiv')
        if not fptr:
            raise RuntimeError('The function glGetActiveUniformBlockiv is not available (maybe GL has not been initialized yet?)')
        __glGetActiveUniformBlockiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetActiveUniformBlockiv_impl
        __glGetActiveUniformBlockiv_impl = (lambda program,uniformBlockIndex,pname,params: tmp(program,uniformBlockIndex,pname,(c_uint8*len(params)).from_buffer(params)))
        global glGetActiveUniformBlockiv
        glGetActiveUniformBlockiv =__glGetActiveUniformBlockiv_impl
    return __glGetActiveUniformBlockiv_impl(program,uniformBlockIndex,pname,params)

__glGetActiveUniformName_impl = None
def glGetActiveUniformName ( program:int,uniformIndex:int,bufSize:int,length:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],uniformName:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetActiveUniformName_impl
    if not __glGetActiveUniformName_impl:
        fptr = __pyglGetFuncAddress('glGetActiveUniformName')
        if not fptr:
            raise RuntimeError('The function glGetActiveUniformName is not available (maybe GL has not been initialized yet?)')
        __glGetActiveUniformName_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_int,c_void_p,c_void_p )(fptr)
        tmp = __glGetActiveUniformName_impl
        __glGetActiveUniformName_impl = (lambda program,uniformIndex,bufSize,length,uniformName: tmp(program,uniformIndex,bufSize,(c_uint8*len(length)).from_buffer(length),(c_uint8*len(uniformName)).from_buffer(uniformName)))
        global glGetActiveUniformName
        glGetActiveUniformName =__glGetActiveUniformName_impl
    return __glGetActiveUniformName_impl(program,uniformIndex,bufSize,length,uniformName)

__glGetActiveUniformsiv_impl = None
def glGetActiveUniformsiv ( program:int,uniformCount:int,uniformIndices:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetActiveUniformsiv_impl
    if not __glGetActiveUniformsiv_impl:
        fptr = __pyglGetFuncAddress('glGetActiveUniformsiv')
        if not fptr:
            raise RuntimeError('The function glGetActiveUniformsiv is not available (maybe GL has not been initialized yet?)')
        __glGetActiveUniformsiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_void_p,c_uint,c_void_p )(fptr)
        tmp = __glGetActiveUniformsiv_impl
        __glGetActiveUniformsiv_impl = (lambda program,uniformCount,uniformIndices,pname,params: tmp(program,uniformCount,__pyglGetAsConstVoidPointer(uniformIndices),pname,(c_uint8*len(params)).from_buffer(params)))
        global glGetActiveUniformsiv
        glGetActiveUniformsiv =__glGetActiveUniformsiv_impl
    return __glGetActiveUniformsiv_impl(program,uniformCount,uniformIndices,pname,params)

__glGetAttachedShaders_impl = None
def glGetAttachedShaders ( program:int,maxCount:int,count:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],shaders:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetAttachedShaders_impl
    if not __glGetAttachedShaders_impl:
        fptr = __pyglGetFuncAddress('glGetAttachedShaders')
        if not fptr:
            raise RuntimeError('The function glGetAttachedShaders is not available (maybe GL has not been initialized yet?)')
        __glGetAttachedShaders_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_void_p,c_void_p )(fptr)
        tmp = __glGetAttachedShaders_impl
        __glGetAttachedShaders_impl = (lambda program,maxCount,count,shaders: tmp(program,maxCount,(c_uint8*len(count)).from_buffer(count),(c_uint8*len(shaders)).from_buffer(shaders)))
        global glGetAttachedShaders
        glGetAttachedShaders =__glGetAttachedShaders_impl
    return __glGetAttachedShaders_impl(program,maxCount,count,shaders)

__glGetAttribLocation_impl = None
def glGetAttribLocation ( program:int,name:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> int :
    global __glGetAttribLocation_impl
    if not __glGetAttribLocation_impl:
        fptr = __pyglGetFuncAddress('glGetAttribLocation')
        if not fptr:
            raise RuntimeError('The function glGetAttribLocation is not available (maybe GL has not been initialized yet?)')
        __glGetAttribLocation_impl = __PYGL_FUNC_TYPE( c_int,c_uint,c_void_p )(fptr)
        tmp = __glGetAttribLocation_impl
        __glGetAttribLocation_impl = (lambda program,name: tmp(program,c_char_p(name.encode())))
        global glGetAttribLocation
        glGetAttribLocation =__glGetAttribLocation_impl
    return __glGetAttribLocation_impl(program,name)

__glGetBooleani_v_impl = None
def glGetBooleani_v ( target:int,index:int,data:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetBooleani_v_impl
    if not __glGetBooleani_v_impl:
        fptr = __pyglGetFuncAddress('glGetBooleani_v')
        if not fptr:
            raise RuntimeError('The function glGetBooleani_v is not available (maybe GL has not been initialized yet?)')
        __glGetBooleani_v_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetBooleani_v_impl
        __glGetBooleani_v_impl = (lambda target,index,data: tmp(target,index,(c_uint8*len(data)).from_buffer(data)))
        global glGetBooleani_v
        glGetBooleani_v =__glGetBooleani_v_impl
    return __glGetBooleani_v_impl(target,index,data)

__glGetBooleanv_impl = None
def glGetBooleanv ( pname:int,data:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetBooleanv_impl
    if not __glGetBooleanv_impl:
        fptr = __pyglGetFuncAddress('glGetBooleanv')
        if not fptr:
            raise RuntimeError('The function glGetBooleanv is not available (maybe GL has not been initialized yet?)')
        __glGetBooleanv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p )(fptr)
        tmp = __glGetBooleanv_impl
        __glGetBooleanv_impl = (lambda pname,data: tmp(pname,(c_uint8*len(data)).from_buffer(data)))
        global glGetBooleanv
        glGetBooleanv =__glGetBooleanv_impl
    return __glGetBooleanv_impl(pname,data)

__glGetBufferParameteri64v_impl = None
def glGetBufferParameteri64v ( target:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetBufferParameteri64v_impl
    if not __glGetBufferParameteri64v_impl:
        fptr = __pyglGetFuncAddress('glGetBufferParameteri64v')
        if not fptr:
            raise RuntimeError('The function glGetBufferParameteri64v is not available (maybe GL has not been initialized yet?)')
        __glGetBufferParameteri64v_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetBufferParameteri64v_impl
        __glGetBufferParameteri64v_impl = (lambda target,pname,params: tmp(target,pname,(c_uint8*len(params)).from_buffer(params)))
        global glGetBufferParameteri64v
        glGetBufferParameteri64v =__glGetBufferParameteri64v_impl
    return __glGetBufferParameteri64v_impl(target,pname,params)

__glGetBufferParameteriv_impl = None
def glGetBufferParameteriv ( target:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetBufferParameteriv_impl
    if not __glGetBufferParameteriv_impl:
        fptr = __pyglGetFuncAddress('glGetBufferParameteriv')
        if not fptr:
            raise RuntimeError('The function glGetBufferParameteriv is not available (maybe GL has not been initialized yet?)')
        __glGetBufferParameteriv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetBufferParameteriv_impl
        __glGetBufferParameteriv_impl = (lambda target,pname,params: tmp(target,pname,(c_uint8*len(params)).from_buffer(params)))
        global glGetBufferParameteriv
        glGetBufferParameteriv =__glGetBufferParameteriv_impl
    return __glGetBufferParameteriv_impl(target,pname,params)

__glGetBufferPointerv_impl = None
def glGetBufferPointerv ( target:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetBufferPointerv_impl
    if not __glGetBufferPointerv_impl:
        fptr = __pyglGetFuncAddress('glGetBufferPointerv')
        if not fptr:
            raise RuntimeError('The function glGetBufferPointerv is not available (maybe GL has not been initialized yet?)')
        __glGetBufferPointerv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetBufferPointerv_impl
        __glGetBufferPointerv_impl = (lambda target,pname,params: tmp(target,pname,(c_uint8*len(params)).from_buffer(params)))
        global glGetBufferPointerv
        glGetBufferPointerv =__glGetBufferPointerv_impl
    return __glGetBufferPointerv_impl(target,pname,params)

__glGetBufferSubData_impl = None
def glGetBufferSubData ( target:int,offset:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],size:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],data:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetBufferSubData_impl
    if not __glGetBufferSubData_impl:
        fptr = __pyglGetFuncAddress('glGetBufferSubData')
        if not fptr:
            raise RuntimeError('The function glGetBufferSubData is not available (maybe GL has not been initialized yet?)')
        __glGetBufferSubData_impl = __PYGL_FUNC_TYPE( None,c_uint,c_size_t,c_void_p,c_void_p )(fptr)
        tmp = __glGetBufferSubData_impl
        __glGetBufferSubData_impl = (lambda target,offset,size,data: tmp(target,offset,size,(c_uint8*len(data)).from_buffer(data)))
        global glGetBufferSubData
        glGetBufferSubData =__glGetBufferSubData_impl
    return __glGetBufferSubData_impl(target,offset,size,data)

__glGetCompressedTexImage_impl = None
def glGetCompressedTexImage ( target:int,level:int,img:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetCompressedTexImage_impl
    if not __glGetCompressedTexImage_impl:
        fptr = __pyglGetFuncAddress('glGetCompressedTexImage')
        if not fptr:
            raise RuntimeError('The function glGetCompressedTexImage is not available (maybe GL has not been initialized yet?)')
        __glGetCompressedTexImage_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_void_p )(fptr)
        tmp = __glGetCompressedTexImage_impl
        __glGetCompressedTexImage_impl = (lambda target,level,img: tmp(target,level,(c_uint8*len(img)).from_buffer(img)))
        global glGetCompressedTexImage
        glGetCompressedTexImage =__glGetCompressedTexImage_impl
    return __glGetCompressedTexImage_impl(target,level,img)

__glGetCompressedTextureImage_impl = None
def glGetCompressedTextureImage ( texture:int,level:int,bufSize:int,pixels:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetCompressedTextureImage_impl
    if not __glGetCompressedTextureImage_impl:
        fptr = __pyglGetFuncAddress('glGetCompressedTextureImage')
        if not fptr:
            raise RuntimeError('The function glGetCompressedTextureImage is not available (maybe GL has not been initialized yet?)')
        __glGetCompressedTextureImage_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_void_p )(fptr)
        tmp = __glGetCompressedTextureImage_impl
        __glGetCompressedTextureImage_impl = (lambda texture,level,bufSize,pixels: tmp(texture,level,bufSize,(c_uint8*len(pixels)).from_buffer(pixels)))
        global glGetCompressedTextureImage
        glGetCompressedTextureImage =__glGetCompressedTextureImage_impl
    return __glGetCompressedTextureImage_impl(texture,level,bufSize,pixels)

__glGetCompressedTextureSubImage_impl = None
def glGetCompressedTextureSubImage ( texture:int,level:int,xoffset:int,yoffset:int,zoffset:int,width:int,height:int,depth:int,bufSize:int,pixels:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetCompressedTextureSubImage_impl
    if not __glGetCompressedTextureSubImage_impl:
        fptr = __pyglGetFuncAddress('glGetCompressedTextureSubImage')
        if not fptr:
            raise RuntimeError('The function glGetCompressedTextureSubImage is not available (maybe GL has not been initialized yet?)')
        __glGetCompressedTextureSubImage_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_int,c_int,c_int,c_int,c_int,c_int,c_void_p )(fptr)
        tmp = __glGetCompressedTextureSubImage_impl
        __glGetCompressedTextureSubImage_impl = (lambda texture,level,xoffset,yoffset,zoffset,width,height,depth,bufSize,pixels: tmp(texture,level,xoffset,yoffset,zoffset,width,height,depth,bufSize,(c_uint8*len(pixels)).from_buffer(pixels)))
        global glGetCompressedTextureSubImage
        glGetCompressedTextureSubImage =__glGetCompressedTextureSubImage_impl
    return __glGetCompressedTextureSubImage_impl(texture,level,xoffset,yoffset,zoffset,width,height,depth,bufSize,pixels)

__glGetDebugMessageLog_impl = None
def glGetDebugMessageLog ( count:int,bufSize:int,sources:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],types:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],ids:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],severities:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],lengths:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],messageLog:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> int :
    global __glGetDebugMessageLog_impl
    if not __glGetDebugMessageLog_impl:
        fptr = __pyglGetFuncAddress('glGetDebugMessageLog')
        if not fptr:
            raise RuntimeError('The function glGetDebugMessageLog is not available (maybe GL has not been initialized yet?)')
        __glGetDebugMessageLog_impl = __PYGL_FUNC_TYPE( c_uint,c_uint,c_int,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p )(fptr)
        tmp = __glGetDebugMessageLog_impl
        __glGetDebugMessageLog_impl = (lambda count,bufSize,sources,types,ids,severities,lengths,messageLog: tmp(count,bufSize,(c_uint8*len(sources)).from_buffer(sources),(c_uint8*len(types)).from_buffer(types),(c_uint8*len(ids)).from_buffer(ids),(c_uint8*len(severities)).from_buffer(severities),(c_uint8*len(lengths)).from_buffer(lengths),(c_uint8*len(messageLog)).from_buffer(messageLog)))
        global glGetDebugMessageLog
        glGetDebugMessageLog =__glGetDebugMessageLog_impl
    return __glGetDebugMessageLog_impl(count,bufSize,sources,types,ids,severities,lengths,messageLog)

__glGetDoublei_v_impl = None
def glGetDoublei_v ( target:int,index:int,data:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetDoublei_v_impl
    if not __glGetDoublei_v_impl:
        fptr = __pyglGetFuncAddress('glGetDoublei_v')
        if not fptr:
            raise RuntimeError('The function glGetDoublei_v is not available (maybe GL has not been initialized yet?)')
        __glGetDoublei_v_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetDoublei_v_impl
        __glGetDoublei_v_impl = (lambda target,index,data: tmp(target,index,(c_uint8*len(data)).from_buffer(data)))
        global glGetDoublei_v
        glGetDoublei_v =__glGetDoublei_v_impl
    return __glGetDoublei_v_impl(target,index,data)

__glGetDoublev_impl = None
def glGetDoublev ( pname:int,data:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetDoublev_impl
    if not __glGetDoublev_impl:
        fptr = __pyglGetFuncAddress('glGetDoublev')
        if not fptr:
            raise RuntimeError('The function glGetDoublev is not available (maybe GL has not been initialized yet?)')
        __glGetDoublev_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p )(fptr)
        tmp = __glGetDoublev_impl
        __glGetDoublev_impl = (lambda pname,data: tmp(pname,(c_uint8*len(data)).from_buffer(data)))
        global glGetDoublev
        glGetDoublev =__glGetDoublev_impl
    return __glGetDoublev_impl(pname,data)

__glGetError_impl = None
def glGetError (  ) -> int :
    global __glGetError_impl
    if not __glGetError_impl:
        fptr = __pyglGetFuncAddress('glGetError')
        if not fptr:
            raise RuntimeError('The function glGetError is not available (maybe GL has not been initialized yet?)')
        __glGetError_impl = __PYGL_FUNC_TYPE( c_uint )(fptr)
        global glGetError
        glGetError =__glGetError_impl
    return __glGetError_impl()

__glGetFloati_v_impl = None
def glGetFloati_v ( target:int,index:int,data:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetFloati_v_impl
    if not __glGetFloati_v_impl:
        fptr = __pyglGetFuncAddress('glGetFloati_v')
        if not fptr:
            raise RuntimeError('The function glGetFloati_v is not available (maybe GL has not been initialized yet?)')
        __glGetFloati_v_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetFloati_v_impl
        __glGetFloati_v_impl = (lambda target,index,data: tmp(target,index,(c_uint8*len(data)).from_buffer(data)))
        global glGetFloati_v
        glGetFloati_v =__glGetFloati_v_impl
    return __glGetFloati_v_impl(target,index,data)

__glGetFloatv_impl = None
def glGetFloatv ( pname:int,data:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetFloatv_impl
    if not __glGetFloatv_impl:
        fptr = __pyglGetFuncAddress('glGetFloatv')
        if not fptr:
            raise RuntimeError('The function glGetFloatv is not available (maybe GL has not been initialized yet?)')
        __glGetFloatv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p )(fptr)
        tmp = __glGetFloatv_impl
        __glGetFloatv_impl = (lambda pname,data: tmp(pname,(c_uint8*len(data)).from_buffer(data)))
        global glGetFloatv
        glGetFloatv =__glGetFloatv_impl
    return __glGetFloatv_impl(pname,data)

__glGetFragDataIndex_impl = None
def glGetFragDataIndex ( program:int,name:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> int :
    global __glGetFragDataIndex_impl
    if not __glGetFragDataIndex_impl:
        fptr = __pyglGetFuncAddress('glGetFragDataIndex')
        if not fptr:
            raise RuntimeError('The function glGetFragDataIndex is not available (maybe GL has not been initialized yet?)')
        __glGetFragDataIndex_impl = __PYGL_FUNC_TYPE( c_int,c_uint,c_void_p )(fptr)
        tmp = __glGetFragDataIndex_impl
        __glGetFragDataIndex_impl = (lambda program,name: tmp(program,c_char_p(name.encode())))
        global glGetFragDataIndex
        glGetFragDataIndex =__glGetFragDataIndex_impl
    return __glGetFragDataIndex_impl(program,name)

__glGetFragDataLocation_impl = None
def glGetFragDataLocation ( program:int,name:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> int :
    global __glGetFragDataLocation_impl
    if not __glGetFragDataLocation_impl:
        fptr = __pyglGetFuncAddress('glGetFragDataLocation')
        if not fptr:
            raise RuntimeError('The function glGetFragDataLocation is not available (maybe GL has not been initialized yet?)')
        __glGetFragDataLocation_impl = __PYGL_FUNC_TYPE( c_int,c_uint,c_void_p )(fptr)
        tmp = __glGetFragDataLocation_impl
        __glGetFragDataLocation_impl = (lambda program,name: tmp(program,c_char_p(name.encode())))
        global glGetFragDataLocation
        glGetFragDataLocation =__glGetFragDataLocation_impl
    return __glGetFragDataLocation_impl(program,name)

__glGetFramebufferAttachmentParameteriv_impl = None
def glGetFramebufferAttachmentParameteriv ( target:int,attachment:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetFramebufferAttachmentParameteriv_impl
    if not __glGetFramebufferAttachmentParameteriv_impl:
        fptr = __pyglGetFuncAddress('glGetFramebufferAttachmentParameteriv')
        if not fptr:
            raise RuntimeError('The function glGetFramebufferAttachmentParameteriv is not available (maybe GL has not been initialized yet?)')
        __glGetFramebufferAttachmentParameteriv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetFramebufferAttachmentParameteriv_impl
        __glGetFramebufferAttachmentParameteriv_impl = (lambda target,attachment,pname,params: tmp(target,attachment,pname,(c_uint8*len(params)).from_buffer(params)))
        global glGetFramebufferAttachmentParameteriv
        glGetFramebufferAttachmentParameteriv =__glGetFramebufferAttachmentParameteriv_impl
    return __glGetFramebufferAttachmentParameteriv_impl(target,attachment,pname,params)

__glGetFramebufferParameteriv_impl = None
def glGetFramebufferParameteriv ( target:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetFramebufferParameteriv_impl
    if not __glGetFramebufferParameteriv_impl:
        fptr = __pyglGetFuncAddress('glGetFramebufferParameteriv')
        if not fptr:
            raise RuntimeError('The function glGetFramebufferParameteriv is not available (maybe GL has not been initialized yet?)')
        __glGetFramebufferParameteriv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetFramebufferParameteriv_impl
        __glGetFramebufferParameteriv_impl = (lambda target,pname,params: tmp(target,pname,(c_uint8*len(params)).from_buffer(params)))
        global glGetFramebufferParameteriv
        glGetFramebufferParameteriv =__glGetFramebufferParameteriv_impl
    return __glGetFramebufferParameteriv_impl(target,pname,params)

__glGetGraphicsResetStatus_impl = None
def glGetGraphicsResetStatus (  ) -> int :
    global __glGetGraphicsResetStatus_impl
    if not __glGetGraphicsResetStatus_impl:
        fptr = __pyglGetFuncAddress('glGetGraphicsResetStatus')
        if not fptr:
            raise RuntimeError('The function glGetGraphicsResetStatus is not available (maybe GL has not been initialized yet?)')
        __glGetGraphicsResetStatus_impl = __PYGL_FUNC_TYPE( c_uint )(fptr)
        global glGetGraphicsResetStatus
        glGetGraphicsResetStatus =__glGetGraphicsResetStatus_impl
    return __glGetGraphicsResetStatus_impl()

__glGetInteger64i_v_impl = None
def glGetInteger64i_v ( target:int,index:int,data:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetInteger64i_v_impl
    if not __glGetInteger64i_v_impl:
        fptr = __pyglGetFuncAddress('glGetInteger64i_v')
        if not fptr:
            raise RuntimeError('The function glGetInteger64i_v is not available (maybe GL has not been initialized yet?)')
        __glGetInteger64i_v_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetInteger64i_v_impl
        __glGetInteger64i_v_impl = (lambda target,index,data: tmp(target,index,(c_uint8*len(data)).from_buffer(data)))
        global glGetInteger64i_v
        glGetInteger64i_v =__glGetInteger64i_v_impl
    return __glGetInteger64i_v_impl(target,index,data)

__glGetInteger64v_impl = None
def glGetInteger64v ( pname:int,data:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetInteger64v_impl
    if not __glGetInteger64v_impl:
        fptr = __pyglGetFuncAddress('glGetInteger64v')
        if not fptr:
            raise RuntimeError('The function glGetInteger64v is not available (maybe GL has not been initialized yet?)')
        __glGetInteger64v_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p )(fptr)
        tmp = __glGetInteger64v_impl
        __glGetInteger64v_impl = (lambda pname,data: tmp(pname,(c_uint8*len(data)).from_buffer(data)))
        global glGetInteger64v
        glGetInteger64v =__glGetInteger64v_impl
    return __glGetInteger64v_impl(pname,data)

__glGetIntegeri_v_impl = None
def glGetIntegeri_v ( target:int,index:int,data:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetIntegeri_v_impl
    if not __glGetIntegeri_v_impl:
        fptr = __pyglGetFuncAddress('glGetIntegeri_v')
        if not fptr:
            raise RuntimeError('The function glGetIntegeri_v is not available (maybe GL has not been initialized yet?)')
        __glGetIntegeri_v_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetIntegeri_v_impl
        __glGetIntegeri_v_impl = (lambda target,index,data: tmp(target,index,(c_uint8*len(data)).from_buffer(data)))
        global glGetIntegeri_v
        glGetIntegeri_v =__glGetIntegeri_v_impl
    return __glGetIntegeri_v_impl(target,index,data)

__glGetIntegerv_impl = None
def glGetIntegerv ( pname:int,data:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetIntegerv_impl
    if not __glGetIntegerv_impl:
        fptr = __pyglGetFuncAddress('glGetIntegerv')
        if not fptr:
            raise RuntimeError('The function glGetIntegerv is not available (maybe GL has not been initialized yet?)')
        __glGetIntegerv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p )(fptr)
        tmp = __glGetIntegerv_impl
        __glGetIntegerv_impl = (lambda pname,data: tmp(pname,(c_uint8*len(data)).from_buffer(data)))
        global glGetIntegerv
        glGetIntegerv =__glGetIntegerv_impl
    return __glGetIntegerv_impl(pname,data)

__glGetInternalformati64v_impl = None
def glGetInternalformati64v ( target:int,internalformat:int,pname:int,bufSize:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetInternalformati64v_impl
    if not __glGetInternalformati64v_impl:
        fptr = __pyglGetFuncAddress('glGetInternalformati64v')
        if not fptr:
            raise RuntimeError('The function glGetInternalformati64v is not available (maybe GL has not been initialized yet?)')
        __glGetInternalformati64v_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint,c_int,c_void_p )(fptr)
        tmp = __glGetInternalformati64v_impl
        __glGetInternalformati64v_impl = (lambda target,internalformat,pname,bufSize,params: tmp(target,internalformat,pname,bufSize,(c_uint8*len(params)).from_buffer(params)))
        global glGetInternalformati64v
        glGetInternalformati64v =__glGetInternalformati64v_impl
    return __glGetInternalformati64v_impl(target,internalformat,pname,bufSize,params)

__glGetInternalformativ_impl = None
def glGetInternalformativ ( target:int,internalformat:int,pname:int,bufSize:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetInternalformativ_impl
    if not __glGetInternalformativ_impl:
        fptr = __pyglGetFuncAddress('glGetInternalformativ')
        if not fptr:
            raise RuntimeError('The function glGetInternalformativ is not available (maybe GL has not been initialized yet?)')
        __glGetInternalformativ_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint,c_int,c_void_p )(fptr)
        tmp = __glGetInternalformativ_impl
        __glGetInternalformativ_impl = (lambda target,internalformat,pname,bufSize,params: tmp(target,internalformat,pname,bufSize,(c_uint8*len(params)).from_buffer(params)))
        global glGetInternalformativ
        glGetInternalformativ =__glGetInternalformativ_impl
    return __glGetInternalformativ_impl(target,internalformat,pname,bufSize,params)

__glGetMultisamplefv_impl = None
def glGetMultisamplefv ( pname:int,index:int,val:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetMultisamplefv_impl
    if not __glGetMultisamplefv_impl:
        fptr = __pyglGetFuncAddress('glGetMultisamplefv')
        if not fptr:
            raise RuntimeError('The function glGetMultisamplefv is not available (maybe GL has not been initialized yet?)')
        __glGetMultisamplefv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetMultisamplefv_impl
        __glGetMultisamplefv_impl = (lambda pname,index,val: tmp(pname,index,(c_uint8*len(val)).from_buffer(val)))
        global glGetMultisamplefv
        glGetMultisamplefv =__glGetMultisamplefv_impl
    return __glGetMultisamplefv_impl(pname,index,val)

__glGetNamedBufferParameteri64v_impl = None
def glGetNamedBufferParameteri64v ( buffer:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetNamedBufferParameteri64v_impl
    if not __glGetNamedBufferParameteri64v_impl:
        fptr = __pyglGetFuncAddress('glGetNamedBufferParameteri64v')
        if not fptr:
            raise RuntimeError('The function glGetNamedBufferParameteri64v is not available (maybe GL has not been initialized yet?)')
        __glGetNamedBufferParameteri64v_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetNamedBufferParameteri64v_impl
        __glGetNamedBufferParameteri64v_impl = (lambda buffer,pname,params: tmp(buffer,pname,(c_uint8*len(params)).from_buffer(params)))
        global glGetNamedBufferParameteri64v
        glGetNamedBufferParameteri64v =__glGetNamedBufferParameteri64v_impl
    return __glGetNamedBufferParameteri64v_impl(buffer,pname,params)

__glGetNamedBufferParameteriv_impl = None
def glGetNamedBufferParameteriv ( buffer:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetNamedBufferParameteriv_impl
    if not __glGetNamedBufferParameteriv_impl:
        fptr = __pyglGetFuncAddress('glGetNamedBufferParameteriv')
        if not fptr:
            raise RuntimeError('The function glGetNamedBufferParameteriv is not available (maybe GL has not been initialized yet?)')
        __glGetNamedBufferParameteriv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetNamedBufferParameteriv_impl
        __glGetNamedBufferParameteriv_impl = (lambda buffer,pname,params: tmp(buffer,pname,(c_uint8*len(params)).from_buffer(params)))
        global glGetNamedBufferParameteriv
        glGetNamedBufferParameteriv =__glGetNamedBufferParameteriv_impl
    return __glGetNamedBufferParameteriv_impl(buffer,pname,params)

__glGetNamedBufferPointerv_impl = None
def glGetNamedBufferPointerv ( buffer:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetNamedBufferPointerv_impl
    if not __glGetNamedBufferPointerv_impl:
        fptr = __pyglGetFuncAddress('glGetNamedBufferPointerv')
        if not fptr:
            raise RuntimeError('The function glGetNamedBufferPointerv is not available (maybe GL has not been initialized yet?)')
        __glGetNamedBufferPointerv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetNamedBufferPointerv_impl
        __glGetNamedBufferPointerv_impl = (lambda buffer,pname,params: tmp(buffer,pname,(c_uint8*len(params)).from_buffer(params)))
        global glGetNamedBufferPointerv
        glGetNamedBufferPointerv =__glGetNamedBufferPointerv_impl
    return __glGetNamedBufferPointerv_impl(buffer,pname,params)

__glGetNamedBufferSubData_impl = None
def glGetNamedBufferSubData ( buffer:int,offset:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],size:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],data:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetNamedBufferSubData_impl
    if not __glGetNamedBufferSubData_impl:
        fptr = __pyglGetFuncAddress('glGetNamedBufferSubData')
        if not fptr:
            raise RuntimeError('The function glGetNamedBufferSubData is not available (maybe GL has not been initialized yet?)')
        __glGetNamedBufferSubData_impl = __PYGL_FUNC_TYPE( None,c_uint,c_size_t,c_void_p,c_void_p )(fptr)
        tmp = __glGetNamedBufferSubData_impl
        __glGetNamedBufferSubData_impl = (lambda buffer,offset,size,data: tmp(buffer,offset,size,(c_uint8*len(data)).from_buffer(data)))
        global glGetNamedBufferSubData
        glGetNamedBufferSubData =__glGetNamedBufferSubData_impl
    return __glGetNamedBufferSubData_impl(buffer,offset,size,data)

__glGetNamedFramebufferAttachmentParameteriv_impl = None
def glGetNamedFramebufferAttachmentParameteriv ( framebuffer:int,attachment:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetNamedFramebufferAttachmentParameteriv_impl
    if not __glGetNamedFramebufferAttachmentParameteriv_impl:
        fptr = __pyglGetFuncAddress('glGetNamedFramebufferAttachmentParameteriv')
        if not fptr:
            raise RuntimeError('The function glGetNamedFramebufferAttachmentParameteriv is not available (maybe GL has not been initialized yet?)')
        __glGetNamedFramebufferAttachmentParameteriv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetNamedFramebufferAttachmentParameteriv_impl
        __glGetNamedFramebufferAttachmentParameteriv_impl = (lambda framebuffer,attachment,pname,params: tmp(framebuffer,attachment,pname,(c_uint8*len(params)).from_buffer(params)))
        global glGetNamedFramebufferAttachmentParameteriv
        glGetNamedFramebufferAttachmentParameteriv =__glGetNamedFramebufferAttachmentParameteriv_impl
    return __glGetNamedFramebufferAttachmentParameteriv_impl(framebuffer,attachment,pname,params)

__glGetNamedFramebufferParameteriv_impl = None
def glGetNamedFramebufferParameteriv ( framebuffer:int,pname:int,param:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetNamedFramebufferParameteriv_impl
    if not __glGetNamedFramebufferParameteriv_impl:
        fptr = __pyglGetFuncAddress('glGetNamedFramebufferParameteriv')
        if not fptr:
            raise RuntimeError('The function glGetNamedFramebufferParameteriv is not available (maybe GL has not been initialized yet?)')
        __glGetNamedFramebufferParameteriv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetNamedFramebufferParameteriv_impl
        __glGetNamedFramebufferParameteriv_impl = (lambda framebuffer,pname,param: tmp(framebuffer,pname,(c_uint8*len(param)).from_buffer(param)))
        global glGetNamedFramebufferParameteriv
        glGetNamedFramebufferParameteriv =__glGetNamedFramebufferParameteriv_impl
    return __glGetNamedFramebufferParameteriv_impl(framebuffer,pname,param)

__glGetNamedRenderbufferParameteriv_impl = None
def glGetNamedRenderbufferParameteriv ( renderbuffer:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetNamedRenderbufferParameteriv_impl
    if not __glGetNamedRenderbufferParameteriv_impl:
        fptr = __pyglGetFuncAddress('glGetNamedRenderbufferParameteriv')
        if not fptr:
            raise RuntimeError('The function glGetNamedRenderbufferParameteriv is not available (maybe GL has not been initialized yet?)')
        __glGetNamedRenderbufferParameteriv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetNamedRenderbufferParameteriv_impl
        __glGetNamedRenderbufferParameteriv_impl = (lambda renderbuffer,pname,params: tmp(renderbuffer,pname,(c_uint8*len(params)).from_buffer(params)))
        global glGetNamedRenderbufferParameteriv
        glGetNamedRenderbufferParameteriv =__glGetNamedRenderbufferParameteriv_impl
    return __glGetNamedRenderbufferParameteriv_impl(renderbuffer,pname,params)

__glGetObjectLabel_impl = None
def glGetObjectLabel ( identifier:int,name:int,bufSize:int,length:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],label:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetObjectLabel_impl
    if not __glGetObjectLabel_impl:
        fptr = __pyglGetFuncAddress('glGetObjectLabel')
        if not fptr:
            raise RuntimeError('The function glGetObjectLabel is not available (maybe GL has not been initialized yet?)')
        __glGetObjectLabel_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_int,c_void_p,c_void_p )(fptr)
        tmp = __glGetObjectLabel_impl
        __glGetObjectLabel_impl = (lambda identifier,name,bufSize,length,label: tmp(identifier,name,bufSize,(c_uint8*len(length)).from_buffer(length),(c_uint8*len(label)).from_buffer(label)))
        global glGetObjectLabel
        glGetObjectLabel =__glGetObjectLabel_impl
    return __glGetObjectLabel_impl(identifier,name,bufSize,length,label)

__glGetObjectPtrLabel_impl = None
def glGetObjectPtrLabel ( ptr:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],bufSize:int,length:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],label:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetObjectPtrLabel_impl
    if not __glGetObjectPtrLabel_impl:
        fptr = __pyglGetFuncAddress('glGetObjectPtrLabel')
        if not fptr:
            raise RuntimeError('The function glGetObjectPtrLabel is not available (maybe GL has not been initialized yet?)')
        __glGetObjectPtrLabel_impl = __PYGL_FUNC_TYPE( None,c_void_p,c_int,c_void_p,c_void_p )(fptr)
        tmp = __glGetObjectPtrLabel_impl
        __glGetObjectPtrLabel_impl = (lambda ptr,bufSize,length,label: tmp(__pyglGetAsConstVoidPointer(ptr),bufSize,(c_uint8*len(length)).from_buffer(length),(c_uint8*len(label)).from_buffer(label)))
        global glGetObjectPtrLabel
        glGetObjectPtrLabel =__glGetObjectPtrLabel_impl
    return __glGetObjectPtrLabel_impl(ptr,bufSize,length,label)

__glGetProgramBinary_impl = None
def glGetProgramBinary ( program:int,bufSize:int,length:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],binaryFormat:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],binary:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetProgramBinary_impl
    if not __glGetProgramBinary_impl:
        fptr = __pyglGetFuncAddress('glGetProgramBinary')
        if not fptr:
            raise RuntimeError('The function glGetProgramBinary is not available (maybe GL has not been initialized yet?)')
        __glGetProgramBinary_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_void_p,c_void_p,c_void_p )(fptr)
        tmp = __glGetProgramBinary_impl
        __glGetProgramBinary_impl = (lambda program,bufSize,length,binaryFormat,binary: tmp(program,bufSize,(c_uint8*len(length)).from_buffer(length),(c_uint8*len(binaryFormat)).from_buffer(binaryFormat),(c_uint8*len(binary)).from_buffer(binary)))
        global glGetProgramBinary
        glGetProgramBinary =__glGetProgramBinary_impl
    return __glGetProgramBinary_impl(program,bufSize,length,binaryFormat,binary)

__glGetProgramInfoLog_impl = None
def glGetProgramInfoLog ( program:int,bufSize:int,length:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],infoLog:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetProgramInfoLog_impl
    if not __glGetProgramInfoLog_impl:
        fptr = __pyglGetFuncAddress('glGetProgramInfoLog')
        if not fptr:
            raise RuntimeError('The function glGetProgramInfoLog is not available (maybe GL has not been initialized yet?)')
        __glGetProgramInfoLog_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_void_p,c_void_p )(fptr)
        tmp = __glGetProgramInfoLog_impl
        __glGetProgramInfoLog_impl = (lambda program,bufSize,length,infoLog: tmp(program,bufSize,(c_uint8*len(length)).from_buffer(length),(c_uint8*len(infoLog)).from_buffer(infoLog)))
        global glGetProgramInfoLog
        glGetProgramInfoLog =__glGetProgramInfoLog_impl
    return __glGetProgramInfoLog_impl(program,bufSize,length,infoLog)

__glGetProgramInterfaceiv_impl = None
def glGetProgramInterfaceiv ( program:int,programInterface:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetProgramInterfaceiv_impl
    if not __glGetProgramInterfaceiv_impl:
        fptr = __pyglGetFuncAddress('glGetProgramInterfaceiv')
        if not fptr:
            raise RuntimeError('The function glGetProgramInterfaceiv is not available (maybe GL has not been initialized yet?)')
        __glGetProgramInterfaceiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetProgramInterfaceiv_impl
        __glGetProgramInterfaceiv_impl = (lambda program,programInterface,pname,params: tmp(program,programInterface,pname,(c_uint8*len(params)).from_buffer(params)))
        global glGetProgramInterfaceiv
        glGetProgramInterfaceiv =__glGetProgramInterfaceiv_impl
    return __glGetProgramInterfaceiv_impl(program,programInterface,pname,params)

__glGetProgramPipelineInfoLog_impl = None
def glGetProgramPipelineInfoLog ( pipeline:int,bufSize:int,length:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],infoLog:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetProgramPipelineInfoLog_impl
    if not __glGetProgramPipelineInfoLog_impl:
        fptr = __pyglGetFuncAddress('glGetProgramPipelineInfoLog')
        if not fptr:
            raise RuntimeError('The function glGetProgramPipelineInfoLog is not available (maybe GL has not been initialized yet?)')
        __glGetProgramPipelineInfoLog_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_void_p,c_void_p )(fptr)
        tmp = __glGetProgramPipelineInfoLog_impl
        __glGetProgramPipelineInfoLog_impl = (lambda pipeline,bufSize,length,infoLog: tmp(pipeline,bufSize,(c_uint8*len(length)).from_buffer(length),(c_uint8*len(infoLog)).from_buffer(infoLog)))
        global glGetProgramPipelineInfoLog
        glGetProgramPipelineInfoLog =__glGetProgramPipelineInfoLog_impl
    return __glGetProgramPipelineInfoLog_impl(pipeline,bufSize,length,infoLog)

__glGetProgramPipelineiv_impl = None
def glGetProgramPipelineiv ( pipeline:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetProgramPipelineiv_impl
    if not __glGetProgramPipelineiv_impl:
        fptr = __pyglGetFuncAddress('glGetProgramPipelineiv')
        if not fptr:
            raise RuntimeError('The function glGetProgramPipelineiv is not available (maybe GL has not been initialized yet?)')
        __glGetProgramPipelineiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetProgramPipelineiv_impl
        __glGetProgramPipelineiv_impl = (lambda pipeline,pname,params: tmp(pipeline,pname,(c_uint8*len(params)).from_buffer(params)))
        global glGetProgramPipelineiv
        glGetProgramPipelineiv =__glGetProgramPipelineiv_impl
    return __glGetProgramPipelineiv_impl(pipeline,pname,params)

__glGetProgramResourceIndex_impl = None
def glGetProgramResourceIndex ( program:int,programInterface:int,name:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> int :
    global __glGetProgramResourceIndex_impl
    if not __glGetProgramResourceIndex_impl:
        fptr = __pyglGetFuncAddress('glGetProgramResourceIndex')
        if not fptr:
            raise RuntimeError('The function glGetProgramResourceIndex is not available (maybe GL has not been initialized yet?)')
        __glGetProgramResourceIndex_impl = __PYGL_FUNC_TYPE( c_uint,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetProgramResourceIndex_impl
        __glGetProgramResourceIndex_impl = (lambda program,programInterface,name: tmp(program,programInterface,c_char_p(name.encode())))
        global glGetProgramResourceIndex
        glGetProgramResourceIndex =__glGetProgramResourceIndex_impl
    return __glGetProgramResourceIndex_impl(program,programInterface,name)

__glGetProgramResourceLocation_impl = None
def glGetProgramResourceLocation ( program:int,programInterface:int,name:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> int :
    global __glGetProgramResourceLocation_impl
    if not __glGetProgramResourceLocation_impl:
        fptr = __pyglGetFuncAddress('glGetProgramResourceLocation')
        if not fptr:
            raise RuntimeError('The function glGetProgramResourceLocation is not available (maybe GL has not been initialized yet?)')
        __glGetProgramResourceLocation_impl = __PYGL_FUNC_TYPE( c_int,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetProgramResourceLocation_impl
        __glGetProgramResourceLocation_impl = (lambda program,programInterface,name: tmp(program,programInterface,c_char_p(name.encode())))
        global glGetProgramResourceLocation
        glGetProgramResourceLocation =__glGetProgramResourceLocation_impl
    return __glGetProgramResourceLocation_impl(program,programInterface,name)

__glGetProgramResourceLocationIndex_impl = None
def glGetProgramResourceLocationIndex ( program:int,programInterface:int,name:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> int :
    global __glGetProgramResourceLocationIndex_impl
    if not __glGetProgramResourceLocationIndex_impl:
        fptr = __pyglGetFuncAddress('glGetProgramResourceLocationIndex')
        if not fptr:
            raise RuntimeError('The function glGetProgramResourceLocationIndex is not available (maybe GL has not been initialized yet?)')
        __glGetProgramResourceLocationIndex_impl = __PYGL_FUNC_TYPE( c_int,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetProgramResourceLocationIndex_impl
        __glGetProgramResourceLocationIndex_impl = (lambda program,programInterface,name: tmp(program,programInterface,c_char_p(name.encode())))
        global glGetProgramResourceLocationIndex
        glGetProgramResourceLocationIndex =__glGetProgramResourceLocationIndex_impl
    return __glGetProgramResourceLocationIndex_impl(program,programInterface,name)

__glGetProgramResourceName_impl = None
def glGetProgramResourceName ( program:int,programInterface:int,index:int,bufSize:int,length:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],name:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetProgramResourceName_impl
    if not __glGetProgramResourceName_impl:
        fptr = __pyglGetFuncAddress('glGetProgramResourceName')
        if not fptr:
            raise RuntimeError('The function glGetProgramResourceName is not available (maybe GL has not been initialized yet?)')
        __glGetProgramResourceName_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint,c_int,c_void_p,c_void_p )(fptr)
        tmp = __glGetProgramResourceName_impl
        __glGetProgramResourceName_impl = (lambda program,programInterface,index,bufSize,length,name: tmp(program,programInterface,index,bufSize,(c_uint8*len(length)).from_buffer(length),(c_uint8*len(name)).from_buffer(name)))
        global glGetProgramResourceName
        glGetProgramResourceName =__glGetProgramResourceName_impl
    return __glGetProgramResourceName_impl(program,programInterface,index,bufSize,length,name)

__glGetProgramResourceiv_impl = None
def glGetProgramResourceiv ( program:int,programInterface:int,index:int,propCount:int,props:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],bufSize:int,length:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetProgramResourceiv_impl
    if not __glGetProgramResourceiv_impl:
        fptr = __pyglGetFuncAddress('glGetProgramResourceiv')
        if not fptr:
            raise RuntimeError('The function glGetProgramResourceiv is not available (maybe GL has not been initialized yet?)')
        __glGetProgramResourceiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint,c_int,c_void_p,c_int,c_void_p,c_void_p )(fptr)
        tmp = __glGetProgramResourceiv_impl
        __glGetProgramResourceiv_impl = (lambda program,programInterface,index,propCount,props,bufSize,length,params: tmp(program,programInterface,index,propCount,__pyglGetAsConstVoidPointer(props),bufSize,(c_uint8*len(length)).from_buffer(length),(c_uint8*len(params)).from_buffer(params)))
        global glGetProgramResourceiv
        glGetProgramResourceiv =__glGetProgramResourceiv_impl
    return __glGetProgramResourceiv_impl(program,programInterface,index,propCount,props,bufSize,length,params)

__glGetProgramStageiv_impl = None
def glGetProgramStageiv ( program:int,shadertype:int,pname:int,values:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetProgramStageiv_impl
    if not __glGetProgramStageiv_impl:
        fptr = __pyglGetFuncAddress('glGetProgramStageiv')
        if not fptr:
            raise RuntimeError('The function glGetProgramStageiv is not available (maybe GL has not been initialized yet?)')
        __glGetProgramStageiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetProgramStageiv_impl
        __glGetProgramStageiv_impl = (lambda program,shadertype,pname,values: tmp(program,shadertype,pname,(c_uint8*len(values)).from_buffer(values)))
        global glGetProgramStageiv
        glGetProgramStageiv =__glGetProgramStageiv_impl
    return __glGetProgramStageiv_impl(program,shadertype,pname,values)

__glGetProgramiv_impl = None
def glGetProgramiv ( program:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetProgramiv_impl
    if not __glGetProgramiv_impl:
        fptr = __pyglGetFuncAddress('glGetProgramiv')
        if not fptr:
            raise RuntimeError('The function glGetProgramiv is not available (maybe GL has not been initialized yet?)')
        __glGetProgramiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetProgramiv_impl
        __glGetProgramiv_impl = (lambda program,pname,params: tmp(program,pname,(c_uint8*len(params)).from_buffer(params)))
        global glGetProgramiv
        glGetProgramiv =__glGetProgramiv_impl
    return __glGetProgramiv_impl(program,pname,params)

__glGetQueryBufferObjecti64v_impl = None
def glGetQueryBufferObjecti64v ( id:int,buffer:int,pname:int,offset:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetQueryBufferObjecti64v_impl
    if not __glGetQueryBufferObjecti64v_impl:
        fptr = __pyglGetFuncAddress('glGetQueryBufferObjecti64v')
        if not fptr:
            raise RuntimeError('The function glGetQueryBufferObjecti64v is not available (maybe GL has not been initialized yet?)')
        __glGetQueryBufferObjecti64v_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint,c_size_t )(fptr)
        global glGetQueryBufferObjecti64v
        glGetQueryBufferObjecti64v =__glGetQueryBufferObjecti64v_impl
    return __glGetQueryBufferObjecti64v_impl(id,buffer,pname,offset)

__glGetQueryBufferObjectiv_impl = None
def glGetQueryBufferObjectiv ( id:int,buffer:int,pname:int,offset:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetQueryBufferObjectiv_impl
    if not __glGetQueryBufferObjectiv_impl:
        fptr = __pyglGetFuncAddress('glGetQueryBufferObjectiv')
        if not fptr:
            raise RuntimeError('The function glGetQueryBufferObjectiv is not available (maybe GL has not been initialized yet?)')
        __glGetQueryBufferObjectiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint,c_size_t )(fptr)
        global glGetQueryBufferObjectiv
        glGetQueryBufferObjectiv =__glGetQueryBufferObjectiv_impl
    return __glGetQueryBufferObjectiv_impl(id,buffer,pname,offset)

__glGetQueryBufferObjectui64v_impl = None
def glGetQueryBufferObjectui64v ( id:int,buffer:int,pname:int,offset:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetQueryBufferObjectui64v_impl
    if not __glGetQueryBufferObjectui64v_impl:
        fptr = __pyglGetFuncAddress('glGetQueryBufferObjectui64v')
        if not fptr:
            raise RuntimeError('The function glGetQueryBufferObjectui64v is not available (maybe GL has not been initialized yet?)')
        __glGetQueryBufferObjectui64v_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint,c_size_t )(fptr)
        global glGetQueryBufferObjectui64v
        glGetQueryBufferObjectui64v =__glGetQueryBufferObjectui64v_impl
    return __glGetQueryBufferObjectui64v_impl(id,buffer,pname,offset)

__glGetQueryBufferObjectuiv_impl = None
def glGetQueryBufferObjectuiv ( id:int,buffer:int,pname:int,offset:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetQueryBufferObjectuiv_impl
    if not __glGetQueryBufferObjectuiv_impl:
        fptr = __pyglGetFuncAddress('glGetQueryBufferObjectuiv')
        if not fptr:
            raise RuntimeError('The function glGetQueryBufferObjectuiv is not available (maybe GL has not been initialized yet?)')
        __glGetQueryBufferObjectuiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint,c_size_t )(fptr)
        global glGetQueryBufferObjectuiv
        glGetQueryBufferObjectuiv =__glGetQueryBufferObjectuiv_impl
    return __glGetQueryBufferObjectuiv_impl(id,buffer,pname,offset)

__glGetQueryIndexediv_impl = None
def glGetQueryIndexediv ( target:int,index:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetQueryIndexediv_impl
    if not __glGetQueryIndexediv_impl:
        fptr = __pyglGetFuncAddress('glGetQueryIndexediv')
        if not fptr:
            raise RuntimeError('The function glGetQueryIndexediv is not available (maybe GL has not been initialized yet?)')
        __glGetQueryIndexediv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetQueryIndexediv_impl
        __glGetQueryIndexediv_impl = (lambda target,index,pname,params: tmp(target,index,pname,(c_uint8*len(params)).from_buffer(params)))
        global glGetQueryIndexediv
        glGetQueryIndexediv =__glGetQueryIndexediv_impl
    return __glGetQueryIndexediv_impl(target,index,pname,params)

__glGetQueryObjecti64v_impl = None
def glGetQueryObjecti64v ( id:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetQueryObjecti64v_impl
    if not __glGetQueryObjecti64v_impl:
        fptr = __pyglGetFuncAddress('glGetQueryObjecti64v')
        if not fptr:
            raise RuntimeError('The function glGetQueryObjecti64v is not available (maybe GL has not been initialized yet?)')
        __glGetQueryObjecti64v_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetQueryObjecti64v_impl
        __glGetQueryObjecti64v_impl = (lambda id,pname,params: tmp(id,pname,(c_uint8*len(params)).from_buffer(params)))
        global glGetQueryObjecti64v
        glGetQueryObjecti64v =__glGetQueryObjecti64v_impl
    return __glGetQueryObjecti64v_impl(id,pname,params)

__glGetQueryObjectiv_impl = None
def glGetQueryObjectiv ( id:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetQueryObjectiv_impl
    if not __glGetQueryObjectiv_impl:
        fptr = __pyglGetFuncAddress('glGetQueryObjectiv')
        if not fptr:
            raise RuntimeError('The function glGetQueryObjectiv is not available (maybe GL has not been initialized yet?)')
        __glGetQueryObjectiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetQueryObjectiv_impl
        __glGetQueryObjectiv_impl = (lambda id,pname,params: tmp(id,pname,(c_uint8*len(params)).from_buffer(params)))
        global glGetQueryObjectiv
        glGetQueryObjectiv =__glGetQueryObjectiv_impl
    return __glGetQueryObjectiv_impl(id,pname,params)

__glGetQueryObjectui64v_impl = None
def glGetQueryObjectui64v ( id:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetQueryObjectui64v_impl
    if not __glGetQueryObjectui64v_impl:
        fptr = __pyglGetFuncAddress('glGetQueryObjectui64v')
        if not fptr:
            raise RuntimeError('The function glGetQueryObjectui64v is not available (maybe GL has not been initialized yet?)')
        __glGetQueryObjectui64v_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetQueryObjectui64v_impl
        __glGetQueryObjectui64v_impl = (lambda id,pname,params: tmp(id,pname,(c_uint8*len(params)).from_buffer(params)))
        global glGetQueryObjectui64v
        glGetQueryObjectui64v =__glGetQueryObjectui64v_impl
    return __glGetQueryObjectui64v_impl(id,pname,params)

__glGetQueryObjectuiv_impl = None
def glGetQueryObjectuiv ( id:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetQueryObjectuiv_impl
    if not __glGetQueryObjectuiv_impl:
        fptr = __pyglGetFuncAddress('glGetQueryObjectuiv')
        if not fptr:
            raise RuntimeError('The function glGetQueryObjectuiv is not available (maybe GL has not been initialized yet?)')
        __glGetQueryObjectuiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetQueryObjectuiv_impl
        __glGetQueryObjectuiv_impl = (lambda id,pname,params: tmp(id,pname,(c_uint8*len(params)).from_buffer(params)))
        global glGetQueryObjectuiv
        glGetQueryObjectuiv =__glGetQueryObjectuiv_impl
    return __glGetQueryObjectuiv_impl(id,pname,params)

__glGetQueryiv_impl = None
def glGetQueryiv ( target:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetQueryiv_impl
    if not __glGetQueryiv_impl:
        fptr = __pyglGetFuncAddress('glGetQueryiv')
        if not fptr:
            raise RuntimeError('The function glGetQueryiv is not available (maybe GL has not been initialized yet?)')
        __glGetQueryiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetQueryiv_impl
        __glGetQueryiv_impl = (lambda target,pname,params: tmp(target,pname,(c_uint8*len(params)).from_buffer(params)))
        global glGetQueryiv
        glGetQueryiv =__glGetQueryiv_impl
    return __glGetQueryiv_impl(target,pname,params)

__glGetRenderbufferParameteriv_impl = None
def glGetRenderbufferParameteriv ( target:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetRenderbufferParameteriv_impl
    if not __glGetRenderbufferParameteriv_impl:
        fptr = __pyglGetFuncAddress('glGetRenderbufferParameteriv')
        if not fptr:
            raise RuntimeError('The function glGetRenderbufferParameteriv is not available (maybe GL has not been initialized yet?)')
        __glGetRenderbufferParameteriv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetRenderbufferParameteriv_impl
        __glGetRenderbufferParameteriv_impl = (lambda target,pname,params: tmp(target,pname,(c_uint8*len(params)).from_buffer(params)))
        global glGetRenderbufferParameteriv
        glGetRenderbufferParameteriv =__glGetRenderbufferParameteriv_impl
    return __glGetRenderbufferParameteriv_impl(target,pname,params)

__glGetSamplerParameterIiv_impl = None
def glGetSamplerParameterIiv ( sampler:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetSamplerParameterIiv_impl
    if not __glGetSamplerParameterIiv_impl:
        fptr = __pyglGetFuncAddress('glGetSamplerParameterIiv')
        if not fptr:
            raise RuntimeError('The function glGetSamplerParameterIiv is not available (maybe GL has not been initialized yet?)')
        __glGetSamplerParameterIiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetSamplerParameterIiv_impl
        __glGetSamplerParameterIiv_impl = (lambda sampler,pname,params: tmp(sampler,pname,(c_uint8*len(params)).from_buffer(params)))
        global glGetSamplerParameterIiv
        glGetSamplerParameterIiv =__glGetSamplerParameterIiv_impl
    return __glGetSamplerParameterIiv_impl(sampler,pname,params)

__glGetSamplerParameterIuiv_impl = None
def glGetSamplerParameterIuiv ( sampler:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetSamplerParameterIuiv_impl
    if not __glGetSamplerParameterIuiv_impl:
        fptr = __pyglGetFuncAddress('glGetSamplerParameterIuiv')
        if not fptr:
            raise RuntimeError('The function glGetSamplerParameterIuiv is not available (maybe GL has not been initialized yet?)')
        __glGetSamplerParameterIuiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetSamplerParameterIuiv_impl
        __glGetSamplerParameterIuiv_impl = (lambda sampler,pname,params: tmp(sampler,pname,(c_uint8*len(params)).from_buffer(params)))
        global glGetSamplerParameterIuiv
        glGetSamplerParameterIuiv =__glGetSamplerParameterIuiv_impl
    return __glGetSamplerParameterIuiv_impl(sampler,pname,params)

__glGetSamplerParameterfv_impl = None
def glGetSamplerParameterfv ( sampler:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetSamplerParameterfv_impl
    if not __glGetSamplerParameterfv_impl:
        fptr = __pyglGetFuncAddress('glGetSamplerParameterfv')
        if not fptr:
            raise RuntimeError('The function glGetSamplerParameterfv is not available (maybe GL has not been initialized yet?)')
        __glGetSamplerParameterfv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetSamplerParameterfv_impl
        __glGetSamplerParameterfv_impl = (lambda sampler,pname,params: tmp(sampler,pname,(c_uint8*len(params)).from_buffer(params)))
        global glGetSamplerParameterfv
        glGetSamplerParameterfv =__glGetSamplerParameterfv_impl
    return __glGetSamplerParameterfv_impl(sampler,pname,params)

__glGetSamplerParameteriv_impl = None
def glGetSamplerParameteriv ( sampler:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetSamplerParameteriv_impl
    if not __glGetSamplerParameteriv_impl:
        fptr = __pyglGetFuncAddress('glGetSamplerParameteriv')
        if not fptr:
            raise RuntimeError('The function glGetSamplerParameteriv is not available (maybe GL has not been initialized yet?)')
        __glGetSamplerParameteriv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetSamplerParameteriv_impl
        __glGetSamplerParameteriv_impl = (lambda sampler,pname,params: tmp(sampler,pname,(c_uint8*len(params)).from_buffer(params)))
        global glGetSamplerParameteriv
        glGetSamplerParameteriv =__glGetSamplerParameteriv_impl
    return __glGetSamplerParameteriv_impl(sampler,pname,params)

__glGetShaderInfoLog_impl = None
def glGetShaderInfoLog ( shader:int,bufSize:int,length:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],infoLog:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetShaderInfoLog_impl
    if not __glGetShaderInfoLog_impl:
        fptr = __pyglGetFuncAddress('glGetShaderInfoLog')
        if not fptr:
            raise RuntimeError('The function glGetShaderInfoLog is not available (maybe GL has not been initialized yet?)')
        __glGetShaderInfoLog_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_void_p,c_void_p )(fptr)
        tmp = __glGetShaderInfoLog_impl
        __glGetShaderInfoLog_impl = (lambda shader,bufSize,length,infoLog: tmp(shader,bufSize,(c_uint8*len(length)).from_buffer(length),(c_uint8*len(infoLog)).from_buffer(infoLog)))
        global glGetShaderInfoLog
        glGetShaderInfoLog =__glGetShaderInfoLog_impl
    return __glGetShaderInfoLog_impl(shader,bufSize,length,infoLog)

__glGetShaderPrecisionFormat_impl = None
def glGetShaderPrecisionFormat ( shadertype:int,precisiontype:int,range:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],precision:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetShaderPrecisionFormat_impl
    if not __glGetShaderPrecisionFormat_impl:
        fptr = __pyglGetFuncAddress('glGetShaderPrecisionFormat')
        if not fptr:
            raise RuntimeError('The function glGetShaderPrecisionFormat is not available (maybe GL has not been initialized yet?)')
        __glGetShaderPrecisionFormat_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p,c_void_p )(fptr)
        tmp = __glGetShaderPrecisionFormat_impl
        __glGetShaderPrecisionFormat_impl = (lambda shadertype,precisiontype,range,precision: tmp(shadertype,precisiontype,(c_uint8*len(range)).from_buffer(range),(c_uint8*len(precision)).from_buffer(precision)))
        global glGetShaderPrecisionFormat
        glGetShaderPrecisionFormat =__glGetShaderPrecisionFormat_impl
    return __glGetShaderPrecisionFormat_impl(shadertype,precisiontype,range,precision)

__glGetShaderSource_impl = None
def glGetShaderSource ( shader:int,bufSize:int,length:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],source:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetShaderSource_impl
    if not __glGetShaderSource_impl:
        fptr = __pyglGetFuncAddress('glGetShaderSource')
        if not fptr:
            raise RuntimeError('The function glGetShaderSource is not available (maybe GL has not been initialized yet?)')
        __glGetShaderSource_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_void_p,c_void_p )(fptr)
        tmp = __glGetShaderSource_impl
        __glGetShaderSource_impl = (lambda shader,bufSize,length,source: tmp(shader,bufSize,(c_uint8*len(length)).from_buffer(length),(c_uint8*len(source)).from_buffer(source)))
        global glGetShaderSource
        glGetShaderSource =__glGetShaderSource_impl
    return __glGetShaderSource_impl(shader,bufSize,length,source)

__glGetShaderiv_impl = None
def glGetShaderiv ( shader:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetShaderiv_impl
    if not __glGetShaderiv_impl:
        fptr = __pyglGetFuncAddress('glGetShaderiv')
        if not fptr:
            raise RuntimeError('The function glGetShaderiv is not available (maybe GL has not been initialized yet?)')
        __glGetShaderiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetShaderiv_impl
        __glGetShaderiv_impl = (lambda shader,pname,params: tmp(shader,pname,(c_uint8*len(params)).from_buffer(params)))
        global glGetShaderiv
        glGetShaderiv =__glGetShaderiv_impl
    return __glGetShaderiv_impl(shader,pname,params)

__glGetString_impl = None
def glGetString ( name:int ) -> c_char_p :
    global __glGetString_impl
    if not __glGetString_impl:
        fptr = __pyglGetFuncAddress('glGetString')
        if not fptr:
            raise RuntimeError('The function glGetString is not available (maybe GL has not been initialized yet?)')
        __glGetString_impl = __PYGL_FUNC_TYPE( c_char_p,c_uint )(fptr)
        global glGetString
        glGetString =__glGetString_impl
    return __glGetString_impl(name)

__glGetStringi_impl = None
def glGetStringi ( name:int,index:int ) -> c_char_p :
    global __glGetStringi_impl
    if not __glGetStringi_impl:
        fptr = __pyglGetFuncAddress('glGetStringi')
        if not fptr:
            raise RuntimeError('The function glGetStringi is not available (maybe GL has not been initialized yet?)')
        __glGetStringi_impl = __PYGL_FUNC_TYPE( c_char_p,c_uint,c_uint )(fptr)
        global glGetStringi
        glGetStringi =__glGetStringi_impl
    return __glGetStringi_impl(name,index)

__glGetSubroutineIndex_impl = None
def glGetSubroutineIndex ( program:int,shadertype:int,name:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> int :
    global __glGetSubroutineIndex_impl
    if not __glGetSubroutineIndex_impl:
        fptr = __pyglGetFuncAddress('glGetSubroutineIndex')
        if not fptr:
            raise RuntimeError('The function glGetSubroutineIndex is not available (maybe GL has not been initialized yet?)')
        __glGetSubroutineIndex_impl = __PYGL_FUNC_TYPE( c_uint,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetSubroutineIndex_impl
        __glGetSubroutineIndex_impl = (lambda program,shadertype,name: tmp(program,shadertype,c_char_p(name.encode())))
        global glGetSubroutineIndex
        glGetSubroutineIndex =__glGetSubroutineIndex_impl
    return __glGetSubroutineIndex_impl(program,shadertype,name)

__glGetSubroutineUniformLocation_impl = None
def glGetSubroutineUniformLocation ( program:int,shadertype:int,name:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> int :
    global __glGetSubroutineUniformLocation_impl
    if not __glGetSubroutineUniformLocation_impl:
        fptr = __pyglGetFuncAddress('glGetSubroutineUniformLocation')
        if not fptr:
            raise RuntimeError('The function glGetSubroutineUniformLocation is not available (maybe GL has not been initialized yet?)')
        __glGetSubroutineUniformLocation_impl = __PYGL_FUNC_TYPE( c_int,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetSubroutineUniformLocation_impl
        __glGetSubroutineUniformLocation_impl = (lambda program,shadertype,name: tmp(program,shadertype,c_char_p(name.encode())))
        global glGetSubroutineUniformLocation
        glGetSubroutineUniformLocation =__glGetSubroutineUniformLocation_impl
    return __glGetSubroutineUniformLocation_impl(program,shadertype,name)

__glGetSynciv_impl = None
def glGetSynciv ( sync:typing.Any,pname:int,bufSize:int,length:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],values:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetSynciv_impl
    if not __glGetSynciv_impl:
        fptr = __pyglGetFuncAddress('glGetSynciv')
        if not fptr:
            raise RuntimeError('The function glGetSynciv is not available (maybe GL has not been initialized yet?)')
        __glGetSynciv_impl = __PYGL_FUNC_TYPE( None,c_void_p,c_uint,c_int,c_void_p,c_void_p )(fptr)
        tmp = __glGetSynciv_impl
        __glGetSynciv_impl = (lambda sync,pname,bufSize,length,values: tmp(sync,pname,bufSize,(c_uint8*len(length)).from_buffer(length),(c_uint8*len(values)).from_buffer(values)))
        global glGetSynciv
        glGetSynciv =__glGetSynciv_impl
    return __glGetSynciv_impl(sync,pname,bufSize,length,values)

__glGetTexImage_impl = None
def glGetTexImage ( target:int,level:int,format:int,type:int,pixels:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetTexImage_impl
    if not __glGetTexImage_impl:
        fptr = __pyglGetFuncAddress('glGetTexImage')
        if not fptr:
            raise RuntimeError('The function glGetTexImage is not available (maybe GL has not been initialized yet?)')
        __glGetTexImage_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetTexImage_impl
        __glGetTexImage_impl = (lambda target,level,format,type,pixels: tmp(target,level,format,type,(c_uint8*len(pixels)).from_buffer(pixels)))
        global glGetTexImage
        glGetTexImage =__glGetTexImage_impl
    return __glGetTexImage_impl(target,level,format,type,pixels)

__glGetTexLevelParameterfv_impl = None
def glGetTexLevelParameterfv ( target:int,level:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetTexLevelParameterfv_impl
    if not __glGetTexLevelParameterfv_impl:
        fptr = __pyglGetFuncAddress('glGetTexLevelParameterfv')
        if not fptr:
            raise RuntimeError('The function glGetTexLevelParameterfv is not available (maybe GL has not been initialized yet?)')
        __glGetTexLevelParameterfv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_uint,c_void_p )(fptr)
        tmp = __glGetTexLevelParameterfv_impl
        __glGetTexLevelParameterfv_impl = (lambda target,level,pname,params: tmp(target,level,pname,(c_uint8*len(params)).from_buffer(params)))
        global glGetTexLevelParameterfv
        glGetTexLevelParameterfv =__glGetTexLevelParameterfv_impl
    return __glGetTexLevelParameterfv_impl(target,level,pname,params)

__glGetTexLevelParameteriv_impl = None
def glGetTexLevelParameteriv ( target:int,level:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetTexLevelParameteriv_impl
    if not __glGetTexLevelParameteriv_impl:
        fptr = __pyglGetFuncAddress('glGetTexLevelParameteriv')
        if not fptr:
            raise RuntimeError('The function glGetTexLevelParameteriv is not available (maybe GL has not been initialized yet?)')
        __glGetTexLevelParameteriv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_uint,c_void_p )(fptr)
        tmp = __glGetTexLevelParameteriv_impl
        __glGetTexLevelParameteriv_impl = (lambda target,level,pname,params: tmp(target,level,pname,(c_uint8*len(params)).from_buffer(params)))
        global glGetTexLevelParameteriv
        glGetTexLevelParameteriv =__glGetTexLevelParameteriv_impl
    return __glGetTexLevelParameteriv_impl(target,level,pname,params)

__glGetTexParameterIiv_impl = None
def glGetTexParameterIiv ( target:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetTexParameterIiv_impl
    if not __glGetTexParameterIiv_impl:
        fptr = __pyglGetFuncAddress('glGetTexParameterIiv')
        if not fptr:
            raise RuntimeError('The function glGetTexParameterIiv is not available (maybe GL has not been initialized yet?)')
        __glGetTexParameterIiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetTexParameterIiv_impl
        __glGetTexParameterIiv_impl = (lambda target,pname,params: tmp(target,pname,(c_uint8*len(params)).from_buffer(params)))
        global glGetTexParameterIiv
        glGetTexParameterIiv =__glGetTexParameterIiv_impl
    return __glGetTexParameterIiv_impl(target,pname,params)

__glGetTexParameterIuiv_impl = None
def glGetTexParameterIuiv ( target:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetTexParameterIuiv_impl
    if not __glGetTexParameterIuiv_impl:
        fptr = __pyglGetFuncAddress('glGetTexParameterIuiv')
        if not fptr:
            raise RuntimeError('The function glGetTexParameterIuiv is not available (maybe GL has not been initialized yet?)')
        __glGetTexParameterIuiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetTexParameterIuiv_impl
        __glGetTexParameterIuiv_impl = (lambda target,pname,params: tmp(target,pname,(c_uint8*len(params)).from_buffer(params)))
        global glGetTexParameterIuiv
        glGetTexParameterIuiv =__glGetTexParameterIuiv_impl
    return __glGetTexParameterIuiv_impl(target,pname,params)

__glGetTexParameterfv_impl = None
def glGetTexParameterfv ( target:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetTexParameterfv_impl
    if not __glGetTexParameterfv_impl:
        fptr = __pyglGetFuncAddress('glGetTexParameterfv')
        if not fptr:
            raise RuntimeError('The function glGetTexParameterfv is not available (maybe GL has not been initialized yet?)')
        __glGetTexParameterfv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetTexParameterfv_impl
        __glGetTexParameterfv_impl = (lambda target,pname,params: tmp(target,pname,(c_uint8*len(params)).from_buffer(params)))
        global glGetTexParameterfv
        glGetTexParameterfv =__glGetTexParameterfv_impl
    return __glGetTexParameterfv_impl(target,pname,params)

__glGetTexParameteriv_impl = None
def glGetTexParameteriv ( target:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetTexParameteriv_impl
    if not __glGetTexParameteriv_impl:
        fptr = __pyglGetFuncAddress('glGetTexParameteriv')
        if not fptr:
            raise RuntimeError('The function glGetTexParameteriv is not available (maybe GL has not been initialized yet?)')
        __glGetTexParameteriv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetTexParameteriv_impl
        __glGetTexParameteriv_impl = (lambda target,pname,params: tmp(target,pname,(c_uint8*len(params)).from_buffer(params)))
        global glGetTexParameteriv
        glGetTexParameteriv =__glGetTexParameteriv_impl
    return __glGetTexParameteriv_impl(target,pname,params)

__glGetTextureImage_impl = None
def glGetTextureImage ( texture:int,level:int,format:int,type:int,bufSize:int,pixels:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetTextureImage_impl
    if not __glGetTextureImage_impl:
        fptr = __pyglGetFuncAddress('glGetTextureImage')
        if not fptr:
            raise RuntimeError('The function glGetTextureImage is not available (maybe GL has not been initialized yet?)')
        __glGetTextureImage_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_uint,c_uint,c_int,c_void_p )(fptr)
        tmp = __glGetTextureImage_impl
        __glGetTextureImage_impl = (lambda texture,level,format,type,bufSize,pixels: tmp(texture,level,format,type,bufSize,(c_uint8*len(pixels)).from_buffer(pixels)))
        global glGetTextureImage
        glGetTextureImage =__glGetTextureImage_impl
    return __glGetTextureImage_impl(texture,level,format,type,bufSize,pixels)

__glGetTextureLevelParameterfv_impl = None
def glGetTextureLevelParameterfv ( texture:int,level:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetTextureLevelParameterfv_impl
    if not __glGetTextureLevelParameterfv_impl:
        fptr = __pyglGetFuncAddress('glGetTextureLevelParameterfv')
        if not fptr:
            raise RuntimeError('The function glGetTextureLevelParameterfv is not available (maybe GL has not been initialized yet?)')
        __glGetTextureLevelParameterfv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_uint,c_void_p )(fptr)
        tmp = __glGetTextureLevelParameterfv_impl
        __glGetTextureLevelParameterfv_impl = (lambda texture,level,pname,params: tmp(texture,level,pname,(c_uint8*len(params)).from_buffer(params)))
        global glGetTextureLevelParameterfv
        glGetTextureLevelParameterfv =__glGetTextureLevelParameterfv_impl
    return __glGetTextureLevelParameterfv_impl(texture,level,pname,params)

__glGetTextureLevelParameteriv_impl = None
def glGetTextureLevelParameteriv ( texture:int,level:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetTextureLevelParameteriv_impl
    if not __glGetTextureLevelParameteriv_impl:
        fptr = __pyglGetFuncAddress('glGetTextureLevelParameteriv')
        if not fptr:
            raise RuntimeError('The function glGetTextureLevelParameteriv is not available (maybe GL has not been initialized yet?)')
        __glGetTextureLevelParameteriv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_uint,c_void_p )(fptr)
        tmp = __glGetTextureLevelParameteriv_impl
        __glGetTextureLevelParameteriv_impl = (lambda texture,level,pname,params: tmp(texture,level,pname,(c_uint8*len(params)).from_buffer(params)))
        global glGetTextureLevelParameteriv
        glGetTextureLevelParameteriv =__glGetTextureLevelParameteriv_impl
    return __glGetTextureLevelParameteriv_impl(texture,level,pname,params)

__glGetTextureParameterIiv_impl = None
def glGetTextureParameterIiv ( texture:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetTextureParameterIiv_impl
    if not __glGetTextureParameterIiv_impl:
        fptr = __pyglGetFuncAddress('glGetTextureParameterIiv')
        if not fptr:
            raise RuntimeError('The function glGetTextureParameterIiv is not available (maybe GL has not been initialized yet?)')
        __glGetTextureParameterIiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetTextureParameterIiv_impl
        __glGetTextureParameterIiv_impl = (lambda texture,pname,params: tmp(texture,pname,(c_uint8*len(params)).from_buffer(params)))
        global glGetTextureParameterIiv
        glGetTextureParameterIiv =__glGetTextureParameterIiv_impl
    return __glGetTextureParameterIiv_impl(texture,pname,params)

__glGetTextureParameterIuiv_impl = None
def glGetTextureParameterIuiv ( texture:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetTextureParameterIuiv_impl
    if not __glGetTextureParameterIuiv_impl:
        fptr = __pyglGetFuncAddress('glGetTextureParameterIuiv')
        if not fptr:
            raise RuntimeError('The function glGetTextureParameterIuiv is not available (maybe GL has not been initialized yet?)')
        __glGetTextureParameterIuiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetTextureParameterIuiv_impl
        __glGetTextureParameterIuiv_impl = (lambda texture,pname,params: tmp(texture,pname,(c_uint8*len(params)).from_buffer(params)))
        global glGetTextureParameterIuiv
        glGetTextureParameterIuiv =__glGetTextureParameterIuiv_impl
    return __glGetTextureParameterIuiv_impl(texture,pname,params)

__glGetTextureParameterfv_impl = None
def glGetTextureParameterfv ( texture:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetTextureParameterfv_impl
    if not __glGetTextureParameterfv_impl:
        fptr = __pyglGetFuncAddress('glGetTextureParameterfv')
        if not fptr:
            raise RuntimeError('The function glGetTextureParameterfv is not available (maybe GL has not been initialized yet?)')
        __glGetTextureParameterfv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetTextureParameterfv_impl
        __glGetTextureParameterfv_impl = (lambda texture,pname,params: tmp(texture,pname,(c_uint8*len(params)).from_buffer(params)))
        global glGetTextureParameterfv
        glGetTextureParameterfv =__glGetTextureParameterfv_impl
    return __glGetTextureParameterfv_impl(texture,pname,params)

__glGetTextureParameteriv_impl = None
def glGetTextureParameteriv ( texture:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetTextureParameteriv_impl
    if not __glGetTextureParameteriv_impl:
        fptr = __pyglGetFuncAddress('glGetTextureParameteriv')
        if not fptr:
            raise RuntimeError('The function glGetTextureParameteriv is not available (maybe GL has not been initialized yet?)')
        __glGetTextureParameteriv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetTextureParameteriv_impl
        __glGetTextureParameteriv_impl = (lambda texture,pname,params: tmp(texture,pname,(c_uint8*len(params)).from_buffer(params)))
        global glGetTextureParameteriv
        glGetTextureParameteriv =__glGetTextureParameteriv_impl
    return __glGetTextureParameteriv_impl(texture,pname,params)

__glGetTextureSubImage_impl = None
def glGetTextureSubImage ( texture:int,level:int,xoffset:int,yoffset:int,zoffset:int,width:int,height:int,depth:int,format:int,type:int,bufSize:int,pixels:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetTextureSubImage_impl
    if not __glGetTextureSubImage_impl:
        fptr = __pyglGetFuncAddress('glGetTextureSubImage')
        if not fptr:
            raise RuntimeError('The function glGetTextureSubImage is not available (maybe GL has not been initialized yet?)')
        __glGetTextureSubImage_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_int,c_int,c_int,c_int,c_int,c_uint,c_uint,c_int,c_void_p )(fptr)
        tmp = __glGetTextureSubImage_impl
        __glGetTextureSubImage_impl = (lambda texture,level,xoffset,yoffset,zoffset,width,height,depth,format,type,bufSize,pixels: tmp(texture,level,xoffset,yoffset,zoffset,width,height,depth,format,type,bufSize,(c_uint8*len(pixels)).from_buffer(pixels)))
        global glGetTextureSubImage
        glGetTextureSubImage =__glGetTextureSubImage_impl
    return __glGetTextureSubImage_impl(texture,level,xoffset,yoffset,zoffset,width,height,depth,format,type,bufSize,pixels)

__glGetTransformFeedbackVarying_impl = None
def glGetTransformFeedbackVarying ( program:int,index:int,bufSize:int,length:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],size:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],type:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],name:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetTransformFeedbackVarying_impl
    if not __glGetTransformFeedbackVarying_impl:
        fptr = __pyglGetFuncAddress('glGetTransformFeedbackVarying')
        if not fptr:
            raise RuntimeError('The function glGetTransformFeedbackVarying is not available (maybe GL has not been initialized yet?)')
        __glGetTransformFeedbackVarying_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_int,c_void_p,c_void_p,c_void_p,c_void_p )(fptr)
        tmp = __glGetTransformFeedbackVarying_impl
        __glGetTransformFeedbackVarying_impl = (lambda program,index,bufSize,length,size,type,name: tmp(program,index,bufSize,(c_uint8*len(length)).from_buffer(length),(c_uint8*len(size)).from_buffer(size),(c_uint8*len(type)).from_buffer(type),(c_uint8*len(name)).from_buffer(name)))
        global glGetTransformFeedbackVarying
        glGetTransformFeedbackVarying =__glGetTransformFeedbackVarying_impl
    return __glGetTransformFeedbackVarying_impl(program,index,bufSize,length,size,type,name)

__glGetTransformFeedbacki64_v_impl = None
def glGetTransformFeedbacki64_v ( xfb:int,pname:int,index:int,param:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetTransformFeedbacki64_v_impl
    if not __glGetTransformFeedbacki64_v_impl:
        fptr = __pyglGetFuncAddress('glGetTransformFeedbacki64_v')
        if not fptr:
            raise RuntimeError('The function glGetTransformFeedbacki64_v is not available (maybe GL has not been initialized yet?)')
        __glGetTransformFeedbacki64_v_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetTransformFeedbacki64_v_impl
        __glGetTransformFeedbacki64_v_impl = (lambda xfb,pname,index,param: tmp(xfb,pname,index,(c_uint8*len(param)).from_buffer(param)))
        global glGetTransformFeedbacki64_v
        glGetTransformFeedbacki64_v =__glGetTransformFeedbacki64_v_impl
    return __glGetTransformFeedbacki64_v_impl(xfb,pname,index,param)

__glGetTransformFeedbacki_v_impl = None
def glGetTransformFeedbacki_v ( xfb:int,pname:int,index:int,param:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetTransformFeedbacki_v_impl
    if not __glGetTransformFeedbacki_v_impl:
        fptr = __pyglGetFuncAddress('glGetTransformFeedbacki_v')
        if not fptr:
            raise RuntimeError('The function glGetTransformFeedbacki_v is not available (maybe GL has not been initialized yet?)')
        __glGetTransformFeedbacki_v_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetTransformFeedbacki_v_impl
        __glGetTransformFeedbacki_v_impl = (lambda xfb,pname,index,param: tmp(xfb,pname,index,(c_uint8*len(param)).from_buffer(param)))
        global glGetTransformFeedbacki_v
        glGetTransformFeedbacki_v =__glGetTransformFeedbacki_v_impl
    return __glGetTransformFeedbacki_v_impl(xfb,pname,index,param)

__glGetTransformFeedbackiv_impl = None
def glGetTransformFeedbackiv ( xfb:int,pname:int,param:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetTransformFeedbackiv_impl
    if not __glGetTransformFeedbackiv_impl:
        fptr = __pyglGetFuncAddress('glGetTransformFeedbackiv')
        if not fptr:
            raise RuntimeError('The function glGetTransformFeedbackiv is not available (maybe GL has not been initialized yet?)')
        __glGetTransformFeedbackiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetTransformFeedbackiv_impl
        __glGetTransformFeedbackiv_impl = (lambda xfb,pname,param: tmp(xfb,pname,(c_uint8*len(param)).from_buffer(param)))
        global glGetTransformFeedbackiv
        glGetTransformFeedbackiv =__glGetTransformFeedbackiv_impl
    return __glGetTransformFeedbackiv_impl(xfb,pname,param)

__glGetUniformBlockIndex_impl = None
def glGetUniformBlockIndex ( program:int,uniformBlockName:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> int :
    global __glGetUniformBlockIndex_impl
    if not __glGetUniformBlockIndex_impl:
        fptr = __pyglGetFuncAddress('glGetUniformBlockIndex')
        if not fptr:
            raise RuntimeError('The function glGetUniformBlockIndex is not available (maybe GL has not been initialized yet?)')
        __glGetUniformBlockIndex_impl = __PYGL_FUNC_TYPE( c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetUniformBlockIndex_impl
        __glGetUniformBlockIndex_impl = (lambda program,uniformBlockName: tmp(program,c_char_p(uniformBlockName.encode())))
        global glGetUniformBlockIndex
        glGetUniformBlockIndex =__glGetUniformBlockIndex_impl
    return __glGetUniformBlockIndex_impl(program,uniformBlockName)

__glGetUniformIndices_impl = None
def glGetUniformIndices ( program:int,uniformCount:int,uniformNames:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],uniformIndices:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetUniformIndices_impl
    if not __glGetUniformIndices_impl:
        fptr = __pyglGetFuncAddress('glGetUniformIndices')
        if not fptr:
            raise RuntimeError('The function glGetUniformIndices is not available (maybe GL has not been initialized yet?)')
        __glGetUniformIndices_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_void_p,c_void_p )(fptr)
        tmp = __glGetUniformIndices_impl
        __glGetUniformIndices_impl = (lambda program,uniformCount,uniformNames,uniformIndices: tmp(program,uniformCount,c_char_p(uniformNames.encode()),(c_uint8*len(uniformIndices)).from_buffer(uniformIndices)))
        global glGetUniformIndices
        glGetUniformIndices =__glGetUniformIndices_impl
    return __glGetUniformIndices_impl(program,uniformCount,uniformNames,uniformIndices)

__glGetUniformLocation_impl = None
def glGetUniformLocation ( program:int,name:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> int :
    global __glGetUniformLocation_impl
    if not __glGetUniformLocation_impl:
        fptr = __pyglGetFuncAddress('glGetUniformLocation')
        if not fptr:
            raise RuntimeError('The function glGetUniformLocation is not available (maybe GL has not been initialized yet?)')
        __glGetUniformLocation_impl = __PYGL_FUNC_TYPE( c_int,c_uint,c_void_p )(fptr)
        tmp = __glGetUniformLocation_impl
        __glGetUniformLocation_impl = (lambda program,name: tmp(program,c_char_p(name.encode())))
        global glGetUniformLocation
        glGetUniformLocation =__glGetUniformLocation_impl
    return __glGetUniformLocation_impl(program,name)

__glGetUniformSubroutineuiv_impl = None
def glGetUniformSubroutineuiv ( shadertype:int,location:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetUniformSubroutineuiv_impl
    if not __glGetUniformSubroutineuiv_impl:
        fptr = __pyglGetFuncAddress('glGetUniformSubroutineuiv')
        if not fptr:
            raise RuntimeError('The function glGetUniformSubroutineuiv is not available (maybe GL has not been initialized yet?)')
        __glGetUniformSubroutineuiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_void_p )(fptr)
        tmp = __glGetUniformSubroutineuiv_impl
        __glGetUniformSubroutineuiv_impl = (lambda shadertype,location,params: tmp(shadertype,location,(c_uint8*len(params)).from_buffer(params)))
        global glGetUniformSubroutineuiv
        glGetUniformSubroutineuiv =__glGetUniformSubroutineuiv_impl
    return __glGetUniformSubroutineuiv_impl(shadertype,location,params)

__glGetUniformdv_impl = None
def glGetUniformdv ( program:int,location:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetUniformdv_impl
    if not __glGetUniformdv_impl:
        fptr = __pyglGetFuncAddress('glGetUniformdv')
        if not fptr:
            raise RuntimeError('The function glGetUniformdv is not available (maybe GL has not been initialized yet?)')
        __glGetUniformdv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_void_p )(fptr)
        tmp = __glGetUniformdv_impl
        __glGetUniformdv_impl = (lambda program,location,params: tmp(program,location,(c_uint8*len(params)).from_buffer(params)))
        global glGetUniformdv
        glGetUniformdv =__glGetUniformdv_impl
    return __glGetUniformdv_impl(program,location,params)

__glGetUniformfv_impl = None
def glGetUniformfv ( program:int,location:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetUniformfv_impl
    if not __glGetUniformfv_impl:
        fptr = __pyglGetFuncAddress('glGetUniformfv')
        if not fptr:
            raise RuntimeError('The function glGetUniformfv is not available (maybe GL has not been initialized yet?)')
        __glGetUniformfv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_void_p )(fptr)
        tmp = __glGetUniformfv_impl
        __glGetUniformfv_impl = (lambda program,location,params: tmp(program,location,(c_uint8*len(params)).from_buffer(params)))
        global glGetUniformfv
        glGetUniformfv =__glGetUniformfv_impl
    return __glGetUniformfv_impl(program,location,params)

__glGetUniformiv_impl = None
def glGetUniformiv ( program:int,location:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetUniformiv_impl
    if not __glGetUniformiv_impl:
        fptr = __pyglGetFuncAddress('glGetUniformiv')
        if not fptr:
            raise RuntimeError('The function glGetUniformiv is not available (maybe GL has not been initialized yet?)')
        __glGetUniformiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_void_p )(fptr)
        tmp = __glGetUniformiv_impl
        __glGetUniformiv_impl = (lambda program,location,params: tmp(program,location,(c_uint8*len(params)).from_buffer(params)))
        global glGetUniformiv
        glGetUniformiv =__glGetUniformiv_impl
    return __glGetUniformiv_impl(program,location,params)

__glGetUniformuiv_impl = None
def glGetUniformuiv ( program:int,location:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetUniformuiv_impl
    if not __glGetUniformuiv_impl:
        fptr = __pyglGetFuncAddress('glGetUniformuiv')
        if not fptr:
            raise RuntimeError('The function glGetUniformuiv is not available (maybe GL has not been initialized yet?)')
        __glGetUniformuiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_void_p )(fptr)
        tmp = __glGetUniformuiv_impl
        __glGetUniformuiv_impl = (lambda program,location,params: tmp(program,location,(c_uint8*len(params)).from_buffer(params)))
        global glGetUniformuiv
        glGetUniformuiv =__glGetUniformuiv_impl
    return __glGetUniformuiv_impl(program,location,params)

__glGetVertexArrayIndexed64iv_impl = None
def glGetVertexArrayIndexed64iv ( vaobj:int,index:int,pname:int,param:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetVertexArrayIndexed64iv_impl
    if not __glGetVertexArrayIndexed64iv_impl:
        fptr = __pyglGetFuncAddress('glGetVertexArrayIndexed64iv')
        if not fptr:
            raise RuntimeError('The function glGetVertexArrayIndexed64iv is not available (maybe GL has not been initialized yet?)')
        __glGetVertexArrayIndexed64iv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetVertexArrayIndexed64iv_impl
        __glGetVertexArrayIndexed64iv_impl = (lambda vaobj,index,pname,param: tmp(vaobj,index,pname,(c_uint8*len(param)).from_buffer(param)))
        global glGetVertexArrayIndexed64iv
        glGetVertexArrayIndexed64iv =__glGetVertexArrayIndexed64iv_impl
    return __glGetVertexArrayIndexed64iv_impl(vaobj,index,pname,param)

__glGetVertexArrayIndexediv_impl = None
def glGetVertexArrayIndexediv ( vaobj:int,index:int,pname:int,param:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetVertexArrayIndexediv_impl
    if not __glGetVertexArrayIndexediv_impl:
        fptr = __pyglGetFuncAddress('glGetVertexArrayIndexediv')
        if not fptr:
            raise RuntimeError('The function glGetVertexArrayIndexediv is not available (maybe GL has not been initialized yet?)')
        __glGetVertexArrayIndexediv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetVertexArrayIndexediv_impl
        __glGetVertexArrayIndexediv_impl = (lambda vaobj,index,pname,param: tmp(vaobj,index,pname,(c_uint8*len(param)).from_buffer(param)))
        global glGetVertexArrayIndexediv
        glGetVertexArrayIndexediv =__glGetVertexArrayIndexediv_impl
    return __glGetVertexArrayIndexediv_impl(vaobj,index,pname,param)

__glGetVertexArrayiv_impl = None
def glGetVertexArrayiv ( vaobj:int,pname:int,param:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetVertexArrayiv_impl
    if not __glGetVertexArrayiv_impl:
        fptr = __pyglGetFuncAddress('glGetVertexArrayiv')
        if not fptr:
            raise RuntimeError('The function glGetVertexArrayiv is not available (maybe GL has not been initialized yet?)')
        __glGetVertexArrayiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetVertexArrayiv_impl
        __glGetVertexArrayiv_impl = (lambda vaobj,pname,param: tmp(vaobj,pname,(c_uint8*len(param)).from_buffer(param)))
        global glGetVertexArrayiv
        glGetVertexArrayiv =__glGetVertexArrayiv_impl
    return __glGetVertexArrayiv_impl(vaobj,pname,param)

__glGetVertexAttribIiv_impl = None
def glGetVertexAttribIiv ( index:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetVertexAttribIiv_impl
    if not __glGetVertexAttribIiv_impl:
        fptr = __pyglGetFuncAddress('glGetVertexAttribIiv')
        if not fptr:
            raise RuntimeError('The function glGetVertexAttribIiv is not available (maybe GL has not been initialized yet?)')
        __glGetVertexAttribIiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetVertexAttribIiv_impl
        __glGetVertexAttribIiv_impl = (lambda index,pname,params: tmp(index,pname,(c_uint8*len(params)).from_buffer(params)))
        global glGetVertexAttribIiv
        glGetVertexAttribIiv =__glGetVertexAttribIiv_impl
    return __glGetVertexAttribIiv_impl(index,pname,params)

__glGetVertexAttribIuiv_impl = None
def glGetVertexAttribIuiv ( index:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetVertexAttribIuiv_impl
    if not __glGetVertexAttribIuiv_impl:
        fptr = __pyglGetFuncAddress('glGetVertexAttribIuiv')
        if not fptr:
            raise RuntimeError('The function glGetVertexAttribIuiv is not available (maybe GL has not been initialized yet?)')
        __glGetVertexAttribIuiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetVertexAttribIuiv_impl
        __glGetVertexAttribIuiv_impl = (lambda index,pname,params: tmp(index,pname,(c_uint8*len(params)).from_buffer(params)))
        global glGetVertexAttribIuiv
        glGetVertexAttribIuiv =__glGetVertexAttribIuiv_impl
    return __glGetVertexAttribIuiv_impl(index,pname,params)

__glGetVertexAttribLdv_impl = None
def glGetVertexAttribLdv ( index:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetVertexAttribLdv_impl
    if not __glGetVertexAttribLdv_impl:
        fptr = __pyglGetFuncAddress('glGetVertexAttribLdv')
        if not fptr:
            raise RuntimeError('The function glGetVertexAttribLdv is not available (maybe GL has not been initialized yet?)')
        __glGetVertexAttribLdv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetVertexAttribLdv_impl
        __glGetVertexAttribLdv_impl = (lambda index,pname,params: tmp(index,pname,(c_uint8*len(params)).from_buffer(params)))
        global glGetVertexAttribLdv
        glGetVertexAttribLdv =__glGetVertexAttribLdv_impl
    return __glGetVertexAttribLdv_impl(index,pname,params)

__glGetVertexAttribPointerv_impl = None
def glGetVertexAttribPointerv ( index:int,pname:int,pointer:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetVertexAttribPointerv_impl
    if not __glGetVertexAttribPointerv_impl:
        fptr = __pyglGetFuncAddress('glGetVertexAttribPointerv')
        if not fptr:
            raise RuntimeError('The function glGetVertexAttribPointerv is not available (maybe GL has not been initialized yet?)')
        __glGetVertexAttribPointerv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetVertexAttribPointerv_impl
        __glGetVertexAttribPointerv_impl = (lambda index,pname,pointer: tmp(index,pname,(c_uint8*len(pointer)).from_buffer(pointer)))
        global glGetVertexAttribPointerv
        glGetVertexAttribPointerv =__glGetVertexAttribPointerv_impl
    return __glGetVertexAttribPointerv_impl(index,pname,pointer)

__glGetVertexAttribdv_impl = None
def glGetVertexAttribdv ( index:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetVertexAttribdv_impl
    if not __glGetVertexAttribdv_impl:
        fptr = __pyglGetFuncAddress('glGetVertexAttribdv')
        if not fptr:
            raise RuntimeError('The function glGetVertexAttribdv is not available (maybe GL has not been initialized yet?)')
        __glGetVertexAttribdv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetVertexAttribdv_impl
        __glGetVertexAttribdv_impl = (lambda index,pname,params: tmp(index,pname,(c_uint8*len(params)).from_buffer(params)))
        global glGetVertexAttribdv
        glGetVertexAttribdv =__glGetVertexAttribdv_impl
    return __glGetVertexAttribdv_impl(index,pname,params)

__glGetVertexAttribfv_impl = None
def glGetVertexAttribfv ( index:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetVertexAttribfv_impl
    if not __glGetVertexAttribfv_impl:
        fptr = __pyglGetFuncAddress('glGetVertexAttribfv')
        if not fptr:
            raise RuntimeError('The function glGetVertexAttribfv is not available (maybe GL has not been initialized yet?)')
        __glGetVertexAttribfv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetVertexAttribfv_impl
        __glGetVertexAttribfv_impl = (lambda index,pname,params: tmp(index,pname,(c_uint8*len(params)).from_buffer(params)))
        global glGetVertexAttribfv
        glGetVertexAttribfv =__glGetVertexAttribfv_impl
    return __glGetVertexAttribfv_impl(index,pname,params)

__glGetVertexAttribiv_impl = None
def glGetVertexAttribiv ( index:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetVertexAttribiv_impl
    if not __glGetVertexAttribiv_impl:
        fptr = __pyglGetFuncAddress('glGetVertexAttribiv')
        if not fptr:
            raise RuntimeError('The function glGetVertexAttribiv is not available (maybe GL has not been initialized yet?)')
        __glGetVertexAttribiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glGetVertexAttribiv_impl
        __glGetVertexAttribiv_impl = (lambda index,pname,params: tmp(index,pname,(c_uint8*len(params)).from_buffer(params)))
        global glGetVertexAttribiv
        glGetVertexAttribiv =__glGetVertexAttribiv_impl
    return __glGetVertexAttribiv_impl(index,pname,params)

__glGetnCompressedTexImage_impl = None
def glGetnCompressedTexImage ( target:int,lod:int,bufSize:int,pixels:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetnCompressedTexImage_impl
    if not __glGetnCompressedTexImage_impl:
        fptr = __pyglGetFuncAddress('glGetnCompressedTexImage')
        if not fptr:
            raise RuntimeError('The function glGetnCompressedTexImage is not available (maybe GL has not been initialized yet?)')
        __glGetnCompressedTexImage_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_void_p )(fptr)
        tmp = __glGetnCompressedTexImage_impl
        __glGetnCompressedTexImage_impl = (lambda target,lod,bufSize,pixels: tmp(target,lod,bufSize,(c_uint8*len(pixels)).from_buffer(pixels)))
        global glGetnCompressedTexImage
        glGetnCompressedTexImage =__glGetnCompressedTexImage_impl
    return __glGetnCompressedTexImage_impl(target,lod,bufSize,pixels)

__glGetnTexImage_impl = None
def glGetnTexImage ( target:int,level:int,format:int,type:int,bufSize:int,pixels:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetnTexImage_impl
    if not __glGetnTexImage_impl:
        fptr = __pyglGetFuncAddress('glGetnTexImage')
        if not fptr:
            raise RuntimeError('The function glGetnTexImage is not available (maybe GL has not been initialized yet?)')
        __glGetnTexImage_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_uint,c_uint,c_int,c_void_p )(fptr)
        tmp = __glGetnTexImage_impl
        __glGetnTexImage_impl = (lambda target,level,format,type,bufSize,pixels: tmp(target,level,format,type,bufSize,(c_uint8*len(pixels)).from_buffer(pixels)))
        global glGetnTexImage
        glGetnTexImage =__glGetnTexImage_impl
    return __glGetnTexImage_impl(target,level,format,type,bufSize,pixels)

__glGetnUniformdv_impl = None
def glGetnUniformdv ( program:int,location:int,bufSize:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetnUniformdv_impl
    if not __glGetnUniformdv_impl:
        fptr = __pyglGetFuncAddress('glGetnUniformdv')
        if not fptr:
            raise RuntimeError('The function glGetnUniformdv is not available (maybe GL has not been initialized yet?)')
        __glGetnUniformdv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_void_p )(fptr)
        tmp = __glGetnUniformdv_impl
        __glGetnUniformdv_impl = (lambda program,location,bufSize,params: tmp(program,location,bufSize,(c_uint8*len(params)).from_buffer(params)))
        global glGetnUniformdv
        glGetnUniformdv =__glGetnUniformdv_impl
    return __glGetnUniformdv_impl(program,location,bufSize,params)

__glGetnUniformfv_impl = None
def glGetnUniformfv ( program:int,location:int,bufSize:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetnUniformfv_impl
    if not __glGetnUniformfv_impl:
        fptr = __pyglGetFuncAddress('glGetnUniformfv')
        if not fptr:
            raise RuntimeError('The function glGetnUniformfv is not available (maybe GL has not been initialized yet?)')
        __glGetnUniformfv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_void_p )(fptr)
        tmp = __glGetnUniformfv_impl
        __glGetnUniformfv_impl = (lambda program,location,bufSize,params: tmp(program,location,bufSize,(c_uint8*len(params)).from_buffer(params)))
        global glGetnUniformfv
        glGetnUniformfv =__glGetnUniformfv_impl
    return __glGetnUniformfv_impl(program,location,bufSize,params)

__glGetnUniformiv_impl = None
def glGetnUniformiv ( program:int,location:int,bufSize:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetnUniformiv_impl
    if not __glGetnUniformiv_impl:
        fptr = __pyglGetFuncAddress('glGetnUniformiv')
        if not fptr:
            raise RuntimeError('The function glGetnUniformiv is not available (maybe GL has not been initialized yet?)')
        __glGetnUniformiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_void_p )(fptr)
        tmp = __glGetnUniformiv_impl
        __glGetnUniformiv_impl = (lambda program,location,bufSize,params: tmp(program,location,bufSize,(c_uint8*len(params)).from_buffer(params)))
        global glGetnUniformiv
        glGetnUniformiv =__glGetnUniformiv_impl
    return __glGetnUniformiv_impl(program,location,bufSize,params)

__glGetnUniformuiv_impl = None
def glGetnUniformuiv ( program:int,location:int,bufSize:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glGetnUniformuiv_impl
    if not __glGetnUniformuiv_impl:
        fptr = __pyglGetFuncAddress('glGetnUniformuiv')
        if not fptr:
            raise RuntimeError('The function glGetnUniformuiv is not available (maybe GL has not been initialized yet?)')
        __glGetnUniformuiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_void_p )(fptr)
        tmp = __glGetnUniformuiv_impl
        __glGetnUniformuiv_impl = (lambda program,location,bufSize,params: tmp(program,location,bufSize,(c_uint8*len(params)).from_buffer(params)))
        global glGetnUniformuiv
        glGetnUniformuiv =__glGetnUniformuiv_impl
    return __glGetnUniformuiv_impl(program,location,bufSize,params)

__glHint_impl = None
def glHint ( target:int,mode:int ) -> None :
    global __glHint_impl
    if not __glHint_impl:
        fptr = __pyglGetFuncAddress('glHint')
        if not fptr:
            raise RuntimeError('The function glHint is not available (maybe GL has not been initialized yet?)')
        __glHint_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint )(fptr)
        global glHint
        glHint =__glHint_impl
    return __glHint_impl(target,mode)

__glInvalidateBufferData_impl = None
def glInvalidateBufferData ( buffer:int ) -> None :
    global __glInvalidateBufferData_impl
    if not __glInvalidateBufferData_impl:
        fptr = __pyglGetFuncAddress('glInvalidateBufferData')
        if not fptr:
            raise RuntimeError('The function glInvalidateBufferData is not available (maybe GL has not been initialized yet?)')
        __glInvalidateBufferData_impl = __PYGL_FUNC_TYPE( None,c_uint )(fptr)
        global glInvalidateBufferData
        glInvalidateBufferData =__glInvalidateBufferData_impl
    return __glInvalidateBufferData_impl(buffer)

__glInvalidateBufferSubData_impl = None
def glInvalidateBufferSubData ( buffer:int,offset:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],length:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glInvalidateBufferSubData_impl
    if not __glInvalidateBufferSubData_impl:
        fptr = __pyglGetFuncAddress('glInvalidateBufferSubData')
        if not fptr:
            raise RuntimeError('The function glInvalidateBufferSubData is not available (maybe GL has not been initialized yet?)')
        __glInvalidateBufferSubData_impl = __PYGL_FUNC_TYPE( None,c_uint,c_size_t,c_void_p )(fptr)
        global glInvalidateBufferSubData
        glInvalidateBufferSubData =__glInvalidateBufferSubData_impl
    return __glInvalidateBufferSubData_impl(buffer,offset,length)

__glInvalidateFramebuffer_impl = None
def glInvalidateFramebuffer ( target:int,numAttachments:int,attachments:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glInvalidateFramebuffer_impl
    if not __glInvalidateFramebuffer_impl:
        fptr = __pyglGetFuncAddress('glInvalidateFramebuffer')
        if not fptr:
            raise RuntimeError('The function glInvalidateFramebuffer is not available (maybe GL has not been initialized yet?)')
        __glInvalidateFramebuffer_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_void_p )(fptr)
        tmp = __glInvalidateFramebuffer_impl
        __glInvalidateFramebuffer_impl = (lambda target,numAttachments,attachments: tmp(target,numAttachments,__pyglGetAsConstVoidPointer(attachments)))
        global glInvalidateFramebuffer
        glInvalidateFramebuffer =__glInvalidateFramebuffer_impl
    return __glInvalidateFramebuffer_impl(target,numAttachments,attachments)

__glInvalidateNamedFramebufferData_impl = None
def glInvalidateNamedFramebufferData ( framebuffer:int,numAttachments:int,attachments:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glInvalidateNamedFramebufferData_impl
    if not __glInvalidateNamedFramebufferData_impl:
        fptr = __pyglGetFuncAddress('glInvalidateNamedFramebufferData')
        if not fptr:
            raise RuntimeError('The function glInvalidateNamedFramebufferData is not available (maybe GL has not been initialized yet?)')
        __glInvalidateNamedFramebufferData_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_void_p )(fptr)
        tmp = __glInvalidateNamedFramebufferData_impl
        __glInvalidateNamedFramebufferData_impl = (lambda framebuffer,numAttachments,attachments: tmp(framebuffer,numAttachments,__pyglGetAsConstVoidPointer(attachments)))
        global glInvalidateNamedFramebufferData
        glInvalidateNamedFramebufferData =__glInvalidateNamedFramebufferData_impl
    return __glInvalidateNamedFramebufferData_impl(framebuffer,numAttachments,attachments)

__glInvalidateNamedFramebufferSubData_impl = None
def glInvalidateNamedFramebufferSubData ( framebuffer:int,numAttachments:int,attachments:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],x:int,y:int,width:int,height:int ) -> None :
    global __glInvalidateNamedFramebufferSubData_impl
    if not __glInvalidateNamedFramebufferSubData_impl:
        fptr = __pyglGetFuncAddress('glInvalidateNamedFramebufferSubData')
        if not fptr:
            raise RuntimeError('The function glInvalidateNamedFramebufferSubData is not available (maybe GL has not been initialized yet?)')
        __glInvalidateNamedFramebufferSubData_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_void_p,c_int,c_int,c_int,c_int )(fptr)
        tmp = __glInvalidateNamedFramebufferSubData_impl
        __glInvalidateNamedFramebufferSubData_impl = (lambda framebuffer,numAttachments,attachments,x,y,width,height: tmp(framebuffer,numAttachments,__pyglGetAsConstVoidPointer(attachments),x,y,width,height))
        global glInvalidateNamedFramebufferSubData
        glInvalidateNamedFramebufferSubData =__glInvalidateNamedFramebufferSubData_impl
    return __glInvalidateNamedFramebufferSubData_impl(framebuffer,numAttachments,attachments,x,y,width,height)

__glInvalidateSubFramebuffer_impl = None
def glInvalidateSubFramebuffer ( target:int,numAttachments:int,attachments:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],x:int,y:int,width:int,height:int ) -> None :
    global __glInvalidateSubFramebuffer_impl
    if not __glInvalidateSubFramebuffer_impl:
        fptr = __pyglGetFuncAddress('glInvalidateSubFramebuffer')
        if not fptr:
            raise RuntimeError('The function glInvalidateSubFramebuffer is not available (maybe GL has not been initialized yet?)')
        __glInvalidateSubFramebuffer_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_void_p,c_int,c_int,c_int,c_int )(fptr)
        tmp = __glInvalidateSubFramebuffer_impl
        __glInvalidateSubFramebuffer_impl = (lambda target,numAttachments,attachments,x,y,width,height: tmp(target,numAttachments,__pyglGetAsConstVoidPointer(attachments),x,y,width,height))
        global glInvalidateSubFramebuffer
        glInvalidateSubFramebuffer =__glInvalidateSubFramebuffer_impl
    return __glInvalidateSubFramebuffer_impl(target,numAttachments,attachments,x,y,width,height)

__glInvalidateTexImage_impl = None
def glInvalidateTexImage ( texture:int,level:int ) -> None :
    global __glInvalidateTexImage_impl
    if not __glInvalidateTexImage_impl:
        fptr = __pyglGetFuncAddress('glInvalidateTexImage')
        if not fptr:
            raise RuntimeError('The function glInvalidateTexImage is not available (maybe GL has not been initialized yet?)')
        __glInvalidateTexImage_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int )(fptr)
        global glInvalidateTexImage
        glInvalidateTexImage =__glInvalidateTexImage_impl
    return __glInvalidateTexImage_impl(texture,level)

__glInvalidateTexSubImage_impl = None
def glInvalidateTexSubImage ( texture:int,level:int,xoffset:int,yoffset:int,zoffset:int,width:int,height:int,depth:int ) -> None :
    global __glInvalidateTexSubImage_impl
    if not __glInvalidateTexSubImage_impl:
        fptr = __pyglGetFuncAddress('glInvalidateTexSubImage')
        if not fptr:
            raise RuntimeError('The function glInvalidateTexSubImage is not available (maybe GL has not been initialized yet?)')
        __glInvalidateTexSubImage_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_int,c_int,c_int,c_int,c_int )(fptr)
        global glInvalidateTexSubImage
        glInvalidateTexSubImage =__glInvalidateTexSubImage_impl
    return __glInvalidateTexSubImage_impl(texture,level,xoffset,yoffset,zoffset,width,height,depth)

__glIsBuffer_impl = None
def glIsBuffer ( buffer:int ) -> bool :
    global __glIsBuffer_impl
    if not __glIsBuffer_impl:
        fptr = __pyglGetFuncAddress('glIsBuffer')
        if not fptr:
            raise RuntimeError('The function glIsBuffer is not available (maybe GL has not been initialized yet?)')
        __glIsBuffer_impl = __PYGL_FUNC_TYPE( c_char,c_uint )(fptr)
        global glIsBuffer
        glIsBuffer =__glIsBuffer_impl
    return __glIsBuffer_impl(buffer)

__glIsEnabled_impl = None
def glIsEnabled ( cap:int ) -> bool :
    global __glIsEnabled_impl
    if not __glIsEnabled_impl:
        fptr = __pyglGetFuncAddress('glIsEnabled')
        if not fptr:
            raise RuntimeError('The function glIsEnabled is not available (maybe GL has not been initialized yet?)')
        __glIsEnabled_impl = __PYGL_FUNC_TYPE( c_char,c_uint )(fptr)
        global glIsEnabled
        glIsEnabled =__glIsEnabled_impl
    return __glIsEnabled_impl(cap)

__glIsEnabledi_impl = None
def glIsEnabledi ( target:int,index:int ) -> bool :
    global __glIsEnabledi_impl
    if not __glIsEnabledi_impl:
        fptr = __pyglGetFuncAddress('glIsEnabledi')
        if not fptr:
            raise RuntimeError('The function glIsEnabledi is not available (maybe GL has not been initialized yet?)')
        __glIsEnabledi_impl = __PYGL_FUNC_TYPE( c_char,c_uint,c_uint )(fptr)
        global glIsEnabledi
        glIsEnabledi =__glIsEnabledi_impl
    return __glIsEnabledi_impl(target,index)

__glIsFramebuffer_impl = None
def glIsFramebuffer ( framebuffer:int ) -> bool :
    global __glIsFramebuffer_impl
    if not __glIsFramebuffer_impl:
        fptr = __pyglGetFuncAddress('glIsFramebuffer')
        if not fptr:
            raise RuntimeError('The function glIsFramebuffer is not available (maybe GL has not been initialized yet?)')
        __glIsFramebuffer_impl = __PYGL_FUNC_TYPE( c_char,c_uint )(fptr)
        global glIsFramebuffer
        glIsFramebuffer =__glIsFramebuffer_impl
    return __glIsFramebuffer_impl(framebuffer)

__glIsProgram_impl = None
def glIsProgram ( program:int ) -> bool :
    global __glIsProgram_impl
    if not __glIsProgram_impl:
        fptr = __pyglGetFuncAddress('glIsProgram')
        if not fptr:
            raise RuntimeError('The function glIsProgram is not available (maybe GL has not been initialized yet?)')
        __glIsProgram_impl = __PYGL_FUNC_TYPE( c_char,c_uint )(fptr)
        global glIsProgram
        glIsProgram =__glIsProgram_impl
    return __glIsProgram_impl(program)

__glIsProgramPipeline_impl = None
def glIsProgramPipeline ( pipeline:int ) -> bool :
    global __glIsProgramPipeline_impl
    if not __glIsProgramPipeline_impl:
        fptr = __pyglGetFuncAddress('glIsProgramPipeline')
        if not fptr:
            raise RuntimeError('The function glIsProgramPipeline is not available (maybe GL has not been initialized yet?)')
        __glIsProgramPipeline_impl = __PYGL_FUNC_TYPE( c_char,c_uint )(fptr)
        global glIsProgramPipeline
        glIsProgramPipeline =__glIsProgramPipeline_impl
    return __glIsProgramPipeline_impl(pipeline)

__glIsQuery_impl = None
def glIsQuery ( id:int ) -> bool :
    global __glIsQuery_impl
    if not __glIsQuery_impl:
        fptr = __pyglGetFuncAddress('glIsQuery')
        if not fptr:
            raise RuntimeError('The function glIsQuery is not available (maybe GL has not been initialized yet?)')
        __glIsQuery_impl = __PYGL_FUNC_TYPE( c_char,c_uint )(fptr)
        global glIsQuery
        glIsQuery =__glIsQuery_impl
    return __glIsQuery_impl(id)

__glIsRenderbuffer_impl = None
def glIsRenderbuffer ( renderbuffer:int ) -> bool :
    global __glIsRenderbuffer_impl
    if not __glIsRenderbuffer_impl:
        fptr = __pyglGetFuncAddress('glIsRenderbuffer')
        if not fptr:
            raise RuntimeError('The function glIsRenderbuffer is not available (maybe GL has not been initialized yet?)')
        __glIsRenderbuffer_impl = __PYGL_FUNC_TYPE( c_char,c_uint )(fptr)
        global glIsRenderbuffer
        glIsRenderbuffer =__glIsRenderbuffer_impl
    return __glIsRenderbuffer_impl(renderbuffer)

__glIsSampler_impl = None
def glIsSampler ( sampler:int ) -> bool :
    global __glIsSampler_impl
    if not __glIsSampler_impl:
        fptr = __pyglGetFuncAddress('glIsSampler')
        if not fptr:
            raise RuntimeError('The function glIsSampler is not available (maybe GL has not been initialized yet?)')
        __glIsSampler_impl = __PYGL_FUNC_TYPE( c_char,c_uint )(fptr)
        global glIsSampler
        glIsSampler =__glIsSampler_impl
    return __glIsSampler_impl(sampler)

__glIsShader_impl = None
def glIsShader ( shader:int ) -> bool :
    global __glIsShader_impl
    if not __glIsShader_impl:
        fptr = __pyglGetFuncAddress('glIsShader')
        if not fptr:
            raise RuntimeError('The function glIsShader is not available (maybe GL has not been initialized yet?)')
        __glIsShader_impl = __PYGL_FUNC_TYPE( c_char,c_uint )(fptr)
        global glIsShader
        glIsShader =__glIsShader_impl
    return __glIsShader_impl(shader)

__glIsSync_impl = None
def glIsSync ( sync:typing.Any ) -> bool :
    global __glIsSync_impl
    if not __glIsSync_impl:
        fptr = __pyglGetFuncAddress('glIsSync')
        if not fptr:
            raise RuntimeError('The function glIsSync is not available (maybe GL has not been initialized yet?)')
        __glIsSync_impl = __PYGL_FUNC_TYPE( c_char,c_void_p )(fptr)
        global glIsSync
        glIsSync =__glIsSync_impl
    return __glIsSync_impl(sync)

__glIsTexture_impl = None
def glIsTexture ( texture:int ) -> bool :
    global __glIsTexture_impl
    if not __glIsTexture_impl:
        fptr = __pyglGetFuncAddress('glIsTexture')
        if not fptr:
            raise RuntimeError('The function glIsTexture is not available (maybe GL has not been initialized yet?)')
        __glIsTexture_impl = __PYGL_FUNC_TYPE( c_char,c_uint )(fptr)
        global glIsTexture
        glIsTexture =__glIsTexture_impl
    return __glIsTexture_impl(texture)

__glIsTransformFeedback_impl = None
def glIsTransformFeedback ( id:int ) -> bool :
    global __glIsTransformFeedback_impl
    if not __glIsTransformFeedback_impl:
        fptr = __pyglGetFuncAddress('glIsTransformFeedback')
        if not fptr:
            raise RuntimeError('The function glIsTransformFeedback is not available (maybe GL has not been initialized yet?)')
        __glIsTransformFeedback_impl = __PYGL_FUNC_TYPE( c_char,c_uint )(fptr)
        global glIsTransformFeedback
        glIsTransformFeedback =__glIsTransformFeedback_impl
    return __glIsTransformFeedback_impl(id)

__glIsVertexArray_impl = None
def glIsVertexArray ( array:int ) -> bool :
    global __glIsVertexArray_impl
    if not __glIsVertexArray_impl:
        fptr = __pyglGetFuncAddress('glIsVertexArray')
        if not fptr:
            raise RuntimeError('The function glIsVertexArray is not available (maybe GL has not been initialized yet?)')
        __glIsVertexArray_impl = __PYGL_FUNC_TYPE( c_char,c_uint )(fptr)
        global glIsVertexArray
        glIsVertexArray =__glIsVertexArray_impl
    return __glIsVertexArray_impl(array)

__glLineWidth_impl = None
def glLineWidth ( width:float ) -> None :
    global __glLineWidth_impl
    if not __glLineWidth_impl:
        fptr = __pyglGetFuncAddress('glLineWidth')
        if not fptr:
            raise RuntimeError('The function glLineWidth is not available (maybe GL has not been initialized yet?)')
        __glLineWidth_impl = __PYGL_FUNC_TYPE( None,c_float )(fptr)
        global glLineWidth
        glLineWidth =__glLineWidth_impl
    return __glLineWidth_impl(width)

__glLinkProgram_impl = None
def glLinkProgram ( program:int ) -> None :
    global __glLinkProgram_impl
    if not __glLinkProgram_impl:
        fptr = __pyglGetFuncAddress('glLinkProgram')
        if not fptr:
            raise RuntimeError('The function glLinkProgram is not available (maybe GL has not been initialized yet?)')
        __glLinkProgram_impl = __PYGL_FUNC_TYPE( None,c_uint )(fptr)
        global glLinkProgram
        glLinkProgram =__glLinkProgram_impl
    return __glLinkProgram_impl(program)

__glLogicOp_impl = None
def glLogicOp ( opcode:int ) -> None :
    global __glLogicOp_impl
    if not __glLogicOp_impl:
        fptr = __pyglGetFuncAddress('glLogicOp')
        if not fptr:
            raise RuntimeError('The function glLogicOp is not available (maybe GL has not been initialized yet?)')
        __glLogicOp_impl = __PYGL_FUNC_TYPE( None,c_uint )(fptr)
        global glLogicOp
        glLogicOp =__glLogicOp_impl
    return __glLogicOp_impl(opcode)

__glMapBuffer_impl = None
def glMapBuffer ( target:int,access:int ) -> c_void_p :
    global __glMapBuffer_impl
    if not __glMapBuffer_impl:
        fptr = __pyglGetFuncAddress('glMapBuffer')
        if not fptr:
            raise RuntimeError('The function glMapBuffer is not available (maybe GL has not been initialized yet?)')
        __glMapBuffer_impl = __PYGL_FUNC_TYPE( c_void_p,c_uint,c_uint )(fptr)
        global glMapBuffer
        glMapBuffer =__glMapBuffer_impl
    return __glMapBuffer_impl(target,access)

__glMapBufferRange_impl = None
def glMapBufferRange ( target:int,offset:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],length:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],access:int ) -> c_void_p :
    global __glMapBufferRange_impl
    if not __glMapBufferRange_impl:
        fptr = __pyglGetFuncAddress('glMapBufferRange')
        if not fptr:
            raise RuntimeError('The function glMapBufferRange is not available (maybe GL has not been initialized yet?)')
        __glMapBufferRange_impl = __PYGL_FUNC_TYPE( c_void_p,c_uint,c_size_t,c_void_p,c_uint )(fptr)
        global glMapBufferRange
        glMapBufferRange =__glMapBufferRange_impl
    return __glMapBufferRange_impl(target,offset,length,access)

__glMapNamedBuffer_impl = None
def glMapNamedBuffer ( buffer:int,access:int ) -> c_void_p :
    global __glMapNamedBuffer_impl
    if not __glMapNamedBuffer_impl:
        fptr = __pyglGetFuncAddress('glMapNamedBuffer')
        if not fptr:
            raise RuntimeError('The function glMapNamedBuffer is not available (maybe GL has not been initialized yet?)')
        __glMapNamedBuffer_impl = __PYGL_FUNC_TYPE( c_void_p,c_uint,c_uint )(fptr)
        global glMapNamedBuffer
        glMapNamedBuffer =__glMapNamedBuffer_impl
    return __glMapNamedBuffer_impl(buffer,access)

__glMapNamedBufferRange_impl = None
def glMapNamedBufferRange ( buffer:int,offset:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],length:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],access:int ) -> c_void_p :
    global __glMapNamedBufferRange_impl
    if not __glMapNamedBufferRange_impl:
        fptr = __pyglGetFuncAddress('glMapNamedBufferRange')
        if not fptr:
            raise RuntimeError('The function glMapNamedBufferRange is not available (maybe GL has not been initialized yet?)')
        __glMapNamedBufferRange_impl = __PYGL_FUNC_TYPE( c_void_p,c_uint,c_size_t,c_void_p,c_uint )(fptr)
        global glMapNamedBufferRange
        glMapNamedBufferRange =__glMapNamedBufferRange_impl
    return __glMapNamedBufferRange_impl(buffer,offset,length,access)

__glMemoryBarrier_impl = None
def glMemoryBarrier ( barriers:int ) -> None :
    global __glMemoryBarrier_impl
    if not __glMemoryBarrier_impl:
        fptr = __pyglGetFuncAddress('glMemoryBarrier')
        if not fptr:
            raise RuntimeError('The function glMemoryBarrier is not available (maybe GL has not been initialized yet?)')
        __glMemoryBarrier_impl = __PYGL_FUNC_TYPE( None,c_uint )(fptr)
        global glMemoryBarrier
        glMemoryBarrier =__glMemoryBarrier_impl
    return __glMemoryBarrier_impl(barriers)

__glMemoryBarrierByRegion_impl = None
def glMemoryBarrierByRegion ( barriers:int ) -> None :
    global __glMemoryBarrierByRegion_impl
    if not __glMemoryBarrierByRegion_impl:
        fptr = __pyglGetFuncAddress('glMemoryBarrierByRegion')
        if not fptr:
            raise RuntimeError('The function glMemoryBarrierByRegion is not available (maybe GL has not been initialized yet?)')
        __glMemoryBarrierByRegion_impl = __PYGL_FUNC_TYPE( None,c_uint )(fptr)
        global glMemoryBarrierByRegion
        glMemoryBarrierByRegion =__glMemoryBarrierByRegion_impl
    return __glMemoryBarrierByRegion_impl(barriers)

__glMinSampleShading_impl = None
def glMinSampleShading ( value:float ) -> None :
    global __glMinSampleShading_impl
    if not __glMinSampleShading_impl:
        fptr = __pyglGetFuncAddress('glMinSampleShading')
        if not fptr:
            raise RuntimeError('The function glMinSampleShading is not available (maybe GL has not been initialized yet?)')
        __glMinSampleShading_impl = __PYGL_FUNC_TYPE( None,c_float )(fptr)
        global glMinSampleShading
        glMinSampleShading =__glMinSampleShading_impl
    return __glMinSampleShading_impl(value)

__glMultiDrawArrays_impl = None
def glMultiDrawArrays ( mode:int,first:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],count:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],drawcount:int ) -> None :
    global __glMultiDrawArrays_impl
    if not __glMultiDrawArrays_impl:
        fptr = __pyglGetFuncAddress('glMultiDrawArrays')
        if not fptr:
            raise RuntimeError('The function glMultiDrawArrays is not available (maybe GL has not been initialized yet?)')
        __glMultiDrawArrays_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p,c_void_p,c_int )(fptr)
        tmp = __glMultiDrawArrays_impl
        __glMultiDrawArrays_impl = (lambda mode,first,count,drawcount: tmp(mode,__pyglGetAsConstVoidPointer(first),__pyglGetAsConstVoidPointer(count),drawcount))
    for _f in __universal_hooks:
        _f("glMultiDrawArrays",glMultiDrawArrays,mode,first,count,drawcount)
    if 'glMultiDrawArrays' in __hooks:
        for _f in __hooks['glMultiDrawArrays']:
            _f("glMultiDrawArrays",glMultiDrawArrays,mode,first,count,drawcount)
    rv = __glMultiDrawArrays_impl(mode,first,count,drawcount)
    if 'glMultiDrawArrays' in __posthooks:
        for _f in __posthooks['glMultiDrawArrays']:
            _f(rv,"glMultiDrawArrays",glMultiDrawArrays,mode,first,count,drawcount)
    for _f in __universal_posthooks:
        _f(rv,"glMultiDrawArrays",glMultiDrawArrays,mode,first,count,drawcount)
    return rv

__glMultiDrawArraysIndirect_impl = None
def glMultiDrawArraysIndirect ( mode:int,indirect:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],drawcount:int,stride:int ) -> None :
    global __glMultiDrawArraysIndirect_impl
    if not __glMultiDrawArraysIndirect_impl:
        fptr = __pyglGetFuncAddress('glMultiDrawArraysIndirect')
        if not fptr:
            raise RuntimeError('The function glMultiDrawArraysIndirect is not available (maybe GL has not been initialized yet?)')
        __glMultiDrawArraysIndirect_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p,c_int,c_int )(fptr)
        tmp = __glMultiDrawArraysIndirect_impl
        __glMultiDrawArraysIndirect_impl = (lambda mode,indirect,drawcount,stride: tmp(mode,__pyglGetAsConstVoidPointer(indirect),drawcount,stride))
    for _f in __universal_hooks:
        _f("glMultiDrawArraysIndirect",glMultiDrawArraysIndirect,mode,indirect,drawcount,stride)
    if 'glMultiDrawArraysIndirect' in __hooks:
        for _f in __hooks['glMultiDrawArraysIndirect']:
            _f("glMultiDrawArraysIndirect",glMultiDrawArraysIndirect,mode,indirect,drawcount,stride)
    rv = __glMultiDrawArraysIndirect_impl(mode,indirect,drawcount,stride)
    if 'glMultiDrawArraysIndirect' in __posthooks:
        for _f in __posthooks['glMultiDrawArraysIndirect']:
            _f(rv,"glMultiDrawArraysIndirect",glMultiDrawArraysIndirect,mode,indirect,drawcount,stride)
    for _f in __universal_posthooks:
        _f(rv,"glMultiDrawArraysIndirect",glMultiDrawArraysIndirect,mode,indirect,drawcount,stride)
    return rv

__glMultiDrawElements_impl = None
def glMultiDrawElements ( mode:int,count:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],type:int,indices:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],drawcount:int ) -> None :
    global __glMultiDrawElements_impl
    if not __glMultiDrawElements_impl:
        fptr = __pyglGetFuncAddress('glMultiDrawElements')
        if not fptr:
            raise RuntimeError('The function glMultiDrawElements is not available (maybe GL has not been initialized yet?)')
        __glMultiDrawElements_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p,c_uint,c_void_p,c_int )(fptr)
        tmp = __glMultiDrawElements_impl
        __glMultiDrawElements_impl = (lambda mode,count,type,indices,drawcount: tmp(mode,__pyglGetAsConstVoidPointer(count),type,__pyglGetAsConstVoidPointer(indices),drawcount))
    for _f in __universal_hooks:
        _f("glMultiDrawElements",glMultiDrawElements,mode,count,type,indices,drawcount)
    if 'glMultiDrawElements' in __hooks:
        for _f in __hooks['glMultiDrawElements']:
            _f("glMultiDrawElements",glMultiDrawElements,mode,count,type,indices,drawcount)
    rv = __glMultiDrawElements_impl(mode,count,type,indices,drawcount)
    if 'glMultiDrawElements' in __posthooks:
        for _f in __posthooks['glMultiDrawElements']:
            _f(rv,"glMultiDrawElements",glMultiDrawElements,mode,count,type,indices,drawcount)
    for _f in __universal_posthooks:
        _f(rv,"glMultiDrawElements",glMultiDrawElements,mode,count,type,indices,drawcount)
    return rv

__glMultiDrawElementsBaseVertex_impl = None
def glMultiDrawElementsBaseVertex ( mode:int,count:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],type:int,indices:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],drawcount:int,basevertex:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glMultiDrawElementsBaseVertex_impl
    if not __glMultiDrawElementsBaseVertex_impl:
        fptr = __pyglGetFuncAddress('glMultiDrawElementsBaseVertex')
        if not fptr:
            raise RuntimeError('The function glMultiDrawElementsBaseVertex is not available (maybe GL has not been initialized yet?)')
        __glMultiDrawElementsBaseVertex_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p,c_uint,c_void_p,c_int,c_void_p )(fptr)
        tmp = __glMultiDrawElementsBaseVertex_impl
        __glMultiDrawElementsBaseVertex_impl = (lambda mode,count,type,indices,drawcount,basevertex: tmp(mode,__pyglGetAsConstVoidPointer(count),type,__pyglGetAsConstVoidPointer(indices),drawcount,__pyglGetAsConstVoidPointer(basevertex)))
    for _f in __universal_hooks:
        _f("glMultiDrawElementsBaseVertex",glMultiDrawElementsBaseVertex,mode,count,type,indices,drawcount,basevertex)
    if 'glMultiDrawElementsBaseVertex' in __hooks:
        for _f in __hooks['glMultiDrawElementsBaseVertex']:
            _f("glMultiDrawElementsBaseVertex",glMultiDrawElementsBaseVertex,mode,count,type,indices,drawcount,basevertex)
    rv = __glMultiDrawElementsBaseVertex_impl(mode,count,type,indices,drawcount,basevertex)
    if 'glMultiDrawElementsBaseVertex' in __posthooks:
        for _f in __posthooks['glMultiDrawElementsBaseVertex']:
            _f(rv,"glMultiDrawElementsBaseVertex",glMultiDrawElementsBaseVertex,mode,count,type,indices,drawcount,basevertex)
    for _f in __universal_posthooks:
        _f(rv,"glMultiDrawElementsBaseVertex",glMultiDrawElementsBaseVertex,mode,count,type,indices,drawcount,basevertex)
    return rv

__glMultiDrawElementsIndirect_impl = None
def glMultiDrawElementsIndirect ( mode:int,type:int,indirect:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],drawcount:int,stride:int ) -> None :
    global __glMultiDrawElementsIndirect_impl
    if not __glMultiDrawElementsIndirect_impl:
        fptr = __pyglGetFuncAddress('glMultiDrawElementsIndirect')
        if not fptr:
            raise RuntimeError('The function glMultiDrawElementsIndirect is not available (maybe GL has not been initialized yet?)')
        __glMultiDrawElementsIndirect_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p,c_int,c_int )(fptr)
        tmp = __glMultiDrawElementsIndirect_impl
        __glMultiDrawElementsIndirect_impl = (lambda mode,type,indirect,drawcount,stride: tmp(mode,type,__pyglGetAsConstVoidPointer(indirect),drawcount,stride))
    for _f in __universal_hooks:
        _f("glMultiDrawElementsIndirect",glMultiDrawElementsIndirect,mode,type,indirect,drawcount,stride)
    if 'glMultiDrawElementsIndirect' in __hooks:
        for _f in __hooks['glMultiDrawElementsIndirect']:
            _f("glMultiDrawElementsIndirect",glMultiDrawElementsIndirect,mode,type,indirect,drawcount,stride)
    rv = __glMultiDrawElementsIndirect_impl(mode,type,indirect,drawcount,stride)
    if 'glMultiDrawElementsIndirect' in __posthooks:
        for _f in __posthooks['glMultiDrawElementsIndirect']:
            _f(rv,"glMultiDrawElementsIndirect",glMultiDrawElementsIndirect,mode,type,indirect,drawcount,stride)
    for _f in __universal_posthooks:
        _f(rv,"glMultiDrawElementsIndirect",glMultiDrawElementsIndirect,mode,type,indirect,drawcount,stride)
    return rv

__glNamedBufferData_impl = None
def glNamedBufferData ( buffer:int,size:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],data:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],usage:int ) -> None :
    global __glNamedBufferData_impl
    if not __glNamedBufferData_impl:
        fptr = __pyglGetFuncAddress('glNamedBufferData')
        if not fptr:
            raise RuntimeError('The function glNamedBufferData is not available (maybe GL has not been initialized yet?)')
        __glNamedBufferData_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p,c_void_p,c_uint )(fptr)
        tmp = __glNamedBufferData_impl
        __glNamedBufferData_impl = (lambda buffer,size,data,usage: tmp(buffer,size,__pyglGetAsConstVoidPointer(data),usage))
        global glNamedBufferData
        glNamedBufferData =__glNamedBufferData_impl
    return __glNamedBufferData_impl(buffer,size,data,usage)

__glNamedBufferStorage_impl = None
def glNamedBufferStorage ( buffer:int,size:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],data:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],flags:int ) -> None :
    global __glNamedBufferStorage_impl
    if not __glNamedBufferStorage_impl:
        fptr = __pyglGetFuncAddress('glNamedBufferStorage')
        if not fptr:
            raise RuntimeError('The function glNamedBufferStorage is not available (maybe GL has not been initialized yet?)')
        __glNamedBufferStorage_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p,c_void_p,c_uint )(fptr)
        tmp = __glNamedBufferStorage_impl
        __glNamedBufferStorage_impl = (lambda buffer,size,data,flags: tmp(buffer,size,__pyglGetAsConstVoidPointer(data),flags))
        global glNamedBufferStorage
        glNamedBufferStorage =__glNamedBufferStorage_impl
    return __glNamedBufferStorage_impl(buffer,size,data,flags)

__glNamedBufferSubData_impl = None
def glNamedBufferSubData ( buffer:int,offset:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],size:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],data:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glNamedBufferSubData_impl
    if not __glNamedBufferSubData_impl:
        fptr = __pyglGetFuncAddress('glNamedBufferSubData')
        if not fptr:
            raise RuntimeError('The function glNamedBufferSubData is not available (maybe GL has not been initialized yet?)')
        __glNamedBufferSubData_impl = __PYGL_FUNC_TYPE( None,c_uint,c_size_t,c_void_p,c_void_p )(fptr)
        tmp = __glNamedBufferSubData_impl
        __glNamedBufferSubData_impl = (lambda buffer,offset,size,data: tmp(buffer,offset,size,__pyglGetAsConstVoidPointer(data)))
        global glNamedBufferSubData
        glNamedBufferSubData =__glNamedBufferSubData_impl
    return __glNamedBufferSubData_impl(buffer,offset,size,data)

__glNamedFramebufferDrawBuffer_impl = None
def glNamedFramebufferDrawBuffer ( framebuffer:int,buf:int ) -> None :
    global __glNamedFramebufferDrawBuffer_impl
    if not __glNamedFramebufferDrawBuffer_impl:
        fptr = __pyglGetFuncAddress('glNamedFramebufferDrawBuffer')
        if not fptr:
            raise RuntimeError('The function glNamedFramebufferDrawBuffer is not available (maybe GL has not been initialized yet?)')
        __glNamedFramebufferDrawBuffer_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint )(fptr)
        global glNamedFramebufferDrawBuffer
        glNamedFramebufferDrawBuffer =__glNamedFramebufferDrawBuffer_impl
    return __glNamedFramebufferDrawBuffer_impl(framebuffer,buf)

__glNamedFramebufferDrawBuffers_impl = None
def glNamedFramebufferDrawBuffers ( framebuffer:int,n:int,bufs:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glNamedFramebufferDrawBuffers_impl
    if not __glNamedFramebufferDrawBuffers_impl:
        fptr = __pyglGetFuncAddress('glNamedFramebufferDrawBuffers')
        if not fptr:
            raise RuntimeError('The function glNamedFramebufferDrawBuffers is not available (maybe GL has not been initialized yet?)')
        __glNamedFramebufferDrawBuffers_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_void_p )(fptr)
        tmp = __glNamedFramebufferDrawBuffers_impl
        __glNamedFramebufferDrawBuffers_impl = (lambda framebuffer,n,bufs: tmp(framebuffer,n,__pyglGetAsConstVoidPointer(bufs)))
        global glNamedFramebufferDrawBuffers
        glNamedFramebufferDrawBuffers =__glNamedFramebufferDrawBuffers_impl
    return __glNamedFramebufferDrawBuffers_impl(framebuffer,n,bufs)

__glNamedFramebufferParameteri_impl = None
def glNamedFramebufferParameteri ( framebuffer:int,pname:int,param:int ) -> None :
    global __glNamedFramebufferParameteri_impl
    if not __glNamedFramebufferParameteri_impl:
        fptr = __pyglGetFuncAddress('glNamedFramebufferParameteri')
        if not fptr:
            raise RuntimeError('The function glNamedFramebufferParameteri is not available (maybe GL has not been initialized yet?)')
        __glNamedFramebufferParameteri_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_int )(fptr)
        global glNamedFramebufferParameteri
        glNamedFramebufferParameteri =__glNamedFramebufferParameteri_impl
    return __glNamedFramebufferParameteri_impl(framebuffer,pname,param)

__glNamedFramebufferReadBuffer_impl = None
def glNamedFramebufferReadBuffer ( framebuffer:int,src:int ) -> None :
    global __glNamedFramebufferReadBuffer_impl
    if not __glNamedFramebufferReadBuffer_impl:
        fptr = __pyglGetFuncAddress('glNamedFramebufferReadBuffer')
        if not fptr:
            raise RuntimeError('The function glNamedFramebufferReadBuffer is not available (maybe GL has not been initialized yet?)')
        __glNamedFramebufferReadBuffer_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint )(fptr)
        global glNamedFramebufferReadBuffer
        glNamedFramebufferReadBuffer =__glNamedFramebufferReadBuffer_impl
    return __glNamedFramebufferReadBuffer_impl(framebuffer,src)

__glNamedFramebufferRenderbuffer_impl = None
def glNamedFramebufferRenderbuffer ( framebuffer:int,attachment:int,renderbuffertarget:int,renderbuffer:int ) -> None :
    global __glNamedFramebufferRenderbuffer_impl
    if not __glNamedFramebufferRenderbuffer_impl:
        fptr = __pyglGetFuncAddress('glNamedFramebufferRenderbuffer')
        if not fptr:
            raise RuntimeError('The function glNamedFramebufferRenderbuffer is not available (maybe GL has not been initialized yet?)')
        __glNamedFramebufferRenderbuffer_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint,c_uint )(fptr)
        global glNamedFramebufferRenderbuffer
        glNamedFramebufferRenderbuffer =__glNamedFramebufferRenderbuffer_impl
    return __glNamedFramebufferRenderbuffer_impl(framebuffer,attachment,renderbuffertarget,renderbuffer)

__glNamedFramebufferTexture_impl = None
def glNamedFramebufferTexture ( framebuffer:int,attachment:int,texture:int,level:int ) -> None :
    global __glNamedFramebufferTexture_impl
    if not __glNamedFramebufferTexture_impl:
        fptr = __pyglGetFuncAddress('glNamedFramebufferTexture')
        if not fptr:
            raise RuntimeError('The function glNamedFramebufferTexture is not available (maybe GL has not been initialized yet?)')
        __glNamedFramebufferTexture_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint,c_int )(fptr)
        global glNamedFramebufferTexture
        glNamedFramebufferTexture =__glNamedFramebufferTexture_impl
    return __glNamedFramebufferTexture_impl(framebuffer,attachment,texture,level)

__glNamedFramebufferTextureLayer_impl = None
def glNamedFramebufferTextureLayer ( framebuffer:int,attachment:int,texture:int,level:int,layer:int ) -> None :
    global __glNamedFramebufferTextureLayer_impl
    if not __glNamedFramebufferTextureLayer_impl:
        fptr = __pyglGetFuncAddress('glNamedFramebufferTextureLayer')
        if not fptr:
            raise RuntimeError('The function glNamedFramebufferTextureLayer is not available (maybe GL has not been initialized yet?)')
        __glNamedFramebufferTextureLayer_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint,c_int,c_int )(fptr)
        global glNamedFramebufferTextureLayer
        glNamedFramebufferTextureLayer =__glNamedFramebufferTextureLayer_impl
    return __glNamedFramebufferTextureLayer_impl(framebuffer,attachment,texture,level,layer)

__glNamedRenderbufferStorage_impl = None
def glNamedRenderbufferStorage ( renderbuffer:int,internalformat:int,width:int,height:int ) -> None :
    global __glNamedRenderbufferStorage_impl
    if not __glNamedRenderbufferStorage_impl:
        fptr = __pyglGetFuncAddress('glNamedRenderbufferStorage')
        if not fptr:
            raise RuntimeError('The function glNamedRenderbufferStorage is not available (maybe GL has not been initialized yet?)')
        __glNamedRenderbufferStorage_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_int,c_int )(fptr)
        global glNamedRenderbufferStorage
        glNamedRenderbufferStorage =__glNamedRenderbufferStorage_impl
    return __glNamedRenderbufferStorage_impl(renderbuffer,internalformat,width,height)

__glNamedRenderbufferStorageMultisample_impl = None
def glNamedRenderbufferStorageMultisample ( renderbuffer:int,samples:int,internalformat:int,width:int,height:int ) -> None :
    global __glNamedRenderbufferStorageMultisample_impl
    if not __glNamedRenderbufferStorageMultisample_impl:
        fptr = __pyglGetFuncAddress('glNamedRenderbufferStorageMultisample')
        if not fptr:
            raise RuntimeError('The function glNamedRenderbufferStorageMultisample is not available (maybe GL has not been initialized yet?)')
        __glNamedRenderbufferStorageMultisample_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_uint,c_int,c_int )(fptr)
        global glNamedRenderbufferStorageMultisample
        glNamedRenderbufferStorageMultisample =__glNamedRenderbufferStorageMultisample_impl
    return __glNamedRenderbufferStorageMultisample_impl(renderbuffer,samples,internalformat,width,height)

__glObjectLabel_impl = None
def glObjectLabel ( identifier:int,name:int,length:int,label:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glObjectLabel_impl
    if not __glObjectLabel_impl:
        fptr = __pyglGetFuncAddress('glObjectLabel')
        if not fptr:
            raise RuntimeError('The function glObjectLabel is not available (maybe GL has not been initialized yet?)')
        __glObjectLabel_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_int,c_void_p )(fptr)
        tmp = __glObjectLabel_impl
        __glObjectLabel_impl = (lambda identifier,name,length,label: tmp(identifier,name,length,c_char_p(label.encode())))
        global glObjectLabel
        glObjectLabel =__glObjectLabel_impl
    return __glObjectLabel_impl(identifier,name,length,label)

__glObjectPtrLabel_impl = None
def glObjectPtrLabel ( ptr:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],length:int,label:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glObjectPtrLabel_impl
    if not __glObjectPtrLabel_impl:
        fptr = __pyglGetFuncAddress('glObjectPtrLabel')
        if not fptr:
            raise RuntimeError('The function glObjectPtrLabel is not available (maybe GL has not been initialized yet?)')
        __glObjectPtrLabel_impl = __PYGL_FUNC_TYPE( None,c_void_p,c_int,c_void_p )(fptr)
        tmp = __glObjectPtrLabel_impl
        __glObjectPtrLabel_impl = (lambda ptr,length,label: tmp(__pyglGetAsConstVoidPointer(ptr),length,c_char_p(label.encode())))
        global glObjectPtrLabel
        glObjectPtrLabel =__glObjectPtrLabel_impl
    return __glObjectPtrLabel_impl(ptr,length,label)

__glPatchParameterfv_impl = None
def glPatchParameterfv ( pname:int,values:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glPatchParameterfv_impl
    if not __glPatchParameterfv_impl:
        fptr = __pyglGetFuncAddress('glPatchParameterfv')
        if not fptr:
            raise RuntimeError('The function glPatchParameterfv is not available (maybe GL has not been initialized yet?)')
        __glPatchParameterfv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p )(fptr)
        tmp = __glPatchParameterfv_impl
        __glPatchParameterfv_impl = (lambda pname,values: tmp(pname,__pyglGetAsConstVoidPointer(values)))
        global glPatchParameterfv
        glPatchParameterfv =__glPatchParameterfv_impl
    return __glPatchParameterfv_impl(pname,values)

__glPatchParameteri_impl = None
def glPatchParameteri ( pname:int,value:int ) -> None :
    global __glPatchParameteri_impl
    if not __glPatchParameteri_impl:
        fptr = __pyglGetFuncAddress('glPatchParameteri')
        if not fptr:
            raise RuntimeError('The function glPatchParameteri is not available (maybe GL has not been initialized yet?)')
        __glPatchParameteri_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int )(fptr)
        global glPatchParameteri
        glPatchParameteri =__glPatchParameteri_impl
    return __glPatchParameteri_impl(pname,value)

__glPauseTransformFeedback_impl = None
def glPauseTransformFeedback (  ) -> None :
    global __glPauseTransformFeedback_impl
    if not __glPauseTransformFeedback_impl:
        fptr = __pyglGetFuncAddress('glPauseTransformFeedback')
        if not fptr:
            raise RuntimeError('The function glPauseTransformFeedback is not available (maybe GL has not been initialized yet?)')
        __glPauseTransformFeedback_impl = __PYGL_FUNC_TYPE( None )(fptr)
        global glPauseTransformFeedback
        glPauseTransformFeedback =__glPauseTransformFeedback_impl
    return __glPauseTransformFeedback_impl()

__glPixelStoref_impl = None
def glPixelStoref ( pname:int,param:float ) -> None :
    global __glPixelStoref_impl
    if not __glPixelStoref_impl:
        fptr = __pyglGetFuncAddress('glPixelStoref')
        if not fptr:
            raise RuntimeError('The function glPixelStoref is not available (maybe GL has not been initialized yet?)')
        __glPixelStoref_impl = __PYGL_FUNC_TYPE( None,c_uint,c_float )(fptr)
        global glPixelStoref
        glPixelStoref =__glPixelStoref_impl
    return __glPixelStoref_impl(pname,param)

__glPixelStorei_impl = None
def glPixelStorei ( pname:int,param:int ) -> None :
    global __glPixelStorei_impl
    if not __glPixelStorei_impl:
        fptr = __pyglGetFuncAddress('glPixelStorei')
        if not fptr:
            raise RuntimeError('The function glPixelStorei is not available (maybe GL has not been initialized yet?)')
        __glPixelStorei_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int )(fptr)
        global glPixelStorei
        glPixelStorei =__glPixelStorei_impl
    return __glPixelStorei_impl(pname,param)

__glPointParameterf_impl = None
def glPointParameterf ( pname:int,param:float ) -> None :
    global __glPointParameterf_impl
    if not __glPointParameterf_impl:
        fptr = __pyglGetFuncAddress('glPointParameterf')
        if not fptr:
            raise RuntimeError('The function glPointParameterf is not available (maybe GL has not been initialized yet?)')
        __glPointParameterf_impl = __PYGL_FUNC_TYPE( None,c_uint,c_float )(fptr)
        global glPointParameterf
        glPointParameterf =__glPointParameterf_impl
    return __glPointParameterf_impl(pname,param)

__glPointParameterfv_impl = None
def glPointParameterfv ( pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glPointParameterfv_impl
    if not __glPointParameterfv_impl:
        fptr = __pyglGetFuncAddress('glPointParameterfv')
        if not fptr:
            raise RuntimeError('The function glPointParameterfv is not available (maybe GL has not been initialized yet?)')
        __glPointParameterfv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p )(fptr)
        tmp = __glPointParameterfv_impl
        __glPointParameterfv_impl = (lambda pname,params: tmp(pname,__pyglGetAsConstVoidPointer(params)))
        global glPointParameterfv
        glPointParameterfv =__glPointParameterfv_impl
    return __glPointParameterfv_impl(pname,params)

__glPointParameteri_impl = None
def glPointParameteri ( pname:int,param:int ) -> None :
    global __glPointParameteri_impl
    if not __glPointParameteri_impl:
        fptr = __pyglGetFuncAddress('glPointParameteri')
        if not fptr:
            raise RuntimeError('The function glPointParameteri is not available (maybe GL has not been initialized yet?)')
        __glPointParameteri_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int )(fptr)
        global glPointParameteri
        glPointParameteri =__glPointParameteri_impl
    return __glPointParameteri_impl(pname,param)

__glPointParameteriv_impl = None
def glPointParameteriv ( pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glPointParameteriv_impl
    if not __glPointParameteriv_impl:
        fptr = __pyglGetFuncAddress('glPointParameteriv')
        if not fptr:
            raise RuntimeError('The function glPointParameteriv is not available (maybe GL has not been initialized yet?)')
        __glPointParameteriv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p )(fptr)
        tmp = __glPointParameteriv_impl
        __glPointParameteriv_impl = (lambda pname,params: tmp(pname,__pyglGetAsConstVoidPointer(params)))
        global glPointParameteriv
        glPointParameteriv =__glPointParameteriv_impl
    return __glPointParameteriv_impl(pname,params)

__glPointSize_impl = None
def glPointSize ( size:float ) -> None :
    global __glPointSize_impl
    if not __glPointSize_impl:
        fptr = __pyglGetFuncAddress('glPointSize')
        if not fptr:
            raise RuntimeError('The function glPointSize is not available (maybe GL has not been initialized yet?)')
        __glPointSize_impl = __PYGL_FUNC_TYPE( None,c_float )(fptr)
        global glPointSize
        glPointSize =__glPointSize_impl
    return __glPointSize_impl(size)

__glPolygonMode_impl = None
def glPolygonMode ( face:int,mode:int ) -> None :
    global __glPolygonMode_impl
    if not __glPolygonMode_impl:
        fptr = __pyglGetFuncAddress('glPolygonMode')
        if not fptr:
            raise RuntimeError('The function glPolygonMode is not available (maybe GL has not been initialized yet?)')
        __glPolygonMode_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint )(fptr)
        global glPolygonMode
        glPolygonMode =__glPolygonMode_impl
    return __glPolygonMode_impl(face,mode)

__glPolygonOffset_impl = None
def glPolygonOffset ( factor:float,units:float ) -> None :
    global __glPolygonOffset_impl
    if not __glPolygonOffset_impl:
        fptr = __pyglGetFuncAddress('glPolygonOffset')
        if not fptr:
            raise RuntimeError('The function glPolygonOffset is not available (maybe GL has not been initialized yet?)')
        __glPolygonOffset_impl = __PYGL_FUNC_TYPE( None,c_float,c_float )(fptr)
        global glPolygonOffset
        glPolygonOffset =__glPolygonOffset_impl
    return __glPolygonOffset_impl(factor,units)

__glPopDebugGroup_impl = None
def glPopDebugGroup (  ) -> None :
    global __glPopDebugGroup_impl
    if not __glPopDebugGroup_impl:
        fptr = __pyglGetFuncAddress('glPopDebugGroup')
        if not fptr:
            raise RuntimeError('The function glPopDebugGroup is not available (maybe GL has not been initialized yet?)')
        __glPopDebugGroup_impl = __PYGL_FUNC_TYPE( None )(fptr)
        global glPopDebugGroup
        glPopDebugGroup =__glPopDebugGroup_impl
    return __glPopDebugGroup_impl()

__glPrimitiveRestartIndex_impl = None
def glPrimitiveRestartIndex ( index:int ) -> None :
    global __glPrimitiveRestartIndex_impl
    if not __glPrimitiveRestartIndex_impl:
        fptr = __pyglGetFuncAddress('glPrimitiveRestartIndex')
        if not fptr:
            raise RuntimeError('The function glPrimitiveRestartIndex is not available (maybe GL has not been initialized yet?)')
        __glPrimitiveRestartIndex_impl = __PYGL_FUNC_TYPE( None,c_uint )(fptr)
        global glPrimitiveRestartIndex
        glPrimitiveRestartIndex =__glPrimitiveRestartIndex_impl
    return __glPrimitiveRestartIndex_impl(index)

__glProgramBinary_impl = None
def glProgramBinary ( program:int,binaryFormat:int,binary:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],length:int ) -> None :
    global __glProgramBinary_impl
    if not __glProgramBinary_impl:
        fptr = __pyglGetFuncAddress('glProgramBinary')
        if not fptr:
            raise RuntimeError('The function glProgramBinary is not available (maybe GL has not been initialized yet?)')
        __glProgramBinary_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p,c_int )(fptr)
        tmp = __glProgramBinary_impl
        __glProgramBinary_impl = (lambda program,binaryFormat,binary,length: tmp(program,binaryFormat,__pyglGetAsConstVoidPointer(binary),length))
        global glProgramBinary
        glProgramBinary =__glProgramBinary_impl
    return __glProgramBinary_impl(program,binaryFormat,binary,length)

__glProgramParameteri_impl = None
def glProgramParameteri ( program:int,pname:int,value:int ) -> None :
    global __glProgramParameteri_impl
    if not __glProgramParameteri_impl:
        fptr = __pyglGetFuncAddress('glProgramParameteri')
        if not fptr:
            raise RuntimeError('The function glProgramParameteri is not available (maybe GL has not been initialized yet?)')
        __glProgramParameteri_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_int )(fptr)
        global glProgramParameteri
        glProgramParameteri =__glProgramParameteri_impl
    return __glProgramParameteri_impl(program,pname,value)

__glProgramUniform1d_impl = None
def glProgramUniform1d ( program:int,location:int,v0:float ) -> None :
    global __glProgramUniform1d_impl
    if not __glProgramUniform1d_impl:
        fptr = __pyglGetFuncAddress('glProgramUniform1d')
        if not fptr:
            raise RuntimeError('The function glProgramUniform1d is not available (maybe GL has not been initialized yet?)')
        __glProgramUniform1d_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_double )(fptr)
        global glProgramUniform1d
        glProgramUniform1d =__glProgramUniform1d_impl
    return __glProgramUniform1d_impl(program,location,v0)

__glProgramUniform1dv_impl = None
def glProgramUniform1dv ( program:int,location:int,count:int,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glProgramUniform1dv_impl
    if not __glProgramUniform1dv_impl:
        fptr = __pyglGetFuncAddress('glProgramUniform1dv')
        if not fptr:
            raise RuntimeError('The function glProgramUniform1dv is not available (maybe GL has not been initialized yet?)')
        __glProgramUniform1dv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_void_p )(fptr)
        tmp = __glProgramUniform1dv_impl
        __glProgramUniform1dv_impl = (lambda program,location,count,value: tmp(program,location,count,__pyglGetAsConstVoidPointer(value)))
        global glProgramUniform1dv
        glProgramUniform1dv =__glProgramUniform1dv_impl
    return __glProgramUniform1dv_impl(program,location,count,value)

__glProgramUniform1f_impl = None
def glProgramUniform1f ( program:int,location:int,v0:float ) -> None :
    global __glProgramUniform1f_impl
    if not __glProgramUniform1f_impl:
        fptr = __pyglGetFuncAddress('glProgramUniform1f')
        if not fptr:
            raise RuntimeError('The function glProgramUniform1f is not available (maybe GL has not been initialized yet?)')
        __glProgramUniform1f_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_float )(fptr)
        global glProgramUniform1f
        glProgramUniform1f =__glProgramUniform1f_impl
    return __glProgramUniform1f_impl(program,location,v0)

__glProgramUniform1fv_impl = None
def glProgramUniform1fv ( program:int,location:int,count:int,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glProgramUniform1fv_impl
    if not __glProgramUniform1fv_impl:
        fptr = __pyglGetFuncAddress('glProgramUniform1fv')
        if not fptr:
            raise RuntimeError('The function glProgramUniform1fv is not available (maybe GL has not been initialized yet?)')
        __glProgramUniform1fv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_void_p )(fptr)
        tmp = __glProgramUniform1fv_impl
        __glProgramUniform1fv_impl = (lambda program,location,count,value: tmp(program,location,count,__pyglGetAsConstVoidPointer(value)))
        global glProgramUniform1fv
        glProgramUniform1fv =__glProgramUniform1fv_impl
    return __glProgramUniform1fv_impl(program,location,count,value)

__glProgramUniform1i_impl = None
def glProgramUniform1i ( program:int,location:int,v0:int ) -> None :
    global __glProgramUniform1i_impl
    if not __glProgramUniform1i_impl:
        fptr = __pyglGetFuncAddress('glProgramUniform1i')
        if not fptr:
            raise RuntimeError('The function glProgramUniform1i is not available (maybe GL has not been initialized yet?)')
        __glProgramUniform1i_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int )(fptr)
        global glProgramUniform1i
        glProgramUniform1i =__glProgramUniform1i_impl
    return __glProgramUniform1i_impl(program,location,v0)

__glProgramUniform1iv_impl = None
def glProgramUniform1iv ( program:int,location:int,count:int,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glProgramUniform1iv_impl
    if not __glProgramUniform1iv_impl:
        fptr = __pyglGetFuncAddress('glProgramUniform1iv')
        if not fptr:
            raise RuntimeError('The function glProgramUniform1iv is not available (maybe GL has not been initialized yet?)')
        __glProgramUniform1iv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_void_p )(fptr)
        tmp = __glProgramUniform1iv_impl
        __glProgramUniform1iv_impl = (lambda program,location,count,value: tmp(program,location,count,__pyglGetAsConstVoidPointer(value)))
        global glProgramUniform1iv
        glProgramUniform1iv =__glProgramUniform1iv_impl
    return __glProgramUniform1iv_impl(program,location,count,value)

__glProgramUniform1ui_impl = None
def glProgramUniform1ui ( program:int,location:int,v0:int ) -> None :
    global __glProgramUniform1ui_impl
    if not __glProgramUniform1ui_impl:
        fptr = __pyglGetFuncAddress('glProgramUniform1ui')
        if not fptr:
            raise RuntimeError('The function glProgramUniform1ui is not available (maybe GL has not been initialized yet?)')
        __glProgramUniform1ui_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_uint )(fptr)
        global glProgramUniform1ui
        glProgramUniform1ui =__glProgramUniform1ui_impl
    return __glProgramUniform1ui_impl(program,location,v0)

__glProgramUniform1uiv_impl = None
def glProgramUniform1uiv ( program:int,location:int,count:int,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glProgramUniform1uiv_impl
    if not __glProgramUniform1uiv_impl:
        fptr = __pyglGetFuncAddress('glProgramUniform1uiv')
        if not fptr:
            raise RuntimeError('The function glProgramUniform1uiv is not available (maybe GL has not been initialized yet?)')
        __glProgramUniform1uiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_void_p )(fptr)
        tmp = __glProgramUniform1uiv_impl
        __glProgramUniform1uiv_impl = (lambda program,location,count,value: tmp(program,location,count,__pyglGetAsConstVoidPointer(value)))
        global glProgramUniform1uiv
        glProgramUniform1uiv =__glProgramUniform1uiv_impl
    return __glProgramUniform1uiv_impl(program,location,count,value)

__glProgramUniform2d_impl = None
def glProgramUniform2d ( program:int,location:int,v0:float,v1:float ) -> None :
    global __glProgramUniform2d_impl
    if not __glProgramUniform2d_impl:
        fptr = __pyglGetFuncAddress('glProgramUniform2d')
        if not fptr:
            raise RuntimeError('The function glProgramUniform2d is not available (maybe GL has not been initialized yet?)')
        __glProgramUniform2d_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_double,c_double )(fptr)
        global glProgramUniform2d
        glProgramUniform2d =__glProgramUniform2d_impl
    return __glProgramUniform2d_impl(program,location,v0,v1)

__glProgramUniform2dv_impl = None
def glProgramUniform2dv ( program:int,location:int,count:int,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glProgramUniform2dv_impl
    if not __glProgramUniform2dv_impl:
        fptr = __pyglGetFuncAddress('glProgramUniform2dv')
        if not fptr:
            raise RuntimeError('The function glProgramUniform2dv is not available (maybe GL has not been initialized yet?)')
        __glProgramUniform2dv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_void_p )(fptr)
        tmp = __glProgramUniform2dv_impl
        __glProgramUniform2dv_impl = (lambda program,location,count,value: tmp(program,location,count,__pyglGetAsConstVoidPointer(value)))
        global glProgramUniform2dv
        glProgramUniform2dv =__glProgramUniform2dv_impl
    return __glProgramUniform2dv_impl(program,location,count,value)

__glProgramUniform2f_impl = None
def glProgramUniform2f ( program:int,location:int,v0:float,v1:float ) -> None :
    global __glProgramUniform2f_impl
    if not __glProgramUniform2f_impl:
        fptr = __pyglGetFuncAddress('glProgramUniform2f')
        if not fptr:
            raise RuntimeError('The function glProgramUniform2f is not available (maybe GL has not been initialized yet?)')
        __glProgramUniform2f_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_float,c_float )(fptr)
        global glProgramUniform2f
        glProgramUniform2f =__glProgramUniform2f_impl
    return __glProgramUniform2f_impl(program,location,v0,v1)

__glProgramUniform2fv_impl = None
def glProgramUniform2fv ( program:int,location:int,count:int,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glProgramUniform2fv_impl
    if not __glProgramUniform2fv_impl:
        fptr = __pyglGetFuncAddress('glProgramUniform2fv')
        if not fptr:
            raise RuntimeError('The function glProgramUniform2fv is not available (maybe GL has not been initialized yet?)')
        __glProgramUniform2fv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_void_p )(fptr)
        tmp = __glProgramUniform2fv_impl
        __glProgramUniform2fv_impl = (lambda program,location,count,value: tmp(program,location,count,__pyglGetAsConstVoidPointer(value)))
        global glProgramUniform2fv
        glProgramUniform2fv =__glProgramUniform2fv_impl
    return __glProgramUniform2fv_impl(program,location,count,value)

__glProgramUniform2i_impl = None
def glProgramUniform2i ( program:int,location:int,v0:int,v1:int ) -> None :
    global __glProgramUniform2i_impl
    if not __glProgramUniform2i_impl:
        fptr = __pyglGetFuncAddress('glProgramUniform2i')
        if not fptr:
            raise RuntimeError('The function glProgramUniform2i is not available (maybe GL has not been initialized yet?)')
        __glProgramUniform2i_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_int )(fptr)
        global glProgramUniform2i
        glProgramUniform2i =__glProgramUniform2i_impl
    return __glProgramUniform2i_impl(program,location,v0,v1)

__glProgramUniform2iv_impl = None
def glProgramUniform2iv ( program:int,location:int,count:int,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glProgramUniform2iv_impl
    if not __glProgramUniform2iv_impl:
        fptr = __pyglGetFuncAddress('glProgramUniform2iv')
        if not fptr:
            raise RuntimeError('The function glProgramUniform2iv is not available (maybe GL has not been initialized yet?)')
        __glProgramUniform2iv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_void_p )(fptr)
        tmp = __glProgramUniform2iv_impl
        __glProgramUniform2iv_impl = (lambda program,location,count,value: tmp(program,location,count,__pyglGetAsConstVoidPointer(value)))
        global glProgramUniform2iv
        glProgramUniform2iv =__glProgramUniform2iv_impl
    return __glProgramUniform2iv_impl(program,location,count,value)

__glProgramUniform2ui_impl = None
def glProgramUniform2ui ( program:int,location:int,v0:int,v1:int ) -> None :
    global __glProgramUniform2ui_impl
    if not __glProgramUniform2ui_impl:
        fptr = __pyglGetFuncAddress('glProgramUniform2ui')
        if not fptr:
            raise RuntimeError('The function glProgramUniform2ui is not available (maybe GL has not been initialized yet?)')
        __glProgramUniform2ui_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_uint,c_uint )(fptr)
        global glProgramUniform2ui
        glProgramUniform2ui =__glProgramUniform2ui_impl
    return __glProgramUniform2ui_impl(program,location,v0,v1)

__glProgramUniform2uiv_impl = None
def glProgramUniform2uiv ( program:int,location:int,count:int,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glProgramUniform2uiv_impl
    if not __glProgramUniform2uiv_impl:
        fptr = __pyglGetFuncAddress('glProgramUniform2uiv')
        if not fptr:
            raise RuntimeError('The function glProgramUniform2uiv is not available (maybe GL has not been initialized yet?)')
        __glProgramUniform2uiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_void_p )(fptr)
        tmp = __glProgramUniform2uiv_impl
        __glProgramUniform2uiv_impl = (lambda program,location,count,value: tmp(program,location,count,__pyglGetAsConstVoidPointer(value)))
        global glProgramUniform2uiv
        glProgramUniform2uiv =__glProgramUniform2uiv_impl
    return __glProgramUniform2uiv_impl(program,location,count,value)

__glProgramUniform3d_impl = None
def glProgramUniform3d ( program:int,location:int,v0:float,v1:float,v2:float ) -> None :
    global __glProgramUniform3d_impl
    if not __glProgramUniform3d_impl:
        fptr = __pyglGetFuncAddress('glProgramUniform3d')
        if not fptr:
            raise RuntimeError('The function glProgramUniform3d is not available (maybe GL has not been initialized yet?)')
        __glProgramUniform3d_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_double,c_double,c_double )(fptr)
        global glProgramUniform3d
        glProgramUniform3d =__glProgramUniform3d_impl
    return __glProgramUniform3d_impl(program,location,v0,v1,v2)

__glProgramUniform3dv_impl = None
def glProgramUniform3dv ( program:int,location:int,count:int,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glProgramUniform3dv_impl
    if not __glProgramUniform3dv_impl:
        fptr = __pyglGetFuncAddress('glProgramUniform3dv')
        if not fptr:
            raise RuntimeError('The function glProgramUniform3dv is not available (maybe GL has not been initialized yet?)')
        __glProgramUniform3dv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_void_p )(fptr)
        tmp = __glProgramUniform3dv_impl
        __glProgramUniform3dv_impl = (lambda program,location,count,value: tmp(program,location,count,__pyglGetAsConstVoidPointer(value)))
        global glProgramUniform3dv
        glProgramUniform3dv =__glProgramUniform3dv_impl
    return __glProgramUniform3dv_impl(program,location,count,value)

__glProgramUniform3f_impl = None
def glProgramUniform3f ( program:int,location:int,v0:float,v1:float,v2:float ) -> None :
    global __glProgramUniform3f_impl
    if not __glProgramUniform3f_impl:
        fptr = __pyglGetFuncAddress('glProgramUniform3f')
        if not fptr:
            raise RuntimeError('The function glProgramUniform3f is not available (maybe GL has not been initialized yet?)')
        __glProgramUniform3f_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_float,c_float,c_float )(fptr)
        global glProgramUniform3f
        glProgramUniform3f =__glProgramUniform3f_impl
    return __glProgramUniform3f_impl(program,location,v0,v1,v2)

__glProgramUniform3fv_impl = None
def glProgramUniform3fv ( program:int,location:int,count:int,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glProgramUniform3fv_impl
    if not __glProgramUniform3fv_impl:
        fptr = __pyglGetFuncAddress('glProgramUniform3fv')
        if not fptr:
            raise RuntimeError('The function glProgramUniform3fv is not available (maybe GL has not been initialized yet?)')
        __glProgramUniform3fv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_void_p )(fptr)
        tmp = __glProgramUniform3fv_impl
        __glProgramUniform3fv_impl = (lambda program,location,count,value: tmp(program,location,count,__pyglGetAsConstVoidPointer(value)))
        global glProgramUniform3fv
        glProgramUniform3fv =__glProgramUniform3fv_impl
    return __glProgramUniform3fv_impl(program,location,count,value)

__glProgramUniform3i_impl = None
def glProgramUniform3i ( program:int,location:int,v0:int,v1:int,v2:int ) -> None :
    global __glProgramUniform3i_impl
    if not __glProgramUniform3i_impl:
        fptr = __pyglGetFuncAddress('glProgramUniform3i')
        if not fptr:
            raise RuntimeError('The function glProgramUniform3i is not available (maybe GL has not been initialized yet?)')
        __glProgramUniform3i_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_int,c_int )(fptr)
        global glProgramUniform3i
        glProgramUniform3i =__glProgramUniform3i_impl
    return __glProgramUniform3i_impl(program,location,v0,v1,v2)

__glProgramUniform3iv_impl = None
def glProgramUniform3iv ( program:int,location:int,count:int,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glProgramUniform3iv_impl
    if not __glProgramUniform3iv_impl:
        fptr = __pyglGetFuncAddress('glProgramUniform3iv')
        if not fptr:
            raise RuntimeError('The function glProgramUniform3iv is not available (maybe GL has not been initialized yet?)')
        __glProgramUniform3iv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_void_p )(fptr)
        tmp = __glProgramUniform3iv_impl
        __glProgramUniform3iv_impl = (lambda program,location,count,value: tmp(program,location,count,__pyglGetAsConstVoidPointer(value)))
        global glProgramUniform3iv
        glProgramUniform3iv =__glProgramUniform3iv_impl
    return __glProgramUniform3iv_impl(program,location,count,value)

__glProgramUniform3ui_impl = None
def glProgramUniform3ui ( program:int,location:int,v0:int,v1:int,v2:int ) -> None :
    global __glProgramUniform3ui_impl
    if not __glProgramUniform3ui_impl:
        fptr = __pyglGetFuncAddress('glProgramUniform3ui')
        if not fptr:
            raise RuntimeError('The function glProgramUniform3ui is not available (maybe GL has not been initialized yet?)')
        __glProgramUniform3ui_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_uint,c_uint,c_uint )(fptr)
        global glProgramUniform3ui
        glProgramUniform3ui =__glProgramUniform3ui_impl
    return __glProgramUniform3ui_impl(program,location,v0,v1,v2)

__glProgramUniform3uiv_impl = None
def glProgramUniform3uiv ( program:int,location:int,count:int,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glProgramUniform3uiv_impl
    if not __glProgramUniform3uiv_impl:
        fptr = __pyglGetFuncAddress('glProgramUniform3uiv')
        if not fptr:
            raise RuntimeError('The function glProgramUniform3uiv is not available (maybe GL has not been initialized yet?)')
        __glProgramUniform3uiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_void_p )(fptr)
        tmp = __glProgramUniform3uiv_impl
        __glProgramUniform3uiv_impl = (lambda program,location,count,value: tmp(program,location,count,__pyglGetAsConstVoidPointer(value)))
        global glProgramUniform3uiv
        glProgramUniform3uiv =__glProgramUniform3uiv_impl
    return __glProgramUniform3uiv_impl(program,location,count,value)

__glProgramUniform4d_impl = None
def glProgramUniform4d ( program:int,location:int,v0:float,v1:float,v2:float,v3:float ) -> None :
    global __glProgramUniform4d_impl
    if not __glProgramUniform4d_impl:
        fptr = __pyglGetFuncAddress('glProgramUniform4d')
        if not fptr:
            raise RuntimeError('The function glProgramUniform4d is not available (maybe GL has not been initialized yet?)')
        __glProgramUniform4d_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_double,c_double,c_double,c_double )(fptr)
        global glProgramUniform4d
        glProgramUniform4d =__glProgramUniform4d_impl
    return __glProgramUniform4d_impl(program,location,v0,v1,v2,v3)

__glProgramUniform4dv_impl = None
def glProgramUniform4dv ( program:int,location:int,count:int,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glProgramUniform4dv_impl
    if not __glProgramUniform4dv_impl:
        fptr = __pyglGetFuncAddress('glProgramUniform4dv')
        if not fptr:
            raise RuntimeError('The function glProgramUniform4dv is not available (maybe GL has not been initialized yet?)')
        __glProgramUniform4dv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_void_p )(fptr)
        tmp = __glProgramUniform4dv_impl
        __glProgramUniform4dv_impl = (lambda program,location,count,value: tmp(program,location,count,__pyglGetAsConstVoidPointer(value)))
        global glProgramUniform4dv
        glProgramUniform4dv =__glProgramUniform4dv_impl
    return __glProgramUniform4dv_impl(program,location,count,value)

__glProgramUniform4f_impl = None
def glProgramUniform4f ( program:int,location:int,v0:float,v1:float,v2:float,v3:float ) -> None :
    global __glProgramUniform4f_impl
    if not __glProgramUniform4f_impl:
        fptr = __pyglGetFuncAddress('glProgramUniform4f')
        if not fptr:
            raise RuntimeError('The function glProgramUniform4f is not available (maybe GL has not been initialized yet?)')
        __glProgramUniform4f_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_float,c_float,c_float,c_float )(fptr)
        global glProgramUniform4f
        glProgramUniform4f =__glProgramUniform4f_impl
    return __glProgramUniform4f_impl(program,location,v0,v1,v2,v3)

__glProgramUniform4fv_impl = None
def glProgramUniform4fv ( program:int,location:int,count:int,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glProgramUniform4fv_impl
    if not __glProgramUniform4fv_impl:
        fptr = __pyglGetFuncAddress('glProgramUniform4fv')
        if not fptr:
            raise RuntimeError('The function glProgramUniform4fv is not available (maybe GL has not been initialized yet?)')
        __glProgramUniform4fv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_void_p )(fptr)
        tmp = __glProgramUniform4fv_impl
        __glProgramUniform4fv_impl = (lambda program,location,count,value: tmp(program,location,count,__pyglGetAsConstVoidPointer(value)))
        global glProgramUniform4fv
        glProgramUniform4fv =__glProgramUniform4fv_impl
    return __glProgramUniform4fv_impl(program,location,count,value)

__glProgramUniform4i_impl = None
def glProgramUniform4i ( program:int,location:int,v0:int,v1:int,v2:int,v3:int ) -> None :
    global __glProgramUniform4i_impl
    if not __glProgramUniform4i_impl:
        fptr = __pyglGetFuncAddress('glProgramUniform4i')
        if not fptr:
            raise RuntimeError('The function glProgramUniform4i is not available (maybe GL has not been initialized yet?)')
        __glProgramUniform4i_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_int,c_int,c_int )(fptr)
        global glProgramUniform4i
        glProgramUniform4i =__glProgramUniform4i_impl
    return __glProgramUniform4i_impl(program,location,v0,v1,v2,v3)

__glProgramUniform4iv_impl = None
def glProgramUniform4iv ( program:int,location:int,count:int,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glProgramUniform4iv_impl
    if not __glProgramUniform4iv_impl:
        fptr = __pyglGetFuncAddress('glProgramUniform4iv')
        if not fptr:
            raise RuntimeError('The function glProgramUniform4iv is not available (maybe GL has not been initialized yet?)')
        __glProgramUniform4iv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_void_p )(fptr)
        tmp = __glProgramUniform4iv_impl
        __glProgramUniform4iv_impl = (lambda program,location,count,value: tmp(program,location,count,__pyglGetAsConstVoidPointer(value)))
        global glProgramUniform4iv
        glProgramUniform4iv =__glProgramUniform4iv_impl
    return __glProgramUniform4iv_impl(program,location,count,value)

__glProgramUniform4ui_impl = None
def glProgramUniform4ui ( program:int,location:int,v0:int,v1:int,v2:int,v3:int ) -> None :
    global __glProgramUniform4ui_impl
    if not __glProgramUniform4ui_impl:
        fptr = __pyglGetFuncAddress('glProgramUniform4ui')
        if not fptr:
            raise RuntimeError('The function glProgramUniform4ui is not available (maybe GL has not been initialized yet?)')
        __glProgramUniform4ui_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_uint,c_uint,c_uint,c_uint )(fptr)
        global glProgramUniform4ui
        glProgramUniform4ui =__glProgramUniform4ui_impl
    return __glProgramUniform4ui_impl(program,location,v0,v1,v2,v3)

__glProgramUniform4uiv_impl = None
def glProgramUniform4uiv ( program:int,location:int,count:int,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glProgramUniform4uiv_impl
    if not __glProgramUniform4uiv_impl:
        fptr = __pyglGetFuncAddress('glProgramUniform4uiv')
        if not fptr:
            raise RuntimeError('The function glProgramUniform4uiv is not available (maybe GL has not been initialized yet?)')
        __glProgramUniform4uiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_void_p )(fptr)
        tmp = __glProgramUniform4uiv_impl
        __glProgramUniform4uiv_impl = (lambda program,location,count,value: tmp(program,location,count,__pyglGetAsConstVoidPointer(value)))
        global glProgramUniform4uiv
        glProgramUniform4uiv =__glProgramUniform4uiv_impl
    return __glProgramUniform4uiv_impl(program,location,count,value)

__glProgramUniformMatrix2dv_impl = None
def glProgramUniformMatrix2dv ( program:int,location:int,count:int,transpose:bool,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glProgramUniformMatrix2dv_impl
    if not __glProgramUniformMatrix2dv_impl:
        fptr = __pyglGetFuncAddress('glProgramUniformMatrix2dv')
        if not fptr:
            raise RuntimeError('The function glProgramUniformMatrix2dv is not available (maybe GL has not been initialized yet?)')
        __glProgramUniformMatrix2dv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_char,c_void_p )(fptr)
        tmp = __glProgramUniformMatrix2dv_impl
        __glProgramUniformMatrix2dv_impl = (lambda program,location,count,transpose,value: tmp(program,location,count,transpose,__pyglGetAsConstVoidPointer(value)))
        global glProgramUniformMatrix2dv
        glProgramUniformMatrix2dv =__glProgramUniformMatrix2dv_impl
    return __glProgramUniformMatrix2dv_impl(program,location,count,transpose,value)

__glProgramUniformMatrix2fv_impl = None
def glProgramUniformMatrix2fv ( program:int,location:int,count:int,transpose:bool,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glProgramUniformMatrix2fv_impl
    if not __glProgramUniformMatrix2fv_impl:
        fptr = __pyglGetFuncAddress('glProgramUniformMatrix2fv')
        if not fptr:
            raise RuntimeError('The function glProgramUniformMatrix2fv is not available (maybe GL has not been initialized yet?)')
        __glProgramUniformMatrix2fv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_char,c_void_p )(fptr)
        tmp = __glProgramUniformMatrix2fv_impl
        __glProgramUniformMatrix2fv_impl = (lambda program,location,count,transpose,value: tmp(program,location,count,transpose,__pyglGetAsConstVoidPointer(value)))
        global glProgramUniformMatrix2fv
        glProgramUniformMatrix2fv =__glProgramUniformMatrix2fv_impl
    return __glProgramUniformMatrix2fv_impl(program,location,count,transpose,value)

__glProgramUniformMatrix2x3dv_impl = None
def glProgramUniformMatrix2x3dv ( program:int,location:int,count:int,transpose:bool,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glProgramUniformMatrix2x3dv_impl
    if not __glProgramUniformMatrix2x3dv_impl:
        fptr = __pyglGetFuncAddress('glProgramUniformMatrix2x3dv')
        if not fptr:
            raise RuntimeError('The function glProgramUniformMatrix2x3dv is not available (maybe GL has not been initialized yet?)')
        __glProgramUniformMatrix2x3dv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_char,c_void_p )(fptr)
        tmp = __glProgramUniformMatrix2x3dv_impl
        __glProgramUniformMatrix2x3dv_impl = (lambda program,location,count,transpose,value: tmp(program,location,count,transpose,__pyglGetAsConstVoidPointer(value)))
        global glProgramUniformMatrix2x3dv
        glProgramUniformMatrix2x3dv =__glProgramUniformMatrix2x3dv_impl
    return __glProgramUniformMatrix2x3dv_impl(program,location,count,transpose,value)

__glProgramUniformMatrix2x3fv_impl = None
def glProgramUniformMatrix2x3fv ( program:int,location:int,count:int,transpose:bool,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glProgramUniformMatrix2x3fv_impl
    if not __glProgramUniformMatrix2x3fv_impl:
        fptr = __pyglGetFuncAddress('glProgramUniformMatrix2x3fv')
        if not fptr:
            raise RuntimeError('The function glProgramUniformMatrix2x3fv is not available (maybe GL has not been initialized yet?)')
        __glProgramUniformMatrix2x3fv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_char,c_void_p )(fptr)
        tmp = __glProgramUniformMatrix2x3fv_impl
        __glProgramUniformMatrix2x3fv_impl = (lambda program,location,count,transpose,value: tmp(program,location,count,transpose,__pyglGetAsConstVoidPointer(value)))
        global glProgramUniformMatrix2x3fv
        glProgramUniformMatrix2x3fv =__glProgramUniformMatrix2x3fv_impl
    return __glProgramUniformMatrix2x3fv_impl(program,location,count,transpose,value)

__glProgramUniformMatrix2x4dv_impl = None
def glProgramUniformMatrix2x4dv ( program:int,location:int,count:int,transpose:bool,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glProgramUniformMatrix2x4dv_impl
    if not __glProgramUniformMatrix2x4dv_impl:
        fptr = __pyglGetFuncAddress('glProgramUniformMatrix2x4dv')
        if not fptr:
            raise RuntimeError('The function glProgramUniformMatrix2x4dv is not available (maybe GL has not been initialized yet?)')
        __glProgramUniformMatrix2x4dv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_char,c_void_p )(fptr)
        tmp = __glProgramUniformMatrix2x4dv_impl
        __glProgramUniformMatrix2x4dv_impl = (lambda program,location,count,transpose,value: tmp(program,location,count,transpose,__pyglGetAsConstVoidPointer(value)))
        global glProgramUniformMatrix2x4dv
        glProgramUniformMatrix2x4dv =__glProgramUniformMatrix2x4dv_impl
    return __glProgramUniformMatrix2x4dv_impl(program,location,count,transpose,value)

__glProgramUniformMatrix2x4fv_impl = None
def glProgramUniformMatrix2x4fv ( program:int,location:int,count:int,transpose:bool,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glProgramUniformMatrix2x4fv_impl
    if not __glProgramUniformMatrix2x4fv_impl:
        fptr = __pyglGetFuncAddress('glProgramUniformMatrix2x4fv')
        if not fptr:
            raise RuntimeError('The function glProgramUniformMatrix2x4fv is not available (maybe GL has not been initialized yet?)')
        __glProgramUniformMatrix2x4fv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_char,c_void_p )(fptr)
        tmp = __glProgramUniformMatrix2x4fv_impl
        __glProgramUniformMatrix2x4fv_impl = (lambda program,location,count,transpose,value: tmp(program,location,count,transpose,__pyglGetAsConstVoidPointer(value)))
        global glProgramUniformMatrix2x4fv
        glProgramUniformMatrix2x4fv =__glProgramUniformMatrix2x4fv_impl
    return __glProgramUniformMatrix2x4fv_impl(program,location,count,transpose,value)

__glProgramUniformMatrix3dv_impl = None
def glProgramUniformMatrix3dv ( program:int,location:int,count:int,transpose:bool,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glProgramUniformMatrix3dv_impl
    if not __glProgramUniformMatrix3dv_impl:
        fptr = __pyglGetFuncAddress('glProgramUniformMatrix3dv')
        if not fptr:
            raise RuntimeError('The function glProgramUniformMatrix3dv is not available (maybe GL has not been initialized yet?)')
        __glProgramUniformMatrix3dv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_char,c_void_p )(fptr)
        tmp = __glProgramUniformMatrix3dv_impl
        __glProgramUniformMatrix3dv_impl = (lambda program,location,count,transpose,value: tmp(program,location,count,transpose,__pyglGetAsConstVoidPointer(value)))
        global glProgramUniformMatrix3dv
        glProgramUniformMatrix3dv =__glProgramUniformMatrix3dv_impl
    return __glProgramUniformMatrix3dv_impl(program,location,count,transpose,value)

__glProgramUniformMatrix3fv_impl = None
def glProgramUniformMatrix3fv ( program:int,location:int,count:int,transpose:bool,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glProgramUniformMatrix3fv_impl
    if not __glProgramUniformMatrix3fv_impl:
        fptr = __pyglGetFuncAddress('glProgramUniformMatrix3fv')
        if not fptr:
            raise RuntimeError('The function glProgramUniformMatrix3fv is not available (maybe GL has not been initialized yet?)')
        __glProgramUniformMatrix3fv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_char,c_void_p )(fptr)
        tmp = __glProgramUniformMatrix3fv_impl
        __glProgramUniformMatrix3fv_impl = (lambda program,location,count,transpose,value: tmp(program,location,count,transpose,__pyglGetAsConstVoidPointer(value)))
        global glProgramUniformMatrix3fv
        glProgramUniformMatrix3fv =__glProgramUniformMatrix3fv_impl
    return __glProgramUniformMatrix3fv_impl(program,location,count,transpose,value)

__glProgramUniformMatrix3x2dv_impl = None
def glProgramUniformMatrix3x2dv ( program:int,location:int,count:int,transpose:bool,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glProgramUniformMatrix3x2dv_impl
    if not __glProgramUniformMatrix3x2dv_impl:
        fptr = __pyglGetFuncAddress('glProgramUniformMatrix3x2dv')
        if not fptr:
            raise RuntimeError('The function glProgramUniformMatrix3x2dv is not available (maybe GL has not been initialized yet?)')
        __glProgramUniformMatrix3x2dv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_char,c_void_p )(fptr)
        tmp = __glProgramUniformMatrix3x2dv_impl
        __glProgramUniformMatrix3x2dv_impl = (lambda program,location,count,transpose,value: tmp(program,location,count,transpose,__pyglGetAsConstVoidPointer(value)))
        global glProgramUniformMatrix3x2dv
        glProgramUniformMatrix3x2dv =__glProgramUniformMatrix3x2dv_impl
    return __glProgramUniformMatrix3x2dv_impl(program,location,count,transpose,value)

__glProgramUniformMatrix3x2fv_impl = None
def glProgramUniformMatrix3x2fv ( program:int,location:int,count:int,transpose:bool,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glProgramUniformMatrix3x2fv_impl
    if not __glProgramUniformMatrix3x2fv_impl:
        fptr = __pyglGetFuncAddress('glProgramUniformMatrix3x2fv')
        if not fptr:
            raise RuntimeError('The function glProgramUniformMatrix3x2fv is not available (maybe GL has not been initialized yet?)')
        __glProgramUniformMatrix3x2fv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_char,c_void_p )(fptr)
        tmp = __glProgramUniformMatrix3x2fv_impl
        __glProgramUniformMatrix3x2fv_impl = (lambda program,location,count,transpose,value: tmp(program,location,count,transpose,__pyglGetAsConstVoidPointer(value)))
        global glProgramUniformMatrix3x2fv
        glProgramUniformMatrix3x2fv =__glProgramUniformMatrix3x2fv_impl
    return __glProgramUniformMatrix3x2fv_impl(program,location,count,transpose,value)

__glProgramUniformMatrix3x4dv_impl = None
def glProgramUniformMatrix3x4dv ( program:int,location:int,count:int,transpose:bool,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glProgramUniformMatrix3x4dv_impl
    if not __glProgramUniformMatrix3x4dv_impl:
        fptr = __pyglGetFuncAddress('glProgramUniformMatrix3x4dv')
        if not fptr:
            raise RuntimeError('The function glProgramUniformMatrix3x4dv is not available (maybe GL has not been initialized yet?)')
        __glProgramUniformMatrix3x4dv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_char,c_void_p )(fptr)
        tmp = __glProgramUniformMatrix3x4dv_impl
        __glProgramUniformMatrix3x4dv_impl = (lambda program,location,count,transpose,value: tmp(program,location,count,transpose,__pyglGetAsConstVoidPointer(value)))
        global glProgramUniformMatrix3x4dv
        glProgramUniformMatrix3x4dv =__glProgramUniformMatrix3x4dv_impl
    return __glProgramUniformMatrix3x4dv_impl(program,location,count,transpose,value)

__glProgramUniformMatrix3x4fv_impl = None
def glProgramUniformMatrix3x4fv ( program:int,location:int,count:int,transpose:bool,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glProgramUniformMatrix3x4fv_impl
    if not __glProgramUniformMatrix3x4fv_impl:
        fptr = __pyglGetFuncAddress('glProgramUniformMatrix3x4fv')
        if not fptr:
            raise RuntimeError('The function glProgramUniformMatrix3x4fv is not available (maybe GL has not been initialized yet?)')
        __glProgramUniformMatrix3x4fv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_char,c_void_p )(fptr)
        tmp = __glProgramUniformMatrix3x4fv_impl
        __glProgramUniformMatrix3x4fv_impl = (lambda program,location,count,transpose,value: tmp(program,location,count,transpose,__pyglGetAsConstVoidPointer(value)))
        global glProgramUniformMatrix3x4fv
        glProgramUniformMatrix3x4fv =__glProgramUniformMatrix3x4fv_impl
    return __glProgramUniformMatrix3x4fv_impl(program,location,count,transpose,value)

__glProgramUniformMatrix4dv_impl = None
def glProgramUniformMatrix4dv ( program:int,location:int,count:int,transpose:bool,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glProgramUniformMatrix4dv_impl
    if not __glProgramUniformMatrix4dv_impl:
        fptr = __pyglGetFuncAddress('glProgramUniformMatrix4dv')
        if not fptr:
            raise RuntimeError('The function glProgramUniformMatrix4dv is not available (maybe GL has not been initialized yet?)')
        __glProgramUniformMatrix4dv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_char,c_void_p )(fptr)
        tmp = __glProgramUniformMatrix4dv_impl
        __glProgramUniformMatrix4dv_impl = (lambda program,location,count,transpose,value: tmp(program,location,count,transpose,__pyglGetAsConstVoidPointer(value)))
        global glProgramUniformMatrix4dv
        glProgramUniformMatrix4dv =__glProgramUniformMatrix4dv_impl
    return __glProgramUniformMatrix4dv_impl(program,location,count,transpose,value)

__glProgramUniformMatrix4fv_impl = None
def glProgramUniformMatrix4fv ( program:int,location:int,count:int,transpose:bool,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glProgramUniformMatrix4fv_impl
    if not __glProgramUniformMatrix4fv_impl:
        fptr = __pyglGetFuncAddress('glProgramUniformMatrix4fv')
        if not fptr:
            raise RuntimeError('The function glProgramUniformMatrix4fv is not available (maybe GL has not been initialized yet?)')
        __glProgramUniformMatrix4fv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_char,c_void_p )(fptr)
        tmp = __glProgramUniformMatrix4fv_impl
        __glProgramUniformMatrix4fv_impl = (lambda program,location,count,transpose,value: tmp(program,location,count,transpose,__pyglGetAsConstVoidPointer(value)))
        global glProgramUniformMatrix4fv
        glProgramUniformMatrix4fv =__glProgramUniformMatrix4fv_impl
    return __glProgramUniformMatrix4fv_impl(program,location,count,transpose,value)

__glProgramUniformMatrix4x2dv_impl = None
def glProgramUniformMatrix4x2dv ( program:int,location:int,count:int,transpose:bool,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glProgramUniformMatrix4x2dv_impl
    if not __glProgramUniformMatrix4x2dv_impl:
        fptr = __pyglGetFuncAddress('glProgramUniformMatrix4x2dv')
        if not fptr:
            raise RuntimeError('The function glProgramUniformMatrix4x2dv is not available (maybe GL has not been initialized yet?)')
        __glProgramUniformMatrix4x2dv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_char,c_void_p )(fptr)
        tmp = __glProgramUniformMatrix4x2dv_impl
        __glProgramUniformMatrix4x2dv_impl = (lambda program,location,count,transpose,value: tmp(program,location,count,transpose,__pyglGetAsConstVoidPointer(value)))
        global glProgramUniformMatrix4x2dv
        glProgramUniformMatrix4x2dv =__glProgramUniformMatrix4x2dv_impl
    return __glProgramUniformMatrix4x2dv_impl(program,location,count,transpose,value)

__glProgramUniformMatrix4x2fv_impl = None
def glProgramUniformMatrix4x2fv ( program:int,location:int,count:int,transpose:bool,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glProgramUniformMatrix4x2fv_impl
    if not __glProgramUniformMatrix4x2fv_impl:
        fptr = __pyglGetFuncAddress('glProgramUniformMatrix4x2fv')
        if not fptr:
            raise RuntimeError('The function glProgramUniformMatrix4x2fv is not available (maybe GL has not been initialized yet?)')
        __glProgramUniformMatrix4x2fv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_char,c_void_p )(fptr)
        tmp = __glProgramUniformMatrix4x2fv_impl
        __glProgramUniformMatrix4x2fv_impl = (lambda program,location,count,transpose,value: tmp(program,location,count,transpose,__pyglGetAsConstVoidPointer(value)))
        global glProgramUniformMatrix4x2fv
        glProgramUniformMatrix4x2fv =__glProgramUniformMatrix4x2fv_impl
    return __glProgramUniformMatrix4x2fv_impl(program,location,count,transpose,value)

__glProgramUniformMatrix4x3dv_impl = None
def glProgramUniformMatrix4x3dv ( program:int,location:int,count:int,transpose:bool,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glProgramUniformMatrix4x3dv_impl
    if not __glProgramUniformMatrix4x3dv_impl:
        fptr = __pyglGetFuncAddress('glProgramUniformMatrix4x3dv')
        if not fptr:
            raise RuntimeError('The function glProgramUniformMatrix4x3dv is not available (maybe GL has not been initialized yet?)')
        __glProgramUniformMatrix4x3dv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_char,c_void_p )(fptr)
        tmp = __glProgramUniformMatrix4x3dv_impl
        __glProgramUniformMatrix4x3dv_impl = (lambda program,location,count,transpose,value: tmp(program,location,count,transpose,__pyglGetAsConstVoidPointer(value)))
        global glProgramUniformMatrix4x3dv
        glProgramUniformMatrix4x3dv =__glProgramUniformMatrix4x3dv_impl
    return __glProgramUniformMatrix4x3dv_impl(program,location,count,transpose,value)

__glProgramUniformMatrix4x3fv_impl = None
def glProgramUniformMatrix4x3fv ( program:int,location:int,count:int,transpose:bool,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glProgramUniformMatrix4x3fv_impl
    if not __glProgramUniformMatrix4x3fv_impl:
        fptr = __pyglGetFuncAddress('glProgramUniformMatrix4x3fv')
        if not fptr:
            raise RuntimeError('The function glProgramUniformMatrix4x3fv is not available (maybe GL has not been initialized yet?)')
        __glProgramUniformMatrix4x3fv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_char,c_void_p )(fptr)
        tmp = __glProgramUniformMatrix4x3fv_impl
        __glProgramUniformMatrix4x3fv_impl = (lambda program,location,count,transpose,value: tmp(program,location,count,transpose,__pyglGetAsConstVoidPointer(value)))
        global glProgramUniformMatrix4x3fv
        glProgramUniformMatrix4x3fv =__glProgramUniformMatrix4x3fv_impl
    return __glProgramUniformMatrix4x3fv_impl(program,location,count,transpose,value)

__glProvokingVertex_impl = None
def glProvokingVertex ( mode:int ) -> None :
    global __glProvokingVertex_impl
    if not __glProvokingVertex_impl:
        fptr = __pyglGetFuncAddress('glProvokingVertex')
        if not fptr:
            raise RuntimeError('The function glProvokingVertex is not available (maybe GL has not been initialized yet?)')
        __glProvokingVertex_impl = __PYGL_FUNC_TYPE( None,c_uint )(fptr)
        global glProvokingVertex
        glProvokingVertex =__glProvokingVertex_impl
    return __glProvokingVertex_impl(mode)

__glPushDebugGroup_impl = None
def glPushDebugGroup ( source:int,id:int,length:int,message:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glPushDebugGroup_impl
    if not __glPushDebugGroup_impl:
        fptr = __pyglGetFuncAddress('glPushDebugGroup')
        if not fptr:
            raise RuntimeError('The function glPushDebugGroup is not available (maybe GL has not been initialized yet?)')
        __glPushDebugGroup_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_int,c_void_p )(fptr)
        tmp = __glPushDebugGroup_impl
        __glPushDebugGroup_impl = (lambda source,id,length,message: tmp(source,id,length,c_char_p(message.encode())))
        global glPushDebugGroup
        glPushDebugGroup =__glPushDebugGroup_impl
    return __glPushDebugGroup_impl(source,id,length,message)

__glQueryCounter_impl = None
def glQueryCounter ( id:int,target:int ) -> None :
    global __glQueryCounter_impl
    if not __glQueryCounter_impl:
        fptr = __pyglGetFuncAddress('glQueryCounter')
        if not fptr:
            raise RuntimeError('The function glQueryCounter is not available (maybe GL has not been initialized yet?)')
        __glQueryCounter_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint )(fptr)
        global glQueryCounter
        glQueryCounter =__glQueryCounter_impl
    return __glQueryCounter_impl(id,target)

__glReadBuffer_impl = None
def glReadBuffer ( src:int ) -> None :
    global __glReadBuffer_impl
    if not __glReadBuffer_impl:
        fptr = __pyglGetFuncAddress('glReadBuffer')
        if not fptr:
            raise RuntimeError('The function glReadBuffer is not available (maybe GL has not been initialized yet?)')
        __glReadBuffer_impl = __PYGL_FUNC_TYPE( None,c_uint )(fptr)
        global glReadBuffer
        glReadBuffer =__glReadBuffer_impl
    return __glReadBuffer_impl(src)

__glReadPixels_impl = None
def glReadPixels ( x:int,y:int,width:int,height:int,format:int,type:int,pixels:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glReadPixels_impl
    if not __glReadPixels_impl:
        fptr = __pyglGetFuncAddress('glReadPixels')
        if not fptr:
            raise RuntimeError('The function glReadPixels is not available (maybe GL has not been initialized yet?)')
        __glReadPixels_impl = __PYGL_FUNC_TYPE( None,c_int,c_int,c_int,c_int,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glReadPixels_impl
        __glReadPixels_impl = (lambda x,y,width,height,format,type,pixels: tmp(x,y,width,height,format,type,(c_uint8*len(pixels)).from_buffer(pixels)))
        global glReadPixels
        glReadPixels =__glReadPixels_impl
    return __glReadPixels_impl(x,y,width,height,format,type,pixels)

__glReadnPixels_impl = None
def glReadnPixels ( x:int,y:int,width:int,height:int,format:int,type:int,bufSize:int,data:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glReadnPixels_impl
    if not __glReadnPixels_impl:
        fptr = __pyglGetFuncAddress('glReadnPixels')
        if not fptr:
            raise RuntimeError('The function glReadnPixels is not available (maybe GL has not been initialized yet?)')
        __glReadnPixels_impl = __PYGL_FUNC_TYPE( None,c_int,c_int,c_int,c_int,c_uint,c_uint,c_int,c_void_p )(fptr)
        tmp = __glReadnPixels_impl
        __glReadnPixels_impl = (lambda x,y,width,height,format,type,bufSize,data: tmp(x,y,width,height,format,type,bufSize,(c_uint8*len(data)).from_buffer(data)))
        global glReadnPixels
        glReadnPixels =__glReadnPixels_impl
    return __glReadnPixels_impl(x,y,width,height,format,type,bufSize,data)

__glReleaseShaderCompiler_impl = None
def glReleaseShaderCompiler (  ) -> None :
    global __glReleaseShaderCompiler_impl
    if not __glReleaseShaderCompiler_impl:
        fptr = __pyglGetFuncAddress('glReleaseShaderCompiler')
        if not fptr:
            raise RuntimeError('The function glReleaseShaderCompiler is not available (maybe GL has not been initialized yet?)')
        __glReleaseShaderCompiler_impl = __PYGL_FUNC_TYPE( None )(fptr)
        global glReleaseShaderCompiler
        glReleaseShaderCompiler =__glReleaseShaderCompiler_impl
    return __glReleaseShaderCompiler_impl()

__glRenderbufferStorage_impl = None
def glRenderbufferStorage ( target:int,internalformat:int,width:int,height:int ) -> None :
    global __glRenderbufferStorage_impl
    if not __glRenderbufferStorage_impl:
        fptr = __pyglGetFuncAddress('glRenderbufferStorage')
        if not fptr:
            raise RuntimeError('The function glRenderbufferStorage is not available (maybe GL has not been initialized yet?)')
        __glRenderbufferStorage_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_int,c_int )(fptr)
        global glRenderbufferStorage
        glRenderbufferStorage =__glRenderbufferStorage_impl
    return __glRenderbufferStorage_impl(target,internalformat,width,height)

__glRenderbufferStorageMultisample_impl = None
def glRenderbufferStorageMultisample ( target:int,samples:int,internalformat:int,width:int,height:int ) -> None :
    global __glRenderbufferStorageMultisample_impl
    if not __glRenderbufferStorageMultisample_impl:
        fptr = __pyglGetFuncAddress('glRenderbufferStorageMultisample')
        if not fptr:
            raise RuntimeError('The function glRenderbufferStorageMultisample is not available (maybe GL has not been initialized yet?)')
        __glRenderbufferStorageMultisample_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_uint,c_int,c_int )(fptr)
        global glRenderbufferStorageMultisample
        glRenderbufferStorageMultisample =__glRenderbufferStorageMultisample_impl
    return __glRenderbufferStorageMultisample_impl(target,samples,internalformat,width,height)

__glResumeTransformFeedback_impl = None
def glResumeTransformFeedback (  ) -> None :
    global __glResumeTransformFeedback_impl
    if not __glResumeTransformFeedback_impl:
        fptr = __pyglGetFuncAddress('glResumeTransformFeedback')
        if not fptr:
            raise RuntimeError('The function glResumeTransformFeedback is not available (maybe GL has not been initialized yet?)')
        __glResumeTransformFeedback_impl = __PYGL_FUNC_TYPE( None )(fptr)
        global glResumeTransformFeedback
        glResumeTransformFeedback =__glResumeTransformFeedback_impl
    return __glResumeTransformFeedback_impl()

__glSampleCoverage_impl = None
def glSampleCoverage ( value:float,invert:bool ) -> None :
    global __glSampleCoverage_impl
    if not __glSampleCoverage_impl:
        fptr = __pyglGetFuncAddress('glSampleCoverage')
        if not fptr:
            raise RuntimeError('The function glSampleCoverage is not available (maybe GL has not been initialized yet?)')
        __glSampleCoverage_impl = __PYGL_FUNC_TYPE( None,c_float,c_char )(fptr)
        global glSampleCoverage
        glSampleCoverage =__glSampleCoverage_impl
    return __glSampleCoverage_impl(value,invert)

__glSampleMaski_impl = None
def glSampleMaski ( maskNumber:int,mask:int ) -> None :
    global __glSampleMaski_impl
    if not __glSampleMaski_impl:
        fptr = __pyglGetFuncAddress('glSampleMaski')
        if not fptr:
            raise RuntimeError('The function glSampleMaski is not available (maybe GL has not been initialized yet?)')
        __glSampleMaski_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint )(fptr)
        global glSampleMaski
        glSampleMaski =__glSampleMaski_impl
    return __glSampleMaski_impl(maskNumber,mask)

__glSamplerParameterIiv_impl = None
def glSamplerParameterIiv ( sampler:int,pname:int,param:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glSamplerParameterIiv_impl
    if not __glSamplerParameterIiv_impl:
        fptr = __pyglGetFuncAddress('glSamplerParameterIiv')
        if not fptr:
            raise RuntimeError('The function glSamplerParameterIiv is not available (maybe GL has not been initialized yet?)')
        __glSamplerParameterIiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glSamplerParameterIiv_impl
        __glSamplerParameterIiv_impl = (lambda sampler,pname,param: tmp(sampler,pname,__pyglGetAsConstVoidPointer(param)))
        global glSamplerParameterIiv
        glSamplerParameterIiv =__glSamplerParameterIiv_impl
    return __glSamplerParameterIiv_impl(sampler,pname,param)

__glSamplerParameterIuiv_impl = None
def glSamplerParameterIuiv ( sampler:int,pname:int,param:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glSamplerParameterIuiv_impl
    if not __glSamplerParameterIuiv_impl:
        fptr = __pyglGetFuncAddress('glSamplerParameterIuiv')
        if not fptr:
            raise RuntimeError('The function glSamplerParameterIuiv is not available (maybe GL has not been initialized yet?)')
        __glSamplerParameterIuiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glSamplerParameterIuiv_impl
        __glSamplerParameterIuiv_impl = (lambda sampler,pname,param: tmp(sampler,pname,__pyglGetAsConstVoidPointer(param)))
        global glSamplerParameterIuiv
        glSamplerParameterIuiv =__glSamplerParameterIuiv_impl
    return __glSamplerParameterIuiv_impl(sampler,pname,param)

__glSamplerParameterf_impl = None
def glSamplerParameterf ( sampler:int,pname:int,param:float ) -> None :
    global __glSamplerParameterf_impl
    if not __glSamplerParameterf_impl:
        fptr = __pyglGetFuncAddress('glSamplerParameterf')
        if not fptr:
            raise RuntimeError('The function glSamplerParameterf is not available (maybe GL has not been initialized yet?)')
        __glSamplerParameterf_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_float )(fptr)
        global glSamplerParameterf
        glSamplerParameterf =__glSamplerParameterf_impl
    return __glSamplerParameterf_impl(sampler,pname,param)

__glSamplerParameterfv_impl = None
def glSamplerParameterfv ( sampler:int,pname:int,param:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glSamplerParameterfv_impl
    if not __glSamplerParameterfv_impl:
        fptr = __pyglGetFuncAddress('glSamplerParameterfv')
        if not fptr:
            raise RuntimeError('The function glSamplerParameterfv is not available (maybe GL has not been initialized yet?)')
        __glSamplerParameterfv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glSamplerParameterfv_impl
        __glSamplerParameterfv_impl = (lambda sampler,pname,param: tmp(sampler,pname,__pyglGetAsConstVoidPointer(param)))
        global glSamplerParameterfv
        glSamplerParameterfv =__glSamplerParameterfv_impl
    return __glSamplerParameterfv_impl(sampler,pname,param)

__glSamplerParameteri_impl = None
def glSamplerParameteri ( sampler:int,pname:int,param:int ) -> None :
    global __glSamplerParameteri_impl
    if not __glSamplerParameteri_impl:
        fptr = __pyglGetFuncAddress('glSamplerParameteri')
        if not fptr:
            raise RuntimeError('The function glSamplerParameteri is not available (maybe GL has not been initialized yet?)')
        __glSamplerParameteri_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_int )(fptr)
        global glSamplerParameteri
        glSamplerParameteri =__glSamplerParameteri_impl
    return __glSamplerParameteri_impl(sampler,pname,param)

__glSamplerParameteriv_impl = None
def glSamplerParameteriv ( sampler:int,pname:int,param:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glSamplerParameteriv_impl
    if not __glSamplerParameteriv_impl:
        fptr = __pyglGetFuncAddress('glSamplerParameteriv')
        if not fptr:
            raise RuntimeError('The function glSamplerParameteriv is not available (maybe GL has not been initialized yet?)')
        __glSamplerParameteriv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glSamplerParameteriv_impl
        __glSamplerParameteriv_impl = (lambda sampler,pname,param: tmp(sampler,pname,__pyglGetAsConstVoidPointer(param)))
        global glSamplerParameteriv
        glSamplerParameteriv =__glSamplerParameteriv_impl
    return __glSamplerParameteriv_impl(sampler,pname,param)

__glScissor_impl = None
def glScissor ( x:int,y:int,width:int,height:int ) -> None :
    global __glScissor_impl
    if not __glScissor_impl:
        fptr = __pyglGetFuncAddress('glScissor')
        if not fptr:
            raise RuntimeError('The function glScissor is not available (maybe GL has not been initialized yet?)')
        __glScissor_impl = __PYGL_FUNC_TYPE( None,c_int,c_int,c_int,c_int )(fptr)
        global glScissor
        glScissor =__glScissor_impl
    return __glScissor_impl(x,y,width,height)

__glScissorArrayv_impl = None
def glScissorArrayv ( first:int,count:int,v:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glScissorArrayv_impl
    if not __glScissorArrayv_impl:
        fptr = __pyglGetFuncAddress('glScissorArrayv')
        if not fptr:
            raise RuntimeError('The function glScissorArrayv is not available (maybe GL has not been initialized yet?)')
        __glScissorArrayv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_void_p )(fptr)
        tmp = __glScissorArrayv_impl
        __glScissorArrayv_impl = (lambda first,count,v: tmp(first,count,__pyglGetAsConstVoidPointer(v)))
        global glScissorArrayv
        glScissorArrayv =__glScissorArrayv_impl
    return __glScissorArrayv_impl(first,count,v)

__glScissorIndexed_impl = None
def glScissorIndexed ( index:int,left:int,bottom:int,width:int,height:int ) -> None :
    global __glScissorIndexed_impl
    if not __glScissorIndexed_impl:
        fptr = __pyglGetFuncAddress('glScissorIndexed')
        if not fptr:
            raise RuntimeError('The function glScissorIndexed is not available (maybe GL has not been initialized yet?)')
        __glScissorIndexed_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_int,c_int )(fptr)
        global glScissorIndexed
        glScissorIndexed =__glScissorIndexed_impl
    return __glScissorIndexed_impl(index,left,bottom,width,height)

__glScissorIndexedv_impl = None
def glScissorIndexedv ( index:int,v:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glScissorIndexedv_impl
    if not __glScissorIndexedv_impl:
        fptr = __pyglGetFuncAddress('glScissorIndexedv')
        if not fptr:
            raise RuntimeError('The function glScissorIndexedv is not available (maybe GL has not been initialized yet?)')
        __glScissorIndexedv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p )(fptr)
        tmp = __glScissorIndexedv_impl
        __glScissorIndexedv_impl = (lambda index,v: tmp(index,__pyglGetAsConstVoidPointer(v)))
        global glScissorIndexedv
        glScissorIndexedv =__glScissorIndexedv_impl
    return __glScissorIndexedv_impl(index,v)

__glShaderBinary_impl = None
def glShaderBinary ( count:int,shaders:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],binaryformat:int,binary:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],length:int ) -> None :
    global __glShaderBinary_impl
    if not __glShaderBinary_impl:
        fptr = __pyglGetFuncAddress('glShaderBinary')
        if not fptr:
            raise RuntimeError('The function glShaderBinary is not available (maybe GL has not been initialized yet?)')
        __glShaderBinary_impl = __PYGL_FUNC_TYPE( None,c_int,c_void_p,c_uint,c_void_p,c_int )(fptr)
        tmp = __glShaderBinary_impl
        __glShaderBinary_impl = (lambda count,shaders,binaryformat,binary,length: tmp(count,__pyglGetAsConstVoidPointer(shaders),binaryformat,__pyglGetAsConstVoidPointer(binary),length))
        global glShaderBinary
        glShaderBinary =__glShaderBinary_impl
    return __glShaderBinary_impl(count,shaders,binaryformat,binary,length)

__glShaderStorageBlockBinding_impl = None
def glShaderStorageBlockBinding ( program:int,storageBlockIndex:int,storageBlockBinding:int ) -> None :
    global __glShaderStorageBlockBinding_impl
    if not __glShaderStorageBlockBinding_impl:
        fptr = __pyglGetFuncAddress('glShaderStorageBlockBinding')
        if not fptr:
            raise RuntimeError('The function glShaderStorageBlockBinding is not available (maybe GL has not been initialized yet?)')
        __glShaderStorageBlockBinding_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint )(fptr)
        global glShaderStorageBlockBinding
        glShaderStorageBlockBinding =__glShaderStorageBlockBinding_impl
    return __glShaderStorageBlockBinding_impl(program,storageBlockIndex,storageBlockBinding)

__glStencilFunc_impl = None
def glStencilFunc ( func:int,ref:int,mask:int ) -> None :
    global __glStencilFunc_impl
    if not __glStencilFunc_impl:
        fptr = __pyglGetFuncAddress('glStencilFunc')
        if not fptr:
            raise RuntimeError('The function glStencilFunc is not available (maybe GL has not been initialized yet?)')
        __glStencilFunc_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_uint )(fptr)
        global glStencilFunc
        glStencilFunc =__glStencilFunc_impl
    return __glStencilFunc_impl(func,ref,mask)

__glStencilFuncSeparate_impl = None
def glStencilFuncSeparate ( face:int,func:int,ref:int,mask:int ) -> None :
    global __glStencilFuncSeparate_impl
    if not __glStencilFuncSeparate_impl:
        fptr = __pyglGetFuncAddress('glStencilFuncSeparate')
        if not fptr:
            raise RuntimeError('The function glStencilFuncSeparate is not available (maybe GL has not been initialized yet?)')
        __glStencilFuncSeparate_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_int,c_uint )(fptr)
        global glStencilFuncSeparate
        glStencilFuncSeparate =__glStencilFuncSeparate_impl
    return __glStencilFuncSeparate_impl(face,func,ref,mask)

__glStencilMask_impl = None
def glStencilMask ( mask:int ) -> None :
    global __glStencilMask_impl
    if not __glStencilMask_impl:
        fptr = __pyglGetFuncAddress('glStencilMask')
        if not fptr:
            raise RuntimeError('The function glStencilMask is not available (maybe GL has not been initialized yet?)')
        __glStencilMask_impl = __PYGL_FUNC_TYPE( None,c_uint )(fptr)
        global glStencilMask
        glStencilMask =__glStencilMask_impl
    return __glStencilMask_impl(mask)

__glStencilMaskSeparate_impl = None
def glStencilMaskSeparate ( face:int,mask:int ) -> None :
    global __glStencilMaskSeparate_impl
    if not __glStencilMaskSeparate_impl:
        fptr = __pyglGetFuncAddress('glStencilMaskSeparate')
        if not fptr:
            raise RuntimeError('The function glStencilMaskSeparate is not available (maybe GL has not been initialized yet?)')
        __glStencilMaskSeparate_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint )(fptr)
        global glStencilMaskSeparate
        glStencilMaskSeparate =__glStencilMaskSeparate_impl
    return __glStencilMaskSeparate_impl(face,mask)

__glStencilOp_impl = None
def glStencilOp ( fail:int,zfail:int,zpass:int ) -> None :
    global __glStencilOp_impl
    if not __glStencilOp_impl:
        fptr = __pyglGetFuncAddress('glStencilOp')
        if not fptr:
            raise RuntimeError('The function glStencilOp is not available (maybe GL has not been initialized yet?)')
        __glStencilOp_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint )(fptr)
        global glStencilOp
        glStencilOp =__glStencilOp_impl
    return __glStencilOp_impl(fail,zfail,zpass)

__glStencilOpSeparate_impl = None
def glStencilOpSeparate ( face:int,sfail:int,dpfail:int,dppass:int ) -> None :
    global __glStencilOpSeparate_impl
    if not __glStencilOpSeparate_impl:
        fptr = __pyglGetFuncAddress('glStencilOpSeparate')
        if not fptr:
            raise RuntimeError('The function glStencilOpSeparate is not available (maybe GL has not been initialized yet?)')
        __glStencilOpSeparate_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint,c_uint )(fptr)
        global glStencilOpSeparate
        glStencilOpSeparate =__glStencilOpSeparate_impl
    return __glStencilOpSeparate_impl(face,sfail,dpfail,dppass)

__glTexBuffer_impl = None
def glTexBuffer ( target:int,internalformat:int,buffer:int ) -> None :
    global __glTexBuffer_impl
    if not __glTexBuffer_impl:
        fptr = __pyglGetFuncAddress('glTexBuffer')
        if not fptr:
            raise RuntimeError('The function glTexBuffer is not available (maybe GL has not been initialized yet?)')
        __glTexBuffer_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint )(fptr)
        global glTexBuffer
        glTexBuffer =__glTexBuffer_impl
    return __glTexBuffer_impl(target,internalformat,buffer)

__glTexBufferRange_impl = None
def glTexBufferRange ( target:int,internalformat:int,buffer:int,offset:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],size:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glTexBufferRange_impl
    if not __glTexBufferRange_impl:
        fptr = __pyglGetFuncAddress('glTexBufferRange')
        if not fptr:
            raise RuntimeError('The function glTexBufferRange is not available (maybe GL has not been initialized yet?)')
        __glTexBufferRange_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint,c_size_t,c_void_p )(fptr)
        global glTexBufferRange
        glTexBufferRange =__glTexBufferRange_impl
    return __glTexBufferRange_impl(target,internalformat,buffer,offset,size)

__glTexImage1D_impl = None
def glTexImage1D ( target:int,level:int,internalformat:int,width:int,border:int,format:int,type:int,pixels:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glTexImage1D_impl
    if not __glTexImage1D_impl:
        fptr = __pyglGetFuncAddress('glTexImage1D')
        if not fptr:
            raise RuntimeError('The function glTexImage1D is not available (maybe GL has not been initialized yet?)')
        __glTexImage1D_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_int,c_int,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glTexImage1D_impl
        __glTexImage1D_impl = (lambda target,level,internalformat,width,border,format,type,pixels: tmp(target,level,internalformat,width,border,format,type,__pyglGetAsConstVoidPointer(pixels)))
    for _f in __universal_hooks:
        _f("glTexImage1D",glTexImage1D,target,level,internalformat,width,border,format,type,pixels)
    if 'glTexImage1D' in __hooks:
        for _f in __hooks['glTexImage1D']:
            _f("glTexImage1D",glTexImage1D,target,level,internalformat,width,border,format,type,pixels)
    rv = __glTexImage1D_impl(target,level,internalformat,width,border,format,type,pixels)
    if 'glTexImage1D' in __posthooks:
        for _f in __posthooks['glTexImage1D']:
            _f(rv,"glTexImage1D",glTexImage1D,target,level,internalformat,width,border,format,type,pixels)
    for _f in __universal_posthooks:
        _f(rv,"glTexImage1D",glTexImage1D,target,level,internalformat,width,border,format,type,pixels)
    return rv

__glTexImage2D_impl = None
def glTexImage2D ( target:int,level:int,internalformat:int,width:int,height:int,border:int,format:int,type:int,pixels:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glTexImage2D_impl
    if not __glTexImage2D_impl:
        fptr = __pyglGetFuncAddress('glTexImage2D')
        if not fptr:
            raise RuntimeError('The function glTexImage2D is not available (maybe GL has not been initialized yet?)')
        __glTexImage2D_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_int,c_int,c_int,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glTexImage2D_impl
        __glTexImage2D_impl = (lambda target,level,internalformat,width,height,border,format,type,pixels: tmp(target,level,internalformat,width,height,border,format,type,__pyglGetAsConstVoidPointer(pixels)))
    for _f in __universal_hooks:
        _f("glTexImage2D",glTexImage2D,target,level,internalformat,width,height,border,format,type,pixels)
    if 'glTexImage2D' in __hooks:
        for _f in __hooks['glTexImage2D']:
            _f("glTexImage2D",glTexImage2D,target,level,internalformat,width,height,border,format,type,pixels)
    rv = __glTexImage2D_impl(target,level,internalformat,width,height,border,format,type,pixels)
    if 'glTexImage2D' in __posthooks:
        for _f in __posthooks['glTexImage2D']:
            _f(rv,"glTexImage2D",glTexImage2D,target,level,internalformat,width,height,border,format,type,pixels)
    for _f in __universal_posthooks:
        _f(rv,"glTexImage2D",glTexImage2D,target,level,internalformat,width,height,border,format,type,pixels)
    return rv

__glTexImage3D_impl = None
def glTexImage3D ( target:int,level:int,internalformat:int,width:int,height:int,depth:int,border:int,format:int,type:int,pixels:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glTexImage3D_impl
    if not __glTexImage3D_impl:
        fptr = __pyglGetFuncAddress('glTexImage3D')
        if not fptr:
            raise RuntimeError('The function glTexImage3D is not available (maybe GL has not been initialized yet?)')
        __glTexImage3D_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_int,c_int,c_int,c_int,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glTexImage3D_impl
        __glTexImage3D_impl = (lambda target,level,internalformat,width,height,depth,border,format,type,pixels: tmp(target,level,internalformat,width,height,depth,border,format,type,__pyglGetAsConstVoidPointer(pixels)))
    for _f in __universal_hooks:
        _f("glTexImage3D",glTexImage3D,target,level,internalformat,width,height,depth,border,format,type,pixels)
    if 'glTexImage3D' in __hooks:
        for _f in __hooks['glTexImage3D']:
            _f("glTexImage3D",glTexImage3D,target,level,internalformat,width,height,depth,border,format,type,pixels)
    rv = __glTexImage3D_impl(target,level,internalformat,width,height,depth,border,format,type,pixels)
    if 'glTexImage3D' in __posthooks:
        for _f in __posthooks['glTexImage3D']:
            _f(rv,"glTexImage3D",glTexImage3D,target,level,internalformat,width,height,depth,border,format,type,pixels)
    for _f in __universal_posthooks:
        _f(rv,"glTexImage3D",glTexImage3D,target,level,internalformat,width,height,depth,border,format,type,pixels)
    return rv

__glTexParameterIiv_impl = None
def glTexParameterIiv ( target:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glTexParameterIiv_impl
    if not __glTexParameterIiv_impl:
        fptr = __pyglGetFuncAddress('glTexParameterIiv')
        if not fptr:
            raise RuntimeError('The function glTexParameterIiv is not available (maybe GL has not been initialized yet?)')
        __glTexParameterIiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glTexParameterIiv_impl
        __glTexParameterIiv_impl = (lambda target,pname,params: tmp(target,pname,__pyglGetAsConstVoidPointer(params)))
        global glTexParameterIiv
        glTexParameterIiv =__glTexParameterIiv_impl
    return __glTexParameterIiv_impl(target,pname,params)

__glTexParameterIuiv_impl = None
def glTexParameterIuiv ( target:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glTexParameterIuiv_impl
    if not __glTexParameterIuiv_impl:
        fptr = __pyglGetFuncAddress('glTexParameterIuiv')
        if not fptr:
            raise RuntimeError('The function glTexParameterIuiv is not available (maybe GL has not been initialized yet?)')
        __glTexParameterIuiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glTexParameterIuiv_impl
        __glTexParameterIuiv_impl = (lambda target,pname,params: tmp(target,pname,__pyglGetAsConstVoidPointer(params)))
        global glTexParameterIuiv
        glTexParameterIuiv =__glTexParameterIuiv_impl
    return __glTexParameterIuiv_impl(target,pname,params)

__glTexParameterf_impl = None
def glTexParameterf ( target:int,pname:int,param:float ) -> None :
    global __glTexParameterf_impl
    if not __glTexParameterf_impl:
        fptr = __pyglGetFuncAddress('glTexParameterf')
        if not fptr:
            raise RuntimeError('The function glTexParameterf is not available (maybe GL has not been initialized yet?)')
        __glTexParameterf_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_float )(fptr)
        global glTexParameterf
        glTexParameterf =__glTexParameterf_impl
    return __glTexParameterf_impl(target,pname,param)

__glTexParameterfv_impl = None
def glTexParameterfv ( target:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glTexParameterfv_impl
    if not __glTexParameterfv_impl:
        fptr = __pyglGetFuncAddress('glTexParameterfv')
        if not fptr:
            raise RuntimeError('The function glTexParameterfv is not available (maybe GL has not been initialized yet?)')
        __glTexParameterfv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glTexParameterfv_impl
        __glTexParameterfv_impl = (lambda target,pname,params: tmp(target,pname,__pyglGetAsConstVoidPointer(params)))
        global glTexParameterfv
        glTexParameterfv =__glTexParameterfv_impl
    return __glTexParameterfv_impl(target,pname,params)

__glTexParameteri_impl = None
def glTexParameteri ( target:int,pname:int,param:int ) -> None :
    global __glTexParameteri_impl
    if not __glTexParameteri_impl:
        fptr = __pyglGetFuncAddress('glTexParameteri')
        if not fptr:
            raise RuntimeError('The function glTexParameteri is not available (maybe GL has not been initialized yet?)')
        __glTexParameteri_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_int )(fptr)
        global glTexParameteri
        glTexParameteri =__glTexParameteri_impl
    return __glTexParameteri_impl(target,pname,param)

__glTexParameteriv_impl = None
def glTexParameteriv ( target:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glTexParameteriv_impl
    if not __glTexParameteriv_impl:
        fptr = __pyglGetFuncAddress('glTexParameteriv')
        if not fptr:
            raise RuntimeError('The function glTexParameteriv is not available (maybe GL has not been initialized yet?)')
        __glTexParameteriv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glTexParameteriv_impl
        __glTexParameteriv_impl = (lambda target,pname,params: tmp(target,pname,__pyglGetAsConstVoidPointer(params)))
        global glTexParameteriv
        glTexParameteriv =__glTexParameteriv_impl
    return __glTexParameteriv_impl(target,pname,params)

__glTexStorage1D_impl = None
def glTexStorage1D ( target:int,levels:int,internalformat:int,width:int ) -> None :
    global __glTexStorage1D_impl
    if not __glTexStorage1D_impl:
        fptr = __pyglGetFuncAddress('glTexStorage1D')
        if not fptr:
            raise RuntimeError('The function glTexStorage1D is not available (maybe GL has not been initialized yet?)')
        __glTexStorage1D_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_uint,c_int )(fptr)
        global glTexStorage1D
        glTexStorage1D =__glTexStorage1D_impl
    return __glTexStorage1D_impl(target,levels,internalformat,width)

__glTexStorage2D_impl = None
def glTexStorage2D ( target:int,levels:int,internalformat:int,width:int,height:int ) -> None :
    global __glTexStorage2D_impl
    if not __glTexStorage2D_impl:
        fptr = __pyglGetFuncAddress('glTexStorage2D')
        if not fptr:
            raise RuntimeError('The function glTexStorage2D is not available (maybe GL has not been initialized yet?)')
        __glTexStorage2D_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_uint,c_int,c_int )(fptr)
        global glTexStorage2D
        glTexStorage2D =__glTexStorage2D_impl
    return __glTexStorage2D_impl(target,levels,internalformat,width,height)

__glTexStorage3D_impl = None
def glTexStorage3D ( target:int,levels:int,internalformat:int,width:int,height:int,depth:int ) -> None :
    global __glTexStorage3D_impl
    if not __glTexStorage3D_impl:
        fptr = __pyglGetFuncAddress('glTexStorage3D')
        if not fptr:
            raise RuntimeError('The function glTexStorage3D is not available (maybe GL has not been initialized yet?)')
        __glTexStorage3D_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_uint,c_int,c_int,c_int )(fptr)
        global glTexStorage3D
        glTexStorage3D =__glTexStorage3D_impl
    return __glTexStorage3D_impl(target,levels,internalformat,width,height,depth)

__glTexSubImage1D_impl = None
def glTexSubImage1D ( target:int,level:int,xoffset:int,width:int,format:int,type:int,pixels:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glTexSubImage1D_impl
    if not __glTexSubImage1D_impl:
        fptr = __pyglGetFuncAddress('glTexSubImage1D')
        if not fptr:
            raise RuntimeError('The function glTexSubImage1D is not available (maybe GL has not been initialized yet?)')
        __glTexSubImage1D_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_int,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glTexSubImage1D_impl
        __glTexSubImage1D_impl = (lambda target,level,xoffset,width,format,type,pixels: tmp(target,level,xoffset,width,format,type,__pyglGetAsConstVoidPointer(pixels)))
        global glTexSubImage1D
        glTexSubImage1D =__glTexSubImage1D_impl
    return __glTexSubImage1D_impl(target,level,xoffset,width,format,type,pixels)

__glTexSubImage2D_impl = None
def glTexSubImage2D ( target:int,level:int,xoffset:int,yoffset:int,width:int,height:int,format:int,type:int,pixels:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glTexSubImage2D_impl
    if not __glTexSubImage2D_impl:
        fptr = __pyglGetFuncAddress('glTexSubImage2D')
        if not fptr:
            raise RuntimeError('The function glTexSubImage2D is not available (maybe GL has not been initialized yet?)')
        __glTexSubImage2D_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_int,c_int,c_int,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glTexSubImage2D_impl
        __glTexSubImage2D_impl = (lambda target,level,xoffset,yoffset,width,height,format,type,pixels: tmp(target,level,xoffset,yoffset,width,height,format,type,__pyglGetAsConstVoidPointer(pixels)))
        global glTexSubImage2D
        glTexSubImage2D =__glTexSubImage2D_impl
    return __glTexSubImage2D_impl(target,level,xoffset,yoffset,width,height,format,type,pixels)

__glTexSubImage3D_impl = None
def glTexSubImage3D ( target:int,level:int,xoffset:int,yoffset:int,zoffset:int,width:int,height:int,depth:int,format:int,type:int,pixels:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glTexSubImage3D_impl
    if not __glTexSubImage3D_impl:
        fptr = __pyglGetFuncAddress('glTexSubImage3D')
        if not fptr:
            raise RuntimeError('The function glTexSubImage3D is not available (maybe GL has not been initialized yet?)')
        __glTexSubImage3D_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_int,c_int,c_int,c_int,c_int,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glTexSubImage3D_impl
        __glTexSubImage3D_impl = (lambda target,level,xoffset,yoffset,zoffset,width,height,depth,format,type,pixels: tmp(target,level,xoffset,yoffset,zoffset,width,height,depth,format,type,__pyglGetAsConstVoidPointer(pixels)))
        global glTexSubImage3D
        glTexSubImage3D =__glTexSubImage3D_impl
    return __glTexSubImage3D_impl(target,level,xoffset,yoffset,zoffset,width,height,depth,format,type,pixels)

__glTextureBarrier_impl = None
def glTextureBarrier (  ) -> None :
    global __glTextureBarrier_impl
    if not __glTextureBarrier_impl:
        fptr = __pyglGetFuncAddress('glTextureBarrier')
        if not fptr:
            raise RuntimeError('The function glTextureBarrier is not available (maybe GL has not been initialized yet?)')
        __glTextureBarrier_impl = __PYGL_FUNC_TYPE( None )(fptr)
        global glTextureBarrier
        glTextureBarrier =__glTextureBarrier_impl
    return __glTextureBarrier_impl()

__glTextureBuffer_impl = None
def glTextureBuffer ( texture:int,internalformat:int,buffer:int ) -> None :
    global __glTextureBuffer_impl
    if not __glTextureBuffer_impl:
        fptr = __pyglGetFuncAddress('glTextureBuffer')
        if not fptr:
            raise RuntimeError('The function glTextureBuffer is not available (maybe GL has not been initialized yet?)')
        __glTextureBuffer_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint )(fptr)
        global glTextureBuffer
        glTextureBuffer =__glTextureBuffer_impl
    return __glTextureBuffer_impl(texture,internalformat,buffer)

__glTextureBufferRange_impl = None
def glTextureBufferRange ( texture:int,internalformat:int,buffer:int,offset:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],size:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glTextureBufferRange_impl
    if not __glTextureBufferRange_impl:
        fptr = __pyglGetFuncAddress('glTextureBufferRange')
        if not fptr:
            raise RuntimeError('The function glTextureBufferRange is not available (maybe GL has not been initialized yet?)')
        __glTextureBufferRange_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint,c_size_t,c_void_p )(fptr)
        global glTextureBufferRange
        glTextureBufferRange =__glTextureBufferRange_impl
    return __glTextureBufferRange_impl(texture,internalformat,buffer,offset,size)

__glTextureParameterIiv_impl = None
def glTextureParameterIiv ( texture:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glTextureParameterIiv_impl
    if not __glTextureParameterIiv_impl:
        fptr = __pyglGetFuncAddress('glTextureParameterIiv')
        if not fptr:
            raise RuntimeError('The function glTextureParameterIiv is not available (maybe GL has not been initialized yet?)')
        __glTextureParameterIiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glTextureParameterIiv_impl
        __glTextureParameterIiv_impl = (lambda texture,pname,params: tmp(texture,pname,__pyglGetAsConstVoidPointer(params)))
        global glTextureParameterIiv
        glTextureParameterIiv =__glTextureParameterIiv_impl
    return __glTextureParameterIiv_impl(texture,pname,params)

__glTextureParameterIuiv_impl = None
def glTextureParameterIuiv ( texture:int,pname:int,params:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glTextureParameterIuiv_impl
    if not __glTextureParameterIuiv_impl:
        fptr = __pyglGetFuncAddress('glTextureParameterIuiv')
        if not fptr:
            raise RuntimeError('The function glTextureParameterIuiv is not available (maybe GL has not been initialized yet?)')
        __glTextureParameterIuiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glTextureParameterIuiv_impl
        __glTextureParameterIuiv_impl = (lambda texture,pname,params: tmp(texture,pname,__pyglGetAsConstVoidPointer(params)))
        global glTextureParameterIuiv
        glTextureParameterIuiv =__glTextureParameterIuiv_impl
    return __glTextureParameterIuiv_impl(texture,pname,params)

__glTextureParameterf_impl = None
def glTextureParameterf ( texture:int,pname:int,param:float ) -> None :
    global __glTextureParameterf_impl
    if not __glTextureParameterf_impl:
        fptr = __pyglGetFuncAddress('glTextureParameterf')
        if not fptr:
            raise RuntimeError('The function glTextureParameterf is not available (maybe GL has not been initialized yet?)')
        __glTextureParameterf_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_float )(fptr)
        global glTextureParameterf
        glTextureParameterf =__glTextureParameterf_impl
    return __glTextureParameterf_impl(texture,pname,param)

__glTextureParameterfv_impl = None
def glTextureParameterfv ( texture:int,pname:int,param:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glTextureParameterfv_impl
    if not __glTextureParameterfv_impl:
        fptr = __pyglGetFuncAddress('glTextureParameterfv')
        if not fptr:
            raise RuntimeError('The function glTextureParameterfv is not available (maybe GL has not been initialized yet?)')
        __glTextureParameterfv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glTextureParameterfv_impl
        __glTextureParameterfv_impl = (lambda texture,pname,param: tmp(texture,pname,__pyglGetAsConstVoidPointer(param)))
        global glTextureParameterfv
        glTextureParameterfv =__glTextureParameterfv_impl
    return __glTextureParameterfv_impl(texture,pname,param)

__glTextureParameteri_impl = None
def glTextureParameteri ( texture:int,pname:int,param:int ) -> None :
    global __glTextureParameteri_impl
    if not __glTextureParameteri_impl:
        fptr = __pyglGetFuncAddress('glTextureParameteri')
        if not fptr:
            raise RuntimeError('The function glTextureParameteri is not available (maybe GL has not been initialized yet?)')
        __glTextureParameteri_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_int )(fptr)
        global glTextureParameteri
        glTextureParameteri =__glTextureParameteri_impl
    return __glTextureParameteri_impl(texture,pname,param)

__glTextureParameteriv_impl = None
def glTextureParameteriv ( texture:int,pname:int,param:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glTextureParameteriv_impl
    if not __glTextureParameteriv_impl:
        fptr = __pyglGetFuncAddress('glTextureParameteriv')
        if not fptr:
            raise RuntimeError('The function glTextureParameteriv is not available (maybe GL has not been initialized yet?)')
        __glTextureParameteriv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glTextureParameteriv_impl
        __glTextureParameteriv_impl = (lambda texture,pname,param: tmp(texture,pname,__pyglGetAsConstVoidPointer(param)))
        global glTextureParameteriv
        glTextureParameteriv =__glTextureParameteriv_impl
    return __glTextureParameteriv_impl(texture,pname,param)

__glTextureStorage1D_impl = None
def glTextureStorage1D ( texture:int,levels:int,internalformat:int,width:int ) -> None :
    global __glTextureStorage1D_impl
    if not __glTextureStorage1D_impl:
        fptr = __pyglGetFuncAddress('glTextureStorage1D')
        if not fptr:
            raise RuntimeError('The function glTextureStorage1D is not available (maybe GL has not been initialized yet?)')
        __glTextureStorage1D_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_uint,c_int )(fptr)
        global glTextureStorage1D
        glTextureStorage1D =__glTextureStorage1D_impl
    return __glTextureStorage1D_impl(texture,levels,internalformat,width)

__glTextureStorage2D_impl = None
def glTextureStorage2D ( texture:int,levels:int,internalformat:int,width:int,height:int ) -> None :
    global __glTextureStorage2D_impl
    if not __glTextureStorage2D_impl:
        fptr = __pyglGetFuncAddress('glTextureStorage2D')
        if not fptr:
            raise RuntimeError('The function glTextureStorage2D is not available (maybe GL has not been initialized yet?)')
        __glTextureStorage2D_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_uint,c_int,c_int )(fptr)
        global glTextureStorage2D
        glTextureStorage2D =__glTextureStorage2D_impl
    return __glTextureStorage2D_impl(texture,levels,internalformat,width,height)

__glTextureStorage3D_impl = None
def glTextureStorage3D ( texture:int,levels:int,internalformat:int,width:int,height:int,depth:int ) -> None :
    global __glTextureStorage3D_impl
    if not __glTextureStorage3D_impl:
        fptr = __pyglGetFuncAddress('glTextureStorage3D')
        if not fptr:
            raise RuntimeError('The function glTextureStorage3D is not available (maybe GL has not been initialized yet?)')
        __glTextureStorage3D_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_uint,c_int,c_int,c_int )(fptr)
        global glTextureStorage3D
        glTextureStorage3D =__glTextureStorage3D_impl
    return __glTextureStorage3D_impl(texture,levels,internalformat,width,height,depth)

__glTextureSubImage1D_impl = None
def glTextureSubImage1D ( texture:int,level:int,xoffset:int,width:int,format:int,type:int,pixels:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glTextureSubImage1D_impl
    if not __glTextureSubImage1D_impl:
        fptr = __pyglGetFuncAddress('glTextureSubImage1D')
        if not fptr:
            raise RuntimeError('The function glTextureSubImage1D is not available (maybe GL has not been initialized yet?)')
        __glTextureSubImage1D_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_int,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glTextureSubImage1D_impl
        __glTextureSubImage1D_impl = (lambda texture,level,xoffset,width,format,type,pixels: tmp(texture,level,xoffset,width,format,type,__pyglGetAsConstVoidPointer(pixels)))
        global glTextureSubImage1D
        glTextureSubImage1D =__glTextureSubImage1D_impl
    return __glTextureSubImage1D_impl(texture,level,xoffset,width,format,type,pixels)

__glTextureSubImage2D_impl = None
def glTextureSubImage2D ( texture:int,level:int,xoffset:int,yoffset:int,width:int,height:int,format:int,type:int,pixels:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glTextureSubImage2D_impl
    if not __glTextureSubImage2D_impl:
        fptr = __pyglGetFuncAddress('glTextureSubImage2D')
        if not fptr:
            raise RuntimeError('The function glTextureSubImage2D is not available (maybe GL has not been initialized yet?)')
        __glTextureSubImage2D_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_int,c_int,c_int,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glTextureSubImage2D_impl
        __glTextureSubImage2D_impl = (lambda texture,level,xoffset,yoffset,width,height,format,type,pixels: tmp(texture,level,xoffset,yoffset,width,height,format,type,__pyglGetAsConstVoidPointer(pixels)))
        global glTextureSubImage2D
        glTextureSubImage2D =__glTextureSubImage2D_impl
    return __glTextureSubImage2D_impl(texture,level,xoffset,yoffset,width,height,format,type,pixels)

__glTextureSubImage3D_impl = None
def glTextureSubImage3D ( texture:int,level:int,xoffset:int,yoffset:int,zoffset:int,width:int,height:int,depth:int,format:int,type:int,pixels:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glTextureSubImage3D_impl
    if not __glTextureSubImage3D_impl:
        fptr = __pyglGetFuncAddress('glTextureSubImage3D')
        if not fptr:
            raise RuntimeError('The function glTextureSubImage3D is not available (maybe GL has not been initialized yet?)')
        __glTextureSubImage3D_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_int,c_int,c_int,c_int,c_int,c_uint,c_uint,c_void_p )(fptr)
        tmp = __glTextureSubImage3D_impl
        __glTextureSubImage3D_impl = (lambda texture,level,xoffset,yoffset,zoffset,width,height,depth,format,type,pixels: tmp(texture,level,xoffset,yoffset,zoffset,width,height,depth,format,type,__pyglGetAsConstVoidPointer(pixels)))
        global glTextureSubImage3D
        glTextureSubImage3D =__glTextureSubImage3D_impl
    return __glTextureSubImage3D_impl(texture,level,xoffset,yoffset,zoffset,width,height,depth,format,type,pixels)

__glTextureView_impl = None
def glTextureView ( texture:int,target:int,origtexture:int,internalformat:int,minlevel:int,numlevels:int,minlayer:int,numlayers:int ) -> None :
    global __glTextureView_impl
    if not __glTextureView_impl:
        fptr = __pyglGetFuncAddress('glTextureView')
        if not fptr:
            raise RuntimeError('The function glTextureView is not available (maybe GL has not been initialized yet?)')
        __glTextureView_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint,c_uint,c_uint,c_uint,c_uint,c_uint )(fptr)
        global glTextureView
        glTextureView =__glTextureView_impl
    return __glTextureView_impl(texture,target,origtexture,internalformat,minlevel,numlevels,minlayer,numlayers)

__glTransformFeedbackBufferBase_impl = None
def glTransformFeedbackBufferBase ( xfb:int,index:int,buffer:int ) -> None :
    global __glTransformFeedbackBufferBase_impl
    if not __glTransformFeedbackBufferBase_impl:
        fptr = __pyglGetFuncAddress('glTransformFeedbackBufferBase')
        if not fptr:
            raise RuntimeError('The function glTransformFeedbackBufferBase is not available (maybe GL has not been initialized yet?)')
        __glTransformFeedbackBufferBase_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint )(fptr)
        global glTransformFeedbackBufferBase
        glTransformFeedbackBufferBase =__glTransformFeedbackBufferBase_impl
    return __glTransformFeedbackBufferBase_impl(xfb,index,buffer)

__glTransformFeedbackBufferRange_impl = None
def glTransformFeedbackBufferRange ( xfb:int,index:int,buffer:int,offset:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],size:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glTransformFeedbackBufferRange_impl
    if not __glTransformFeedbackBufferRange_impl:
        fptr = __pyglGetFuncAddress('glTransformFeedbackBufferRange')
        if not fptr:
            raise RuntimeError('The function glTransformFeedbackBufferRange is not available (maybe GL has not been initialized yet?)')
        __glTransformFeedbackBufferRange_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint,c_size_t,c_void_p )(fptr)
        global glTransformFeedbackBufferRange
        glTransformFeedbackBufferRange =__glTransformFeedbackBufferRange_impl
    return __glTransformFeedbackBufferRange_impl(xfb,index,buffer,offset,size)

__glTransformFeedbackVaryings_impl = None
def glTransformFeedbackVaryings ( program:int,count:int,varyings:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],bufferMode:int ) -> None :
    global __glTransformFeedbackVaryings_impl
    if not __glTransformFeedbackVaryings_impl:
        fptr = __pyglGetFuncAddress('glTransformFeedbackVaryings')
        if not fptr:
            raise RuntimeError('The function glTransformFeedbackVaryings is not available (maybe GL has not been initialized yet?)')
        __glTransformFeedbackVaryings_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_void_p,c_uint )(fptr)
        tmp = __glTransformFeedbackVaryings_impl
        __glTransformFeedbackVaryings_impl = (lambda program,count,varyings,bufferMode: tmp(program,count,c_char_p(varyings.encode()),bufferMode))
        global glTransformFeedbackVaryings
        glTransformFeedbackVaryings =__glTransformFeedbackVaryings_impl
    return __glTransformFeedbackVaryings_impl(program,count,varyings,bufferMode)

__glUniform1d_impl = None
def glUniform1d ( location:int,x:float ) -> None :
    global __glUniform1d_impl
    if not __glUniform1d_impl:
        fptr = __pyglGetFuncAddress('glUniform1d')
        if not fptr:
            raise RuntimeError('The function glUniform1d is not available (maybe GL has not been initialized yet?)')
        __glUniform1d_impl = __PYGL_FUNC_TYPE( None,c_int,c_double )(fptr)
        global glUniform1d
        glUniform1d =__glUniform1d_impl
    return __glUniform1d_impl(location,x)

__glUniform1dv_impl = None
def glUniform1dv ( location:int,count:int,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glUniform1dv_impl
    if not __glUniform1dv_impl:
        fptr = __pyglGetFuncAddress('glUniform1dv')
        if not fptr:
            raise RuntimeError('The function glUniform1dv is not available (maybe GL has not been initialized yet?)')
        __glUniform1dv_impl = __PYGL_FUNC_TYPE( None,c_int,c_int,c_void_p )(fptr)
        tmp = __glUniform1dv_impl
        __glUniform1dv_impl = (lambda location,count,value: tmp(location,count,__pyglGetAsConstVoidPointer(value)))
        global glUniform1dv
        glUniform1dv =__glUniform1dv_impl
    return __glUniform1dv_impl(location,count,value)

__glUniform1f_impl = None
def glUniform1f ( location:int,v0:float ) -> None :
    global __glUniform1f_impl
    if not __glUniform1f_impl:
        fptr = __pyglGetFuncAddress('glUniform1f')
        if not fptr:
            raise RuntimeError('The function glUniform1f is not available (maybe GL has not been initialized yet?)')
        __glUniform1f_impl = __PYGL_FUNC_TYPE( None,c_int,c_float )(fptr)
        global glUniform1f
        glUniform1f =__glUniform1f_impl
    return __glUniform1f_impl(location,v0)

__glUniform1fv_impl = None
def glUniform1fv ( location:int,count:int,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glUniform1fv_impl
    if not __glUniform1fv_impl:
        fptr = __pyglGetFuncAddress('glUniform1fv')
        if not fptr:
            raise RuntimeError('The function glUniform1fv is not available (maybe GL has not been initialized yet?)')
        __glUniform1fv_impl = __PYGL_FUNC_TYPE( None,c_int,c_int,c_void_p )(fptr)
        tmp = __glUniform1fv_impl
        __glUniform1fv_impl = (lambda location,count,value: tmp(location,count,__pyglGetAsConstVoidPointer(value)))
        global glUniform1fv
        glUniform1fv =__glUniform1fv_impl
    return __glUniform1fv_impl(location,count,value)

__glUniform1i_impl = None
def glUniform1i ( location:int,v0:int ) -> None :
    global __glUniform1i_impl
    if not __glUniform1i_impl:
        fptr = __pyglGetFuncAddress('glUniform1i')
        if not fptr:
            raise RuntimeError('The function glUniform1i is not available (maybe GL has not been initialized yet?)')
        __glUniform1i_impl = __PYGL_FUNC_TYPE( None,c_int,c_int )(fptr)
        global glUniform1i
        glUniform1i =__glUniform1i_impl
    return __glUniform1i_impl(location,v0)

__glUniform1iv_impl = None
def glUniform1iv ( location:int,count:int,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glUniform1iv_impl
    if not __glUniform1iv_impl:
        fptr = __pyglGetFuncAddress('glUniform1iv')
        if not fptr:
            raise RuntimeError('The function glUniform1iv is not available (maybe GL has not been initialized yet?)')
        __glUniform1iv_impl = __PYGL_FUNC_TYPE( None,c_int,c_int,c_void_p )(fptr)
        tmp = __glUniform1iv_impl
        __glUniform1iv_impl = (lambda location,count,value: tmp(location,count,__pyglGetAsConstVoidPointer(value)))
        global glUniform1iv
        glUniform1iv =__glUniform1iv_impl
    return __glUniform1iv_impl(location,count,value)

__glUniform1ui_impl = None
def glUniform1ui ( location:int,v0:int ) -> None :
    global __glUniform1ui_impl
    if not __glUniform1ui_impl:
        fptr = __pyglGetFuncAddress('glUniform1ui')
        if not fptr:
            raise RuntimeError('The function glUniform1ui is not available (maybe GL has not been initialized yet?)')
        __glUniform1ui_impl = __PYGL_FUNC_TYPE( None,c_int,c_uint )(fptr)
        global glUniform1ui
        glUniform1ui =__glUniform1ui_impl
    return __glUniform1ui_impl(location,v0)

__glUniform1uiv_impl = None
def glUniform1uiv ( location:int,count:int,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glUniform1uiv_impl
    if not __glUniform1uiv_impl:
        fptr = __pyglGetFuncAddress('glUniform1uiv')
        if not fptr:
            raise RuntimeError('The function glUniform1uiv is not available (maybe GL has not been initialized yet?)')
        __glUniform1uiv_impl = __PYGL_FUNC_TYPE( None,c_int,c_int,c_void_p )(fptr)
        tmp = __glUniform1uiv_impl
        __glUniform1uiv_impl = (lambda location,count,value: tmp(location,count,__pyglGetAsConstVoidPointer(value)))
        global glUniform1uiv
        glUniform1uiv =__glUniform1uiv_impl
    return __glUniform1uiv_impl(location,count,value)

__glUniform2d_impl = None
def glUniform2d ( location:int,x:float,y:float ) -> None :
    global __glUniform2d_impl
    if not __glUniform2d_impl:
        fptr = __pyglGetFuncAddress('glUniform2d')
        if not fptr:
            raise RuntimeError('The function glUniform2d is not available (maybe GL has not been initialized yet?)')
        __glUniform2d_impl = __PYGL_FUNC_TYPE( None,c_int,c_double,c_double )(fptr)
        global glUniform2d
        glUniform2d =__glUniform2d_impl
    return __glUniform2d_impl(location,x,y)

__glUniform2dv_impl = None
def glUniform2dv ( location:int,count:int,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glUniform2dv_impl
    if not __glUniform2dv_impl:
        fptr = __pyglGetFuncAddress('glUniform2dv')
        if not fptr:
            raise RuntimeError('The function glUniform2dv is not available (maybe GL has not been initialized yet?)')
        __glUniform2dv_impl = __PYGL_FUNC_TYPE( None,c_int,c_int,c_void_p )(fptr)
        tmp = __glUniform2dv_impl
        __glUniform2dv_impl = (lambda location,count,value: tmp(location,count,__pyglGetAsConstVoidPointer(value)))
        global glUniform2dv
        glUniform2dv =__glUniform2dv_impl
    return __glUniform2dv_impl(location,count,value)

__glUniform2f_impl = None
def glUniform2f ( location:int,v0:float,v1:float ) -> None :
    global __glUniform2f_impl
    if not __glUniform2f_impl:
        fptr = __pyglGetFuncAddress('glUniform2f')
        if not fptr:
            raise RuntimeError('The function glUniform2f is not available (maybe GL has not been initialized yet?)')
        __glUniform2f_impl = __PYGL_FUNC_TYPE( None,c_int,c_float,c_float )(fptr)
        global glUniform2f
        glUniform2f =__glUniform2f_impl
    return __glUniform2f_impl(location,v0,v1)

__glUniform2fv_impl = None
def glUniform2fv ( location:int,count:int,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glUniform2fv_impl
    if not __glUniform2fv_impl:
        fptr = __pyglGetFuncAddress('glUniform2fv')
        if not fptr:
            raise RuntimeError('The function glUniform2fv is not available (maybe GL has not been initialized yet?)')
        __glUniform2fv_impl = __PYGL_FUNC_TYPE( None,c_int,c_int,c_void_p )(fptr)
        tmp = __glUniform2fv_impl
        __glUniform2fv_impl = (lambda location,count,value: tmp(location,count,__pyglGetAsConstVoidPointer(value)))
        global glUniform2fv
        glUniform2fv =__glUniform2fv_impl
    return __glUniform2fv_impl(location,count,value)

__glUniform2i_impl = None
def glUniform2i ( location:int,v0:int,v1:int ) -> None :
    global __glUniform2i_impl
    if not __glUniform2i_impl:
        fptr = __pyglGetFuncAddress('glUniform2i')
        if not fptr:
            raise RuntimeError('The function glUniform2i is not available (maybe GL has not been initialized yet?)')
        __glUniform2i_impl = __PYGL_FUNC_TYPE( None,c_int,c_int,c_int )(fptr)
        global glUniform2i
        glUniform2i =__glUniform2i_impl
    return __glUniform2i_impl(location,v0,v1)

__glUniform2iv_impl = None
def glUniform2iv ( location:int,count:int,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glUniform2iv_impl
    if not __glUniform2iv_impl:
        fptr = __pyglGetFuncAddress('glUniform2iv')
        if not fptr:
            raise RuntimeError('The function glUniform2iv is not available (maybe GL has not been initialized yet?)')
        __glUniform2iv_impl = __PYGL_FUNC_TYPE( None,c_int,c_int,c_void_p )(fptr)
        tmp = __glUniform2iv_impl
        __glUniform2iv_impl = (lambda location,count,value: tmp(location,count,__pyglGetAsConstVoidPointer(value)))
        global glUniform2iv
        glUniform2iv =__glUniform2iv_impl
    return __glUniform2iv_impl(location,count,value)

__glUniform2ui_impl = None
def glUniform2ui ( location:int,v0:int,v1:int ) -> None :
    global __glUniform2ui_impl
    if not __glUniform2ui_impl:
        fptr = __pyglGetFuncAddress('glUniform2ui')
        if not fptr:
            raise RuntimeError('The function glUniform2ui is not available (maybe GL has not been initialized yet?)')
        __glUniform2ui_impl = __PYGL_FUNC_TYPE( None,c_int,c_uint,c_uint )(fptr)
        global glUniform2ui
        glUniform2ui =__glUniform2ui_impl
    return __glUniform2ui_impl(location,v0,v1)

__glUniform2uiv_impl = None
def glUniform2uiv ( location:int,count:int,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glUniform2uiv_impl
    if not __glUniform2uiv_impl:
        fptr = __pyglGetFuncAddress('glUniform2uiv')
        if not fptr:
            raise RuntimeError('The function glUniform2uiv is not available (maybe GL has not been initialized yet?)')
        __glUniform2uiv_impl = __PYGL_FUNC_TYPE( None,c_int,c_int,c_void_p )(fptr)
        tmp = __glUniform2uiv_impl
        __glUniform2uiv_impl = (lambda location,count,value: tmp(location,count,__pyglGetAsConstVoidPointer(value)))
        global glUniform2uiv
        glUniform2uiv =__glUniform2uiv_impl
    return __glUniform2uiv_impl(location,count,value)

__glUniform3d_impl = None
def glUniform3d ( location:int,x:float,y:float,z:float ) -> None :
    global __glUniform3d_impl
    if not __glUniform3d_impl:
        fptr = __pyglGetFuncAddress('glUniform3d')
        if not fptr:
            raise RuntimeError('The function glUniform3d is not available (maybe GL has not been initialized yet?)')
        __glUniform3d_impl = __PYGL_FUNC_TYPE( None,c_int,c_double,c_double,c_double )(fptr)
        global glUniform3d
        glUniform3d =__glUniform3d_impl
    return __glUniform3d_impl(location,x,y,z)

__glUniform3dv_impl = None
def glUniform3dv ( location:int,count:int,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glUniform3dv_impl
    if not __glUniform3dv_impl:
        fptr = __pyglGetFuncAddress('glUniform3dv')
        if not fptr:
            raise RuntimeError('The function glUniform3dv is not available (maybe GL has not been initialized yet?)')
        __glUniform3dv_impl = __PYGL_FUNC_TYPE( None,c_int,c_int,c_void_p )(fptr)
        tmp = __glUniform3dv_impl
        __glUniform3dv_impl = (lambda location,count,value: tmp(location,count,__pyglGetAsConstVoidPointer(value)))
        global glUniform3dv
        glUniform3dv =__glUniform3dv_impl
    return __glUniform3dv_impl(location,count,value)

__glUniform3f_impl = None
def glUniform3f ( location:int,v0:float,v1:float,v2:float ) -> None :
    global __glUniform3f_impl
    if not __glUniform3f_impl:
        fptr = __pyglGetFuncAddress('glUniform3f')
        if not fptr:
            raise RuntimeError('The function glUniform3f is not available (maybe GL has not been initialized yet?)')
        __glUniform3f_impl = __PYGL_FUNC_TYPE( None,c_int,c_float,c_float,c_float )(fptr)
        global glUniform3f
        glUniform3f =__glUniform3f_impl
    return __glUniform3f_impl(location,v0,v1,v2)

__glUniform3fv_impl = None
def glUniform3fv ( location:int,count:int,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glUniform3fv_impl
    if not __glUniform3fv_impl:
        fptr = __pyglGetFuncAddress('glUniform3fv')
        if not fptr:
            raise RuntimeError('The function glUniform3fv is not available (maybe GL has not been initialized yet?)')
        __glUniform3fv_impl = __PYGL_FUNC_TYPE( None,c_int,c_int,c_void_p )(fptr)
        tmp = __glUniform3fv_impl
        __glUniform3fv_impl = (lambda location,count,value: tmp(location,count,__pyglGetAsConstVoidPointer(value)))
        global glUniform3fv
        glUniform3fv =__glUniform3fv_impl
    return __glUniform3fv_impl(location,count,value)

__glUniform3i_impl = None
def glUniform3i ( location:int,v0:int,v1:int,v2:int ) -> None :
    global __glUniform3i_impl
    if not __glUniform3i_impl:
        fptr = __pyglGetFuncAddress('glUniform3i')
        if not fptr:
            raise RuntimeError('The function glUniform3i is not available (maybe GL has not been initialized yet?)')
        __glUniform3i_impl = __PYGL_FUNC_TYPE( None,c_int,c_int,c_int,c_int )(fptr)
        global glUniform3i
        glUniform3i =__glUniform3i_impl
    return __glUniform3i_impl(location,v0,v1,v2)

__glUniform3iv_impl = None
def glUniform3iv ( location:int,count:int,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glUniform3iv_impl
    if not __glUniform3iv_impl:
        fptr = __pyglGetFuncAddress('glUniform3iv')
        if not fptr:
            raise RuntimeError('The function glUniform3iv is not available (maybe GL has not been initialized yet?)')
        __glUniform3iv_impl = __PYGL_FUNC_TYPE( None,c_int,c_int,c_void_p )(fptr)
        tmp = __glUniform3iv_impl
        __glUniform3iv_impl = (lambda location,count,value: tmp(location,count,__pyglGetAsConstVoidPointer(value)))
        global glUniform3iv
        glUniform3iv =__glUniform3iv_impl
    return __glUniform3iv_impl(location,count,value)

__glUniform3ui_impl = None
def glUniform3ui ( location:int,v0:int,v1:int,v2:int ) -> None :
    global __glUniform3ui_impl
    if not __glUniform3ui_impl:
        fptr = __pyglGetFuncAddress('glUniform3ui')
        if not fptr:
            raise RuntimeError('The function glUniform3ui is not available (maybe GL has not been initialized yet?)')
        __glUniform3ui_impl = __PYGL_FUNC_TYPE( None,c_int,c_uint,c_uint,c_uint )(fptr)
        global glUniform3ui
        glUniform3ui =__glUniform3ui_impl
    return __glUniform3ui_impl(location,v0,v1,v2)

__glUniform3uiv_impl = None
def glUniform3uiv ( location:int,count:int,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glUniform3uiv_impl
    if not __glUniform3uiv_impl:
        fptr = __pyglGetFuncAddress('glUniform3uiv')
        if not fptr:
            raise RuntimeError('The function glUniform3uiv is not available (maybe GL has not been initialized yet?)')
        __glUniform3uiv_impl = __PYGL_FUNC_TYPE( None,c_int,c_int,c_void_p )(fptr)
        tmp = __glUniform3uiv_impl
        __glUniform3uiv_impl = (lambda location,count,value: tmp(location,count,__pyglGetAsConstVoidPointer(value)))
        global glUniform3uiv
        glUniform3uiv =__glUniform3uiv_impl
    return __glUniform3uiv_impl(location,count,value)

__glUniform4d_impl = None
def glUniform4d ( location:int,x:float,y:float,z:float,w:float ) -> None :
    global __glUniform4d_impl
    if not __glUniform4d_impl:
        fptr = __pyglGetFuncAddress('glUniform4d')
        if not fptr:
            raise RuntimeError('The function glUniform4d is not available (maybe GL has not been initialized yet?)')
        __glUniform4d_impl = __PYGL_FUNC_TYPE( None,c_int,c_double,c_double,c_double,c_double )(fptr)
        global glUniform4d
        glUniform4d =__glUniform4d_impl
    return __glUniform4d_impl(location,x,y,z,w)

__glUniform4dv_impl = None
def glUniform4dv ( location:int,count:int,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glUniform4dv_impl
    if not __glUniform4dv_impl:
        fptr = __pyglGetFuncAddress('glUniform4dv')
        if not fptr:
            raise RuntimeError('The function glUniform4dv is not available (maybe GL has not been initialized yet?)')
        __glUniform4dv_impl = __PYGL_FUNC_TYPE( None,c_int,c_int,c_void_p )(fptr)
        tmp = __glUniform4dv_impl
        __glUniform4dv_impl = (lambda location,count,value: tmp(location,count,__pyglGetAsConstVoidPointer(value)))
        global glUniform4dv
        glUniform4dv =__glUniform4dv_impl
    return __glUniform4dv_impl(location,count,value)

__glUniform4f_impl = None
def glUniform4f ( location:int,v0:float,v1:float,v2:float,v3:float ) -> None :
    global __glUniform4f_impl
    if not __glUniform4f_impl:
        fptr = __pyglGetFuncAddress('glUniform4f')
        if not fptr:
            raise RuntimeError('The function glUniform4f is not available (maybe GL has not been initialized yet?)')
        __glUniform4f_impl = __PYGL_FUNC_TYPE( None,c_int,c_float,c_float,c_float,c_float )(fptr)
        global glUniform4f
        glUniform4f =__glUniform4f_impl
    return __glUniform4f_impl(location,v0,v1,v2,v3)

__glUniform4fv_impl = None
def glUniform4fv ( location:int,count:int,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glUniform4fv_impl
    if not __glUniform4fv_impl:
        fptr = __pyglGetFuncAddress('glUniform4fv')
        if not fptr:
            raise RuntimeError('The function glUniform4fv is not available (maybe GL has not been initialized yet?)')
        __glUniform4fv_impl = __PYGL_FUNC_TYPE( None,c_int,c_int,c_void_p )(fptr)
        tmp = __glUniform4fv_impl
        __glUniform4fv_impl = (lambda location,count,value: tmp(location,count,__pyglGetAsConstVoidPointer(value)))
        global glUniform4fv
        glUniform4fv =__glUniform4fv_impl
    return __glUniform4fv_impl(location,count,value)

__glUniform4i_impl = None
def glUniform4i ( location:int,v0:int,v1:int,v2:int,v3:int ) -> None :
    global __glUniform4i_impl
    if not __glUniform4i_impl:
        fptr = __pyglGetFuncAddress('glUniform4i')
        if not fptr:
            raise RuntimeError('The function glUniform4i is not available (maybe GL has not been initialized yet?)')
        __glUniform4i_impl = __PYGL_FUNC_TYPE( None,c_int,c_int,c_int,c_int,c_int )(fptr)
        global glUniform4i
        glUniform4i =__glUniform4i_impl
    return __glUniform4i_impl(location,v0,v1,v2,v3)

__glUniform4iv_impl = None
def glUniform4iv ( location:int,count:int,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glUniform4iv_impl
    if not __glUniform4iv_impl:
        fptr = __pyglGetFuncAddress('glUniform4iv')
        if not fptr:
            raise RuntimeError('The function glUniform4iv is not available (maybe GL has not been initialized yet?)')
        __glUniform4iv_impl = __PYGL_FUNC_TYPE( None,c_int,c_int,c_void_p )(fptr)
        tmp = __glUniform4iv_impl
        __glUniform4iv_impl = (lambda location,count,value: tmp(location,count,__pyglGetAsConstVoidPointer(value)))
        global glUniform4iv
        glUniform4iv =__glUniform4iv_impl
    return __glUniform4iv_impl(location,count,value)

__glUniform4ui_impl = None
def glUniform4ui ( location:int,v0:int,v1:int,v2:int,v3:int ) -> None :
    global __glUniform4ui_impl
    if not __glUniform4ui_impl:
        fptr = __pyglGetFuncAddress('glUniform4ui')
        if not fptr:
            raise RuntimeError('The function glUniform4ui is not available (maybe GL has not been initialized yet?)')
        __glUniform4ui_impl = __PYGL_FUNC_TYPE( None,c_int,c_uint,c_uint,c_uint,c_uint )(fptr)
        global glUniform4ui
        glUniform4ui =__glUniform4ui_impl
    return __glUniform4ui_impl(location,v0,v1,v2,v3)

__glUniform4uiv_impl = None
def glUniform4uiv ( location:int,count:int,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glUniform4uiv_impl
    if not __glUniform4uiv_impl:
        fptr = __pyglGetFuncAddress('glUniform4uiv')
        if not fptr:
            raise RuntimeError('The function glUniform4uiv is not available (maybe GL has not been initialized yet?)')
        __glUniform4uiv_impl = __PYGL_FUNC_TYPE( None,c_int,c_int,c_void_p )(fptr)
        tmp = __glUniform4uiv_impl
        __glUniform4uiv_impl = (lambda location,count,value: tmp(location,count,__pyglGetAsConstVoidPointer(value)))
        global glUniform4uiv
        glUniform4uiv =__glUniform4uiv_impl
    return __glUniform4uiv_impl(location,count,value)

__glUniformBlockBinding_impl = None
def glUniformBlockBinding ( program:int,uniformBlockIndex:int,uniformBlockBinding:int ) -> None :
    global __glUniformBlockBinding_impl
    if not __glUniformBlockBinding_impl:
        fptr = __pyglGetFuncAddress('glUniformBlockBinding')
        if not fptr:
            raise RuntimeError('The function glUniformBlockBinding is not available (maybe GL has not been initialized yet?)')
        __glUniformBlockBinding_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint )(fptr)
        global glUniformBlockBinding
        glUniformBlockBinding =__glUniformBlockBinding_impl
    return __glUniformBlockBinding_impl(program,uniformBlockIndex,uniformBlockBinding)

__glUniformMatrix2dv_impl = None
def glUniformMatrix2dv ( location:int,count:int,transpose:bool,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glUniformMatrix2dv_impl
    if not __glUniformMatrix2dv_impl:
        fptr = __pyglGetFuncAddress('glUniformMatrix2dv')
        if not fptr:
            raise RuntimeError('The function glUniformMatrix2dv is not available (maybe GL has not been initialized yet?)')
        __glUniformMatrix2dv_impl = __PYGL_FUNC_TYPE( None,c_int,c_int,c_char,c_void_p )(fptr)
        tmp = __glUniformMatrix2dv_impl
        __glUniformMatrix2dv_impl = (lambda location,count,transpose,value: tmp(location,count,transpose,__pyglGetAsConstVoidPointer(value)))
        global glUniformMatrix2dv
        glUniformMatrix2dv =__glUniformMatrix2dv_impl
    return __glUniformMatrix2dv_impl(location,count,transpose,value)

__glUniformMatrix2fv_impl = None
def glUniformMatrix2fv ( location:int,count:int,transpose:bool,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glUniformMatrix2fv_impl
    if not __glUniformMatrix2fv_impl:
        fptr = __pyglGetFuncAddress('glUniformMatrix2fv')
        if not fptr:
            raise RuntimeError('The function glUniformMatrix2fv is not available (maybe GL has not been initialized yet?)')
        __glUniformMatrix2fv_impl = __PYGL_FUNC_TYPE( None,c_int,c_int,c_char,c_void_p )(fptr)
        tmp = __glUniformMatrix2fv_impl
        __glUniformMatrix2fv_impl = (lambda location,count,transpose,value: tmp(location,count,transpose,__pyglGetAsConstVoidPointer(value)))
        global glUniformMatrix2fv
        glUniformMatrix2fv =__glUniformMatrix2fv_impl
    return __glUniformMatrix2fv_impl(location,count,transpose,value)

__glUniformMatrix2x3dv_impl = None
def glUniformMatrix2x3dv ( location:int,count:int,transpose:bool,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glUniformMatrix2x3dv_impl
    if not __glUniformMatrix2x3dv_impl:
        fptr = __pyglGetFuncAddress('glUniformMatrix2x3dv')
        if not fptr:
            raise RuntimeError('The function glUniformMatrix2x3dv is not available (maybe GL has not been initialized yet?)')
        __glUniformMatrix2x3dv_impl = __PYGL_FUNC_TYPE( None,c_int,c_int,c_char,c_void_p )(fptr)
        tmp = __glUniformMatrix2x3dv_impl
        __glUniformMatrix2x3dv_impl = (lambda location,count,transpose,value: tmp(location,count,transpose,__pyglGetAsConstVoidPointer(value)))
        global glUniformMatrix2x3dv
        glUniformMatrix2x3dv =__glUniformMatrix2x3dv_impl
    return __glUniformMatrix2x3dv_impl(location,count,transpose,value)

__glUniformMatrix2x3fv_impl = None
def glUniformMatrix2x3fv ( location:int,count:int,transpose:bool,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glUniformMatrix2x3fv_impl
    if not __glUniformMatrix2x3fv_impl:
        fptr = __pyglGetFuncAddress('glUniformMatrix2x3fv')
        if not fptr:
            raise RuntimeError('The function glUniformMatrix2x3fv is not available (maybe GL has not been initialized yet?)')
        __glUniformMatrix2x3fv_impl = __PYGL_FUNC_TYPE( None,c_int,c_int,c_char,c_void_p )(fptr)
        tmp = __glUniformMatrix2x3fv_impl
        __glUniformMatrix2x3fv_impl = (lambda location,count,transpose,value: tmp(location,count,transpose,__pyglGetAsConstVoidPointer(value)))
        global glUniformMatrix2x3fv
        glUniformMatrix2x3fv =__glUniformMatrix2x3fv_impl
    return __glUniformMatrix2x3fv_impl(location,count,transpose,value)

__glUniformMatrix2x4dv_impl = None
def glUniformMatrix2x4dv ( location:int,count:int,transpose:bool,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glUniformMatrix2x4dv_impl
    if not __glUniformMatrix2x4dv_impl:
        fptr = __pyglGetFuncAddress('glUniformMatrix2x4dv')
        if not fptr:
            raise RuntimeError('The function glUniformMatrix2x4dv is not available (maybe GL has not been initialized yet?)')
        __glUniformMatrix2x4dv_impl = __PYGL_FUNC_TYPE( None,c_int,c_int,c_char,c_void_p )(fptr)
        tmp = __glUniformMatrix2x4dv_impl
        __glUniformMatrix2x4dv_impl = (lambda location,count,transpose,value: tmp(location,count,transpose,__pyglGetAsConstVoidPointer(value)))
        global glUniformMatrix2x4dv
        glUniformMatrix2x4dv =__glUniformMatrix2x4dv_impl
    return __glUniformMatrix2x4dv_impl(location,count,transpose,value)

__glUniformMatrix2x4fv_impl = None
def glUniformMatrix2x4fv ( location:int,count:int,transpose:bool,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glUniformMatrix2x4fv_impl
    if not __glUniformMatrix2x4fv_impl:
        fptr = __pyglGetFuncAddress('glUniformMatrix2x4fv')
        if not fptr:
            raise RuntimeError('The function glUniformMatrix2x4fv is not available (maybe GL has not been initialized yet?)')
        __glUniformMatrix2x4fv_impl = __PYGL_FUNC_TYPE( None,c_int,c_int,c_char,c_void_p )(fptr)
        tmp = __glUniformMatrix2x4fv_impl
        __glUniformMatrix2x4fv_impl = (lambda location,count,transpose,value: tmp(location,count,transpose,__pyglGetAsConstVoidPointer(value)))
        global glUniformMatrix2x4fv
        glUniformMatrix2x4fv =__glUniformMatrix2x4fv_impl
    return __glUniformMatrix2x4fv_impl(location,count,transpose,value)

__glUniformMatrix3dv_impl = None
def glUniformMatrix3dv ( location:int,count:int,transpose:bool,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glUniformMatrix3dv_impl
    if not __glUniformMatrix3dv_impl:
        fptr = __pyglGetFuncAddress('glUniformMatrix3dv')
        if not fptr:
            raise RuntimeError('The function glUniformMatrix3dv is not available (maybe GL has not been initialized yet?)')
        __glUniformMatrix3dv_impl = __PYGL_FUNC_TYPE( None,c_int,c_int,c_char,c_void_p )(fptr)
        tmp = __glUniformMatrix3dv_impl
        __glUniformMatrix3dv_impl = (lambda location,count,transpose,value: tmp(location,count,transpose,__pyglGetAsConstVoidPointer(value)))
        global glUniformMatrix3dv
        glUniformMatrix3dv =__glUniformMatrix3dv_impl
    return __glUniformMatrix3dv_impl(location,count,transpose,value)

__glUniformMatrix3fv_impl = None
def glUniformMatrix3fv ( location:int,count:int,transpose:bool,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glUniformMatrix3fv_impl
    if not __glUniformMatrix3fv_impl:
        fptr = __pyglGetFuncAddress('glUniformMatrix3fv')
        if not fptr:
            raise RuntimeError('The function glUniformMatrix3fv is not available (maybe GL has not been initialized yet?)')
        __glUniformMatrix3fv_impl = __PYGL_FUNC_TYPE( None,c_int,c_int,c_char,c_void_p )(fptr)
        tmp = __glUniformMatrix3fv_impl
        __glUniformMatrix3fv_impl = (lambda location,count,transpose,value: tmp(location,count,transpose,__pyglGetAsConstVoidPointer(value)))
        global glUniformMatrix3fv
        glUniformMatrix3fv =__glUniformMatrix3fv_impl
    return __glUniformMatrix3fv_impl(location,count,transpose,value)

__glUniformMatrix3x2dv_impl = None
def glUniformMatrix3x2dv ( location:int,count:int,transpose:bool,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glUniformMatrix3x2dv_impl
    if not __glUniformMatrix3x2dv_impl:
        fptr = __pyglGetFuncAddress('glUniformMatrix3x2dv')
        if not fptr:
            raise RuntimeError('The function glUniformMatrix3x2dv is not available (maybe GL has not been initialized yet?)')
        __glUniformMatrix3x2dv_impl = __PYGL_FUNC_TYPE( None,c_int,c_int,c_char,c_void_p )(fptr)
        tmp = __glUniformMatrix3x2dv_impl
        __glUniformMatrix3x2dv_impl = (lambda location,count,transpose,value: tmp(location,count,transpose,__pyglGetAsConstVoidPointer(value)))
        global glUniformMatrix3x2dv
        glUniformMatrix3x2dv =__glUniformMatrix3x2dv_impl
    return __glUniformMatrix3x2dv_impl(location,count,transpose,value)

__glUniformMatrix3x2fv_impl = None
def glUniformMatrix3x2fv ( location:int,count:int,transpose:bool,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glUniformMatrix3x2fv_impl
    if not __glUniformMatrix3x2fv_impl:
        fptr = __pyglGetFuncAddress('glUniformMatrix3x2fv')
        if not fptr:
            raise RuntimeError('The function glUniformMatrix3x2fv is not available (maybe GL has not been initialized yet?)')
        __glUniformMatrix3x2fv_impl = __PYGL_FUNC_TYPE( None,c_int,c_int,c_char,c_void_p )(fptr)
        tmp = __glUniformMatrix3x2fv_impl
        __glUniformMatrix3x2fv_impl = (lambda location,count,transpose,value: tmp(location,count,transpose,__pyglGetAsConstVoidPointer(value)))
        global glUniformMatrix3x2fv
        glUniformMatrix3x2fv =__glUniformMatrix3x2fv_impl
    return __glUniformMatrix3x2fv_impl(location,count,transpose,value)

__glUniformMatrix3x4dv_impl = None
def glUniformMatrix3x4dv ( location:int,count:int,transpose:bool,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glUniformMatrix3x4dv_impl
    if not __glUniformMatrix3x4dv_impl:
        fptr = __pyglGetFuncAddress('glUniformMatrix3x4dv')
        if not fptr:
            raise RuntimeError('The function glUniformMatrix3x4dv is not available (maybe GL has not been initialized yet?)')
        __glUniformMatrix3x4dv_impl = __PYGL_FUNC_TYPE( None,c_int,c_int,c_char,c_void_p )(fptr)
        tmp = __glUniformMatrix3x4dv_impl
        __glUniformMatrix3x4dv_impl = (lambda location,count,transpose,value: tmp(location,count,transpose,__pyglGetAsConstVoidPointer(value)))
        global glUniformMatrix3x4dv
        glUniformMatrix3x4dv =__glUniformMatrix3x4dv_impl
    return __glUniformMatrix3x4dv_impl(location,count,transpose,value)

__glUniformMatrix3x4fv_impl = None
def glUniformMatrix3x4fv ( location:int,count:int,transpose:bool,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glUniformMatrix3x4fv_impl
    if not __glUniformMatrix3x4fv_impl:
        fptr = __pyglGetFuncAddress('glUniformMatrix3x4fv')
        if not fptr:
            raise RuntimeError('The function glUniformMatrix3x4fv is not available (maybe GL has not been initialized yet?)')
        __glUniformMatrix3x4fv_impl = __PYGL_FUNC_TYPE( None,c_int,c_int,c_char,c_void_p )(fptr)
        tmp = __glUniformMatrix3x4fv_impl
        __glUniformMatrix3x4fv_impl = (lambda location,count,transpose,value: tmp(location,count,transpose,__pyglGetAsConstVoidPointer(value)))
        global glUniformMatrix3x4fv
        glUniformMatrix3x4fv =__glUniformMatrix3x4fv_impl
    return __glUniformMatrix3x4fv_impl(location,count,transpose,value)

__glUniformMatrix4dv_impl = None
def glUniformMatrix4dv ( location:int,count:int,transpose:bool,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glUniformMatrix4dv_impl
    if not __glUniformMatrix4dv_impl:
        fptr = __pyglGetFuncAddress('glUniformMatrix4dv')
        if not fptr:
            raise RuntimeError('The function glUniformMatrix4dv is not available (maybe GL has not been initialized yet?)')
        __glUniformMatrix4dv_impl = __PYGL_FUNC_TYPE( None,c_int,c_int,c_char,c_void_p )(fptr)
        tmp = __glUniformMatrix4dv_impl
        __glUniformMatrix4dv_impl = (lambda location,count,transpose,value: tmp(location,count,transpose,__pyglGetAsConstVoidPointer(value)))
        global glUniformMatrix4dv
        glUniformMatrix4dv =__glUniformMatrix4dv_impl
    return __glUniformMatrix4dv_impl(location,count,transpose,value)

__glUniformMatrix4fv_impl = None
def glUniformMatrix4fv ( location:int,count:int,transpose:bool,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glUniformMatrix4fv_impl
    if not __glUniformMatrix4fv_impl:
        fptr = __pyglGetFuncAddress('glUniformMatrix4fv')
        if not fptr:
            raise RuntimeError('The function glUniformMatrix4fv is not available (maybe GL has not been initialized yet?)')
        __glUniformMatrix4fv_impl = __PYGL_FUNC_TYPE( None,c_int,c_int,c_char,c_void_p )(fptr)
        tmp = __glUniformMatrix4fv_impl
        __glUniformMatrix4fv_impl = (lambda location,count,transpose,value: tmp(location,count,transpose,__pyglGetAsConstVoidPointer(value)))
        global glUniformMatrix4fv
        glUniformMatrix4fv =__glUniformMatrix4fv_impl
    return __glUniformMatrix4fv_impl(location,count,transpose,value)

__glUniformMatrix4x2dv_impl = None
def glUniformMatrix4x2dv ( location:int,count:int,transpose:bool,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glUniformMatrix4x2dv_impl
    if not __glUniformMatrix4x2dv_impl:
        fptr = __pyglGetFuncAddress('glUniformMatrix4x2dv')
        if not fptr:
            raise RuntimeError('The function glUniformMatrix4x2dv is not available (maybe GL has not been initialized yet?)')
        __glUniformMatrix4x2dv_impl = __PYGL_FUNC_TYPE( None,c_int,c_int,c_char,c_void_p )(fptr)
        tmp = __glUniformMatrix4x2dv_impl
        __glUniformMatrix4x2dv_impl = (lambda location,count,transpose,value: tmp(location,count,transpose,__pyglGetAsConstVoidPointer(value)))
        global glUniformMatrix4x2dv
        glUniformMatrix4x2dv =__glUniformMatrix4x2dv_impl
    return __glUniformMatrix4x2dv_impl(location,count,transpose,value)

__glUniformMatrix4x2fv_impl = None
def glUniformMatrix4x2fv ( location:int,count:int,transpose:bool,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glUniformMatrix4x2fv_impl
    if not __glUniformMatrix4x2fv_impl:
        fptr = __pyglGetFuncAddress('glUniformMatrix4x2fv')
        if not fptr:
            raise RuntimeError('The function glUniformMatrix4x2fv is not available (maybe GL has not been initialized yet?)')
        __glUniformMatrix4x2fv_impl = __PYGL_FUNC_TYPE( None,c_int,c_int,c_char,c_void_p )(fptr)
        tmp = __glUniformMatrix4x2fv_impl
        __glUniformMatrix4x2fv_impl = (lambda location,count,transpose,value: tmp(location,count,transpose,__pyglGetAsConstVoidPointer(value)))
        global glUniformMatrix4x2fv
        glUniformMatrix4x2fv =__glUniformMatrix4x2fv_impl
    return __glUniformMatrix4x2fv_impl(location,count,transpose,value)

__glUniformMatrix4x3dv_impl = None
def glUniformMatrix4x3dv ( location:int,count:int,transpose:bool,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glUniformMatrix4x3dv_impl
    if not __glUniformMatrix4x3dv_impl:
        fptr = __pyglGetFuncAddress('glUniformMatrix4x3dv')
        if not fptr:
            raise RuntimeError('The function glUniformMatrix4x3dv is not available (maybe GL has not been initialized yet?)')
        __glUniformMatrix4x3dv_impl = __PYGL_FUNC_TYPE( None,c_int,c_int,c_char,c_void_p )(fptr)
        tmp = __glUniformMatrix4x3dv_impl
        __glUniformMatrix4x3dv_impl = (lambda location,count,transpose,value: tmp(location,count,transpose,__pyglGetAsConstVoidPointer(value)))
        global glUniformMatrix4x3dv
        glUniformMatrix4x3dv =__glUniformMatrix4x3dv_impl
    return __glUniformMatrix4x3dv_impl(location,count,transpose,value)

__glUniformMatrix4x3fv_impl = None
def glUniformMatrix4x3fv ( location:int,count:int,transpose:bool,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glUniformMatrix4x3fv_impl
    if not __glUniformMatrix4x3fv_impl:
        fptr = __pyglGetFuncAddress('glUniformMatrix4x3fv')
        if not fptr:
            raise RuntimeError('The function glUniformMatrix4x3fv is not available (maybe GL has not been initialized yet?)')
        __glUniformMatrix4x3fv_impl = __PYGL_FUNC_TYPE( None,c_int,c_int,c_char,c_void_p )(fptr)
        tmp = __glUniformMatrix4x3fv_impl
        __glUniformMatrix4x3fv_impl = (lambda location,count,transpose,value: tmp(location,count,transpose,__pyglGetAsConstVoidPointer(value)))
        global glUniformMatrix4x3fv
        glUniformMatrix4x3fv =__glUniformMatrix4x3fv_impl
    return __glUniformMatrix4x3fv_impl(location,count,transpose,value)

__glUniformSubroutinesuiv_impl = None
def glUniformSubroutinesuiv ( shadertype:int,count:int,indices:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glUniformSubroutinesuiv_impl
    if not __glUniformSubroutinesuiv_impl:
        fptr = __pyglGetFuncAddress('glUniformSubroutinesuiv')
        if not fptr:
            raise RuntimeError('The function glUniformSubroutinesuiv is not available (maybe GL has not been initialized yet?)')
        __glUniformSubroutinesuiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_void_p )(fptr)
        tmp = __glUniformSubroutinesuiv_impl
        __glUniformSubroutinesuiv_impl = (lambda shadertype,count,indices: tmp(shadertype,count,__pyglGetAsConstVoidPointer(indices)))
        global glUniformSubroutinesuiv
        glUniformSubroutinesuiv =__glUniformSubroutinesuiv_impl
    return __glUniformSubroutinesuiv_impl(shadertype,count,indices)

__glUnmapBuffer_impl = None
def glUnmapBuffer ( target:int ) -> bool :
    global __glUnmapBuffer_impl
    if not __glUnmapBuffer_impl:
        fptr = __pyglGetFuncAddress('glUnmapBuffer')
        if not fptr:
            raise RuntimeError('The function glUnmapBuffer is not available (maybe GL has not been initialized yet?)')
        __glUnmapBuffer_impl = __PYGL_FUNC_TYPE( c_char,c_uint )(fptr)
        global glUnmapBuffer
        glUnmapBuffer =__glUnmapBuffer_impl
    return __glUnmapBuffer_impl(target)

__glUnmapNamedBuffer_impl = None
def glUnmapNamedBuffer ( buffer:int ) -> bool :
    global __glUnmapNamedBuffer_impl
    if not __glUnmapNamedBuffer_impl:
        fptr = __pyglGetFuncAddress('glUnmapNamedBuffer')
        if not fptr:
            raise RuntimeError('The function glUnmapNamedBuffer is not available (maybe GL has not been initialized yet?)')
        __glUnmapNamedBuffer_impl = __PYGL_FUNC_TYPE( c_char,c_uint )(fptr)
        global glUnmapNamedBuffer
        glUnmapNamedBuffer =__glUnmapNamedBuffer_impl
    return __glUnmapNamedBuffer_impl(buffer)

__glUseProgram_impl = None
def glUseProgram ( program:int ) -> None :
    global __glUseProgram_impl
    if not __glUseProgram_impl:
        fptr = __pyglGetFuncAddress('glUseProgram')
        if not fptr:
            raise RuntimeError('The function glUseProgram is not available (maybe GL has not been initialized yet?)')
        __glUseProgram_impl = __PYGL_FUNC_TYPE( None,c_uint )(fptr)
        global glUseProgram
        glUseProgram =__glUseProgram_impl
    return __glUseProgram_impl(program)

__glUseProgramStages_impl = None
def glUseProgramStages ( pipeline:int,stages:int,program:int ) -> None :
    global __glUseProgramStages_impl
    if not __glUseProgramStages_impl:
        fptr = __pyglGetFuncAddress('glUseProgramStages')
        if not fptr:
            raise RuntimeError('The function glUseProgramStages is not available (maybe GL has not been initialized yet?)')
        __glUseProgramStages_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint )(fptr)
        global glUseProgramStages
        glUseProgramStages =__glUseProgramStages_impl
    return __glUseProgramStages_impl(pipeline,stages,program)

__glValidateProgram_impl = None
def glValidateProgram ( program:int ) -> None :
    global __glValidateProgram_impl
    if not __glValidateProgram_impl:
        fptr = __pyglGetFuncAddress('glValidateProgram')
        if not fptr:
            raise RuntimeError('The function glValidateProgram is not available (maybe GL has not been initialized yet?)')
        __glValidateProgram_impl = __PYGL_FUNC_TYPE( None,c_uint )(fptr)
        global glValidateProgram
        glValidateProgram =__glValidateProgram_impl
    return __glValidateProgram_impl(program)

__glValidateProgramPipeline_impl = None
def glValidateProgramPipeline ( pipeline:int ) -> None :
    global __glValidateProgramPipeline_impl
    if not __glValidateProgramPipeline_impl:
        fptr = __pyglGetFuncAddress('glValidateProgramPipeline')
        if not fptr:
            raise RuntimeError('The function glValidateProgramPipeline is not available (maybe GL has not been initialized yet?)')
        __glValidateProgramPipeline_impl = __PYGL_FUNC_TYPE( None,c_uint )(fptr)
        global glValidateProgramPipeline
        glValidateProgramPipeline =__glValidateProgramPipeline_impl
    return __glValidateProgramPipeline_impl(pipeline)

__glVertexArrayAttribBinding_impl = None
def glVertexArrayAttribBinding ( vaobj:int,attribindex:int,bindingindex:int ) -> None :
    global __glVertexArrayAttribBinding_impl
    if not __glVertexArrayAttribBinding_impl:
        fptr = __pyglGetFuncAddress('glVertexArrayAttribBinding')
        if not fptr:
            raise RuntimeError('The function glVertexArrayAttribBinding is not available (maybe GL has not been initialized yet?)')
        __glVertexArrayAttribBinding_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint )(fptr)
        global glVertexArrayAttribBinding
        glVertexArrayAttribBinding =__glVertexArrayAttribBinding_impl
    return __glVertexArrayAttribBinding_impl(vaobj,attribindex,bindingindex)

__glVertexArrayAttribFormat_impl = None
def glVertexArrayAttribFormat ( vaobj:int,attribindex:int,size:int,type:int,normalized:bool,relativeoffset:int ) -> None :
    global __glVertexArrayAttribFormat_impl
    if not __glVertexArrayAttribFormat_impl:
        fptr = __pyglGetFuncAddress('glVertexArrayAttribFormat')
        if not fptr:
            raise RuntimeError('The function glVertexArrayAttribFormat is not available (maybe GL has not been initialized yet?)')
        __glVertexArrayAttribFormat_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_int,c_uint,c_char,c_uint )(fptr)
        global glVertexArrayAttribFormat
        glVertexArrayAttribFormat =__glVertexArrayAttribFormat_impl
    return __glVertexArrayAttribFormat_impl(vaobj,attribindex,size,type,normalized,relativeoffset)

__glVertexArrayBindingDivisor_impl = None
def glVertexArrayBindingDivisor ( vaobj:int,bindingindex:int,divisor:int ) -> None :
    global __glVertexArrayBindingDivisor_impl
    if not __glVertexArrayBindingDivisor_impl:
        fptr = __pyglGetFuncAddress('glVertexArrayBindingDivisor')
        if not fptr:
            raise RuntimeError('The function glVertexArrayBindingDivisor is not available (maybe GL has not been initialized yet?)')
        __glVertexArrayBindingDivisor_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint )(fptr)
        global glVertexArrayBindingDivisor
        glVertexArrayBindingDivisor =__glVertexArrayBindingDivisor_impl
    return __glVertexArrayBindingDivisor_impl(vaobj,bindingindex,divisor)

__glVertexArrayElementBuffer_impl = None
def glVertexArrayElementBuffer ( vaobj:int,buffer:int ) -> None :
    global __glVertexArrayElementBuffer_impl
    if not __glVertexArrayElementBuffer_impl:
        fptr = __pyglGetFuncAddress('glVertexArrayElementBuffer')
        if not fptr:
            raise RuntimeError('The function glVertexArrayElementBuffer is not available (maybe GL has not been initialized yet?)')
        __glVertexArrayElementBuffer_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint )(fptr)
        global glVertexArrayElementBuffer
        glVertexArrayElementBuffer =__glVertexArrayElementBuffer_impl
    return __glVertexArrayElementBuffer_impl(vaobj,buffer)

__glVertexArrayVertexBuffer_impl = None
def glVertexArrayVertexBuffer ( vaobj:int,bindingindex:int,buffer:int,offset:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],stride:int ) -> None :
    global __glVertexArrayVertexBuffer_impl
    if not __glVertexArrayVertexBuffer_impl:
        fptr = __pyglGetFuncAddress('glVertexArrayVertexBuffer')
        if not fptr:
            raise RuntimeError('The function glVertexArrayVertexBuffer is not available (maybe GL has not been initialized yet?)')
        __glVertexArrayVertexBuffer_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint,c_size_t,c_int )(fptr)
        global glVertexArrayVertexBuffer
        glVertexArrayVertexBuffer =__glVertexArrayVertexBuffer_impl
    return __glVertexArrayVertexBuffer_impl(vaobj,bindingindex,buffer,offset,stride)

__glVertexArrayVertexBuffers_impl = None
def glVertexArrayVertexBuffers ( vaobj:int,first:int,count:int,buffers:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],offsets:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview],strides:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glVertexArrayVertexBuffers_impl
    if not __glVertexArrayVertexBuffers_impl:
        fptr = __pyglGetFuncAddress('glVertexArrayVertexBuffers')
        if not fptr:
            raise RuntimeError('The function glVertexArrayVertexBuffers is not available (maybe GL has not been initialized yet?)')
        __glVertexArrayVertexBuffers_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_int,c_void_p,c_void_p,c_void_p )(fptr)
        tmp = __glVertexArrayVertexBuffers_impl
        __glVertexArrayVertexBuffers_impl = (lambda vaobj,first,count,buffers,offsets,strides: tmp(vaobj,first,count,__pyglGetAsConstVoidPointer(buffers),__pyglGetAsConstVoidPointer(offsets),__pyglGetAsConstVoidPointer(strides)))
        global glVertexArrayVertexBuffers
        glVertexArrayVertexBuffers =__glVertexArrayVertexBuffers_impl
    return __glVertexArrayVertexBuffers_impl(vaobj,first,count,buffers,offsets,strides)

__glVertexAttrib1d_impl = None
def glVertexAttrib1d ( index:int,x:float ) -> None :
    global __glVertexAttrib1d_impl
    if not __glVertexAttrib1d_impl:
        fptr = __pyglGetFuncAddress('glVertexAttrib1d')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib1d is not available (maybe GL has not been initialized yet?)')
        __glVertexAttrib1d_impl = __PYGL_FUNC_TYPE( None,c_uint,c_double )(fptr)
        global glVertexAttrib1d
        glVertexAttrib1d =__glVertexAttrib1d_impl
    return __glVertexAttrib1d_impl(index,x)

__glVertexAttrib1dv_impl = None
def glVertexAttrib1dv ( index:int,v:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glVertexAttrib1dv_impl
    if not __glVertexAttrib1dv_impl:
        fptr = __pyglGetFuncAddress('glVertexAttrib1dv')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib1dv is not available (maybe GL has not been initialized yet?)')
        __glVertexAttrib1dv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p )(fptr)
        tmp = __glVertexAttrib1dv_impl
        __glVertexAttrib1dv_impl = (lambda index,v: tmp(index,__pyglGetAsConstVoidPointer(v)))
        global glVertexAttrib1dv
        glVertexAttrib1dv =__glVertexAttrib1dv_impl
    return __glVertexAttrib1dv_impl(index,v)

__glVertexAttrib1f_impl = None
def glVertexAttrib1f ( index:int,x:float ) -> None :
    global __glVertexAttrib1f_impl
    if not __glVertexAttrib1f_impl:
        fptr = __pyglGetFuncAddress('glVertexAttrib1f')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib1f is not available (maybe GL has not been initialized yet?)')
        __glVertexAttrib1f_impl = __PYGL_FUNC_TYPE( None,c_uint,c_float )(fptr)
        global glVertexAttrib1f
        glVertexAttrib1f =__glVertexAttrib1f_impl
    return __glVertexAttrib1f_impl(index,x)

__glVertexAttrib1fv_impl = None
def glVertexAttrib1fv ( index:int,v:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glVertexAttrib1fv_impl
    if not __glVertexAttrib1fv_impl:
        fptr = __pyglGetFuncAddress('glVertexAttrib1fv')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib1fv is not available (maybe GL has not been initialized yet?)')
        __glVertexAttrib1fv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p )(fptr)
        tmp = __glVertexAttrib1fv_impl
        __glVertexAttrib1fv_impl = (lambda index,v: tmp(index,__pyglGetAsConstVoidPointer(v)))
        global glVertexAttrib1fv
        glVertexAttrib1fv =__glVertexAttrib1fv_impl
    return __glVertexAttrib1fv_impl(index,v)

__glVertexAttrib1s_impl = None
def glVertexAttrib1s ( index:int,x:int ) -> None :
    global __glVertexAttrib1s_impl
    if not __glVertexAttrib1s_impl:
        fptr = __pyglGetFuncAddress('glVertexAttrib1s')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib1s is not available (maybe GL has not been initialized yet?)')
        __glVertexAttrib1s_impl = __PYGL_FUNC_TYPE( None,c_uint,c_short )(fptr)
        global glVertexAttrib1s
        glVertexAttrib1s =__glVertexAttrib1s_impl
    return __glVertexAttrib1s_impl(index,x)

__glVertexAttrib1sv_impl = None
def glVertexAttrib1sv ( index:int,v:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glVertexAttrib1sv_impl
    if not __glVertexAttrib1sv_impl:
        fptr = __pyglGetFuncAddress('glVertexAttrib1sv')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib1sv is not available (maybe GL has not been initialized yet?)')
        __glVertexAttrib1sv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p )(fptr)
        tmp = __glVertexAttrib1sv_impl
        __glVertexAttrib1sv_impl = (lambda index,v: tmp(index,__pyglGetAsConstVoidPointer(v)))
        global glVertexAttrib1sv
        glVertexAttrib1sv =__glVertexAttrib1sv_impl
    return __glVertexAttrib1sv_impl(index,v)

__glVertexAttrib2d_impl = None
def glVertexAttrib2d ( index:int,x:float,y:float ) -> None :
    global __glVertexAttrib2d_impl
    if not __glVertexAttrib2d_impl:
        fptr = __pyglGetFuncAddress('glVertexAttrib2d')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib2d is not available (maybe GL has not been initialized yet?)')
        __glVertexAttrib2d_impl = __PYGL_FUNC_TYPE( None,c_uint,c_double,c_double )(fptr)
        global glVertexAttrib2d
        glVertexAttrib2d =__glVertexAttrib2d_impl
    return __glVertexAttrib2d_impl(index,x,y)

__glVertexAttrib2dv_impl = None
def glVertexAttrib2dv ( index:int,v:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glVertexAttrib2dv_impl
    if not __glVertexAttrib2dv_impl:
        fptr = __pyglGetFuncAddress('glVertexAttrib2dv')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib2dv is not available (maybe GL has not been initialized yet?)')
        __glVertexAttrib2dv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p )(fptr)
        tmp = __glVertexAttrib2dv_impl
        __glVertexAttrib2dv_impl = (lambda index,v: tmp(index,__pyglGetAsConstVoidPointer(v)))
        global glVertexAttrib2dv
        glVertexAttrib2dv =__glVertexAttrib2dv_impl
    return __glVertexAttrib2dv_impl(index,v)

__glVertexAttrib2f_impl = None
def glVertexAttrib2f ( index:int,x:float,y:float ) -> None :
    global __glVertexAttrib2f_impl
    if not __glVertexAttrib2f_impl:
        fptr = __pyglGetFuncAddress('glVertexAttrib2f')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib2f is not available (maybe GL has not been initialized yet?)')
        __glVertexAttrib2f_impl = __PYGL_FUNC_TYPE( None,c_uint,c_float,c_float )(fptr)
        global glVertexAttrib2f
        glVertexAttrib2f =__glVertexAttrib2f_impl
    return __glVertexAttrib2f_impl(index,x,y)

__glVertexAttrib2fv_impl = None
def glVertexAttrib2fv ( index:int,v:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glVertexAttrib2fv_impl
    if not __glVertexAttrib2fv_impl:
        fptr = __pyglGetFuncAddress('glVertexAttrib2fv')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib2fv is not available (maybe GL has not been initialized yet?)')
        __glVertexAttrib2fv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p )(fptr)
        tmp = __glVertexAttrib2fv_impl
        __glVertexAttrib2fv_impl = (lambda index,v: tmp(index,__pyglGetAsConstVoidPointer(v)))
        global glVertexAttrib2fv
        glVertexAttrib2fv =__glVertexAttrib2fv_impl
    return __glVertexAttrib2fv_impl(index,v)

__glVertexAttrib2s_impl = None
def glVertexAttrib2s ( index:int,x:int,y:int ) -> None :
    global __glVertexAttrib2s_impl
    if not __glVertexAttrib2s_impl:
        fptr = __pyglGetFuncAddress('glVertexAttrib2s')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib2s is not available (maybe GL has not been initialized yet?)')
        __glVertexAttrib2s_impl = __PYGL_FUNC_TYPE( None,c_uint,c_short,c_short )(fptr)
        global glVertexAttrib2s
        glVertexAttrib2s =__glVertexAttrib2s_impl
    return __glVertexAttrib2s_impl(index,x,y)

__glVertexAttrib2sv_impl = None
def glVertexAttrib2sv ( index:int,v:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glVertexAttrib2sv_impl
    if not __glVertexAttrib2sv_impl:
        fptr = __pyglGetFuncAddress('glVertexAttrib2sv')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib2sv is not available (maybe GL has not been initialized yet?)')
        __glVertexAttrib2sv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p )(fptr)
        tmp = __glVertexAttrib2sv_impl
        __glVertexAttrib2sv_impl = (lambda index,v: tmp(index,__pyglGetAsConstVoidPointer(v)))
        global glVertexAttrib2sv
        glVertexAttrib2sv =__glVertexAttrib2sv_impl
    return __glVertexAttrib2sv_impl(index,v)

__glVertexAttrib3d_impl = None
def glVertexAttrib3d ( index:int,x:float,y:float,z:float ) -> None :
    global __glVertexAttrib3d_impl
    if not __glVertexAttrib3d_impl:
        fptr = __pyglGetFuncAddress('glVertexAttrib3d')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib3d is not available (maybe GL has not been initialized yet?)')
        __glVertexAttrib3d_impl = __PYGL_FUNC_TYPE( None,c_uint,c_double,c_double,c_double )(fptr)
        global glVertexAttrib3d
        glVertexAttrib3d =__glVertexAttrib3d_impl
    return __glVertexAttrib3d_impl(index,x,y,z)

__glVertexAttrib3dv_impl = None
def glVertexAttrib3dv ( index:int,v:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glVertexAttrib3dv_impl
    if not __glVertexAttrib3dv_impl:
        fptr = __pyglGetFuncAddress('glVertexAttrib3dv')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib3dv is not available (maybe GL has not been initialized yet?)')
        __glVertexAttrib3dv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p )(fptr)
        tmp = __glVertexAttrib3dv_impl
        __glVertexAttrib3dv_impl = (lambda index,v: tmp(index,__pyglGetAsConstVoidPointer(v)))
        global glVertexAttrib3dv
        glVertexAttrib3dv =__glVertexAttrib3dv_impl
    return __glVertexAttrib3dv_impl(index,v)

__glVertexAttrib3f_impl = None
def glVertexAttrib3f ( index:int,x:float,y:float,z:float ) -> None :
    global __glVertexAttrib3f_impl
    if not __glVertexAttrib3f_impl:
        fptr = __pyglGetFuncAddress('glVertexAttrib3f')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib3f is not available (maybe GL has not been initialized yet?)')
        __glVertexAttrib3f_impl = __PYGL_FUNC_TYPE( None,c_uint,c_float,c_float,c_float )(fptr)
        global glVertexAttrib3f
        glVertexAttrib3f =__glVertexAttrib3f_impl
    return __glVertexAttrib3f_impl(index,x,y,z)

__glVertexAttrib3fv_impl = None
def glVertexAttrib3fv ( index:int,v:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glVertexAttrib3fv_impl
    if not __glVertexAttrib3fv_impl:
        fptr = __pyglGetFuncAddress('glVertexAttrib3fv')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib3fv is not available (maybe GL has not been initialized yet?)')
        __glVertexAttrib3fv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p )(fptr)
        tmp = __glVertexAttrib3fv_impl
        __glVertexAttrib3fv_impl = (lambda index,v: tmp(index,__pyglGetAsConstVoidPointer(v)))
        global glVertexAttrib3fv
        glVertexAttrib3fv =__glVertexAttrib3fv_impl
    return __glVertexAttrib3fv_impl(index,v)

__glVertexAttrib3s_impl = None
def glVertexAttrib3s ( index:int,x:int,y:int,z:int ) -> None :
    global __glVertexAttrib3s_impl
    if not __glVertexAttrib3s_impl:
        fptr = __pyglGetFuncAddress('glVertexAttrib3s')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib3s is not available (maybe GL has not been initialized yet?)')
        __glVertexAttrib3s_impl = __PYGL_FUNC_TYPE( None,c_uint,c_short,c_short,c_short )(fptr)
        global glVertexAttrib3s
        glVertexAttrib3s =__glVertexAttrib3s_impl
    return __glVertexAttrib3s_impl(index,x,y,z)

__glVertexAttrib3sv_impl = None
def glVertexAttrib3sv ( index:int,v:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glVertexAttrib3sv_impl
    if not __glVertexAttrib3sv_impl:
        fptr = __pyglGetFuncAddress('glVertexAttrib3sv')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib3sv is not available (maybe GL has not been initialized yet?)')
        __glVertexAttrib3sv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p )(fptr)
        tmp = __glVertexAttrib3sv_impl
        __glVertexAttrib3sv_impl = (lambda index,v: tmp(index,__pyglGetAsConstVoidPointer(v)))
        global glVertexAttrib3sv
        glVertexAttrib3sv =__glVertexAttrib3sv_impl
    return __glVertexAttrib3sv_impl(index,v)

__glVertexAttrib4Nbv_impl = None
def glVertexAttrib4Nbv ( index:int,v:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glVertexAttrib4Nbv_impl
    if not __glVertexAttrib4Nbv_impl:
        fptr = __pyglGetFuncAddress('glVertexAttrib4Nbv')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib4Nbv is not available (maybe GL has not been initialized yet?)')
        __glVertexAttrib4Nbv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p )(fptr)
        tmp = __glVertexAttrib4Nbv_impl
        __glVertexAttrib4Nbv_impl = (lambda index,v: tmp(index,__pyglGetAsConstVoidPointer(v)))
        global glVertexAttrib4Nbv
        glVertexAttrib4Nbv =__glVertexAttrib4Nbv_impl
    return __glVertexAttrib4Nbv_impl(index,v)

__glVertexAttrib4Niv_impl = None
def glVertexAttrib4Niv ( index:int,v:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glVertexAttrib4Niv_impl
    if not __glVertexAttrib4Niv_impl:
        fptr = __pyglGetFuncAddress('glVertexAttrib4Niv')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib4Niv is not available (maybe GL has not been initialized yet?)')
        __glVertexAttrib4Niv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p )(fptr)
        tmp = __glVertexAttrib4Niv_impl
        __glVertexAttrib4Niv_impl = (lambda index,v: tmp(index,__pyglGetAsConstVoidPointer(v)))
        global glVertexAttrib4Niv
        glVertexAttrib4Niv =__glVertexAttrib4Niv_impl
    return __glVertexAttrib4Niv_impl(index,v)

__glVertexAttrib4Nsv_impl = None
def glVertexAttrib4Nsv ( index:int,v:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glVertexAttrib4Nsv_impl
    if not __glVertexAttrib4Nsv_impl:
        fptr = __pyglGetFuncAddress('glVertexAttrib4Nsv')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib4Nsv is not available (maybe GL has not been initialized yet?)')
        __glVertexAttrib4Nsv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p )(fptr)
        tmp = __glVertexAttrib4Nsv_impl
        __glVertexAttrib4Nsv_impl = (lambda index,v: tmp(index,__pyglGetAsConstVoidPointer(v)))
        global glVertexAttrib4Nsv
        glVertexAttrib4Nsv =__glVertexAttrib4Nsv_impl
    return __glVertexAttrib4Nsv_impl(index,v)

__glVertexAttrib4Nub_impl = None
def glVertexAttrib4Nub ( index:int,x:int,y:int,z:int,w:int ) -> None :
    global __glVertexAttrib4Nub_impl
    if not __glVertexAttrib4Nub_impl:
        fptr = __pyglGetFuncAddress('glVertexAttrib4Nub')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib4Nub is not available (maybe GL has not been initialized yet?)')
        __glVertexAttrib4Nub_impl = __PYGL_FUNC_TYPE( None,c_uint,c_ubyte,c_ubyte,c_ubyte,c_ubyte )(fptr)
        global glVertexAttrib4Nub
        glVertexAttrib4Nub =__glVertexAttrib4Nub_impl
    return __glVertexAttrib4Nub_impl(index,x,y,z,w)

__glVertexAttrib4Nubv_impl = None
def glVertexAttrib4Nubv ( index:int,v:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glVertexAttrib4Nubv_impl
    if not __glVertexAttrib4Nubv_impl:
        fptr = __pyglGetFuncAddress('glVertexAttrib4Nubv')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib4Nubv is not available (maybe GL has not been initialized yet?)')
        __glVertexAttrib4Nubv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_char_p )(fptr)
        tmp = __glVertexAttrib4Nubv_impl
        __glVertexAttrib4Nubv_impl = (lambda index,v: tmp(index,__pyglGetAsConstVoidPointer(v)))
        global glVertexAttrib4Nubv
        glVertexAttrib4Nubv =__glVertexAttrib4Nubv_impl
    return __glVertexAttrib4Nubv_impl(index,v)

__glVertexAttrib4Nuiv_impl = None
def glVertexAttrib4Nuiv ( index:int,v:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glVertexAttrib4Nuiv_impl
    if not __glVertexAttrib4Nuiv_impl:
        fptr = __pyglGetFuncAddress('glVertexAttrib4Nuiv')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib4Nuiv is not available (maybe GL has not been initialized yet?)')
        __glVertexAttrib4Nuiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p )(fptr)
        tmp = __glVertexAttrib4Nuiv_impl
        __glVertexAttrib4Nuiv_impl = (lambda index,v: tmp(index,__pyglGetAsConstVoidPointer(v)))
        global glVertexAttrib4Nuiv
        glVertexAttrib4Nuiv =__glVertexAttrib4Nuiv_impl
    return __glVertexAttrib4Nuiv_impl(index,v)

__glVertexAttrib4Nusv_impl = None
def glVertexAttrib4Nusv ( index:int,v:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glVertexAttrib4Nusv_impl
    if not __glVertexAttrib4Nusv_impl:
        fptr = __pyglGetFuncAddress('glVertexAttrib4Nusv')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib4Nusv is not available (maybe GL has not been initialized yet?)')
        __glVertexAttrib4Nusv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p )(fptr)
        tmp = __glVertexAttrib4Nusv_impl
        __glVertexAttrib4Nusv_impl = (lambda index,v: tmp(index,__pyglGetAsConstVoidPointer(v)))
        global glVertexAttrib4Nusv
        glVertexAttrib4Nusv =__glVertexAttrib4Nusv_impl
    return __glVertexAttrib4Nusv_impl(index,v)

__glVertexAttrib4bv_impl = None
def glVertexAttrib4bv ( index:int,v:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glVertexAttrib4bv_impl
    if not __glVertexAttrib4bv_impl:
        fptr = __pyglGetFuncAddress('glVertexAttrib4bv')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib4bv is not available (maybe GL has not been initialized yet?)')
        __glVertexAttrib4bv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p )(fptr)
        tmp = __glVertexAttrib4bv_impl
        __glVertexAttrib4bv_impl = (lambda index,v: tmp(index,__pyglGetAsConstVoidPointer(v)))
        global glVertexAttrib4bv
        glVertexAttrib4bv =__glVertexAttrib4bv_impl
    return __glVertexAttrib4bv_impl(index,v)

__glVertexAttrib4d_impl = None
def glVertexAttrib4d ( index:int,x:float,y:float,z:float,w:float ) -> None :
    global __glVertexAttrib4d_impl
    if not __glVertexAttrib4d_impl:
        fptr = __pyglGetFuncAddress('glVertexAttrib4d')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib4d is not available (maybe GL has not been initialized yet?)')
        __glVertexAttrib4d_impl = __PYGL_FUNC_TYPE( None,c_uint,c_double,c_double,c_double,c_double )(fptr)
        global glVertexAttrib4d
        glVertexAttrib4d =__glVertexAttrib4d_impl
    return __glVertexAttrib4d_impl(index,x,y,z,w)

__glVertexAttrib4dv_impl = None
def glVertexAttrib4dv ( index:int,v:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glVertexAttrib4dv_impl
    if not __glVertexAttrib4dv_impl:
        fptr = __pyglGetFuncAddress('glVertexAttrib4dv')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib4dv is not available (maybe GL has not been initialized yet?)')
        __glVertexAttrib4dv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p )(fptr)
        tmp = __glVertexAttrib4dv_impl
        __glVertexAttrib4dv_impl = (lambda index,v: tmp(index,__pyglGetAsConstVoidPointer(v)))
        global glVertexAttrib4dv
        glVertexAttrib4dv =__glVertexAttrib4dv_impl
    return __glVertexAttrib4dv_impl(index,v)

__glVertexAttrib4f_impl = None
def glVertexAttrib4f ( index:int,x:float,y:float,z:float,w:float ) -> None :
    global __glVertexAttrib4f_impl
    if not __glVertexAttrib4f_impl:
        fptr = __pyglGetFuncAddress('glVertexAttrib4f')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib4f is not available (maybe GL has not been initialized yet?)')
        __glVertexAttrib4f_impl = __PYGL_FUNC_TYPE( None,c_uint,c_float,c_float,c_float,c_float )(fptr)
        global glVertexAttrib4f
        glVertexAttrib4f =__glVertexAttrib4f_impl
    return __glVertexAttrib4f_impl(index,x,y,z,w)

__glVertexAttrib4fv_impl = None
def glVertexAttrib4fv ( index:int,v:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glVertexAttrib4fv_impl
    if not __glVertexAttrib4fv_impl:
        fptr = __pyglGetFuncAddress('glVertexAttrib4fv')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib4fv is not available (maybe GL has not been initialized yet?)')
        __glVertexAttrib4fv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p )(fptr)
        tmp = __glVertexAttrib4fv_impl
        __glVertexAttrib4fv_impl = (lambda index,v: tmp(index,__pyglGetAsConstVoidPointer(v)))
        global glVertexAttrib4fv
        glVertexAttrib4fv =__glVertexAttrib4fv_impl
    return __glVertexAttrib4fv_impl(index,v)

__glVertexAttrib4iv_impl = None
def glVertexAttrib4iv ( index:int,v:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glVertexAttrib4iv_impl
    if not __glVertexAttrib4iv_impl:
        fptr = __pyglGetFuncAddress('glVertexAttrib4iv')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib4iv is not available (maybe GL has not been initialized yet?)')
        __glVertexAttrib4iv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p )(fptr)
        tmp = __glVertexAttrib4iv_impl
        __glVertexAttrib4iv_impl = (lambda index,v: tmp(index,__pyglGetAsConstVoidPointer(v)))
        global glVertexAttrib4iv
        glVertexAttrib4iv =__glVertexAttrib4iv_impl
    return __glVertexAttrib4iv_impl(index,v)

__glVertexAttrib4s_impl = None
def glVertexAttrib4s ( index:int,x:int,y:int,z:int,w:int ) -> None :
    global __glVertexAttrib4s_impl
    if not __glVertexAttrib4s_impl:
        fptr = __pyglGetFuncAddress('glVertexAttrib4s')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib4s is not available (maybe GL has not been initialized yet?)')
        __glVertexAttrib4s_impl = __PYGL_FUNC_TYPE( None,c_uint,c_short,c_short,c_short,c_short )(fptr)
        global glVertexAttrib4s
        glVertexAttrib4s =__glVertexAttrib4s_impl
    return __glVertexAttrib4s_impl(index,x,y,z,w)

__glVertexAttrib4sv_impl = None
def glVertexAttrib4sv ( index:int,v:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glVertexAttrib4sv_impl
    if not __glVertexAttrib4sv_impl:
        fptr = __pyglGetFuncAddress('glVertexAttrib4sv')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib4sv is not available (maybe GL has not been initialized yet?)')
        __glVertexAttrib4sv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p )(fptr)
        tmp = __glVertexAttrib4sv_impl
        __glVertexAttrib4sv_impl = (lambda index,v: tmp(index,__pyglGetAsConstVoidPointer(v)))
        global glVertexAttrib4sv
        glVertexAttrib4sv =__glVertexAttrib4sv_impl
    return __glVertexAttrib4sv_impl(index,v)

__glVertexAttrib4ubv_impl = None
def glVertexAttrib4ubv ( index:int,v:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glVertexAttrib4ubv_impl
    if not __glVertexAttrib4ubv_impl:
        fptr = __pyglGetFuncAddress('glVertexAttrib4ubv')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib4ubv is not available (maybe GL has not been initialized yet?)')
        __glVertexAttrib4ubv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_char_p )(fptr)
        tmp = __glVertexAttrib4ubv_impl
        __glVertexAttrib4ubv_impl = (lambda index,v: tmp(index,__pyglGetAsConstVoidPointer(v)))
        global glVertexAttrib4ubv
        glVertexAttrib4ubv =__glVertexAttrib4ubv_impl
    return __glVertexAttrib4ubv_impl(index,v)

__glVertexAttrib4uiv_impl = None
def glVertexAttrib4uiv ( index:int,v:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glVertexAttrib4uiv_impl
    if not __glVertexAttrib4uiv_impl:
        fptr = __pyglGetFuncAddress('glVertexAttrib4uiv')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib4uiv is not available (maybe GL has not been initialized yet?)')
        __glVertexAttrib4uiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p )(fptr)
        tmp = __glVertexAttrib4uiv_impl
        __glVertexAttrib4uiv_impl = (lambda index,v: tmp(index,__pyglGetAsConstVoidPointer(v)))
        global glVertexAttrib4uiv
        glVertexAttrib4uiv =__glVertexAttrib4uiv_impl
    return __glVertexAttrib4uiv_impl(index,v)

__glVertexAttrib4usv_impl = None
def glVertexAttrib4usv ( index:int,v:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glVertexAttrib4usv_impl
    if not __glVertexAttrib4usv_impl:
        fptr = __pyglGetFuncAddress('glVertexAttrib4usv')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib4usv is not available (maybe GL has not been initialized yet?)')
        __glVertexAttrib4usv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p )(fptr)
        tmp = __glVertexAttrib4usv_impl
        __glVertexAttrib4usv_impl = (lambda index,v: tmp(index,__pyglGetAsConstVoidPointer(v)))
        global glVertexAttrib4usv
        glVertexAttrib4usv =__glVertexAttrib4usv_impl
    return __glVertexAttrib4usv_impl(index,v)

__glVertexAttribBinding_impl = None
def glVertexAttribBinding ( attribindex:int,bindingindex:int ) -> None :
    global __glVertexAttribBinding_impl
    if not __glVertexAttribBinding_impl:
        fptr = __pyglGetFuncAddress('glVertexAttribBinding')
        if not fptr:
            raise RuntimeError('The function glVertexAttribBinding is not available (maybe GL has not been initialized yet?)')
        __glVertexAttribBinding_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint )(fptr)
        global glVertexAttribBinding
        glVertexAttribBinding =__glVertexAttribBinding_impl
    return __glVertexAttribBinding_impl(attribindex,bindingindex)

__glVertexAttribDivisor_impl = None
def glVertexAttribDivisor ( index:int,divisor:int ) -> None :
    global __glVertexAttribDivisor_impl
    if not __glVertexAttribDivisor_impl:
        fptr = __pyglGetFuncAddress('glVertexAttribDivisor')
        if not fptr:
            raise RuntimeError('The function glVertexAttribDivisor is not available (maybe GL has not been initialized yet?)')
        __glVertexAttribDivisor_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint )(fptr)
        global glVertexAttribDivisor
        glVertexAttribDivisor =__glVertexAttribDivisor_impl
    return __glVertexAttribDivisor_impl(index,divisor)

__glVertexAttribFormat_impl = None
def glVertexAttribFormat ( attribindex:int,size:int,type:int,normalized:bool,relativeoffset:int ) -> None :
    global __glVertexAttribFormat_impl
    if not __glVertexAttribFormat_impl:
        fptr = __pyglGetFuncAddress('glVertexAttribFormat')
        if not fptr:
            raise RuntimeError('The function glVertexAttribFormat is not available (maybe GL has not been initialized yet?)')
        __glVertexAttribFormat_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_uint,c_char,c_uint )(fptr)
        global glVertexAttribFormat
        glVertexAttribFormat =__glVertexAttribFormat_impl
    return __glVertexAttribFormat_impl(attribindex,size,type,normalized,relativeoffset)

__glVertexAttribI1i_impl = None
def glVertexAttribI1i ( index:int,x:int ) -> None :
    global __glVertexAttribI1i_impl
    if not __glVertexAttribI1i_impl:
        fptr = __pyglGetFuncAddress('glVertexAttribI1i')
        if not fptr:
            raise RuntimeError('The function glVertexAttribI1i is not available (maybe GL has not been initialized yet?)')
        __glVertexAttribI1i_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int )(fptr)
        global glVertexAttribI1i
        glVertexAttribI1i =__glVertexAttribI1i_impl
    return __glVertexAttribI1i_impl(index,x)

__glVertexAttribI1iv_impl = None
def glVertexAttribI1iv ( index:int,v:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glVertexAttribI1iv_impl
    if not __glVertexAttribI1iv_impl:
        fptr = __pyglGetFuncAddress('glVertexAttribI1iv')
        if not fptr:
            raise RuntimeError('The function glVertexAttribI1iv is not available (maybe GL has not been initialized yet?)')
        __glVertexAttribI1iv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p )(fptr)
        tmp = __glVertexAttribI1iv_impl
        __glVertexAttribI1iv_impl = (lambda index,v: tmp(index,__pyglGetAsConstVoidPointer(v)))
        global glVertexAttribI1iv
        glVertexAttribI1iv =__glVertexAttribI1iv_impl
    return __glVertexAttribI1iv_impl(index,v)

__glVertexAttribI1ui_impl = None
def glVertexAttribI1ui ( index:int,x:int ) -> None :
    global __glVertexAttribI1ui_impl
    if not __glVertexAttribI1ui_impl:
        fptr = __pyglGetFuncAddress('glVertexAttribI1ui')
        if not fptr:
            raise RuntimeError('The function glVertexAttribI1ui is not available (maybe GL has not been initialized yet?)')
        __glVertexAttribI1ui_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint )(fptr)
        global glVertexAttribI1ui
        glVertexAttribI1ui =__glVertexAttribI1ui_impl
    return __glVertexAttribI1ui_impl(index,x)

__glVertexAttribI1uiv_impl = None
def glVertexAttribI1uiv ( index:int,v:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glVertexAttribI1uiv_impl
    if not __glVertexAttribI1uiv_impl:
        fptr = __pyglGetFuncAddress('glVertexAttribI1uiv')
        if not fptr:
            raise RuntimeError('The function glVertexAttribI1uiv is not available (maybe GL has not been initialized yet?)')
        __glVertexAttribI1uiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p )(fptr)
        tmp = __glVertexAttribI1uiv_impl
        __glVertexAttribI1uiv_impl = (lambda index,v: tmp(index,__pyglGetAsConstVoidPointer(v)))
        global glVertexAttribI1uiv
        glVertexAttribI1uiv =__glVertexAttribI1uiv_impl
    return __glVertexAttribI1uiv_impl(index,v)

__glVertexAttribI2i_impl = None
def glVertexAttribI2i ( index:int,x:int,y:int ) -> None :
    global __glVertexAttribI2i_impl
    if not __glVertexAttribI2i_impl:
        fptr = __pyglGetFuncAddress('glVertexAttribI2i')
        if not fptr:
            raise RuntimeError('The function glVertexAttribI2i is not available (maybe GL has not been initialized yet?)')
        __glVertexAttribI2i_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int )(fptr)
        global glVertexAttribI2i
        glVertexAttribI2i =__glVertexAttribI2i_impl
    return __glVertexAttribI2i_impl(index,x,y)

__glVertexAttribI2iv_impl = None
def glVertexAttribI2iv ( index:int,v:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glVertexAttribI2iv_impl
    if not __glVertexAttribI2iv_impl:
        fptr = __pyglGetFuncAddress('glVertexAttribI2iv')
        if not fptr:
            raise RuntimeError('The function glVertexAttribI2iv is not available (maybe GL has not been initialized yet?)')
        __glVertexAttribI2iv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p )(fptr)
        tmp = __glVertexAttribI2iv_impl
        __glVertexAttribI2iv_impl = (lambda index,v: tmp(index,__pyglGetAsConstVoidPointer(v)))
        global glVertexAttribI2iv
        glVertexAttribI2iv =__glVertexAttribI2iv_impl
    return __glVertexAttribI2iv_impl(index,v)

__glVertexAttribI2ui_impl = None
def glVertexAttribI2ui ( index:int,x:int,y:int ) -> None :
    global __glVertexAttribI2ui_impl
    if not __glVertexAttribI2ui_impl:
        fptr = __pyglGetFuncAddress('glVertexAttribI2ui')
        if not fptr:
            raise RuntimeError('The function glVertexAttribI2ui is not available (maybe GL has not been initialized yet?)')
        __glVertexAttribI2ui_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint )(fptr)
        global glVertexAttribI2ui
        glVertexAttribI2ui =__glVertexAttribI2ui_impl
    return __glVertexAttribI2ui_impl(index,x,y)

__glVertexAttribI2uiv_impl = None
def glVertexAttribI2uiv ( index:int,v:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glVertexAttribI2uiv_impl
    if not __glVertexAttribI2uiv_impl:
        fptr = __pyglGetFuncAddress('glVertexAttribI2uiv')
        if not fptr:
            raise RuntimeError('The function glVertexAttribI2uiv is not available (maybe GL has not been initialized yet?)')
        __glVertexAttribI2uiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p )(fptr)
        tmp = __glVertexAttribI2uiv_impl
        __glVertexAttribI2uiv_impl = (lambda index,v: tmp(index,__pyglGetAsConstVoidPointer(v)))
        global glVertexAttribI2uiv
        glVertexAttribI2uiv =__glVertexAttribI2uiv_impl
    return __glVertexAttribI2uiv_impl(index,v)

__glVertexAttribI3i_impl = None
def glVertexAttribI3i ( index:int,x:int,y:int,z:int ) -> None :
    global __glVertexAttribI3i_impl
    if not __glVertexAttribI3i_impl:
        fptr = __pyglGetFuncAddress('glVertexAttribI3i')
        if not fptr:
            raise RuntimeError('The function glVertexAttribI3i is not available (maybe GL has not been initialized yet?)')
        __glVertexAttribI3i_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_int )(fptr)
        global glVertexAttribI3i
        glVertexAttribI3i =__glVertexAttribI3i_impl
    return __glVertexAttribI3i_impl(index,x,y,z)

__glVertexAttribI3iv_impl = None
def glVertexAttribI3iv ( index:int,v:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glVertexAttribI3iv_impl
    if not __glVertexAttribI3iv_impl:
        fptr = __pyglGetFuncAddress('glVertexAttribI3iv')
        if not fptr:
            raise RuntimeError('The function glVertexAttribI3iv is not available (maybe GL has not been initialized yet?)')
        __glVertexAttribI3iv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p )(fptr)
        tmp = __glVertexAttribI3iv_impl
        __glVertexAttribI3iv_impl = (lambda index,v: tmp(index,__pyglGetAsConstVoidPointer(v)))
        global glVertexAttribI3iv
        glVertexAttribI3iv =__glVertexAttribI3iv_impl
    return __glVertexAttribI3iv_impl(index,v)

__glVertexAttribI3ui_impl = None
def glVertexAttribI3ui ( index:int,x:int,y:int,z:int ) -> None :
    global __glVertexAttribI3ui_impl
    if not __glVertexAttribI3ui_impl:
        fptr = __pyglGetFuncAddress('glVertexAttribI3ui')
        if not fptr:
            raise RuntimeError('The function glVertexAttribI3ui is not available (maybe GL has not been initialized yet?)')
        __glVertexAttribI3ui_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint,c_uint )(fptr)
        global glVertexAttribI3ui
        glVertexAttribI3ui =__glVertexAttribI3ui_impl
    return __glVertexAttribI3ui_impl(index,x,y,z)

__glVertexAttribI3uiv_impl = None
def glVertexAttribI3uiv ( index:int,v:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glVertexAttribI3uiv_impl
    if not __glVertexAttribI3uiv_impl:
        fptr = __pyglGetFuncAddress('glVertexAttribI3uiv')
        if not fptr:
            raise RuntimeError('The function glVertexAttribI3uiv is not available (maybe GL has not been initialized yet?)')
        __glVertexAttribI3uiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p )(fptr)
        tmp = __glVertexAttribI3uiv_impl
        __glVertexAttribI3uiv_impl = (lambda index,v: tmp(index,__pyglGetAsConstVoidPointer(v)))
        global glVertexAttribI3uiv
        glVertexAttribI3uiv =__glVertexAttribI3uiv_impl
    return __glVertexAttribI3uiv_impl(index,v)

__glVertexAttribI4bv_impl = None
def glVertexAttribI4bv ( index:int,v:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glVertexAttribI4bv_impl
    if not __glVertexAttribI4bv_impl:
        fptr = __pyglGetFuncAddress('glVertexAttribI4bv')
        if not fptr:
            raise RuntimeError('The function glVertexAttribI4bv is not available (maybe GL has not been initialized yet?)')
        __glVertexAttribI4bv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p )(fptr)
        tmp = __glVertexAttribI4bv_impl
        __glVertexAttribI4bv_impl = (lambda index,v: tmp(index,__pyglGetAsConstVoidPointer(v)))
        global glVertexAttribI4bv
        glVertexAttribI4bv =__glVertexAttribI4bv_impl
    return __glVertexAttribI4bv_impl(index,v)

__glVertexAttribI4i_impl = None
def glVertexAttribI4i ( index:int,x:int,y:int,z:int,w:int ) -> None :
    global __glVertexAttribI4i_impl
    if not __glVertexAttribI4i_impl:
        fptr = __pyglGetFuncAddress('glVertexAttribI4i')
        if not fptr:
            raise RuntimeError('The function glVertexAttribI4i is not available (maybe GL has not been initialized yet?)')
        __glVertexAttribI4i_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_int,c_int,c_int )(fptr)
        global glVertexAttribI4i
        glVertexAttribI4i =__glVertexAttribI4i_impl
    return __glVertexAttribI4i_impl(index,x,y,z,w)

__glVertexAttribI4iv_impl = None
def glVertexAttribI4iv ( index:int,v:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glVertexAttribI4iv_impl
    if not __glVertexAttribI4iv_impl:
        fptr = __pyglGetFuncAddress('glVertexAttribI4iv')
        if not fptr:
            raise RuntimeError('The function glVertexAttribI4iv is not available (maybe GL has not been initialized yet?)')
        __glVertexAttribI4iv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p )(fptr)
        tmp = __glVertexAttribI4iv_impl
        __glVertexAttribI4iv_impl = (lambda index,v: tmp(index,__pyglGetAsConstVoidPointer(v)))
        global glVertexAttribI4iv
        glVertexAttribI4iv =__glVertexAttribI4iv_impl
    return __glVertexAttribI4iv_impl(index,v)

__glVertexAttribI4sv_impl = None
def glVertexAttribI4sv ( index:int,v:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glVertexAttribI4sv_impl
    if not __glVertexAttribI4sv_impl:
        fptr = __pyglGetFuncAddress('glVertexAttribI4sv')
        if not fptr:
            raise RuntimeError('The function glVertexAttribI4sv is not available (maybe GL has not been initialized yet?)')
        __glVertexAttribI4sv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p )(fptr)
        tmp = __glVertexAttribI4sv_impl
        __glVertexAttribI4sv_impl = (lambda index,v: tmp(index,__pyglGetAsConstVoidPointer(v)))
        global glVertexAttribI4sv
        glVertexAttribI4sv =__glVertexAttribI4sv_impl
    return __glVertexAttribI4sv_impl(index,v)

__glVertexAttribI4ubv_impl = None
def glVertexAttribI4ubv ( index:int,v:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glVertexAttribI4ubv_impl
    if not __glVertexAttribI4ubv_impl:
        fptr = __pyglGetFuncAddress('glVertexAttribI4ubv')
        if not fptr:
            raise RuntimeError('The function glVertexAttribI4ubv is not available (maybe GL has not been initialized yet?)')
        __glVertexAttribI4ubv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_char_p )(fptr)
        tmp = __glVertexAttribI4ubv_impl
        __glVertexAttribI4ubv_impl = (lambda index,v: tmp(index,__pyglGetAsConstVoidPointer(v)))
        global glVertexAttribI4ubv
        glVertexAttribI4ubv =__glVertexAttribI4ubv_impl
    return __glVertexAttribI4ubv_impl(index,v)

__glVertexAttribI4ui_impl = None
def glVertexAttribI4ui ( index:int,x:int,y:int,z:int,w:int ) -> None :
    global __glVertexAttribI4ui_impl
    if not __glVertexAttribI4ui_impl:
        fptr = __pyglGetFuncAddress('glVertexAttribI4ui')
        if not fptr:
            raise RuntimeError('The function glVertexAttribI4ui is not available (maybe GL has not been initialized yet?)')
        __glVertexAttribI4ui_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_uint,c_uint,c_uint )(fptr)
        global glVertexAttribI4ui
        glVertexAttribI4ui =__glVertexAttribI4ui_impl
    return __glVertexAttribI4ui_impl(index,x,y,z,w)

__glVertexAttribI4uiv_impl = None
def glVertexAttribI4uiv ( index:int,v:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glVertexAttribI4uiv_impl
    if not __glVertexAttribI4uiv_impl:
        fptr = __pyglGetFuncAddress('glVertexAttribI4uiv')
        if not fptr:
            raise RuntimeError('The function glVertexAttribI4uiv is not available (maybe GL has not been initialized yet?)')
        __glVertexAttribI4uiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p )(fptr)
        tmp = __glVertexAttribI4uiv_impl
        __glVertexAttribI4uiv_impl = (lambda index,v: tmp(index,__pyglGetAsConstVoidPointer(v)))
        global glVertexAttribI4uiv
        glVertexAttribI4uiv =__glVertexAttribI4uiv_impl
    return __glVertexAttribI4uiv_impl(index,v)

__glVertexAttribI4usv_impl = None
def glVertexAttribI4usv ( index:int,v:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glVertexAttribI4usv_impl
    if not __glVertexAttribI4usv_impl:
        fptr = __pyglGetFuncAddress('glVertexAttribI4usv')
        if not fptr:
            raise RuntimeError('The function glVertexAttribI4usv is not available (maybe GL has not been initialized yet?)')
        __glVertexAttribI4usv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p )(fptr)
        tmp = __glVertexAttribI4usv_impl
        __glVertexAttribI4usv_impl = (lambda index,v: tmp(index,__pyglGetAsConstVoidPointer(v)))
        global glVertexAttribI4usv
        glVertexAttribI4usv =__glVertexAttribI4usv_impl
    return __glVertexAttribI4usv_impl(index,v)

__glVertexAttribL1d_impl = None
def glVertexAttribL1d ( index:int,x:float ) -> None :
    global __glVertexAttribL1d_impl
    if not __glVertexAttribL1d_impl:
        fptr = __pyglGetFuncAddress('glVertexAttribL1d')
        if not fptr:
            raise RuntimeError('The function glVertexAttribL1d is not available (maybe GL has not been initialized yet?)')
        __glVertexAttribL1d_impl = __PYGL_FUNC_TYPE( None,c_uint,c_double )(fptr)
        global glVertexAttribL1d
        glVertexAttribL1d =__glVertexAttribL1d_impl
    return __glVertexAttribL1d_impl(index,x)

__glVertexAttribL1dv_impl = None
def glVertexAttribL1dv ( index:int,v:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glVertexAttribL1dv_impl
    if not __glVertexAttribL1dv_impl:
        fptr = __pyglGetFuncAddress('glVertexAttribL1dv')
        if not fptr:
            raise RuntimeError('The function glVertexAttribL1dv is not available (maybe GL has not been initialized yet?)')
        __glVertexAttribL1dv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p )(fptr)
        tmp = __glVertexAttribL1dv_impl
        __glVertexAttribL1dv_impl = (lambda index,v: tmp(index,__pyglGetAsConstVoidPointer(v)))
        global glVertexAttribL1dv
        glVertexAttribL1dv =__glVertexAttribL1dv_impl
    return __glVertexAttribL1dv_impl(index,v)

__glVertexAttribL2d_impl = None
def glVertexAttribL2d ( index:int,x:float,y:float ) -> None :
    global __glVertexAttribL2d_impl
    if not __glVertexAttribL2d_impl:
        fptr = __pyglGetFuncAddress('glVertexAttribL2d')
        if not fptr:
            raise RuntimeError('The function glVertexAttribL2d is not available (maybe GL has not been initialized yet?)')
        __glVertexAttribL2d_impl = __PYGL_FUNC_TYPE( None,c_uint,c_double,c_double )(fptr)
        global glVertexAttribL2d
        glVertexAttribL2d =__glVertexAttribL2d_impl
    return __glVertexAttribL2d_impl(index,x,y)

__glVertexAttribL2dv_impl = None
def glVertexAttribL2dv ( index:int,v:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glVertexAttribL2dv_impl
    if not __glVertexAttribL2dv_impl:
        fptr = __pyglGetFuncAddress('glVertexAttribL2dv')
        if not fptr:
            raise RuntimeError('The function glVertexAttribL2dv is not available (maybe GL has not been initialized yet?)')
        __glVertexAttribL2dv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p )(fptr)
        tmp = __glVertexAttribL2dv_impl
        __glVertexAttribL2dv_impl = (lambda index,v: tmp(index,__pyglGetAsConstVoidPointer(v)))
        global glVertexAttribL2dv
        glVertexAttribL2dv =__glVertexAttribL2dv_impl
    return __glVertexAttribL2dv_impl(index,v)

__glVertexAttribL3d_impl = None
def glVertexAttribL3d ( index:int,x:float,y:float,z:float ) -> None :
    global __glVertexAttribL3d_impl
    if not __glVertexAttribL3d_impl:
        fptr = __pyglGetFuncAddress('glVertexAttribL3d')
        if not fptr:
            raise RuntimeError('The function glVertexAttribL3d is not available (maybe GL has not been initialized yet?)')
        __glVertexAttribL3d_impl = __PYGL_FUNC_TYPE( None,c_uint,c_double,c_double,c_double )(fptr)
        global glVertexAttribL3d
        glVertexAttribL3d =__glVertexAttribL3d_impl
    return __glVertexAttribL3d_impl(index,x,y,z)

__glVertexAttribL3dv_impl = None
def glVertexAttribL3dv ( index:int,v:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glVertexAttribL3dv_impl
    if not __glVertexAttribL3dv_impl:
        fptr = __pyglGetFuncAddress('glVertexAttribL3dv')
        if not fptr:
            raise RuntimeError('The function glVertexAttribL3dv is not available (maybe GL has not been initialized yet?)')
        __glVertexAttribL3dv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p )(fptr)
        tmp = __glVertexAttribL3dv_impl
        __glVertexAttribL3dv_impl = (lambda index,v: tmp(index,__pyglGetAsConstVoidPointer(v)))
        global glVertexAttribL3dv
        glVertexAttribL3dv =__glVertexAttribL3dv_impl
    return __glVertexAttribL3dv_impl(index,v)

__glVertexAttribL4d_impl = None
def glVertexAttribL4d ( index:int,x:float,y:float,z:float,w:float ) -> None :
    global __glVertexAttribL4d_impl
    if not __glVertexAttribL4d_impl:
        fptr = __pyglGetFuncAddress('glVertexAttribL4d')
        if not fptr:
            raise RuntimeError('The function glVertexAttribL4d is not available (maybe GL has not been initialized yet?)')
        __glVertexAttribL4d_impl = __PYGL_FUNC_TYPE( None,c_uint,c_double,c_double,c_double,c_double )(fptr)
        global glVertexAttribL4d
        glVertexAttribL4d =__glVertexAttribL4d_impl
    return __glVertexAttribL4d_impl(index,x,y,z,w)

__glVertexAttribL4dv_impl = None
def glVertexAttribL4dv ( index:int,v:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glVertexAttribL4dv_impl
    if not __glVertexAttribL4dv_impl:
        fptr = __pyglGetFuncAddress('glVertexAttribL4dv')
        if not fptr:
            raise RuntimeError('The function glVertexAttribL4dv is not available (maybe GL has not been initialized yet?)')
        __glVertexAttribL4dv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p )(fptr)
        tmp = __glVertexAttribL4dv_impl
        __glVertexAttribL4dv_impl = (lambda index,v: tmp(index,__pyglGetAsConstVoidPointer(v)))
        global glVertexAttribL4dv
        glVertexAttribL4dv =__glVertexAttribL4dv_impl
    return __glVertexAttribL4dv_impl(index,v)

__glVertexAttribP1ui_impl = None
def glVertexAttribP1ui ( index:int,type:int,normalized:bool,value:int ) -> None :
    global __glVertexAttribP1ui_impl
    if not __glVertexAttribP1ui_impl:
        fptr = __pyglGetFuncAddress('glVertexAttribP1ui')
        if not fptr:
            raise RuntimeError('The function glVertexAttribP1ui is not available (maybe GL has not been initialized yet?)')
        __glVertexAttribP1ui_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_char,c_uint )(fptr)
        global glVertexAttribP1ui
        glVertexAttribP1ui =__glVertexAttribP1ui_impl
    return __glVertexAttribP1ui_impl(index,type,normalized,value)

__glVertexAttribP1uiv_impl = None
def glVertexAttribP1uiv ( index:int,type:int,normalized:bool,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glVertexAttribP1uiv_impl
    if not __glVertexAttribP1uiv_impl:
        fptr = __pyglGetFuncAddress('glVertexAttribP1uiv')
        if not fptr:
            raise RuntimeError('The function glVertexAttribP1uiv is not available (maybe GL has not been initialized yet?)')
        __glVertexAttribP1uiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_char,c_void_p )(fptr)
        tmp = __glVertexAttribP1uiv_impl
        __glVertexAttribP1uiv_impl = (lambda index,type,normalized,value: tmp(index,type,normalized,__pyglGetAsConstVoidPointer(value)))
        global glVertexAttribP1uiv
        glVertexAttribP1uiv =__glVertexAttribP1uiv_impl
    return __glVertexAttribP1uiv_impl(index,type,normalized,value)

__glVertexAttribP2ui_impl = None
def glVertexAttribP2ui ( index:int,type:int,normalized:bool,value:int ) -> None :
    global __glVertexAttribP2ui_impl
    if not __glVertexAttribP2ui_impl:
        fptr = __pyglGetFuncAddress('glVertexAttribP2ui')
        if not fptr:
            raise RuntimeError('The function glVertexAttribP2ui is not available (maybe GL has not been initialized yet?)')
        __glVertexAttribP2ui_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_char,c_uint )(fptr)
        global glVertexAttribP2ui
        glVertexAttribP2ui =__glVertexAttribP2ui_impl
    return __glVertexAttribP2ui_impl(index,type,normalized,value)

__glVertexAttribP2uiv_impl = None
def glVertexAttribP2uiv ( index:int,type:int,normalized:bool,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glVertexAttribP2uiv_impl
    if not __glVertexAttribP2uiv_impl:
        fptr = __pyglGetFuncAddress('glVertexAttribP2uiv')
        if not fptr:
            raise RuntimeError('The function glVertexAttribP2uiv is not available (maybe GL has not been initialized yet?)')
        __glVertexAttribP2uiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_char,c_void_p )(fptr)
        tmp = __glVertexAttribP2uiv_impl
        __glVertexAttribP2uiv_impl = (lambda index,type,normalized,value: tmp(index,type,normalized,__pyglGetAsConstVoidPointer(value)))
        global glVertexAttribP2uiv
        glVertexAttribP2uiv =__glVertexAttribP2uiv_impl
    return __glVertexAttribP2uiv_impl(index,type,normalized,value)

__glVertexAttribP3ui_impl = None
def glVertexAttribP3ui ( index:int,type:int,normalized:bool,value:int ) -> None :
    global __glVertexAttribP3ui_impl
    if not __glVertexAttribP3ui_impl:
        fptr = __pyglGetFuncAddress('glVertexAttribP3ui')
        if not fptr:
            raise RuntimeError('The function glVertexAttribP3ui is not available (maybe GL has not been initialized yet?)')
        __glVertexAttribP3ui_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_char,c_uint )(fptr)
        global glVertexAttribP3ui
        glVertexAttribP3ui =__glVertexAttribP3ui_impl
    return __glVertexAttribP3ui_impl(index,type,normalized,value)

__glVertexAttribP3uiv_impl = None
def glVertexAttribP3uiv ( index:int,type:int,normalized:bool,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glVertexAttribP3uiv_impl
    if not __glVertexAttribP3uiv_impl:
        fptr = __pyglGetFuncAddress('glVertexAttribP3uiv')
        if not fptr:
            raise RuntimeError('The function glVertexAttribP3uiv is not available (maybe GL has not been initialized yet?)')
        __glVertexAttribP3uiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_char,c_void_p )(fptr)
        tmp = __glVertexAttribP3uiv_impl
        __glVertexAttribP3uiv_impl = (lambda index,type,normalized,value: tmp(index,type,normalized,__pyglGetAsConstVoidPointer(value)))
        global glVertexAttribP3uiv
        glVertexAttribP3uiv =__glVertexAttribP3uiv_impl
    return __glVertexAttribP3uiv_impl(index,type,normalized,value)

__glVertexAttribP4ui_impl = None
def glVertexAttribP4ui ( index:int,type:int,normalized:bool,value:int ) -> None :
    global __glVertexAttribP4ui_impl
    if not __glVertexAttribP4ui_impl:
        fptr = __pyglGetFuncAddress('glVertexAttribP4ui')
        if not fptr:
            raise RuntimeError('The function glVertexAttribP4ui is not available (maybe GL has not been initialized yet?)')
        __glVertexAttribP4ui_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_char,c_uint )(fptr)
        global glVertexAttribP4ui
        glVertexAttribP4ui =__glVertexAttribP4ui_impl
    return __glVertexAttribP4ui_impl(index,type,normalized,value)

__glVertexAttribP4uiv_impl = None
def glVertexAttribP4uiv ( index:int,type:int,normalized:bool,value:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glVertexAttribP4uiv_impl
    if not __glVertexAttribP4uiv_impl:
        fptr = __pyglGetFuncAddress('glVertexAttribP4uiv')
        if not fptr:
            raise RuntimeError('The function glVertexAttribP4uiv is not available (maybe GL has not been initialized yet?)')
        __glVertexAttribP4uiv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint,c_char,c_void_p )(fptr)
        tmp = __glVertexAttribP4uiv_impl
        __glVertexAttribP4uiv_impl = (lambda index,type,normalized,value: tmp(index,type,normalized,__pyglGetAsConstVoidPointer(value)))
        global glVertexAttribP4uiv
        glVertexAttribP4uiv =__glVertexAttribP4uiv_impl
    return __glVertexAttribP4uiv_impl(index,type,normalized,value)

__glVertexAttribPointer_impl = None
def glVertexAttribPointer ( index:int,size:int,type:int,normalized:bool,stride:int,pointer:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glVertexAttribPointer_impl
    if not __glVertexAttribPointer_impl:
        fptr = __pyglGetFuncAddress('glVertexAttribPointer')
        if not fptr:
            raise RuntimeError('The function glVertexAttribPointer is not available (maybe GL has not been initialized yet?)')
        __glVertexAttribPointer_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_uint,c_char,c_int,c_void_p )(fptr)
        global glVertexAttribPointer
        glVertexAttribPointer =__glVertexAttribPointer_impl
    return __glVertexAttribPointer_impl(index,size,type,normalized,stride,pointer)

__glVertexBindingDivisor_impl = None
def glVertexBindingDivisor ( bindingindex:int,divisor:int ) -> None :
    global __glVertexBindingDivisor_impl
    if not __glVertexBindingDivisor_impl:
        fptr = __pyglGetFuncAddress('glVertexBindingDivisor')
        if not fptr:
            raise RuntimeError('The function glVertexBindingDivisor is not available (maybe GL has not been initialized yet?)')
        __glVertexBindingDivisor_impl = __PYGL_FUNC_TYPE( None,c_uint,c_uint )(fptr)
        global glVertexBindingDivisor
        glVertexBindingDivisor =__glVertexBindingDivisor_impl
    return __glVertexBindingDivisor_impl(bindingindex,divisor)

__glViewport_impl = None
def glViewport ( x:int,y:int,width:int,height:int ) -> None :
    global __glViewport_impl
    if not __glViewport_impl:
        fptr = __pyglGetFuncAddress('glViewport')
        if not fptr:
            raise RuntimeError('The function glViewport is not available (maybe GL has not been initialized yet?)')
        __glViewport_impl = __PYGL_FUNC_TYPE( None,c_int,c_int,c_int,c_int )(fptr)
        global glViewport
        glViewport =__glViewport_impl
    return __glViewport_impl(x,y,width,height)

__glViewportArrayv_impl = None
def glViewportArrayv ( first:int,count:int,v:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glViewportArrayv_impl
    if not __glViewportArrayv_impl:
        fptr = __pyglGetFuncAddress('glViewportArrayv')
        if not fptr:
            raise RuntimeError('The function glViewportArrayv is not available (maybe GL has not been initialized yet?)')
        __glViewportArrayv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_int,c_void_p )(fptr)
        tmp = __glViewportArrayv_impl
        __glViewportArrayv_impl = (lambda first,count,v: tmp(first,count,__pyglGetAsConstVoidPointer(v)))
        global glViewportArrayv
        glViewportArrayv =__glViewportArrayv_impl
    return __glViewportArrayv_impl(first,count,v)

__glViewportIndexedf_impl = None
def glViewportIndexedf ( index:int,x:float,y:float,w:float,h:float ) -> None :
    global __glViewportIndexedf_impl
    if not __glViewportIndexedf_impl:
        fptr = __pyglGetFuncAddress('glViewportIndexedf')
        if not fptr:
            raise RuntimeError('The function glViewportIndexedf is not available (maybe GL has not been initialized yet?)')
        __glViewportIndexedf_impl = __PYGL_FUNC_TYPE( None,c_uint,c_float,c_float,c_float,c_float )(fptr)
        global glViewportIndexedf
        glViewportIndexedf =__glViewportIndexedf_impl
    return __glViewportIndexedf_impl(index,x,y,w,h)

__glViewportIndexedfv_impl = None
def glViewportIndexedfv ( index:int,v:typing.Union[bytes,bytearray,array.array,c_void_p,memoryview] ) -> None :
    global __glViewportIndexedfv_impl
    if not __glViewportIndexedfv_impl:
        fptr = __pyglGetFuncAddress('glViewportIndexedfv')
        if not fptr:
            raise RuntimeError('The function glViewportIndexedfv is not available (maybe GL has not been initialized yet?)')
        __glViewportIndexedfv_impl = __PYGL_FUNC_TYPE( None,c_uint,c_void_p )(fptr)
        tmp = __glViewportIndexedfv_impl
        __glViewportIndexedfv_impl = (lambda index,v: tmp(index,__pyglGetAsConstVoidPointer(v)))
        global glViewportIndexedfv
        glViewportIndexedfv =__glViewportIndexedfv_impl
    return __glViewportIndexedfv_impl(index,v)

__glWaitSync_impl = None
def glWaitSync ( sync:typing.Any,flags:int,timeout:int ) -> None :
    global __glWaitSync_impl
    if not __glWaitSync_impl:
        fptr = __pyglGetFuncAddress('glWaitSync')
        if not fptr:
            raise RuntimeError('The function glWaitSync is not available (maybe GL has not been initialized yet?)')
        __glWaitSync_impl = __PYGL_FUNC_TYPE( None,c_void_p,c_uint,c_ulonglong )(fptr)
        global glWaitSync
        glWaitSync =__glWaitSync_impl
    return __glWaitSync_impl(sync,flags,timeout)

__glShaderSource_impl = None
def glShaderSource(shader,count,list_of_strings,list_of_lengths):
    global __glShaderSource_impl
    if __glShaderSource_impl == None:
        __glShaderSource_impl = __PYGL_FUNC_TYPE(None,c_uint,c_size_t,POINTER(c_char_p),
            POINTER(c_uint))(__pyglGetFuncAddress("glShaderSource"))
    
    if list_of_lengths == None:
        list_of_lengths = [len(q) for q in list_of_strings]
        
    if len(list_of_strings) != len(list_of_lengths):
        raise RuntimeError("List length mismatch")
        
    sarray = (c_char_p * len(list_of_strings))()
    iarray = (c_uint * len(list_of_lengths))()

    for i in range(len(list_of_strings)):
        sarray[i] = list_of_strings[i].encode()
        iarray[i] = list_of_lengths[i]
        
    return __glShaderSource_impl( shader, count, sarray, iarray )

__pyglDebugMessageCallbackFunc=None
__pyglDebugMessageCallbackArg=None
def __pyglDebugMessageCallback(src,typ,id_,sev,le,msg,p):
    if __pyglDebugMessageCallbackFunc:
        __pyglDebugMessageCallbackFunc( src,typ,id_,sev,le,msg.decode(),__pyglDebugMessageCallbackArg)

__glDebugMessageCallback_impl = None
def glDebugMessageCallback(func,parm):
    global __pyglDebugMessageCallbackFunc
    global __pyglDebugMessageCallbackArg
    global __pyglDebugMessageCallbackRef
    global __glDebugMessageCallback_impl
    
    #source,type,id,severity,length,mesg,parm)
    if sys.platform.lower().find("win32") != -1:
        FT = WINFUNCTYPE
    else:
        FT = CFUNCTYPE
        
    __pyglDebugMessageCallbackFunc = func
    __pyglDebugMessageCallbackArg = parm
    
    tmp = FT(None,c_uint,c_uint,c_uint,c_uint,c_uint,c_char_p,c_void_p)
    tmp2 = tmp(__pyglDebugMessageCallback)
    
    #need to hold a reference to the variable
    #to prevent garbage collection
    __pyglDebugMessageCallbackRef = tmp2
    
    if __glDebugMessageCallback_impl == None:
        __glDebugMessageCallback_impl = __PYGL_FUNC_TYPE(None,c_void_p,c_void_p)(
            __pyglGetFuncAddress("glDebugMessageCallback")
        )
    return __glDebugMessageCallback_impl( tmp2, None )

glfuncnames={'glActiveShaderProgram',
 'glActiveTexture',
 'glAttachShader',
 'glBeginConditionalRender',
 'glBeginQuery',
 'glBeginQueryIndexed',
 'glBeginTransformFeedback',
 'glBindAttribLocation',
 'glBindBuffer',
 'glBindBufferBase',
 'glBindBufferRange',
 'glBindBuffersBase',
 'glBindBuffersRange',
 'glBindFragDataLocation',
 'glBindFragDataLocationIndexed',
 'glBindFramebuffer',
 'glBindImageTexture',
 'glBindImageTextures',
 'glBindProgramPipeline',
 'glBindRenderbuffer',
 'glBindSampler',
 'glBindSamplers',
 'glBindTexture',
 'glBindTextureUnit',
 'glBindTextures',
 'glBindTransformFeedback',
 'glBindVertexArray',
 'glBindVertexBuffer',
 'glBindVertexBuffers',
 'glBlendColor',
 'glBlendEquation',
 'glBlendEquationSeparate',
 'glBlendEquationSeparatei',
 'glBlendEquationi',
 'glBlendFunc',
 'glBlendFuncSeparate',
 'glBlendFuncSeparatei',
 'glBlendFunci',
 'glBlitFramebuffer',
 'glBlitNamedFramebuffer',
 'glBufferData',
 'glBufferStorage',
 'glBufferSubData',
 'glCheckFramebufferStatus',
 'glCheckNamedFramebufferStatus',
 'glClampColor',
 'glClear',
 'glClearBufferData',
 'glClearBufferSubData',
 'glClearBufferfi',
 'glClearBufferfv',
 'glClearBufferiv',
 'glClearBufferuiv',
 'glClearColor',
 'glClearDepth',
 'glClearDepthf',
 'glClearNamedBufferData',
 'glClearNamedBufferSubData',
 'glClearNamedFramebufferfi',
 'glClearNamedFramebufferfv',
 'glClearNamedFramebufferiv',
 'glClearNamedFramebufferuiv',
 'glClearStencil',
 'glClearTexImage',
 'glClearTexSubImage',
 'glClientWaitSync',
 'glClipControl',
 'glColorMask',
 'glColorMaski',
 'glCompileShader',
 'glCompressedTexImage1D',
 'glCompressedTexImage2D',
 'glCompressedTexImage3D',
 'glCompressedTexSubImage1D',
 'glCompressedTexSubImage2D',
 'glCompressedTexSubImage3D',
 'glCompressedTextureSubImage1D',
 'glCompressedTextureSubImage2D',
 'glCompressedTextureSubImage3D',
 'glCopyBufferSubData',
 'glCopyImageSubData',
 'glCopyNamedBufferSubData',
 'glCopyTexImage1D',
 'glCopyTexImage2D',
 'glCopyTexSubImage1D',
 'glCopyTexSubImage2D',
 'glCopyTexSubImage3D',
 'glCopyTextureSubImage1D',
 'glCopyTextureSubImage2D',
 'glCopyTextureSubImage3D',
 'glCreateBuffers',
 'glCreateFramebuffers',
 'glCreateProgram',
 'glCreateProgramPipelines',
 'glCreateQueries',
 'glCreateRenderbuffers',
 'glCreateSamplers',
 'glCreateShader',
 'glCreateShaderProgramv',
 'glCreateTextures',
 'glCreateTransformFeedbacks',
 'glCreateVertexArrays',
 'glCullFace',
 'glDebugMessageCallback',
 'glDebugMessageControl',
 'glDebugMessageInsert',
 'glDeleteBuffers',
 'glDeleteFramebuffers',
 'glDeleteProgram',
 'glDeleteProgramPipelines',
 'glDeleteQueries',
 'glDeleteRenderbuffers',
 'glDeleteSamplers',
 'glDeleteShader',
 'glDeleteSync',
 'glDeleteTextures',
 'glDeleteTransformFeedbacks',
 'glDeleteVertexArrays',
 'glDepthFunc',
 'glDepthMask',
 'glDepthRange',
 'glDepthRangeArrayv',
 'glDepthRangeIndexed',
 'glDepthRangef',
 'glDetachShader',
 'glDisable',
 'glDisableVertexArrayAttrib',
 'glDisableVertexAttribArray',
 'glDisablei',
 'glDispatchCompute',
 'glDispatchComputeIndirect',
 'glDrawArrays',
 'glDrawArraysIndirect',
 'glDrawArraysInstanced',
 'glDrawArraysInstancedBaseInstance',
 'glDrawBuffer',
 'glDrawBuffers',
 'glDrawElements',
 'glDrawElementsBaseVertex',
 'glDrawElementsIndirect',
 'glDrawElementsInstanced',
 'glDrawElementsInstancedBaseInstance',
 'glDrawElementsInstancedBaseVertex',
 'glDrawElementsInstancedBaseVertexBaseInstance',
 'glDrawRangeElements',
 'glDrawRangeElementsBaseVertex',
 'glDrawTransformFeedback',
 'glDrawTransformFeedbackInstanced',
 'glDrawTransformFeedbackStream',
 'glDrawTransformFeedbackStreamInstanced',
 'glEnable',
 'glEnableVertexArrayAttrib',
 'glEnableVertexAttribArray',
 'glEnablei',
 'glEndConditionalRender',
 'glEndQuery',
 'glEndQueryIndexed',
 'glEndTransformFeedback',
 'glFenceSync',
 'glFinish',
 'glFlush',
 'glFlushMappedBufferRange',
 'glFlushMappedNamedBufferRange',
 'glFramebufferParameteri',
 'glFramebufferRenderbuffer',
 'glFramebufferTexture',
 'glFramebufferTexture1D',
 'glFramebufferTexture2D',
 'glFramebufferTexture3D',
 'glFramebufferTextureLayer',
 'glFrontFace',
 'glGenBuffers',
 'glGenFramebuffers',
 'glGenProgramPipelines',
 'glGenQueries',
 'glGenRenderbuffers',
 'glGenSamplers',
 'glGenTextures',
 'glGenTransformFeedbacks',
 'glGenVertexArrays',
 'glGenerateMipmap',
 'glGenerateTextureMipmap',
 'glGetActiveAtomicCounterBufferiv',
 'glGetActiveAttrib',
 'glGetActiveSubroutineName',
 'glGetActiveSubroutineUniformName',
 'glGetActiveSubroutineUniformiv',
 'glGetActiveUniform',
 'glGetActiveUniformBlockName',
 'glGetActiveUniformBlockiv',
 'glGetActiveUniformName',
 'glGetActiveUniformsiv',
 'glGetAttachedShaders',
 'glGetAttribLocation',
 'glGetBooleani_v',
 'glGetBooleanv',
 'glGetBufferParameteri64v',
 'glGetBufferParameteriv',
 'glGetBufferPointerv',
 'glGetBufferSubData',
 'glGetCompressedTexImage',
 'glGetCompressedTextureImage',
 'glGetCompressedTextureSubImage',
 'glGetDebugMessageLog',
 'glGetDoublei_v',
 'glGetDoublev',
 'glGetError',
 'glGetFloati_v',
 'glGetFloatv',
 'glGetFragDataIndex',
 'glGetFragDataLocation',
 'glGetFramebufferAttachmentParameteriv',
 'glGetFramebufferParameteriv',
 'glGetGraphicsResetStatus',
 'glGetInteger64i_v',
 'glGetInteger64v',
 'glGetIntegeri_v',
 'glGetIntegerv',
 'glGetInternalformati64v',
 'glGetInternalformativ',
 'glGetMultisamplefv',
 'glGetNamedBufferParameteri64v',
 'glGetNamedBufferParameteriv',
 'glGetNamedBufferPointerv',
 'glGetNamedBufferSubData',
 'glGetNamedFramebufferAttachmentParameteriv',
 'glGetNamedFramebufferParameteriv',
 'glGetNamedRenderbufferParameteriv',
 'glGetObjectLabel',
 'glGetObjectPtrLabel',
 'glGetProgramBinary',
 'glGetProgramInfoLog',
 'glGetProgramInterfaceiv',
 'glGetProgramPipelineInfoLog',
 'glGetProgramPipelineiv',
 'glGetProgramResourceIndex',
 'glGetProgramResourceLocation',
 'glGetProgramResourceLocationIndex',
 'glGetProgramResourceName',
 'glGetProgramResourceiv',
 'glGetProgramStageiv',
 'glGetProgramiv',
 'glGetQueryBufferObjecti64v',
 'glGetQueryBufferObjectiv',
 'glGetQueryBufferObjectui64v',
 'glGetQueryBufferObjectuiv',
 'glGetQueryIndexediv',
 'glGetQueryObjecti64v',
 'glGetQueryObjectiv',
 'glGetQueryObjectui64v',
 'glGetQueryObjectuiv',
 'glGetQueryiv',
 'glGetRenderbufferParameteriv',
 'glGetSamplerParameterIiv',
 'glGetSamplerParameterIuiv',
 'glGetSamplerParameterfv',
 'glGetSamplerParameteriv',
 'glGetShaderInfoLog',
 'glGetShaderPrecisionFormat',
 'glGetShaderSource',
 'glGetShaderiv',
 'glGetString',
 'glGetStringi',
 'glGetSubroutineIndex',
 'glGetSubroutineUniformLocation',
 'glGetSynciv',
 'glGetTexImage',
 'glGetTexLevelParameterfv',
 'glGetTexLevelParameteriv',
 'glGetTexParameterIiv',
 'glGetTexParameterIuiv',
 'glGetTexParameterfv',
 'glGetTexParameteriv',
 'glGetTextureImage',
 'glGetTextureLevelParameterfv',
 'glGetTextureLevelParameteriv',
 'glGetTextureParameterIiv',
 'glGetTextureParameterIuiv',
 'glGetTextureParameterfv',
 'glGetTextureParameteriv',
 'glGetTextureSubImage',
 'glGetTransformFeedbackVarying',
 'glGetTransformFeedbacki64_v',
 'glGetTransformFeedbacki_v',
 'glGetTransformFeedbackiv',
 'glGetUniformBlockIndex',
 'glGetUniformIndices',
 'glGetUniformLocation',
 'glGetUniformSubroutineuiv',
 'glGetUniformdv',
 'glGetUniformfv',
 'glGetUniformiv',
 'glGetUniformuiv',
 'glGetVertexArrayIndexed64iv',
 'glGetVertexArrayIndexediv',
 'glGetVertexArrayiv',
 'glGetVertexAttribIiv',
 'glGetVertexAttribIuiv',
 'glGetVertexAttribLdv',
 'glGetVertexAttribPointerv',
 'glGetVertexAttribdv',
 'glGetVertexAttribfv',
 'glGetVertexAttribiv',
 'glGetnCompressedTexImage',
 'glGetnTexImage',
 'glGetnUniformdv',
 'glGetnUniformfv',
 'glGetnUniformiv',
 'glGetnUniformuiv',
 'glHint',
 'glInvalidateBufferData',
 'glInvalidateBufferSubData',
 'glInvalidateFramebuffer',
 'glInvalidateNamedFramebufferData',
 'glInvalidateNamedFramebufferSubData',
 'glInvalidateSubFramebuffer',
 'glInvalidateTexImage',
 'glInvalidateTexSubImage',
 'glIsBuffer',
 'glIsEnabled',
 'glIsEnabledi',
 'glIsFramebuffer',
 'glIsProgram',
 'glIsProgramPipeline',
 'glIsQuery',
 'glIsRenderbuffer',
 'glIsSampler',
 'glIsShader',
 'glIsSync',
 'glIsTexture',
 'glIsTransformFeedback',
 'glIsVertexArray',
 'glLineWidth',
 'glLinkProgram',
 'glLogicOp',
 'glMapBuffer',
 'glMapBufferRange',
 'glMapNamedBuffer',
 'glMapNamedBufferRange',
 'glMemoryBarrier',
 'glMemoryBarrierByRegion',
 'glMinSampleShading',
 'glMultiDrawArrays',
 'glMultiDrawArraysIndirect',
 'glMultiDrawElements',
 'glMultiDrawElementsBaseVertex',
 'glMultiDrawElementsIndirect',
 'glNamedBufferData',
 'glNamedBufferStorage',
 'glNamedBufferSubData',
 'glNamedFramebufferDrawBuffer',
 'glNamedFramebufferDrawBuffers',
 'glNamedFramebufferParameteri',
 'glNamedFramebufferReadBuffer',
 'glNamedFramebufferRenderbuffer',
 'glNamedFramebufferTexture',
 'glNamedFramebufferTextureLayer',
 'glNamedRenderbufferStorage',
 'glNamedRenderbufferStorageMultisample',
 'glObjectLabel',
 'glObjectPtrLabel',
 'glPatchParameterfv',
 'glPatchParameteri',
 'glPauseTransformFeedback',
 'glPixelStoref',
 'glPixelStorei',
 'glPointParameterf',
 'glPointParameterfv',
 'glPointParameteri',
 'glPointParameteriv',
 'glPointSize',
 'glPolygonMode',
 'glPolygonOffset',
 'glPopDebugGroup',
 'glPrimitiveRestartIndex',
 'glProgramBinary',
 'glProgramParameteri',
 'glProgramUniform1d',
 'glProgramUniform1dv',
 'glProgramUniform1f',
 'glProgramUniform1fv',
 'glProgramUniform1i',
 'glProgramUniform1iv',
 'glProgramUniform1ui',
 'glProgramUniform1uiv',
 'glProgramUniform2d',
 'glProgramUniform2dv',
 'glProgramUniform2f',
 'glProgramUniform2fv',
 'glProgramUniform2i',
 'glProgramUniform2iv',
 'glProgramUniform2ui',
 'glProgramUniform2uiv',
 'glProgramUniform3d',
 'glProgramUniform3dv',
 'glProgramUniform3f',
 'glProgramUniform3fv',
 'glProgramUniform3i',
 'glProgramUniform3iv',
 'glProgramUniform3ui',
 'glProgramUniform3uiv',
 'glProgramUniform4d',
 'glProgramUniform4dv',
 'glProgramUniform4f',
 'glProgramUniform4fv',
 'glProgramUniform4i',
 'glProgramUniform4iv',
 'glProgramUniform4ui',
 'glProgramUniform4uiv',
 'glProgramUniformMatrix2dv',
 'glProgramUniformMatrix2fv',
 'glProgramUniformMatrix2x3dv',
 'glProgramUniformMatrix2x3fv',
 'glProgramUniformMatrix2x4dv',
 'glProgramUniformMatrix2x4fv',
 'glProgramUniformMatrix3dv',
 'glProgramUniformMatrix3fv',
 'glProgramUniformMatrix3x2dv',
 'glProgramUniformMatrix3x2fv',
 'glProgramUniformMatrix3x4dv',
 'glProgramUniformMatrix3x4fv',
 'glProgramUniformMatrix4dv',
 'glProgramUniformMatrix4fv',
 'glProgramUniformMatrix4x2dv',
 'glProgramUniformMatrix4x2fv',
 'glProgramUniformMatrix4x3dv',
 'glProgramUniformMatrix4x3fv',
 'glProvokingVertex',
 'glPushDebugGroup',
 'glQueryCounter',
 'glReadBuffer',
 'glReadPixels',
 'glReadnPixels',
 'glReleaseShaderCompiler',
 'glRenderbufferStorage',
 'glRenderbufferStorageMultisample',
 'glResumeTransformFeedback',
 'glSampleCoverage',
 'glSampleMaski',
 'glSamplerParameterIiv',
 'glSamplerParameterIuiv',
 'glSamplerParameterf',
 'glSamplerParameterfv',
 'glSamplerParameteri',
 'glSamplerParameteriv',
 'glScissor',
 'glScissorArrayv',
 'glScissorIndexed',
 'glScissorIndexedv',
 'glShaderBinary',
 'glShaderSource',
 'glShaderStorageBlockBinding',
 'glStencilFunc',
 'glStencilFuncSeparate',
 'glStencilMask',
 'glStencilMaskSeparate',
 'glStencilOp',
 'glStencilOpSeparate',
 'glTexBuffer',
 'glTexBufferRange',
 'glTexImage1D',
 'glTexImage2D',
 'glTexImage3D',
 'glTexParameterIiv',
 'glTexParameterIuiv',
 'glTexParameterf',
 'glTexParameterfv',
 'glTexParameteri',
 'glTexParameteriv',
 'glTexStorage1D',
 'glTexStorage2D',
 'glTexStorage3D',
 'glTexSubImage1D',
 'glTexSubImage2D',
 'glTexSubImage3D',
 'glTextureBarrier',
 'glTextureBuffer',
 'glTextureBufferRange',
 'glTextureParameterIiv',
 'glTextureParameterIuiv',
 'glTextureParameterf',
 'glTextureParameterfv',
 'glTextureParameteri',
 'glTextureParameteriv',
 'glTextureStorage1D',
 'glTextureStorage2D',
 'glTextureStorage3D',
 'glTextureSubImage1D',
 'glTextureSubImage2D',
 'glTextureSubImage3D',
 'glTextureView',
 'glTransformFeedbackBufferBase',
 'glTransformFeedbackBufferRange',
 'glTransformFeedbackVaryings',
 'glUniform1d',
 'glUniform1dv',
 'glUniform1f',
 'glUniform1fv',
 'glUniform1i',
 'glUniform1iv',
 'glUniform1ui',
 'glUniform1uiv',
 'glUniform2d',
 'glUniform2dv',
 'glUniform2f',
 'glUniform2fv',
 'glUniform2i',
 'glUniform2iv',
 'glUniform2ui',
 'glUniform2uiv',
 'glUniform3d',
 'glUniform3dv',
 'glUniform3f',
 'glUniform3fv',
 'glUniform3i',
 'glUniform3iv',
 'glUniform3ui',
 'glUniform3uiv',
 'glUniform4d',
 'glUniform4dv',
 'glUniform4f',
 'glUniform4fv',
 'glUniform4i',
 'glUniform4iv',
 'glUniform4ui',
 'glUniform4uiv',
 'glUniformBlockBinding',
 'glUniformMatrix2dv',
 'glUniformMatrix2fv',
 'glUniformMatrix2x3dv',
 'glUniformMatrix2x3fv',
 'glUniformMatrix2x4dv',
 'glUniformMatrix2x4fv',
 'glUniformMatrix3dv',
 'glUniformMatrix3fv',
 'glUniformMatrix3x2dv',
 'glUniformMatrix3x2fv',
 'glUniformMatrix3x4dv',
 'glUniformMatrix3x4fv',
 'glUniformMatrix4dv',
 'glUniformMatrix4fv',
 'glUniformMatrix4x2dv',
 'glUniformMatrix4x2fv',
 'glUniformMatrix4x3dv',
 'glUniformMatrix4x3fv',
 'glUniformSubroutinesuiv',
 'glUnmapBuffer',
 'glUnmapNamedBuffer',
 'glUseProgram',
 'glUseProgramStages',
 'glValidateProgram',
 'glValidateProgramPipeline',
 'glVertexArrayAttribBinding',
 'glVertexArrayAttribFormat',
 'glVertexArrayBindingDivisor',
 'glVertexArrayElementBuffer',
 'glVertexArrayVertexBuffer',
 'glVertexArrayVertexBuffers',
 'glVertexAttrib1d',
 'glVertexAttrib1dv',
 'glVertexAttrib1f',
 'glVertexAttrib1fv',
 'glVertexAttrib1s',
 'glVertexAttrib1sv',
 'glVertexAttrib2d',
 'glVertexAttrib2dv',
 'glVertexAttrib2f',
 'glVertexAttrib2fv',
 'glVertexAttrib2s',
 'glVertexAttrib2sv',
 'glVertexAttrib3d',
 'glVertexAttrib3dv',
 'glVertexAttrib3f',
 'glVertexAttrib3fv',
 'glVertexAttrib3s',
 'glVertexAttrib3sv',
 'glVertexAttrib4Nbv',
 'glVertexAttrib4Niv',
 'glVertexAttrib4Nsv',
 'glVertexAttrib4Nub',
 'glVertexAttrib4Nubv',
 'glVertexAttrib4Nuiv',
 'glVertexAttrib4Nusv',
 'glVertexAttrib4bv',
 'glVertexAttrib4d',
 'glVertexAttrib4dv',
 'glVertexAttrib4f',
 'glVertexAttrib4fv',
 'glVertexAttrib4iv',
 'glVertexAttrib4s',
 'glVertexAttrib4sv',
 'glVertexAttrib4ubv',
 'glVertexAttrib4uiv',
 'glVertexAttrib4usv',
 'glVertexAttribBinding',
 'glVertexAttribDivisor',
 'glVertexAttribFormat',
 'glVertexAttribI1i',
 'glVertexAttribI1iv',
 'glVertexAttribI1ui',
 'glVertexAttribI1uiv',
 'glVertexAttribI2i',
 'glVertexAttribI2iv',
 'glVertexAttribI2ui',
 'glVertexAttribI2uiv',
 'glVertexAttribI3i',
 'glVertexAttribI3iv',
 'glVertexAttribI3ui',
 'glVertexAttribI3uiv',
 'glVertexAttribI4bv',
 'glVertexAttribI4i',
 'glVertexAttribI4iv',
 'glVertexAttribI4sv',
 'glVertexAttribI4ubv',
 'glVertexAttribI4ui',
 'glVertexAttribI4uiv',
 'glVertexAttribI4usv',
 'glVertexAttribL1d',
 'glVertexAttribL1dv',
 'glVertexAttribL2d',
 'glVertexAttribL2dv',
 'glVertexAttribL3d',
 'glVertexAttribL3dv',
 'glVertexAttribL4d',
 'glVertexAttribL4dv',
 'glVertexAttribP1ui',
 'glVertexAttribP1uiv',
 'glVertexAttribP2ui',
 'glVertexAttribP2uiv',
 'glVertexAttribP3ui',
 'glVertexAttribP3uiv',
 'glVertexAttribP4ui',
 'glVertexAttribP4uiv',
 'glVertexAttribPointer',
 'glVertexBindingDivisor',
 'glViewport',
 'glViewportArrayv',
 'glViewportIndexedf',
 'glViewportIndexedfv',
 'glWaitSync'}
