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

    verified_output_folder = verify_output_folder(output_folder)
    if not verified_output_folder:
        quit()

    converted_counter = 0

    for file in files_to_convert:
        converted_counter += save_to_png(file)

    if converted_counter > 0:
        print(f"Successfully converted {converted_counter} files.")
    else:
        print("All conversions unsuccessful. Please check your files.")

    quit()


def verify_command_args(args: list) -> bool:
    """Check for correct amount of input args."""
    if len(args) != 3:
        return False
    return True


def input_folder_exists(input_folder: str) -> list:
    """Check input folder exists and return jpg list."""
    directory = pathlib.Path(input_folder)
    if not directory.exists():
        print("Input folder doesn't exist or insufficent permissions.")
        return False
    files_to_convert = jpgs_to_convert(directory)
    if not files_to_convert:
        print("Input folder doesn't contain jpgs.")
        return False
    return files_to_convert


def verify_output_folder(output_folder: str) -> str:
    """Check output folder exists, create if it doesn't."""
    check_folder = pathlib.Path(output_folder)
    if not check_folder.exists():
        print("Output directory does not exist. Attempting to create...")
        try:
            check_folder.mkdir()
        except (FileNotFoundError, FileExistsError) as err:
            print(f"Could not create output folder. See error below:\n{err}")
            return False
        print("Directory created successfully.")
    return str(check_folder)


def jpgs_to_convert(directory: pathlib) -> list:
    """Create a list of jpg files in a directory."""
    files_to_convert = []
    expression = re.compile(r"(\.jpg)|(\.JPG)|(\.jpeg)$")
    for file in directory.iterdir():
        if expression.search(str(file)):
            files_to_convert.append(str(file))
    return files_to_convert


def save_to_png(file_path: str, out) -> int:
    # try:
    #     Image.open(file_path).save()
    #
    # except IOError:
    #
    # return 1
    pass


def print_usage():
    print("Usage: python3 jpg_to_png_converter.py input_folder output_folder")
    quit()


if __name__ == '__main__':
    main()
