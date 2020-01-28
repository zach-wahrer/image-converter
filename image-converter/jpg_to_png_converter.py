"""
Converts all .jpg and .jpeg images from an input folder into an output folder.

Usage: `python3 jpg_to_png_converter.py input_folder/ output_folder/`
"""

from sys import argv
import os
from PIL import Image


def main():
    if not verify_command_args(argv):
        print_usage()

    input_folder = argv[1]
    output_folder = argv[2]

    if not open_input_folder(input_folder):
        print("Input folder doesn't exist or does not contain JPG files.")
    # Check if input folder exists and has jpg files in it

    # Check if output_folder exists, if not, create

    # Loop through input folder
    # Convert images to png
    # Save image to new folder


def verify_command_args(args):
    if len(args) != 3:
        return False
    return True


def open_input_folder():
    pass


def verify_output_folder():
    pass


def print_usage():
    print("Usage: python3 jpg_to_png_converter.py input_folder/ output_folder/")
    quit()
