"""Process tifs into small jpgs"""
import os, sys

from PIL import Image

def main():
    # tell user what app will do
    print('This script processes tifs into small jpgs.')

    # get the src and dst folders from user
    path_to_tifs = get_path('Enter a path to your tifs.')
    output_path = get_path('Where should the processed jpgs go?')

    # get other folders to check for existing images
    paths_to_check = [output_path]
    other_paths = input(
        'Do you want to check another folder for existing jpgs? y/n '
        )
    while other_paths == 'y':
        p = get_path('Enter a path to check for existing jpgs.')
        paths_to_check.append(p)
        other_paths = input('and another? y/n ')

    print('Ok, Scanning...')

    # get all the tifs in the tifs folder
    all_tifs, duplicates = get_all_files(path_to_tifs, '.tif')

    # warn the user of duplicates and exit
    if duplicates:
        print(
            'The following files are duplicates and'
            ' would be overwritten when processing.\n'
            'Please deal with them and try again.'
            )
        for dup in duplicates:
            print(dup)
        return

    # get all the jpg names to check against
    jpg_names = []
    for path_to_check in paths_to_check:
        for jpg_path in get_all_files(path_to_check, '.jpg')[0]:
            jpg_names.append(just_the_name(jpg_path))

    # create a list of tifs to process, excluding those which match jpg names
    tifs_to_process = [
        x for x in all_tifs if not just_the_name(x) in jpg_names
    ]

    print('Found {} new tifs.'.format(len(tifs_to_process)))
    size = int(input('Now enter a size to fit. '))
    input('Great! now hit Enter and processing will begin. ')

    # process the tifs into jpgs and print progress bar after each one
    number_of_tifs = len(tifs_to_process)
    for index, tif_path in enumerate(tifs_to_process):
        process(tif_path, output_path, size=size)
        print_progress(index, number_of_tifs)

    input('Success!!')

# helpers

def process(tif_path, dst_dir, size=800):
    '''take in an image, resize it, and save it out.'''
    dst = os.path.join(dst_dir, just_the_name(tif_path) + '.jpg')
    image = Image.open(tif_path)
    image.thumbnail((size, size))
    image.save(dst)

def just_the_name(path):
    """return just the filename, no extension."""
    name = os.path.splitext(os.path.basename(path))[0]
    return name

def get_all_files(directory, ext):
    """return a tuple of all file paths with a given ext in a given directory
    and all of the duplicates.
    ext should follow the format ".jpg" - lowercase and include the dot.
    """
    exception_message = '"{}" is a duplicate. pls deal w this.'
    file_paths = []
    filenames = []
    duplicates = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            name, extension = os.path.splitext(file)
            if extension.lower() == ext:
                if file in filenames:
                    duplicates.append(file)
                filenames.append(file)
                file_path = os.path.join(root, file)
                file_paths.append(file_path)
    return file_paths, duplicates

def get_path(msg):
    """ask user for a path and validate the response"""
    p = input(msg + ' ')
    while not (p and os.path.exists(p)):
        p = input("That wasn't a path. ")
    return p

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
