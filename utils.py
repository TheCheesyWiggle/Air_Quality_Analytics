import pandas as pd
import os
# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification

#NOTE: docs and inline comments finished
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
    
    try:
        sum = 0
        #loops through array
        for i in values:
            #adds value to sum
            sum += i
        # returns integer
        return sum
    except TypeError:
        raise Exception("Exception: Non numerical value found")

#NOTE: docs and inline comments finished
def maxvalue(values:list)-> float:
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
    try:
        max = 0
        for i in values:
        #checks if the current value is less than the minimum
            if i<max:
                #sets current value to minimum
                max = i
        return max
    except TypeError:
        raise Exception("Exception: Non numerical value found")

#NOTE: docs and inline comments finished
def minvalue(values:list) -> float:
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
    try:
        min = float('inf')
        for i in values:
        #checks if the current value is less than the minimum
            if i<min:
                #sets current value to minimum
                min = i
        return min
    except TypeError:
        raise Exception("Exception: Non numerical value found")

#NOTE: docs and inline comments finished
def meannvalue(values:list) -> float:
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
    # try block catches error during execution
    try:
        #sets total to 0
        total = 0
        count = 0
        # loops through values
        for i in values:
            #makes i a numerical data type
            float(i)
            # adds 1 to total
            total += i
            count += 1
        #returns mean value
        return total/count
    except :
        raise Exception("Exception: Non numerical value found")

#NOTE: docs finished
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

#NOTE: docs finished
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
    
