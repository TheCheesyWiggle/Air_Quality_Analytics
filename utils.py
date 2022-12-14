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
    # the minimum flaot to infinity
    min = float('inf')
    #loops through the values
    for i in values:
        #checks type of the value
        if type(i) != float:
            #raises exception on no numerical values
            raise Exception("Exception: Non numerical value found")
        else:
            #checks if the current value is less than the minimum
            if i<min:
                #sets current value to minimum
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

    try:
        total = 0
        for i in values:
            float(i)
            total += 1
        return total/len(values)
    except :
        raise Exception("Exception: Non numerical value found")

def countvalue(values:list,x)->int:
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

def csvs_to_dict()->dict:
    """
    Parameters: 
    -  file name
    Code:
    - pd.read_csv() reads the csv file and outputs a pandas dataframe
    - well read all the csv files and store their corresponding data frames in a dictionary
    - finally we return the nested dictionary
    """
    data = {"London Harlington":pd.read_csv('data\\Pollution-London Harlington.csv'),"London Marylebone Road":pd.read_csv('data\\Pollution-London Marylebone Road.csv'),"London N Kensington":pd.read_csv('data\\Pollution-London N Kensington.csv')}
    return data
    
