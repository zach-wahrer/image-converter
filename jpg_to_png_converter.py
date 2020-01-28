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
        converted_counter += save_to_png(file, verified_output_folder)

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
    if not check_existing(input_folder):
        print("Input folder doesn't exist or insufficent permissions.")
        return False
    files_to_convert = jpgs_to_convert(input_folder)
    if not files_to_convert:
        print("Input folder doesn't contain jpgs.")
        return False
    return files_to_convert


def verify_output_folder(output_folder: str) -> str:
    """Check output folder exists, create if it doesn't."""
    if not check_existing(output_folder):
        print("Output directory does not exist. Attempting to create...")
        try:
            pathlib.Path(output_folder).mkdir()
        except (FileNotFoundError, FileExistsError) as err:
            print(f"Could not create output folder. See error below:\n{err}")
            return False
        print("Directory created successfully.")
    return output_folder


def jpgs_to_convert(folder: str) -> list:
    """Create a list of jpg files in a directory."""
    files_to_convert = []
    expression = re.compile(r"(\.jpg)|(\.JPG)|(\.jpeg)$")
    for file in pathlib.Path(folder).iterdir():
        if expression.search(str(file)):
            files_to_convert.append(str(file))
    return files_to_convert


def save_to_png(file_with_path: str, save_dir: str) -> int:
    """Convert jpg file to png and save to specified directory."""
    filename = get_file_name(file_with_path)
    save_file_with_path = save_dir + "/" + filename + ".png"
    if check_existing(save_file_with_path):
        print(f"{save_file_with_path} already exists. Skipping.")
        return 0
    else:
        try:
            Image.open(file_with_path).save(save_file_with_path)

        except IOError:
            print(f"{file_with_path} couldn't be converted.")
            return 0

        print(f"{save_file_with_path} saved successfully.")
        return 1


def check_existing(dir_or_file: str) -> bool:
    """Check for existing output file or directory."""
    return pathlib.Path(dir_or_file).exists()


def get_file_name(file_with_path: str) -> str:
    """Extract file name from a path/filename.jpg."""
    return file_with_path.split("/")[-1].split(".")[0]


def print_usage():
    print("Usage: python3 jpg_to_png_converter.py input_folder output_folder")
    quit()


if __name__ == '__main__':
    main()
