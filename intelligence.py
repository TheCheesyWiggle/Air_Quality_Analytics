from skimage import io, util
import numpy as np
# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification

def find_red_pixels(*args,**kwargs):
    """Your documentation goes here"""
    map_filename = args[0]
    upper_threshold = kwargs["upper_threshold"]
    lower_threshold = kwargs["lower_threshold"]

    img_data = io.imread(map_filename)
    
    array = np.zeros((img_data.shape[0],img_data.shape[1]))

    for i, x in enumerate(img_data):
        for j, y in enumerate(x):
            if y[0]> upper_threshold and y[1]<lower_threshold and y[2] < lower_threshold:
                array[i][j] = 1
    io.imsave("data//map-red-pixels.jpg",array)
    

def find_cyan_pixels(*args,**kwargs):
    """Your documentation goes here"""
    map_filename = args[0]
    upper_threshold = kwargs["upper_threshold"]
    lower_threshold = kwargs["lower_threshold"]

    img_data = io.imread(map_filename)
    
    array = np.zeros((img_data.shape[0],img_data.shape[1]))

    for i, x in enumerate(img_data):
        for j, y in enumerate(x):
            if y[0]< lower_threshold and y[1]>upper_threshold and y[2] > upper_threshold:
                array[i][j] = 1
    print(array)
    io.imsave("data//map-cyan-pixels.jpg",array)


def detect_connected_components(*args,**kwargs):
    """Your documentation goes here"""
    # Your code goes here

def detect_connected_components_sorted(*args,**kwargs):
    """Your documentation goes here"""
    # Your code goes here

map_filename = "data\\map.png"
find_red_pixels(map_filename, upper_threshold=100, lower_threshold=50)
find_cyan_pixels(map_filename, upper_threshold=100, lower_threshold=50)