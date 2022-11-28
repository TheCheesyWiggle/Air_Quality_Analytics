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
    MARK = np.zeros((IMG.shape[0],IMG.shape[1]))
    Q = np.empty(shape=(0),dtype=object)
    # loops through the pixels in the image
    for x, i in enumerate(IMG):
        for y, j in enumerate(i):
            # if the pixel is a 1 and not marked
            if j == 1 and MARK[x][y]==0:
                # mark the pixel
                MARK[x][y] = 1
                # add the pixel to the queue
                coord = [i,j]
                Q = np.append(Q,coord)
                # checks if there are still unvisted valid neighbours
                while len(Q) == 0:
                    # deletes the first element in the queue
                    q = Q[0]
                    Q = np.delete(Q,0)
                    # gets the neighbours of the pixel
                    for i in get_neighbors(q[0],q[y]):
                        # if the neighbour is a 1 and not marked mark then mark it and add it to the queue
                        if IMG[i[0]][i[1]]== 1 and MARK[i[0]][i[1]] == 0:
                            MARK[i[0]][i[1]] = 1
                            Q = np.append(Q,[i[0],i[1]])
    print(len(Q))

def get_neighbors(x:int,y:int)->list:
    if x==0 and y==0:
        neighbors = [[x,y+1],[x+1,y+1],[x+1,y]]
    elif x == 0:
        neighbors = [[x-1,y],[x-1,y+1],[x,y+1],[x+1,y+1],[x+1,y]]
        return neighbors
    elif y == 0:
        neighbors = [[x,y+1],[x+1,y+1],[x+1,y],[x+1,y-1],[x,y-1]]
        return neighbors
    else:
        neighbors = [[x,y-1],[x-1,y-1],[x-1,y],[x-1,y+1],[x,y+1],[x+1,y+1],[x+1,y],[x+1,y-1]]
        return neighbors

def detect_connected_components_sorted(*args,**kwargs):
    """Your documentation goesnp.delete)
    for each here"""
    # Your code goes here

detect_connected_components(find_red_pixels("data\\map.png", upper_threshold=100, lower_threshold=50))
#detect_connected_components(find_cyan_pixels("data\\map.png", upper_threshold=100, lower_threshold=50))

