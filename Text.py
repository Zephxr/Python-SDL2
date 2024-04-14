
from FullScreenQuad import FullScreenQuad
from gl import *
from glconstants import *
from ImageTexture2DArray import ImageTexture2DArray
from DataTexture2DArray import DataTexture2DArray
from Program import Program

def initialize():
    global fsq
    fsq = FullScreenQuad()
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    global tex
    tex = ImageTexture2DArray("consolefont14.ora")
    global prog
    prog = Program(vs="textvs.txt",fs="textfs.txt")
    global rows
    rows=512//20
    global cols
    cols=512//10
    global chars
    chars = bytearray( rows*cols )
    global charTex
    charTex = DataTexture2DArray( cols,rows,1,
            GL_R8I, GL_RED_INTEGER, GL_BYTE )
    global dirty
    dirty = True
    
def putChar( row, col, c):
    global chars,dirty,cols
    idx = row*cols+col
    chars[idx] = ord(c)
    dirty = True
    
    
def print(row, *args):
    col=0
    for word in args:
        for char in word:
            putChar(row,col,char)
            col+=1
        col+=1
            
def clear():
    global chars,dirty
    chars = bytearray( rows*cols )
    dirty=True
    
def draw():
    global dirty, charTex, chars, prog, tex, charTex, fsq
    if dirty:
        dirty=False
        charTex.setData(chars,
            GL_RED_INTEGER, GL_BYTE)
    oldprog = Program.current
    prog.use()
    tex.bind(0)
    charTex.bind(15)
    fsq.draw()
    if oldprog:
        oldprog.use()
