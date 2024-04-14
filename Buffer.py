from gl import *
from glconstants import *
import array

class Buffer:
    def __init__(self,data,usage=GL_STATIC_DRAW):
        tmp = array.array("I", [0] )
        glGenBuffers(1,tmp)
        self.buffID = tmp[0]
        glBindBuffer( GL_ARRAY_BUFFER, self.buffID )
        assert type(data) == array.array
        tmp = data.tobytes()
        glBufferData( GL_ARRAY_BUFFER, len(tmp), tmp, usage)
        glBindBuffer( GL_ARRAY_BUFFER, 0 )
    def bind(self,target):
        glBindBuffer(target, self.buffID )
    def bindBase(self,target,index):
        glBindBufferBase(target,index,self.buffID )

