from gl import *
from glconstants import *

class Sampler:
    def __init__(self):
        tmp = array.array("I",[0])
        glGenSamplers(1,tmp)
        self.samp = tmp[0]
    def bind(self,unit):
        glBindSampler(unit, self.samp )

class NearestSampler(Sampler):
    def __init__(self):
        super().__init__()
        glSamplerParameteri( self.samp,
                GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
        glSamplerParameteri( self.samp,
                GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
        glSamplerParameteri( self.samp,
                GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glSamplerParameteri( self.samp,
                GL_TEXTURE_MIN_FILTER, GL_NEAREST)


class MipSampler(Sampler):
    def __init__(self):
        super().__init__()
        glSamplerParameteri( self.samp,
                GL_TEXTURE_WRAP_S, GL_REPEAT)
        glSamplerParameteri( self.samp,
                GL_TEXTURE_WRAP_T, GL_REPEAT)
        glSamplerParameteri( self.samp,
                GL_TEXTURE_MAG_FILTER, GL_LINEAR) 
        glSamplerParameteri( self.samp,
                GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR) 
