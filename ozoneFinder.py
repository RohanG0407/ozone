from PIL import Image
import numpy as np
from geojson import GeometryCollection, Polygon, Point, Feature, dump, FeatureCollection
import webcolors

def clamp(x):
    return max(0, min(x, 255))

def xChange(x):
    return((5.625*x)-180)
def yChange(y):
    return((-5.625*y)+90)

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

for y in range(2048):
    #mapVals.append([])
    for x in range(4096):
        r, g, b = rgb_map.getpixel((x, y))
        mapVals[y][x] = (r,g,b)


ozoneVals = np.zeros((32,64))

features = []
counter = 0
tempPoly = []
for i in range(4):
    for j in range(8):
        for k in range(398):
            for l in range(40):
                print(i,j,k,l)
                if (mapVals[j][i]) == (scaleVals[k][l]):
                    ozoneVals[i][j] = pixeltoDOB * k
        poly = Polygon([[(xChange(j),yChange(i)), (xChange(j+1), yChange(i)) , (xChange(j+1), yChange(i+1)) ,(xChange(j), yChange(i+1)), (xChange(j), yChange(i))]])
        color = (mapVals[(j*32)][(i*32)])
        print(color)
        hex = webcolors.rgb_to_hex(color)
        print(hex)
        features.append(Feature(geometry=poly, properties={"country": "Spain", "fill": hex}))

# add more features...

feature_collection = FeatureCollection(features)

with open('myfile.geojson', 'w') as f:
    dump(feature_collection, f)
