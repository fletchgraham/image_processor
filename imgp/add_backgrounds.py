import os
from PIL import Image

images = [
    x for x in os.listdir()
    if os.path.splitext(x)[1] in ['.tif', '.png']
]

dst = 'with_bg'

color = (255, 255, 255, 255)

def add_background(img):
    background = Image.new('RGBA', (img.size), color)
    comp = Image.alpha_composite(background, img)
    return comp 

def main():
    try:
        os.makedirs(dst)
    except:
        pass
    
    for image_name in images:
        img = Image.open(image_name)
        comp = add_background(img)
        comp = comp.convert('RGB')
        new_name = image_name.replace('.tif', '.jpg')
        comp.save(os.path.join(dst, new_name))

        print(f'completed {image_name}')

main()