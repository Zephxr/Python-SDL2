#DataTexture2DArray.py

from Texture2DArray import Texture2DArray
import array
from gl import *
from glconstants import *

class DataTexture2DArray(Texture2DArray):
    def __init__(self, w,h,slices, iformat, eformat, etype):
        super().__init__(w,h,slices)
        tmp = array.array("I",[0])
        glGenTextures(1,tmp)
        self.tex = tmp[0]
        self.bind(0)
        self.ifmt=iformat
        glTexImage3D( GL_TEXTURE_2D_ARRAY, 0, iformat,
            self.w, self.h, self.slices, 0, eformat, etype, None )
        self.unbind(0)
    def setData(self, data, eformat, etype):
        self.bind(0)
        glTexSubImage3D(GL_TEXTURE_2D_ARRAY, #target
            0, #mip level
            0, 0, 0, #x,y,z
            self.w, self.h, self.slices,
            eformat, etype, data )
        self.unbind(0)
    def bindImage(self,idx):
        glBindImageTexture(idx, self.tex, 
            0,1,0,          #mipLevel, isLayered, layerNum
            GL_READ_WRITE,  #permissions
            self.ifmt)
