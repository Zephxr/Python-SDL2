import sys
import os
import os.path
import traceback
import array

############################

#sys.path.append( os.path.join( os.path.dirname(__file__),"..","..","lib"))

if "PYSDL2_DLL_PATH" not in os.environ:
    os.environ["PYSDL2_DLL_PATH"] = os.path.join( os.path.dirname(__file__),"bin")

import pysdl2.sdl2 as sdl2
import gl
import glconstants
import image


def debugCallback( source, msgType, msgId, severity, length,
    message, param ):
        
    #don't print shader compile errors; these are reported through the Program object
    if source == glconstants.GL_DEBUG_SOURCE_SHADER_COMPILER and severity == glconstants.GL_DEBUG_SEVERITY_HIGH:
        print("Shader error (check shader log for more information)")
        return
    
    print(msgId,":",message)
    if severity == glconstants.GL_DEBUG_SEVERITY_HIGH:
        S = traceback.extract_stack()
        L = S.format()
        flagged=False
        for i in range(len(S)):
            x=S[i]
            if x.filename.split(os.path.sep)[-1] == "gl.py" and not flagged:
                break
                # ~ print("+================================================+")
                # ~ print("| Frames below this point are from the libraries |")
                # ~ print("| and are likely not interesting to you.         |")
                # ~ print("+================================================+")
                # ~ flagged=True
            print(L[i],end="")


def createWindow(**kw):
    """Call this to create the window + OpenGL context. Supported keyword
    arguments include the following (defaults are in parentheses):
        width       Width of window (512)
        height      Height of window (512)
        depth       Depth buffer size (24)
        stencil     Stencil buffer size (8)
        glMajor     OpenGL major version (4)
        glMinor     OpenGL minor version (3)
        debug       If False, do not try to create a debug context and
                    don't setup debug callbacks (True)
        msbuffers   Number of multisample buffers (1)
        mssamples   Number of multisample samples (4)
    """
    
    GL_VERSION = kw.get("glMajor",4), kw.get("glMinor",3)
    
    sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO)
    sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_PROFILE_MASK, sdl2.SDL_GL_CONTEXT_PROFILE_CORE)
    sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_DEPTH_SIZE, kw.get("depth",24) )
    sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_STENCIL_SIZE, kw.get("stencil",8) )
    sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_ALPHA_SIZE, kw.get("alpha",8) )
    sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MAJOR_VERSION, kw.get("glMajor", 4) )
    sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MINOR_VERSION, kw.get("glMinor", 3) )
    if kw.get("debug",True):
        sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_FLAGS, sdl2.SDL_GL_CONTEXT_DEBUG_FLAG)
    sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_PROFILE_MASK, sdl2.SDL_GL_CONTEXT_PROFILE_CORE)
    if kw.get("ms",True):
        sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_MULTISAMPLEBUFFERS,kw.get("msbuffers",1) )
        sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_MULTISAMPLESAMPLES,kw.get("mssamples",4) )
    win = sdl2.SDL_CreateWindow( b"ETGG",20,20, kw.get("width",512), kw.get("height",512), sdl2.SDL_WINDOW_OPENGL)
    if not win: 
        raise RuntimeError("Could not create window for GL {}.{}".format(GL_VERSION[0], GL_VERSION[1]))
        return

    rc = sdl2.SDL_GL_CreateContext(win)
    if not rc:
        raise RuntimeError("Cannot create GL context")
        
    if kw.get("debug",True):
        gl.glDebugMessageCallback( debugCallback, None )
        
        # Source, type, severity, count, ids, enabled
        gl.glDebugMessageControl(glconstants.GL_DONT_CARE, glconstants.GL_DONT_CARE, glconstants.GL_DONT_CARE,
            0, None, True )
            
        gl.glEnable(glconstants.GL_DEBUG_OUTPUT_SYNCHRONOUS)
        gl.glEnable(glconstants.GL_DEBUG_OUTPUT)

    if os.getenv("GRADE_2801"):
        drew=0
        def da(*args):
            print("NOTE: Using glDrawArrays")
        gl.addGLHook("glDrawArrays", da )
        #gl.addGLHook("glDrawElementsBaseVertex", da )
       
    
    clearcount=0
    printOnExpensiveOperations=False
    def cl(*args):
        nonlocal clearcount,printOnExpensiveOperations
        if clearcount < 2:
            clearcount+=1
        elif clearcount == 2:
            printOnExpensiveOperations=True
            clearcount +=1
        else:
            pass
        
        
    gl.addGLHook("glClear", cl )
    
    def mkverbose(funcname):
        def func(*a):
            if printOnExpensiveOperations:
                print("NOTE: Called",funcname)
        return func
    
    for f in ["glGenBuffers","glBufferData","glGenTextures","glTexImage1D",
                    "glTexImage2D","glTexImage3D"]:
        gl.addGLHook(f,  mkverbose(f) )
        
    return win


def screenshot(filename):
    """Get a screenshot of the current window contents and write it
       to the given file as a PNG image."""
       
    tmp = array.array("I",[0]*4)
    gl.glGetIntegerv( glconstants.GL_VIEWPORT, tmp)
    w,h = tmp[2:4]
    pix = bytearray(w*h*4)
    gl.glReadPixels(0,0,w,h,glconstants.GL_RGBA,glconstants.GL_UNSIGNED_BYTE,pix)
    stride = w*4
    for y in range(h//2):
        i = y*stride
        j = (h-y-1)*stride
        tmp = pix[i:i+stride]
        pix[i:i+stride] = pix[j:j+stride]
        pix[j:j+stride] = tmp
    p = image.encodePNG(w,h,"RGBA8",pix)
    with open(filename,"wb") as fp:
        fp.write(p)
    
