import os
import argparse
from PIL import Image


def create_parser_for_user_arguments():
    parser = argparse.ArgumentParser(description='Resize image.')
    parser.add_argument('infile', help='Way to image for resize', type=str)
    parser.add_argument('-s', '--scale', nargs='?',
                        help='Resize image by scale', type=float)
    parser.add_argument('-ws', '--width', nargs='?',
                        help='Width of out image', type=int)
    parser.add_argument('-hs', '--height', nargs='?',
                        help='Height of out image', type=int)
    parser.add_argument('-o', '--outfile', nargs='?',
                        help='Way and name of image to save', type=str)
    return parser


def check_proportions(infile, image):
    original_image = Image.open(infile)
    resized_image = image
    original_width = original_image.size[0]
    original_height = original_image.size[1]
    resized_width = resized_image.size[0]
    resized_height = resized_image.size[1]
    numbers_after_point = 2
    infile_proportions = round((original_width / original_height),
                               numbers_after_point)
    outfile_proportions = round((resized_width / resized_height),
                                numbers_after_point)
    attention = 'Attention! Image out with the wrong proportions!'
    if infile_proportions != outfile_proportions:
        return attention


def select_resize_mode(user_argument):
    image = Image.open(user_argument.infile)
    if user_argument.scale:
        new_width = int(image.size[0] / user_argument.scale)
        new_height = int(image.size[1] / user_argument.scale)
        resized_img = image.resize((new_width, new_height))
    elif user_argument.width and user_argument.height:
        resized_img = image.resize((user_argument.width, user_argument.height))
    elif user_argument.width:
        new_height = int(image.size[1] / (image.size[0] / user_argument.width))
        resized_img = image.resize((user_argument.width, new_height))
    elif user_argument.height:
        new_width = int(image.size[0] / (image.size[1] / user_argument.height))
        resized_img = image.resize((new_width, user_argument.height))
    if ((user_argument.width and user_argument.scale) or
            (user_argument.height and user_argument.scale)):
        resized_img = print('Please enter availiable arguments combination!')
    return resized_img


def create_filepath_to_save_image(image, infile):
    width = image.size[0]
    height = image.size[1]
    filepath, image = os.path.splitext(infile)
    new_filepath = '{}__{}x{}{}'.format(filepath, height, width, image)
    return new_filepath


def save_new_image(image, pathfile):
    image.save(pathfile)


if __name__ == '__main__':
    parser = create_parser_for_user_arguments()
    user_argument = parser.parse_args()
    try:
        image = select_resize_mode(user_argument)
        check = check_proportions(user_argument.infile, image)
        if check is not None:
            print(check)
        if user_argument.outfile is None:
            pathfile = create_filepath_to_save_image(image,
                                                     user_argument.infile)
        else:
            pathfile = user_argument.outfile
        save_new_image(image, pathfile)
        print('Success! Image resized!')
    except (FileNotFoundError, OSError) as error:
        print(error)
    except AttributeError:
        image
