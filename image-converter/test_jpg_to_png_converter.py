import unittest
from jpg_to_png_converter import verify_command_args


class TestJPGToPNG(unittest.TestCase):

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
