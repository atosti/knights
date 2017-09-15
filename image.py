from PIL import Image
from mss.windows import MSS as mss  # Used for screenshots


def screenshot():
    mss().shot()


def get_image(image_path):
    width, height = get_center(image_path)
    image = Image.open(image_path, 'r')
    pixel_values = list(image.getdata())
    if image.mode == 'RGB':
        channels = 3
    elif image.mode == 'L':
        channels = 1
    else:
        print("Unknown mode: %s" % image.mode)
        return None
    print(image.getpixel((width/2, height/2)))  # Fetches pixels at a location

    # pixel_values = numpy.array(pixel_values).reshape((width, height, channels))
    # tempA = "Value at (0,0): " + str(pixel_values[0][0])
    # tempB = "Value at (2,2): " + str(pixel_values[2][2])
    # print(tempA)
    # print(tempB)
    return pixel_values

# Returns the center of an image as sequence (x, y)
def get_center(image_path):
    image = Image.open(image_path, 'r')
    width, height = image.size
    return width, height
