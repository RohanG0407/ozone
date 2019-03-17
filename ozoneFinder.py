from PIL import Image
import numpy as np
from geojson import GeometryCollection, Polygon, Point, Feature, dump, FeatureCollection

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

for y in range(32):
    #mapVals.append([])
    for x in range(64):
        r, g, b = rgb_map.getpixel((x*64, y*64))
        mapVals[y][x] = (r,g,b)
        ##mapVals[y][x] = ("#{0:02x}{1:02x}{2:02x}".format(clamp(r), clamp(g), clamp(b)))


ozoneVals = np.zeros((32,64))

features = []
counter = 0
tempPoly = []
for i in range(32):
    for j in range(64):
        for k in range(398):
            for l in range(40):
                print(i,j,k,l)
                if (mapVals[j][i]) == (scaleVals[k][l]):
                    ozoneVals[i][j] = pixeltoDOB * k
        poly = Polygon([[(xChange(j),yChange(i)), (xChange(j+1), yChange(i)) , (xChange(j+1), yChange(i+1)) ,(xChange(j), yChange(i+1)), (xChange(j), yChange(i))]])
        features.append(Feature(geometry=poly, properties={"country": "Spain", "fill": "#80ffff"}))


print(mapVals[2][128]) ##just to see if it works

#poly = Polygon([[(2.38, 57.322), (23.194, -20.28), (-120.43, 19.15), (2.38, 57.322)]])
#poly2 = Point((200.0, 37.24))


#features.append(Feature(geometry=poly, properties={"country": "Spain", "fill": "#80ffff"}))
#features.append(Feature(geometry=poly2, properties={"country": "Spain"}))

# add more features...

feature_collection = FeatureCollection(features)

with open('myfile.geojson', 'w') as f:
    dump(feature_collection, f)
