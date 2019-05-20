"""Process tifs into small jpgs"""
import os

START_MSG = 'This script processes tifs into small jpgs.'

def main():
    print(START_MSG)
    src = input()


def get_path(msg):
    """ask user for a path and validate the response"""
    p = input(msg + ' ')
    while not (p and os.path.exists(p)):
        p = input("That wasn't a path. ")
    return p


if __name__ == '__main__':
    main()
