from PIL import Image
import numpy as np
from geojson import Polygon as poly

def clamp(x):
    return max(0, min(x, 255))

map = Image.open('ozone.png')
scale = Image.open('scale.png')
rgb_map = map.convert('RGB')
rgb_scale = scale.convert('RGB')

pixeltoDOB = 1.0050251256


scaleVals = np.zeros((398,40), dtype=object)
mapVals = np.zeros((2048,4096), dtype=object)


for x in range(398):
    #scaleVals.append([])
    for y in range(40):
        r, g, b = rgb_scale.getpixel((x, y))
        scaleVals[x][y] = (r,g,b)
        #scaleVals[x][y] = ("#{0:02x}{1:02x}{2:02x}".format(clamp(r), clamp(g), clamp(b)))

for y in range(2048):
    #mapVals.append([])
    for x in range(4096):
        r, g, b = rgb_map.getpixel((x, y))
        mapVals[y][x] = (r,g,b)
        ##mapVals[y][x] = ("#{0:02x}{1:02x}{2:02x}".format(clamp(r), clamp(g), clamp(b)))
        #mapVals[x][y] = " " + r + " " + b + " " + ""


ozoneVals = np.zeros((2048,4096))

for i in range(128):
    for j in range(256):
        for k in range(398):
            for l in range(40):
                print(i,j,k,l)
                if (mapVals[i][j]) == (scaleVals[k][l]):
                    ozoneVals[i][j] = pixeltoDOB * k

print(mapVals[2][128]) ##just to see if it works





