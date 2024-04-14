from gl import *
from glconstants import *
from Texture2DArray import Texture2DArray
import io
import image
import zipfile

class ImageTexture2DArray(Texture2DArray):
    def __init__(self, *files):
        super().__init__(0,0,0)
        
        membuf = io.BytesIO()
        
        for fname in files:
            for folder in ["assets","bigassets"]:
                fname1 = os.path.join(os.path.dirname(__file__),folder,fname)
                if os.path.exists(fname1):
                    fname=fname1
                    break
            if fname.endswith(".png") or fname.endswith(".jpg"):
                self.loadImage(membuf,fname)
            elif fname.endswith(".ora") or fname.endswith(".zip"):
                self.loadZip(membuf,fname)
            else:
                raise RuntimeError("Cannot read file "+fname)
        
        self.pushToGPU( membuf )
        
    def loadImage(self,membuf,fname):
        with open(fname,"rb") as fp:
            tmp = fp.read()
        self.addImageDataToBuffer(membuf,tmp)

    def loadZip(self,membuf,fname):
        z = zipfile.ZipFile(fname)
        for n in sorted(z.namelist()):
            if n.lower().endswith(".png") or n.lower().endswith(".jpg"):
                tmp = z.open(n).read()
                self.addImageDataToBuffer( membuf, tmp )

    def addImageDataToBuffer(self,membuf,img):
        pw,ph,fmt,pix = image.decode(img)
        # ~ pix = image.flipY(pw,ph,pix)
        if self.w == 0:
            self.w=pw
            self.h=ph
        else:
            if self.w != pw or self.h != ph:
                raise RuntimeError("Size mismatch")
        self.slices += 1
        membuf.write(pix)
        
    def pushToGPU(self,membuf):
        tmp = array.array("I",[0])
        glGenTextures(1,tmp)
        self.tex = tmp[0]
        self.bind(0)
        glTexImage3D( GL_TEXTURE_2D_ARRAY, 0, GL_RGBA8, self.w, 
                      self.h, self.slices, 0, GL_RGBA, GL_UNSIGNED_BYTE, 
                      membuf.getbuffer() )
        glGenerateMipmap(GL_TEXTURE_2D_ARRAY)
        self.unbind(0)

