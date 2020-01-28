"""
Converts all .jpg and .jpeg images from an input folder into an output folder.

Usage: `python3 jpg_to_png_converter.py input_folder/ output_folder/`
"""

import pathlib
import re
from sys import argv
from PIL import Image


def main():
    if not verify_command_args(argv):
        print_usage()

    input_folder = argv[1]
    output_folder = argv[2]

    if not input_folder_exists(input_folder):
        print("Input folder doesn't exist or insufficent permissions.")
        quit()
    # Check if input folder exists and has jpg files in it

    # Check if output_folder exists, if not, create

    # Loop through input folder
    # Convert images to png
    # Save image to new folder


def verify_command_args(args: list) -> bool:
    if len(args) != 3:
        return False
    return True


def input_folder_exists(input_folder: str) -> list:
    directory = pathlib.Path(input_folder)
    if not directory.exists():
        return False
    return True


def verify_output_folder():
    pass


def jpgs_to_convert(directory: pathlib) -> list:
    # for file in directory.iterdir():
    #     if 'jpg' in str(file):
    #         print(file)
    # return True
    pass


def print_usage():
    print("Usage: python3 jpg_to_png_converter.py input_folder/ output_folder/")
    quit()


if __name__ == '__main__':
    main()
