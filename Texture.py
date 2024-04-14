from gl import *
from glconstants import *

class Texture:
    def __init__(self, typ):
        self.type = typ
        self.tex = None
    def bind(self,unit):
        glActiveTexture(GL_TEXTURE0 + unit)
        glBindTexture(self.type,self.tex)
    def unbind(self,unit):
        glActiveTexture(GL_TEXTURE0 + unit)
        glBindTexture(self.type,0)
