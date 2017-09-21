from PIL import Image, ImageGrab

# More on PIL: http://effbot.org/imagingbook/introduction.htm
# More on ctypes via python: https://stackoverflow.com/questions/1997678/faster-method-of-reading-screen-pixel-in-python-than-pil
# More on compress_level and the speed of PIL: https://github.com/python-pillow/Pillow/issues/1211

# Takes a screenshot, pretty sure it needs the '__name__' passed to it in order to properly function
def screenshot(__name__):
    if __name__ == '__main__':
        im = ImageGrab.grab()  # I think you can set a bbox to get a smaller image
        im.save('ss.png')


#def get_image(image_path):
    #width, height = get_center(image_path)
    #image = Image.open(image_path, 'r')
    #pixel_values = list(image.getdata())
    #if image.mode == 'RGB':
    #    channels = 3
    #elif image.mode == 'L':
    #    channels = 1
    #else:
    #    print("Unknown mode: %s" % image.mode)
    #    return None
    #print(image.getpixel((width/2, height/2)))  # Fetches pixels at a location

    # pixel_values = numpy.array(pixel_values).reshape((width, height, channels))
    # tempA = "Value at (0,0): " + str(pixel_values[0][0])
    # tempB = "Value at (2,2): " + str(pixel_values[2][2])
    # print(tempA)
    # print(tempB)
    #return pixel_values

# Returns the center of an image as sequence (x, y)
#def get_center(image_path):
    #image = Image.open(image_path, 'r')
    #width, height = image.size
    #return width, height

# Apparently super fast screen capture (~0.6 seconds)
# From: https://www.reddit.com/r/programming/comments/8qe1t/fast_x11_screenshots_in_python_see_comment/
#try:
  #img_width = gtk.gdk.screen_width()
  #img_height = gtk.gdk.screen_height()

  #screengrab = gtk.gdk.Pixbuf(
  #  gtk.gdk.COLORSPACE_RGB,
  #  False,
  #  8,
  #  img_width,
  #  img_height
  #)

  #screengrab.get_from_drawable(
  #  gtk.gdk.get_default_root_window(),
  #  gtk.gdk.colormap_get_system(),
  #  0, 0, 0, 0,
  #  img_width,
  #  img_height
  #)

#except:
   #print "Failed taking screenshot"
   #exit()

#print "Converting to PIL image ..."

#final_screengrab = Image.frombuffer(
  #"RGB",
  #(img_width, img_height),
  #screengrab.get_pixels(),
  #"raw",
  #"RGB",
  #screengrab.get_rowstride(),
  #1
#)