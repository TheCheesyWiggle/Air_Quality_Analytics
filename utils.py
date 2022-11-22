import pandas as pd
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

def csv_to_dict(filename:str)->dict:
    """
    Parameters: 
    -  file name
    Code:
    -
    - cwd stores current working directory when os.cwd() returns it
    - pd.read_csv() reads the csv file and outputs a pandas dataframe
    - data_frame.to_dict() converts the dataframe to a dictionary with a 2nd dictionary nested with in
    - finally we return the nested dictionary
    """
    cwd = os.getcwd()
    data = pd.read_csv(cwd+'\\data\\'+filename).to_dict()
    return data