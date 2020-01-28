"""Testing for jpg_to_png_converter script."""

import unittest
from jpg_to_png_converter import (jpgs_to_convert, input_folder_exists,
                                  verify_command_args, verify_output_folder,
                                  pathlib)


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

    def test_input_files_no_jpg_folder(self):
        directory = pathlib.Path('tests/nojpgs/')
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

    # Output folder verification
    def test_output_folder_previously_exists(self):
        input = verify_output_folder('tests/empty')
        output = pathlib.Path('tests/empty')
        self.assertEqual(input, output)

    def test_output_folder_create_folder(self):
        input = verify_output_folder('tests/test_output')
        output = pathlib.Path('tests/test_output')
        self.assertEqual(input, output)
        output.rmdir()

    def test_output_folder_cannot_create_folder(self):
        input = verify_output_folder('tests/this_does_not_exist/test_output')
        self.assertFalse(input)


if __name__ == '__main__':
    unittest.main()
