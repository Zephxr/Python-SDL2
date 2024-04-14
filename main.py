#this one *must* be first
import etgg2801

import pysdl2.sdl2 as sdl2
import pysdl2.sdl2.keycode as keycode
from gl import *
from glconstants import *
import time
from Globals import GlobalVars
import ctypes
import BufferManager
import math
from Program import Program
from Sampler import MipSampler,NearestSampler
from ImageTexture2DArray import ImageTexture2DArray
from math2801 import *
from Camera import Camera
from FullScreenQuad import FullScreenQuad
from GLTFMesh import GLTFMesh
import Text
import Lights
from Cloth import Cloth

def main():
    win = etgg2801.createWindow(width=1920, height=1080)
    print( glGetString(GL_RENDERER), glGetString(GL_VENDOR), glGetString(GL_VERSION), glGetString(GL_SHADING_LANGUAGE_VERSION))  
    globs = GlobalVars()
    setup(globs)
    last = time.time_ns()/1000000000
    DESIRED_FRAMES_PER_SEC = 60
    DESIRED_SEC_PER_FRAME = 1/DESIRED_FRAMES_PER_SEC
    QUANTUM = 0.005
    accumulated=0
    while True:
        now = time.time_ns()/1000000000
        elapsed = now-last
        last=now
        accumulated += elapsed
        while accumulated >= QUANTUM:
            update(QUANTUM,globs)
            accumulated -= QUANTUM
        draw(globs)
        sdl2.SDL_GL_SwapWindow(win)
        end = time.time_ns()/1000000000
        frameTime=end-now
        leftover = DESIRED_SEC_PER_FRAME - frameTime
        if leftover > 0:
            time.sleep(leftover)
        
        
def setup(globs):
    
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    
    globs.keys=set()
    globs.mouseLook=True
    sdl2.SDL_SetRelativeMouseMode(1)
    
    globs.prog = Program(vs="vs.txt",
                    fs="fs.txt")  
    
    globs.camera = Camera(vec3(0,1,2), vec3(0,1,0), vec3(0,1,0) )
    
    
    globs.meshes=[]
    
    fname = os.path.join(
        os.path.dirname(__file__),
        "bigassets",
        "kitchen.gltf")
    
    globs.meshes.append(GLTFMesh(fname))
    
    lightdata = Lights.parseLights(fname)
    
    lightPositionsAndDirectionalFlag=[None]*len(lightdata)
    spotDirectionsAndCosineSpotEdgeStarts=[None]*len(lightdata)
    lightColorsAndCosineSpotAngleCutoffs=[None]*len(lightdata)

    
    for i in range(len(lightdata)):
        lightPositionsAndDirectionalFlag[i] = vec4( lightdata[i].position,1.0 )
        spotDirectionsAndCosineSpotEdgeStarts[i] = vec4(0,-1,0, math.cos(math.radians(lightdata[i].spotCutoffStart) ) )
        lightColorsAndCosineSpotAngleCutoffs[i] = vec4( lightdata[i].energy* vec3(*lightdata[i].color), math.cos(math.radians(lightdata[i].spotCutoffEnd) ) ) 
    
    
    Program.setUniform( "lightPositionsAndDirectionalFlag[0]", lightPositionsAndDirectionalFlag )
    Program.setUniform( "spotDirectionsAndCosineSpotEdgeStarts[0]", spotDirectionsAndCosineSpotEdgeStarts)
    Program.setUniform( "lightColorsAndCosineSpotAngleCutoffs[0]", lightColorsAndCosineSpotAngleCutoffs)
    Program.setUniform( "attenuation", vec3(450,0,3.5) )
    Program.setUniform("alphaFactor",1.0)
    Program.setUniform("animationFrame",1.0)
    
    mipSampler = MipSampler()
    mipSampler.bind(0)          #color texture
    mipSampler.bind(1)          #emission texture
    
    nearestSampler = NearestSampler()
    nearestSampler.bind(15)     #for text
    
    glClearColor(0,0,0,1)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA,GL_ONE_MINUS_SRC_ALPHA)
    
    globs.cloth = Cloth()

    Text.initialize()
    updateText(globs)
    BufferManager.pushToGPU()


def updateText(globs):
    if globs.mouseLook:
        state="off"
    else:
        state="on "
        
    Text.print(0,f"Tab=Mouselook {state}")
    Text.print(1, "WASD=walk/strafe  QE=turn RF=up/down")


def update(elapsed,globs):
    
    
    pumpEvents(globs)

    globs.cloth.update(elapsed)

    if keycode.SDLK_w in globs.keys:
        globs.camera.strafeNoUpOrDown(0,0,2.0*elapsed)
    if keycode.SDLK_s in globs.keys:
        globs.camera.strafeNoUpOrDown(0,0,-2.0*elapsed)
    if keycode.SDLK_a in globs.keys:
        globs.camera.strafeNoUpOrDown(-2.0*elapsed,0,0)
    if keycode.SDLK_d in globs.keys:
        globs.camera.strafeNoUpOrDown(2.0*elapsed,0,0)
    if keycode.SDLK_q in globs.keys:
        globs.camera.turn(elapsed)
    if keycode.SDLK_e in globs.keys:
        globs.camera.turn(-elapsed)
    if keycode.SDLK_r in globs.keys:
        globs.camera.strafeXYZ(0,elapsed,0)
    if keycode.SDLK_f in globs.keys:
        globs.camera.strafeXYZ(0,-elapsed,0)
        


def pumpEvents(globs):
    ev = sdl2.SDL_Event()
    while True:
        eventOccurred = sdl2.SDL_PollEvent(ctypes.byref(ev))
        if not eventOccurred:
            return
        if ev.type == sdl2.SDL_QUIT:
            sdl2.SDL_Quit()
            sys.exit(0)
        if ev.type == sdl2.SDL_KEYDOWN:
            if ev.key.keysym.sym == keycode.SDLK_F1:
                etgg2801.screenshot("screenshot.png")
                print("Wrote screenshot.png")
            elif ev.key.keysym.sym == keycode.SDLK_TAB:
                globs.mouseLook = not globs.mouseLook
                if globs.mouseLook:
                    sdl2.SDL_SetRelativeMouseMode(1)
                else:
                    sdl2.SDL_SetRelativeMouseMode(0)
                updateText(globs)
            elif ev.key.keysym.sym == keycode.SDLK_ESCAPE:
                sdl2.SDL_Quit()
                sys.exit(0)
            globs.keys.add( ev.key.keysym.sym )
        if ev.type == sdl2.SDL_KEYUP:
            globs.keys.discard( ev.key.keysym.sym )
        if ev.type == sdl2.SDL_MOUSEMOTION:
            if globs.mouseLook:
                globs.camera.turnAroundAxis(vec3(0,1,0),  -0.01*ev.motion.xrel,  )
                globs.camera.pitch( -0.01*ev.motion.yrel)




def draw(globs):
    
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    BufferManager.bind()
    globs.prog.use()
    
     
    globs.camera.setUniforms()
    
    Program.setUniform("alphaFactor",1.0)
    Program.setUniform("animationFrame",1.0)
    Program.setUniform("worldMatrix",mat4.identity())
    
    for m in globs.meshes:
        m.draw()

    globs.cloth.draw()

    Text.draw()
  
main()
