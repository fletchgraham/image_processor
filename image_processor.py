"""Process images into jpgs fitting a given size"""
import os, sys

from PIL import Image

def main():
    # tell user what app will do
    print('This script processes images into small jpgs.')

    # get the src and dst folders from user
    target_dir = os.getcwd()
    output_path = os.path.join(target_dir, 'jpg')

    print('Ok, Scanning...')

    img_exts = ['.tif', '.tiff', '.jpg', '.png', '.jpeg']

    images_to_process = [
        x for x
        in os.listdir(target_dir)
        if os.path.splitext(x)[1].lower() in img_exts
        ]

    print('Images to process:')
    for x in images_to_process:
        print(x)

    size = int(input('Now enter a size to fit: '))
    input('Great! now hit Enter and processing will begin. ')

    # process the tifs into jpgs and print progress bar after each one
    total = len(images_to_process)
    for index, img in enumerate(images_to_process):
        img_path = os.path.join(target_dir, img)
        process(img_path, output_path, size=size)
        print_progress(index, total)

    input('Success!!')

# helpers

def process(img_path, dst_dir, size=800):
    '''take in an image, resize it, and save it out.'''
    dst = os.path.join(dst_dir, just_the_name(img_path) + '.jpg')
    image = Image.open(img_path)
    image.thumbnail((size, size))
    image.save(dst)

def just_the_name(path):
    """return just the filename, no extension."""
    name = os.path.splitext(os.path.basename(path))[0]
    return name

def print_progress(iteration, total):
    """Print a progress bar showing a given level of completion."""
    iteration += 1
    prefix = 'Progress'
    suffix = 'Complete'
    length = 50
    fill = u"\u2588"
    fill_alt = '#'

    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    bar_alt = fill_alt * filledLength + '-' * (length - filledLength)

    try:
        sys.stdout.write('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix))
    except:
        sys.stdout.write('\r%s |%s| %s%% %s' % (prefix, bar_alt, percent, suffix))
    sys.stdout.flush()

    # Print New Line on Complete
    if iteration == total:
        print()

if __name__ == '__main__':
    main()
