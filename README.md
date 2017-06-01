# Image Resizer

This program resize your image for custom resolution. Work with .jpg and .png files.

# How to install
Recomended use venv or virtualenv for better isolation.\
Venv setup example:
```
$python -m venv myenv
$source myenv/bin/activate
```
Install requirements:
```
pip3 install -r requirements.txt
```
(may need enter `sudo` before command)


# Quick launch

List of arguments:
1. `-h --help` list of all cimmands.
2. `-s --scale` scale to resize image.
3. `-ws --width` width of out image.
4. `-hs --height` height of out image.
5. `-o --outfile` way and\or name of resized image to save. If this argument
not input image saves to dir with original file with original name and resolution. For example for test.jpg with res 400x400
resized image without `-o` is test__200x200.jpg by command `python resize_image.py test.jpg -s 2`

Availiable combinations of size arguments:
1. `-s` - resize image by scale
2. `-ws` - resize image only by width. Proportions will be saved.
3. `-hs` - resize image only by height. Proportions will be saved.
4. `-ws -hs` - resize image by width and height. **Warning!** Proportions probably will be broken!

Launching example on Linux:
```
$python test.jpg -s 2
Success! Image resized!
```
Launching on Windows is same.
# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
