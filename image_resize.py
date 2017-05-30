from __future__ import print_function
import os, sys
from PIL import Image


def resize_image(path_to_original, path_to_result):
    pass


if __name__ == '__main__':
    infile = 'test.jpeg'
    outfile='test2.jpg'
    im=Image.open(infile)
    print(im.size)
    im=im.resize((150, 150))
    print(im.size)
    im.save(outfile)