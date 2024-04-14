import os.path
from gl import *
from glconstants import *
import itertools
import BufferManager
from ImageTexture2DArray import ImageTexture2DArray

class Mesh:
    
    def __init__(self,fname):
        
        positions = []
        texes = []
        normals = []
        indices = []
        materials = {}
        mtlname = None
        
        for folder in ["assets","bigassets"]:
            p = os.path.join(os.path.dirname(__file__),folder,fname)
            if os.path.exists(p):
                break
        with open(p) as fp:
            for line in fp:
                line = line.strip()
                if line.startswith("v "):
                    positions.append( [float(q) for q in line.split()[1:]] )
                elif line.startswith("vn "):
                    normals.append( [float(q) for q in line.split()[1:]] )
                elif line.startswith("vt "):
                    texes.append( [float(q) for q in line.split()[1:]] )
                elif line.startswith("f "):
                    lst = line.split()[1:]
                    if len(lst) != 3:
                        raise RuntimeError("Mesh {} has non-triangles".format(fname))
                    for s in lst:
                        tmp = s.split("/")
                        vi = int(tmp[0])-1
                        if len(tmp) < 2:
                            raise RuntimeError("Missing texture cooordinates in {}".format(fname))
                        ti = int(tmp[1])-1
                        ni = int(tmp[2])-1
                        indices.append( (vi,ti,ni) )
                elif line.startswith("mtllib "):
                    mtlfile = line.split(" ",1)[1]
                    self.parseMaterialFile( mtlfile, materials )
                elif line.startswith("usemtl "):
                    mtlname = line.split(" ",1)[1]                            
            
    
        if mtlname == None:
            raise RuntimeError("No texture on mesh {}".format(fname))
        elif mtlname not in materials:
            raise RuntimeError(
                "No texture for material {} on mesh {}".format(mtlname,
                fname))
        else:
            self.tex = ImageTexture2DArray( materials[mtlname] )
            
        vertexMap = {}
        remappedPosData = []
        remappedTexData = []
        remappedNormData = []
        remappedIndices = []
        n = 0
        for vertexSpec in indices:
            if vertexSpec not in vertexMap:
                vi,ti,ni = vertexSpec
                remappedPosData += positions[vi]
                remappedTexData += texes[ti]
                remappedNormData += normals[ni]
                vertexMap[vertexSpec] = n
                n += 1
            remappedIndices.append( vertexMap[vertexSpec] )
            
        self.vertexOffset, self.indexStart = BufferManager.addIndexedData(
            positiondata=remappedPosData,
            texturedata=remappedTexData,
            normaldata=remappedNormData,
            indexdata=remappedIndices
        )
        self.numIndices = len(remappedIndices)
        
    def parseMaterialFile( self, mtlfile, materials):
        for folder in ["assets","bigassets"]:
            p = os.path.join(os.path.dirname(__file__),folder,mtlfile)
            if os.path.exists(p):
                break

        with open(p) as fp:
            for line in fp:
                line = line.strip()
                if line.startswith("newmtl"):
                    currmtl = line.split()[1]
                elif line.startswith("map_Kd"):
                    materials[currmtl] = line.split(" ",1)[1]
                
    

    def draw(self):
        self.tex.bind(0)
        glDrawElementsBaseVertex( GL_TRIANGLES, self.numIndices,
            GL_UNSIGNED_INT, self.indexStart, self.vertexOffset )

