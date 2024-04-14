from gl import *
from glconstants import *
from DataTexture2DArray import *
from Program import Program
import BufferManager
from math2801 import *
from ImageTexture2DArray import *
import random

class Cloth:
    updateprog=None
    drawprog=None
    def __init__(self):
        self.n = 64
        self.K = 50
        self.mass = 0.05
        self.gravity = vec3(0,-9.81,0)
        self.damping = .05
        self.time = 0.0001
        self.wind = vec3(.20,0.5,-.20)
        self.data = DataTexture2DArray(self.n, self.n, 4, GL_RGBA32F, 
            GL_RGBA, GL_FLOAT)
        self.data.setData( bytes(self.n*self.n*16*4), GL_RGBA, GL_FLOAT )
        self.data.bind(0)
        glGenerateMipmap(GL_TEXTURE_2D_ARRAY)
        self.data.unbind(0)
        
        self.currentSlice=0     #tells which pair in data to use

        if Cloth.updateprog == None:
            Cloth.updateprog = Program(cs="clothcs.txt")
            Cloth.drawprog = Program(
                vs="clothvs.txt",fs="clothfs.txt"
            )
                
        self.accumulatedTime=0
        self.timeScale=1        #can tweak
        self.makeGridMesh()
        self.worldMatrix = (
                scaling(6/self.n,1/self.n,6/self.n) * 
                translation(8.9,-.05,-4)
            )
        self.inverseWorldMatrix =  (
                translation(0.5,0,0.5) * 
                scaling(self.n,self.n,self.n)
        ) 
            
        self.tex = ImageTexture2DArray("cloth.png")
        
        self.sphere = vec4(0,-0.36,.5,0.10)
        Program.setUniform("clothSphere", self.sphere)
        
        self.clear()
        
        self.R = random.Random(123)
        self.timeToNextWindChange=1

    def clear(self):
        Program.setUniform("clothCurrentSlice",0)
        Program.setUniform("clothInitialize",1)
        self.setUniforms()
        self.updateprog.use()
        self.data.bindImage(0)
        self.updateprog.dispatch(
            int(self.n//64),self.n,1)
        sync = glFenceSync(GL_SYNC_GPU_COMMANDS_COMPLETE,0)
        glClientWaitSync(sync,GL_SYNC_FLUSH_COMMANDS_BIT,-1)
        glDeleteSync(sync)
        glMemoryBarrier(GL_ALL_BARRIER_BITS)
        self.currentSlice = 0
        self.accumulatedTime = 0
        Program.setUniform("clothInitialize",0)

        
    def update(self,elapsed):
        
        self.timeToNextWindChange -= elapsed
        if self.timeToNextWindChange <= 0:
            self.wind = vec3( self.R.uniform( -10/3,20/3 ),
                              self.R.uniform( -3/3,5/3),
                              self.R.uniform( -5/3,5/3 ) )
            self.timeToNextWindChange = self.R.uniform(0,1)
            
        
        self.accumulatedTime += self.timeScale*elapsed
        self.setUniforms()
        self.updateprog.use()
        self.data.bindImage(0)
        while self.accumulatedTime >= self.time:
            Program.setUniform("clothCurrentSlice",
                self.currentSlice)
            self.updateprog.dispatch(
                int(self.n//64),self.n,1)
            sync = glFenceSync(GL_SYNC_GPU_COMMANDS_COMPLETE,0)
            glClientWaitSync(sync,GL_SYNC_FLUSH_COMMANDS_BIT,-1)
            glDeleteSync(sync)
            glMemoryBarrier(GL_ALL_BARRIER_BITS)
            self.currentSlice = 1-self.currentSlice
            self.accumulatedTime -= self.time

    def setUniforms(self):
        Program.setUniform("clothSpringK",self.K)
        Program.setUniform("clothMass",self.mass)
        Program.setUniform("clothGravity",self.gravity)
        Program.setUniform("clothWind",self.wind)
        Program.setUniform("clothDamping",self.damping)
        Program.setUniform("clothTime",self.time)
        Program.setUniform("clothN",self.n)
        Program.setUniform("worldMatrix", self.worldMatrix)
        Program.setUniform("clothInverseWorldMatrix", self.inverseWorldMatrix)
        
    def draw(self):
        self.setUniforms()
        oldprog = Program.current
        Cloth.drawprog.use()
        self.tex.bind(0)
        self.data.bind(1)
        Program.setUniform("clothCurrentSlice",1-self.currentSlice)
        glDrawElementsBaseVertex(GL_TRIANGLES, self.numIndices,
            GL_UNSIGNED_INT, self.indexStart, self.vertexOffset)
        if oldprog:
            oldprog.use()

    def makeGridMesh(self):
        pos=[]; norms=[]; texc=[]
        for i in range(self.n):
            for j in range(self.n):
                pos += [j,0,i]
                norms += [0,0,0]
                texc += [j/(self.n-1),i/(self.n-1)]
        indices = []
        for i in range(self.n-1):
            for j in range(self.n-1):
                #   a +--+ b
                #     | /|
                #     |/ |
                #   c +--+ d
                a = i*self.n + j; b = a+1
                c = a + self.n; d = c+1
                indices += [a,c,b]
                indices += [b,c,d]                
        self.numIndices=len(indices)
        self.vertexOffset,self.indexStart = (
            BufferManager.addIndexedData(
                positiondata=pos, texturedata=texc,
                normaldata=norms,indexdata=indices)
        )              

