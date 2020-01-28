"""Testing for jpg_to_png_converter script."""

import unittest
from jpg_to_png_converter import (jpgs_to_convert, input_folder_exists,
                                  verify_command_args, pathlib)


class TestJPGToPNG(unittest.TestCase):

    # Input files validation
    def test_input_files_valid(self):
        directory = pathlib.Path('tests/images/')
        input = jpgs_to_convert(directory)
        output = ['tests/images/pikachu.jpg', 'tests/images/charmander.jpg',
                  'tests/images/astro.jpeg', 'tests/images/bulbasaur.JPG',
                  'tests/images/squirtle.jpg']
        self.assertEqual(input, output)

    def test_input_files_empty_folder(self):
        directory = pathlib.Path('tests/empty/')
        input = jpgs_to_convert(directory)
        self.assertFalse(input)

    # Input folder validation
    def test_input_folder_valid(self):
        input = input_folder_exists('tests/images/')
        self.assertTrue(input)

    def test_input_folder_invalid_01(self):
        input = input_folder_exists('01')
        self.assertFalse(input)

    def test_input_folder_empty(self):
        input = input_folder_exists('tests/empty')
        self.assertFalse(input)

    def test_input_folder_invalid_blank(self):
        input = input_folder_exists(' ')
        self.assertFalse(input)

    def test_input_folder_invalid_non_existant(self):
        input = input_folder_exists('files/')
        self.assertFalse(input)

    # Command line input validation
    def test_argv_valid(self):
        args = ['jpg_to_png_converter.py', 'images/', 'test/']
        input = verify_command_args(args)
        self.assertTrue(input)

    def test_argv_only_2(self):
        args = ['jpg_to_png_converter.py', 'images/']
        input = verify_command_args(args)
        self.assertFalse(input)


if __name__ == '__main__':
    unittest.main()
