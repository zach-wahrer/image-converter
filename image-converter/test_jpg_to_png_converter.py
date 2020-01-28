import unittest
from jpg_to_png_converter import input_folder_exists, verify_command_args


class TestJPGToPNG(unittest.TestCase):

    # Input folder validation
    def test_input_folder_valid(self):
        input = input_folder_exists('images/')
        self.assertTrue(input)

    def test_input_folder_invalid_01(self):
        input = input_folder_exists('01')
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
