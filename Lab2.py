import gzip
import numpy as np
from PIL import Image

def read_images_from_file(filename):
    with  gzip.open(filename, 'rb') as imageFile:
        magic = imageFile.read(4)
        magic = int.from_bytes(magic, 'big')
        noimg = imageFile.read(4)
        noimg = int.from_bytes(noimg, 'big') # reads number of images
        norow = imageFile.read(4)
        norow = int.from_bytes(norow, 'big') # number of pixels in a row
        nocol = imageFile.read(4)
        nocol = int.from_bytes(nocol, 'big') # number of pixels in a column
        f = imageFile.read()  # reads the rest of the file as bytes
        array = np.array(bytearray(f)).reshape(noimg,norow, nocol)  # aranges the array as numpy array, rearanges it
    return array  # as a 3d-array


def read_lables_from_file(filename):
    with  gzip.open(filename, 'rb') as imageFile:
        magic = imageFile.read(4)  # this are required to shift read by 8 bites
        # magic = int.from_bytes(magic, 'big')
        noimg = imageFile.read(4)  # the number of images the same as in the image file
        # noimg = int.from_bytes(noimg, 'big')
        f = imageFile.read()
        array = np.array(bytearray(f)) # 1-d array of labele
    return array
#############################

def print_image_from_data(dataArray,image_number):  # takes the array from input and the image number to show
    array = dataArray[image_number]  # array starts with image number 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] < 128:  # if pixel value is less then 128 outputs a dot
                print(".",end="")
            else:
                print("#",end="")  # else - #
        print()



images = read_images_from_file('data/train-images-idx3-ubyte.gz')
lables = read_lables_from_file("data/train-labels-idx1-ubyte.gz")
print_image_from_data(images,2)  # third image in the array has number 2
input("Press Enter to create files from set")
for i in range(len(lables)):  # saves images to files in subfolder 
    im = Image.fromarray(images[i])
    im.save("subfolder/train-{:05d}-{:}.png".format(i,lables[i]))  # generated from the number the label
    print("File 'train-{:05d}-{:}.png' had been created in subfolder".format(i,lables[i]))

