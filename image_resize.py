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
    return parser.parse_args()


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
    match_proportions = 'Proportions OK.'
    if infile_proportions != outfile_proportions:
        return attention
    else:
        return match_proportions


def resize_img(user_argument):
    image = Image.open(user_argument.infile)
    new_width = user_argument.width
    new_height = user_argument.height
    if ((user_argument.width and user_argument.scale) or
            (user_argument.height and user_argument.scale)):
        return print('Please enter availiable arguments combination!')
    elif user_argument.width and user_argument.height:
        return image.resize((new_width, new_height))
    elif user_argument.width:
        new_height = int(image.size[1] / (image.size[0] / user_argument.width))
    elif user_argument.height:
        new_width = int(image.size[0] / (image.size[1] / user_argument.height))
    elif user_argument.scale:
        new_width = int(image.size[0] / user_argument.scale)
        new_height = int(image.size[1] / user_argument.scale)
    return image.resize((new_width, new_height))


def create_filepath_to_save_image(image, user_argument):
    if user_argument.outfile is None:
        width = image.size[0]
        height = image.size[1]
        filepath, image = os.path.splitext(user_argument.infile)
        new_filepath = '{}__{}x{}{}'.format(filepath, height, width, image)
        return new_filepath
    else:
        return user_argument.outfile


def save_new_image(image, pathfile):
    image.save(pathfile)
    print(check_proportions(user_argument.infile, image),
          '\nSuccess! Image resized!')


if __name__ == '__main__':
    user_argument = create_parser_for_user_arguments()
    try:
        image = resize_img(user_argument)
        pathfile = create_filepath_to_save_image(image, user_argument)
    except (FileNotFoundError, OSError, AttributeError) as error:
        print(error)
    else:
        save_new_image(image, pathfile)
