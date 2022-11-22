from skimage import io, util
import numpy as np
# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification

def find_red_pixels(*args,**kwargs):
    """Parameters:
    - 
    - Filename
    - Lower colour threshold
    - Upper colour threshold
    Code:
    -
    - io.imread() read the image file into a 3d array
    - np.zeros sets up a array filled with zeros with a width of img_data.shape[0] and a height of img_data.shape[1]
    - the nested for loop enumerates through the image dasta array
    - the if statement changes the zeros 2 ones of the corresponding red pixels in the array
    - io.saved the new array as a image
    """
    map = args[0]
    upper_threshold = kwargs["upper_threshold"]
    lower_threshold = kwargs["lower_threshold"]

    img_data = io.imread(map)
    
    red_pixels = np.zeros((img_data.shape[0],img_data.shape[1]))

    for i, x in enumerate(img_data):
        for j, y in enumerate(x):
            if y[0]> upper_threshold and y[1]<lower_threshold and y[2] < lower_threshold:
                red_pixels[i][j] = 1
    io.imsave("data//map-red-pixels.jpg",red_pixels)
    return red_pixels
    

def find_cyan_pixels(*args,**kwargs):
    """
    Parameters:
    - 
    - Filename
    - Lower colour threshold
    - Upper colour threshold
    Code:
    -
    - io.imread() read the image file into a 3d array
    - np.zeros sets up a array filled with zeros with a width of img_data.shape[0] and a height of img_data.shape[1]
    - the nested for loop enumerates through the image dasta array
    - the if statement changes the zeros 2 ones of the corresponding cyan pixels in the array
    - io.saved the new array as a image
    """
    map = args[0]
    upper_threshold = kwargs["upper_threshold"]
    lower_threshold = kwargs["lower_threshold"]

    img_data = io.imread(map)
    
    cyan_pixels = np.zeros((img_data.shape[0],img_data.shape[1]))

    for i, x in enumerate(img_data):
        for j, y in enumerate(x):
            if y[0]< lower_threshold and y[1]>upper_threshold and y[2] > upper_threshold:
                cyan_pixels[i][j] = 1
    io.imsave("data//map-cyan-pixels.jpg", cyan_pixels)
    return cyan_pixels


def detect_connected_components(*args,**kwargs):
    """Your documentation goes here"""
    IMG = args[0]
    MARK = np.zeros(IMG.shape())
    Q = np.empty()
    for x, i in enumerate(IMG):
        for y, j in enumerate(i):
            if j == 1 and MARK[x][y]==0:
                MARK[x][y] = 1
                Q = np.append(Q,j)
                while len(Q) == 0:
                    q = Q[0]
                    Q = np.delete(Q,0)
                    #for loop throught neighbors and add neighbors to the queue
                    # when queue is empty you have a connected piece

def detect_connected_components_sorted(*args,**kwargs):
    """Your documentation goesnp.delete)
    for each here"""
    # Your code goes here

"""
map_filename = "data\\map.png"
find_red_pixels(map_filename, upper_threshold=100, lower_threshold=50)
find_cyan_pixels(map_filename, upper_threshold=100, lower_threshold=50)
"""

