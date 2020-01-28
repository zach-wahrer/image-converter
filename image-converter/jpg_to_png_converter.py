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

    files_to_convert = input_folder_exists(input_folder)
    if not files_to_convert:
        quit()

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
        print("Input folder doesn't exist or insufficent permissions.")
        return False
    files_to_convert = jpgs_to_convert(directory)
    if not files_to_convert:
        print("Input folder doesn't contain jpgs.")
        return False
    return files_to_convert


def verify_output_folder():
    pass


def jpgs_to_convert(directory: pathlib) -> list:
    """Create a list of jpg files in a directory."""
    files_to_convert = []
    expression = re.compile(r"(.jpg)|(.JPG)|(.jpeg)$")
    for file in directory.iterdir():
        if expression.search(str(file)):
            files_to_convert.append(str(file))
    return files_to_convert


def print_usage():
    print("Usage: python3 jpg_to_png_converter.py input_folder output_folder")
    quit()


if __name__ == '__main__':
    main()
