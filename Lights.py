#helper class for parsing light info from a GLTF file

import collections
import json
import math
import pprint
from math2801 import *

Light = collections.namedtuple("Light",
    "position spotCutoffStart spotCutoffEnd energy color name"
)
    
def parseLights(gltffile):
    with open(gltffile) as fp:
        data=fp.read()
        
    allLights=[]
    
    J=json.loads(data)
    lightlist = J["extensions"]["KHR_lights_punctual"]["lights"]
    for lightinfo in lightlist:
        color=lightinfo["color"]
        typ=lightinfo["type"]
        if typ == "spot":
            spotCutoffStart=math.degrees(lightinfo["spot"]["innerConeAngle"])
            spotCutoffEnd=math.degrees(lightinfo["spot"]["outerConeAngle"])
        elif typ == "point":
            spotCutoffStart=180
            spotCutoffEnd=180
        else:
            print("For",lightinfo["name"],": Unknown type:",typ)
        name=lightinfo["name"]
        energy=lightinfo["intensity"]
        allLights.append( Light( 
            position=None, spotCutoffStart=spotCutoffStart,
            spotCutoffEnd=spotCutoffEnd, energy=energy,
            color=color,name=name) )
            
    
    N = J["nodes"]
    
    nodeParents={}
    for i,n in enumerate(N):
        for c in n.get("children",[]):
            nodeParents[c] = i
            
    for ni,n in enumerate(N):
        if "extensions" in n and "KHR_lights_punctual" in n["extensions"]:
            lightIndex = n["extensions"]["KHR_lights_punctual"]["light"]
            position = vec3(0,0,0)
            
            i = ni
            while True:
                if  "translation" in N[i]:
                    tr = N[i]["translation"]
                    position.x += tr[0]
                    position.y += tr[1]
                    position.z += tr[2]
                if i not in nodeParents:
                    break
                i = nodeParents[i]
                
            allLights[lightIndex] = allLights[lightIndex]._replace(position=position)

    return allLights
    
    
if __name__ == "__main__":
    import sys
    L = parseLights(sys.argv[1])
    pprint.pprint(L)
    print(len(L),"lights")
    
    
    
                    
