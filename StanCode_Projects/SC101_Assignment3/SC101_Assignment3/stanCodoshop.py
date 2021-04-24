"""
File: stanCodoshop.py
Name: Freddy Wu
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

TODO:
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values

    """
    # green_im = SimpleImage.blank(20, 20, 'green')
    # green_pixel = green_im.get_pixel(0,0)               # Make canvas with green background
    # print(get_pixel_dist(green_pixel, 5 , 255, 10))     # ,and use (0,0) to be compared.
    pixel_red = pixel.red
    pixel_green = pixel.green
    pixel_blue = pixel.blue
    color_distance = ((pixel_red-red)**2+(pixel_blue-blue)**2+(pixel_green-green)**2)**0.5
    return color_distance


def get_average(pixels):                   # Pixels is a list. Each element means the pixel at (x,y) for each photo.
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    total_red = 0                           # If there are N pictures, the len of list(pixels) is N
    total_green = 0                         # Ex: pixels(x,y) =[picture1_pixel(x,y), picture2_pixel(x,y),....]
    total_blue = 0
    for i in range(len(pixels)):            # Take each([i]) photo's rgb pixel at(x,y) to calculate average rgb
        total_red += pixels[i].red
        total_green += pixels[i].green
        total_blue += pixels[i].blue
    avr_r = total_red//len(pixels)
    avr_g = total_green//len(pixels)
    avr_b = total_blue//len(pixels)
    return avr_r, avr_g, avr_b


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    best_pixel = []
    avg_list = get_average(pixels)
    color_distance_min = float('inf')                  # Set one infinite value to be a minimum of color_distance
    for i in range(len(pixels)):
        color_distance = get_pixel_dist(pixels[i], avg_list[0], avg_list[1], avg_list[2])
        if color_distance <= color_distance_min:
            best_pixel = pixels[i]
            color_distance_min = color_distance          # 'color_distance_min' would be replaced by 'real' minimum.
        else:
            best_pixel = best_pixel
    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width                              # hoover's width
    height = images[0].height                            # hoover's height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect
    print(len(images))
    for x in range(width):
        for y in range(height):
            new_pixel = result.get_pixel(x, y)
            pixel_list = []
            for z in range(len(images)):                 # Element of list of images is image, but not pixel!!
                img = images[z]
                pixel_list.append(img.get_pixel(x,y))    # Make a list for using method- get_best_pixel and get_average
            best_pixel = get_best_pixel(pixel_list)
            new_pixel.red = best_pixel.red
            new_pixel.green = best_pixel.green
            new_pixel.blue = best_pixel.blue
    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):                                   # This method load all pictures in folder.
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    """
    Description: Use method we built above to make a clean picture.
    """
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]                         # 'args' is a list from index[1] to end
    # args = sys.argv[1]                        #  This 'args' is just a string, but it also works with line173

    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.

    images = load_images(args[0])               # 'args[0]' is the first element in list(ex: hoover)
    # images = load_images(args)                # It also works with line167
    solve(images)


if __name__ == '__main__':
    main()

    # pixels是一個list。 是n張圖片在點(x,y)的pixel，所以有n張圖片的話表示每個list有n個element
    # 所以總共會計算 width*height 次的 list，來取出 best_rgb

