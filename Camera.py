from math2801 import *
from Program import *
import math

class Camera:
    def __init__(self,eye,coi,up):
        self.lookAt(eye,coi,up)
        self.hither=0.01
        self.yon=500
        self.fov = 35       #half angle, in degrees
        self.aspectRatio=1
        self.updateProjMatrix()
        self.setUniforms()
        
    def updateProjMatrix(self):
        hither=self.hither
        yon=self.yon
        d_h = 1.0/math.tan(self.fov/180*math.pi)
        d_v = 1.0/math.tan(self.aspectRatio*self.fov/180*math.pi)
        
        self.projMatrix = mat4(
            d_h,0,0,0,
            0,d_v,0,0,
            0,0,(2*yon)/(hither-yon)+1,-1,
            0,0,(2*hither*yon)/(hither-yon),0)
            
    def lookAt(self,eye,coi,up):
        self.eye = vec4(eye.x, eye.y, eye.z,1)
        self.coi = vec4(coi.x, coi.y, coi.z,1)
        self.look = normalize(self.coi-self.eye)
        self.right = normalize(
            cross(self.look,vec4(up.x,up.y,up.z,0) )
        )
        self.up = cross(self.right,self.look)
        self.updateViewMatrix()
        
    def updateViewMatrix(self):
        cr = -dot(self.eye,self.right)
        cu = -dot(self.eye,self.up)
        cl = dot( self.eye,self.look)
        
        self.viewMatrix = mat4(
            self.right.x, self.up.x, -self.look.x, 0,
            self.right.y, self.up.y, -self.look.y, 0,
            self.right.z, self.up.z, -self.look.z, 0,
            cr,           cu,        cl,           1 ) 
            
    def setUniforms(self):
        #assuming shader does p * M
        Program.setUniform("viewMatrix",self.viewMatrix)
        Program.setUniform("projMatrix",self.projMatrix)
        Program.setUniform("eyePos", self.eye.xyz )
        
    def tilt(self,amt):
        M = axisRotation(self.look, amt)
        self.right = self.right * M
        self.up = self.up * M
        self.updateViewMatrix()
        
    def pan(self,dx,dy):
        self.coi.x += dx
        self.coi.y += dy
        self.updateViewMatrix()
    
    def turn(self, amt): 
        self.yaw(amt)
        
    def walk(self, amt):
        self.strafe(0,0,amt)
        
    def strafe(self,deltaRight, deltaUp, deltaLook):
        self.eye += deltaRight * self.right
        self.eye += deltaUp * self.up
        self.eye += deltaLook * self.look
        self.updateViewMatrix()
        
    def strafeXYZ(self,dX,dY,dZ):
        self.eye += vec4( dX, dY, dZ, 0 )
        self.updateViewMatrix()

    def strafeNoUpOrDown(self,dr,du,dl):
        delta = dr * self.right + du * self.up + dl * self.look
        delta.y = 0
        self.eye += delta 
        self.updateViewMatrix()

    def roll(self, amt):
        M = axisRotation( self.look, amt )
        self.right = self.right * M
        self.up = self.up * M
        self.updateViewMatrix()

    def pitch(self, amt):
        M = axisRotation( self.right, amt )
        self.look = self.look * M
        self.up = self.up * M
        self.updateViewMatrix()
        
    def yaw(self, amt):
        M = axisRotation( self.up, amt )
        self.look = self.look * M
        self.right = self.right * M
        self.updateViewMatrix()

    def turnAroundAxis(self, axis, amt):
        M = axisRotation(axis,amt)
        self.look = self.look * M
        self.right = self.right * M
        self.up = self.up * M
        self.updateViewMatrix()
