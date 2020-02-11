import os
from PIL import Image

pngs = [x for x in os.listdir() if os.path.splitext(x)[1] == '.png']

os.makedirs('smol')

for p in pngs:
    im = Image.open(p)
    im.thumbnail((1600, 1600))
    im.save(os.path.join('smol', p))
    
