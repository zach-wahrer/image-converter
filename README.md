# image-converter
---
Image-Converter is a simple command line program, written in Python3, to convert jpg files to png files. I wrote it as a way to practice working with files in Python, as well as implementing Test-Driven Development principles.


### Installing
---
The image converter uses the Pillow module to do the actual conversions, so you'll need to have it installed in your environment. `conda install -c anaconda pillow
` or `pip install Pillow` will do the trick.

All other dependencies are standard Python modules, so no further installation required.

### Running
---
Usage: `python3 jpg_to_png_converter.py input_folder output_folder`. This will convert all jpg (as well as .jpg-like files, ie. jpeg and JPG) to png files in the output_folder. If the output_folder doesn't exist, the program tries to create it. If a png file of the same name already exists in the output_folder, it will be skipped so as not to overwrite potentially unique files.

### Testing
To test the functionality of the program (perhaps after adding features of your own), you can run `python3 -m unittest` from the root directory.

## Author
---
**Zach Wahrer** - [zachtheclimber](https://github.com/zachtheclimber)
