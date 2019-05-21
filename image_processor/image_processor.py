"""Process tifs into small jpgs"""
import os

START_MSG = 'This script processes tifs into small jpgs.'

def main():
    print(START_MSG) # tell user what app will do

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
    all_tifs = get_all_files(path_to_tifs, '.tif')
    jpgs_to_compare = []

    for path_to_check in paths_to_check:
        for jpg in get_all_files(path_to_check, '.jpg'):
            jpgs_to_compare.append(jpg)

    print('found {} tifs.'.format(len(all_tifs)))
    print('found {} jpgs.'.format(len(jpgs_to_compare)))


def get_all_files(directory, ext):
    """return a list of all file paths with a given ext in a given directory.
    ext should follow the format ".jpg" - lowercase and include the dot.
    """
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            name, ext = os.path.splitext(file)
            if ext.lower() == ext:
                file_path = os.path.join(root, file)
                file_paths.append(file_path)
    return file_paths


def get_path(msg):
    """ask user for a path and validate the response"""
    p = input(msg + ' ')
    while not (p and os.path.exists(p)):
        p = input("That wasn't a path. ")
    return p


if __name__ == '__main__':
    main()
