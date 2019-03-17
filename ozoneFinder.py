from PIL import Image

map = Image.open('ozone.png')
scale = Image.open('scale.png')
rgb_map = map.convert('RGB')
rgb_scale = scale.convert('RGB')

r, g, b = rgb_im.getpixel((2048, 1024))

print(r, g, b)
