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
    io.imsave("data//map-cyan-pixels.jpg",cyan_pixels)
    return cyan_pixels

def detect_connected_components(*args,**kwargs):
    """
    
    Parameters:
    - IMG
    
    Code:
"""
    # gives use IMG variable
    IMG = args[0]
    #Sets up MARK witht the same size as IMG but filled with zeros
    MARK = np.zeros((IMG.shape[0],IMG.shape[1]))
    #sets up a Q for the neigbours
    Q = np.empty((2,0), dtype=list)
    #sets up a list for the connected components
    connected_components = []
    # loops through the pixels in the image
    for x, i in enumerate(IMG):
        for y, j in enumerate(i):
            # if the pixel is a 1 and not marked
            if j == 1 and MARK[x][y]==0:
                # mark the pixel
                MARK[x][y] = 1
                # add the pixel to the queue
                coord = [x , y]
                Q = np.append(Q,coord)
                count = 0
                # checks if there are still unvisted valid neighbours
                while len(Q) != 0:
                    # creates a variable q and deletes the first element in the queue
                    q = [Q.item(0) , Q.item(1)]
                    count += 1
                    #deletes x and y coord
                    Q = np.delete(Q,0)
                    Q = np.delete(Q,0)
                    # loops through and gets the neighbours of the pixel
                    for i in get_neighbors(q[0],q[1], IMG.shape):
                        # if the neighbour is a 1 and not marked mark the neighbour and add its x,y to the queueS
                        if IMG[i[0]][i[1]] == 1 and MARK[i[0]][i[1]] == 0:
                                MARK[i[0]][i[1]] = 1
                                Q = np.append(Q,[i[0],i[1]])
                # adds the number of pixels in the connected component to the list
                connected_components.append(count)
    #opens a file 
    with open("data\\cc-output-2a.txt","w") as out_file:
        #loops through the connected components
        for index, pix_count in enumerate(connected_components):
            #writes the connected component to the file
            out_file.write(f"Connected component: {index+1}, number of pixels = {pix_count} pixels\n")
        #writes the total number of connected components to the file
        out_file.write(f"Total connected components: {len(connected_components)}")
    return MARK

def get_neighbors(x:int,y:int, size:tuple)->list:
    """Your documenation goes here"""
    array = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            temp_x = x + i
            temp_y = y + j
            if temp_x >= 0 and temp_x < size[0] and temp_y >=0 and temp_y < size[1]: # if the bounds are ok
                if temp_x != x or temp_y != y:
                    array.append((x+i, y+j))
    return array
                

def detect_connected_components_sorted(*args,**kwargs):
    """Your documentation goes here"""
    MARK = args[0]
    dictionary = {}
    #Opens cc-output-2a.txt file
    with open("data\\cc-output-2a.txt","r") as in_file:
        #loops through the file
        for line in in_file:
            if line [:27] == "Total connected components:":
                break
            #splits the line into a list
            line = line.split(' ')
            #adds the component number and number of pixels to the dictionary while converting the number of pixels to an int
            #Converted to an in because otherwise the bubble sort would not work
            dictionary[int(line[2][:-1])] = int(line[7])
    #sorts the values
    comp_no, pix_no = bubble_sort(dictionary)
    dictionary = dict(zip(comp_no,pix_no))



def bubble_sort(dictionary:dict)->tuple:
    """Your documentation goes here"""
    comp_no = list(dictionary.keys())
    pix_no =  list(dictionary.values())
    swapped = False
    for i in range(len(pix_no)-1):
        for j in range(0, len(pix_no)-i-1):
            if pix_no[j] < pix_no[j + 1]:
                swapped = True
                comp_no[j], comp_no[j + 1] = comp_no[j + 1], comp_no[j]
                pix_no[j], pix_no[j + 1] = pix_no[j + 1], pix_no[j]
        if not swapped:
            return comp_no, pix_no
    return comp_no, pix_no

#num, pix = bubble_sort([2,8,9,1,5,6,3,4,10,7],[98,34,3,12,23,67,109,84,21,176])
#for i, x in enumerate(num):
    #print(f"Connected component: {x}, number of pixels = {pix[i]} pixels")
detect_connected_components_sorted(detect_connected_components(find_red_pixels("data//map.png",upper_threshold=100,lower_threshold=50)))
