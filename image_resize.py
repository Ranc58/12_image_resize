import sys
import os
import argparse
from PIL import Image


def create_parser_for_user_arguments():
    parser = argparse.ArgumentParser(description='Resize image.')
    parser.add_argument('infile', help='Way to image for resize', type=str)
    parser.add_argument('-s', '--scale', nargs='?', help='Resize image by scale', type=float, const=only_scale_resize)
    parser.add_argument('-ws', '--width', nargs='?', help='Width of out image', type=int)
    parser.add_argument('-hs', '--height', nargs='?', help='Height of out image', type=int)
    parser.add_argument('-o', '--outfile', nargs='?', help='Way and name of image to save', type=str)
    return parser


def only_width(width, infile, outfile):
    im = Image.open(infile)
    new_height = int(im.size[0] / (im.size[1] / width))
    im.resize((new_height, width)).save(outfile)


def only_height(height, infile, outfile):
    im = Image.open(infile)
    new_width = int(im.size[0] / (im.size[1] / height))
    im.resize((new_width, height)).save(outfile)


def width_and_height(width, height, infile, outfile):
    im = Image.open(infile)
    im.resize((height, width)).save(outfile)


def only_scale_resize(scale, infile, outfile):
    im = Image.open(infile)
    new_width = int(im.size[1] / scale)
    new_height = int(im.size[0] / scale)
    im.resize((new_height, new_width)).save(outfile)


def create_filepath_to_save_image():
    pass


if __name__ == '__main__':
    parser = create_parser_for_user_arguments()
    user_argument = parser.parse_args(sys.argv[1:])
    print(user_argument)
    if user_argument.scale:
        only_scale_resize(user_argument.scale, user_argument.infile, user_argument.outfile)
    elif user_argument.width and user_argument.height:
        width_and_height(user_argument.width, user_argument.height, user_argument.infile, user_argument.outfile)
    elif user_argument.width:
        only_width(user_argument.width, user_argument.infile, user_argument.outfile)
    elif user_argument.height:
        only_height(user_argument.height, user_argument.infile, user_argument.outfile)
    else:
        print('Please enter correct arguments!')

