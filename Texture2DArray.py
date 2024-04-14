from glconstants import *
from Texture import Texture

class Texture2DArray(Texture):
    def __init__(self,w,h,slices):
        Texture.__init__(self,GL_TEXTURE_2D_ARRAY)
        self.w=w
        self.h=h
        self.slices=slices
