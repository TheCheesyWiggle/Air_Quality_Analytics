from skimage import io, util
import numpy as np
from colours import fg,bg,decor
# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification

#NOTE:docs and inline comments finished
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
    #gather the arguments
    map = args[0]
    upper_threshold = kwargs["upper_threshold"]
    lower_threshold = kwargs["lower_threshold"]
    #read the image
    img_data = io.imread(map)
    #create an array of zeros with the same size as the image
    red_pixels = np.zeros((img_data.shape[0],img_data.shape[1]))
    #loop through the image data
    for i, x in enumerate(img_data):
        for j, y in enumerate(x):
            #if the pixel is red change the corresponding pixel in the red_pixels array to 1
            if y[0]> upper_threshold and y[1]<lower_threshold and y[2] < lower_threshold:
                red_pixels[i][j] = 1
    #save the red_pixels array as a image
    io.imsave("data//map-red-pixels.jpg",red_pixels)
    #return the red_pixels array
    return red_pixels

#NOTE:docs and inline comments finished
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
    #gather the arguments
    map = args[0]
    upper_threshold = kwargs["upper_threshold"]
    lower_threshold = kwargs["lower_threshold"]
    #read the image
    img_data = io.imread(map)
    #create an array of zeros with the same size as the image
    cyan_pixels = np.zeros((img_data.shape[0],img_data.shape[1]))
    #loop through the image data
    for i, x in enumerate(img_data):
        for j, y in enumerate(x):
            #if the pixel is cyan change the corresponding pixel in the cyan_pixels array to 1
            if y[0]< lower_threshold and y[1]>upper_threshold and y[2] > upper_threshold:
                cyan_pixels[i][j] = 1
    #save the cyan_pixels array as a image
    io.imsave("data//map-cyan-pixels.jpg",cyan_pixels)
    #return the cyan_pixels array
    return cyan_pixels

#NOTE:docs and inline comments finished 
def detect_connected_components(*args,**kwargs):
    """
    
    Parameters:
    -
    - IMG 
    - upper threshold
    - lower threshold
    
    Code:
    -
    - Gets the connected components of a specific colour in an image
"""
    # gives use IMG variable
    IMG = args[0]
    #Sets up MARK witht the same size as IMG but filled with zeros
    MARK = np.zeros((IMG.shape[0],IMG.shape[1]))
    #sets up a Q for the neigbours
    Q = np.empty((2,0), dtype=list)
    #sets up a list for the connected components
    connected_components = []
    component_counter = 1
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
                                #sets mark to the number of the component to keep track of them
                                MARK[i[0]][i[1]] = component_counter
                                Q = np.append(Q,[i[0],i[1]])
                # adds the number of pixels in the connected component to the list
                component_counter += 1
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

#NOTE:docs and inline comments finished
def get_neighbors(x:int,y:int, size:tuple)->list:
    """
    Parameters:
    -
    - x = x coord
    - y = y coord
    - size = tuple with size of the image
    Code:
    -
    - creates an empty array
    - loops through the neighbours
    - creates temp variables for the x and y coords
    - if bounds are ok
    - if the x and y coords are not the same as the original x and y coords
    - add the x and y coords to the array
    - return array
    """
    #creates an empty array
    array = []
    #loops through the neighbours
    for i in range(-1, 2):
        for j in range(-1, 2):
            #creates temp variables for the x and y coords
            temp_x = x + i
            temp_y = y + j
            # if bounds are ok
            if temp_x >= 0 and temp_x < size[0] and temp_y >=0 and temp_y < size[1]: 
                # if the x and y coords are not the same as the original x and y coords
                if temp_x != x or temp_y != y:
                    # add the x and y coords to the array
                    array.append((x+i, y+j))
    #return array
    return array

#NOTE: docs and inline comments finished
def detect_connected_components_sorted(*args,**kwargs):
    """
    Parameters:
    - Mark = Image with the connected components
    -
    Code:
    - 
    - Sorts the connected components by the number of pixels in the component
    - Uses a bubble sort
    - Saves the image with the connected components to a sorted file
    """
    MARK = args[0]
    print(MARK)

    
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
    #opens a file 
    with open("data\\cc-output-2b.txt","w") as out_file:
        #loops through the connected components
        for key,value in dictionary.items():
            #writes the connected component to the file
            out_file.write(f"Connected component: {key}, number of pixels = {value} pixels\n")
        #writes the total number of connected components to the file
        out_file.write(f"Total connected components: {len(dictionary)}")
    #biggest component
    biggest = list(dictionary.items())[0]
    # second biggest component
    second_biggest = list(dictionary.items())[1]
    #prints both components
    print(fg.cyan+f"The biggest connected component is {biggest[0]} with {biggest[1]} pixels")
    print(f"The second biggest connected component is {second_biggest[0]} with {second_biggest[1]} pixels"+decor.reset)

    # create a array of zeros with the same shape as mark 
    top2 = np.zeros((MARK.shape[0],MARK.shape[1]))
    #loops through mark
    for x ,i in enumerate(MARK):
        for y, j in enumerate(i):
            #checks if the  components are the ones we are looking for
            if j == biggest[0]:
                top2[x][y] = 1
            if j == second_biggest[0]:
                top2[x][y] = 1
    # save new array
    io.imsave("data//cc-top-2.jpg",top2)

#NOTE:docs and inline comments finished
def bubble_sort(dictionary:dict)->tuple:
    """
    Parameters:
    -
    - dictionary: a dictionary with the connected component number as the key and the number of pixels as the value

    Code:
    - 
    - Bublesort sorts the components by the number of pixels
    - Sorts 2 arrays in tandem

    """
    # Splits the dictionary into two lists one for component numbers one for number of pixels
    comp_no = list(dictionary.keys())
    pix_no =  list(dictionary.values())
    # Sets swapped to false
    swapped = False
    # loops through the list
    for i in range(len(pix_no)-1):
        for j in range(0, len(pix_no)-i-1):
            # if the number of pixels is less than the next number of pixels swap the two numbers
            if pix_no[j] < pix_no[j + 1]:
                #sets swapped to true
                swapped = True
                #swaps the pixels and component numbers
                comp_no[j], comp_no[j + 1] = comp_no[j + 1], comp_no[j]
                pix_no[j], pix_no[j + 1] = pix_no[j + 1], pix_no[j]
        # if swapped is true return the component numbers and number of pixels
        if not swapped:
            return comp_no, pix_no
    return comp_no, pix_no

if __name__ == '__main__':
    detect_connected_components_sorted(detect_connected_components(find_red_pixels("data//map.png",upper_threshold=100,lower_threshold=50)))
