import csv
import os
# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification


def sumvalues(values:list)->int:
    """
    Parameters:
    -
    - List of values
    Code:
    -
    - Initializes sum variable at 0
    - Loops through values
    - If type isnt a float (by extension double of integer) raise exception
    - Else sum +=1
    - When loop is finished return sum
    """
    sum = 0
    for i in values:
        if type(i) != float:
            raise Exception("Exception: Non numerical value found")
        else:
            sum += i
    return sum


def maxvalue(values:list)-> int:
    """
    Parameters:
    -
    - List of values
    Code:
    -
    - Initializes max variable to 0
    - Loops through values
    - If type isnt a float (by extension double of integer) raise exception
    - Else if i is greater than max the replace max with i
    - When loop is finished return max
    """
    max = 0
    for i in values:
        if type(i) != float:
            raise Exception("Exception: Non numerical value found")
        else:
            if i>max:
                max = i
    return max



def minvalue(values:list):
    """
    Parameters:
    -
    - List of values
    Code:
    -
    - Initializes min variable to infinty
    - Loops through values
    - If type isnt a float (by extension double of integer) raise exception
    - Else if i is less than min the replace min with i
    - When loop is finished return min
    """
    min = float('inf')
    for i in values:
        if type(i) != float:
            raise Exception("Exception: Non numerical value found")
        else:
            if i<min:
                min = i
    return min


def meannvalue(values:list):
    """
    Parameters:
    -
    - List of values
    Code:
    -
    - Initializes total to 0
    - Loops through values
    - If type isnt a float (by extension double of integer) raise exception
    - Else adds i to total
    - When loop is finished return total divided by the length of values
    """
    total = 0
    for i in values:
        if type(i) != float:
            raise Exception("Exception: Non numerical value found")
        else:
            total +=i
    return total/len(values)


def countvalue(values:list,x:any)->int:
    """
    Parameters:
    -
    - List of values
    - Variable x : integer
    Code:
    -
    - Initializes count to 0
    - Loops through values
    - If i equals x add 1 to count
    - return count
    """
    count = 0
    for i in values:
        if i == x:
            count +=1
    return count


def csv_to_array(filename):
    """
    Parameters: 
    -  file name
    Code:
    -
    - cwd stores current working directory when os.cwd() returns it
    - Initailizes data array to store the data from the csv file
    - Using the with statement we open the file as a csvfile, we do this as the with statement autonmatically handles exceptions and closes the file to prevent bugs
    - The csv reader reads the entire file
    - The next() function skips the header row
    - Then we iterate through each row, for each row which intialize a empty rows array and append all the columns in the row to this individually.
    - Then we add the rows array to the data array until we reach the end of the file
    - Once we reach the end of the the file we return the data
    """
    cwd = os.getcwd()
    data = []
    with open(cwd+'\\data\\'+filename, 'r') as csvfile:
        csvread = csv.reader(csvfile)
        next(csvread)
        for row in csvread:
            rows = []
            for col in row:
                rows.append(col)
            data.append(rows)
    return data