import gzip
import numpy as np
from PIL import Image





def read_images_from_file(filename):
    with  gzip.open(filename, 'rb') as imageFile:
        magic = imageFile.read(4)
        magic = int.from_bytes(magic, 'big')
        noimg = imageFile.read(4)
        noimg = int.from_bytes(noimg, 'big') 
        norow = imageFile.read(4)
        norow = int.from_bytes(norow, 'big') 
        nocol = imageFile.read(4)
        nocol = int.from_bytes(nocol, 'big') 
        f = imageFile.read()  
        array = np.array(bytearray(f)).reshape(noimg,norow, nocol) 
    return array 


def read_lables_from_file(filename):
    with  gzip.open(filename, 'rb') as imageFile:
        magic = imageFile.read(4) 
        
        noimg = imageFile.read(4) 
        f = imageFile.read()
        array = np.array(bytearray(f))
    return array
#############################

def print_image_from_data(dataArray,image_number): 
    array = dataArray[image_number] 
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] < 128: 
                print(".",end="")
            else:
                print("#",end="")  
        print()



images = read_images_from_file('data/train-images-idx3-ubyte.gz')
lables = read_lables_from_file("data/train-labels-idx1-ubyte.gz")
print_image_from_data(images,2) 
