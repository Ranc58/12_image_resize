from PIL import Image


def resize_image(path_to_original, path_to_result):
    pass


def only_width(width, infile, outfile):
    im = Image.open(infile)
    new_height = int(im.size[0]/(im.size[1] / width ))
    im.resize((new_height, width)).save(outfile)


def only_height(height, infile, outfile):
    im = Image.open(infile)
    new_width = int(im.size[0] / (im.size[1] / height))
    im.resize((new_width, height)).save(outfile)


def only_scale_resize(scale, infile, outfile):
    im = Image.open(infile)
    new_width = int(im.size[0] / scale)
    new_height = int(im.size[1] / scale)
    im.resize((new_height, new_width)).save(outfile)


if __name__ == '__main__':
    scale = 2
    width = 300
    height = 300
    infile = 'test.jpg'
    outfile = 'test2.jpeg'
    # only_scale_resize(scale, infile, outfile)
    only_width(width, infile, outfile)
    #only_height(height, infile, outfile)