"""Process tifs into small jpgs"""
import os

START_MSG = 'This script processes tifs into small jpgs.'

def main():
    print(START_MSG) # tell user what app will do

    # get the src and dst folders from user
    path_to_tifs = get_path('Enter a path to your tifs.')
    output_path = get_path('Where should the processed jpgs go?')

    # get other folders to check for existing images
    paths_to_check = []
    other_paths = input(
        'do you want to check another folder for existing jpgs?'
        )
    while other_paths == 'y':
        p = get_path('Enter a path to check for existing jpgs')
        paths_to_check.append(p)
        other_paths = input('and another?')

    # get all the tifs in the tifs folder
    tif_paths_to_process = []
    for root, dirs, files in os.walk(path_to_tifs):
        for file in files:
            name, ext = os.path.splitext(file)
            if ext.lower() == '.tif':
                tif_path = os.path.join(root, file)
                tif_paths_to_process.append(tif_path)

    print(tif_paths_to_process)
    input('yay!')

def get_path(msg):
    """ask user for a path and validate the response"""
    p = input(msg + ' ')
    while not (p and os.path.exists(p)):
        p = input("That wasn't a path. ")
    return p


if __name__ == '__main__':
    main()
