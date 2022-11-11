import numpy as np
import csv
import os
# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification


def daily_average(data:list, monitoring_station:str, pollutant:str) -> list:
    """
    Parameters: 
    -                                               
    - data = 2d array
    - monitoring_station = String of the name of the monitoring station
    - polluntant = "no" = Nitric Oxide "PM10" = Inhalable partical matter <= 10µm  "PM25" = Inhalable partical matter <= 2.5µm 
    \n
    Code:
    - 
    - Match Statement assigns numerical value to pollutant based on its collumn
    - Initalizes empty array to store daily averages and initalises counters for the loop/ if statement
    - Loops through data row by row
    - If statement checks if there is data and if we havent iterated through the day yet and performs operation accordingly
    - Returns array with daily averages
    """
    pol_num = pollutant

    daily_avg = []
    temp =[]
    for row in data:
        if row[pol_num]== "No data":
            print("No data")
        elif count == 23:
            count= 0
            daily_avg.append([np.average(temp), row[0], monitoring_station])
            temp =[]
        else:
            count += 1
            temp.append(float(row[pol_num]))
    return daily_avg

def daily_median(data:list, monitoring_station:str, pollutant:str) -> list:
    """
    Parameters: 
    -                                               
    - data = 2d array
    - monitoring_station = String of the name of the monitoring station
    - polluntant = "no" = Nitric Oxide "PM10" = Inhalable partical matter <= 10µm  "PM25" = Inhalable partical matter <= 2.5µm 
    \n
    Code: 
    - 
    - Call function to get pollutant row number
    - Initalizes:
        - Empty array for daily medians
        - Empty temporary array to hold data for the days
        - Counter for loop and if statements
    - Loops through data row by row
    - If statement
        - Checks if there is no data, prints no data
        - Checks counter to see if we have iterated through the day, resets counter, adds median to daliy_med array, resets temporary array
        - Adds 1 two count, adds value to temporary array
    """
    pol_num = pollutant_num(pollutant)
    daily_med = []
    temp= []
    count = 0

    for row in data:
        if row[pol_num]== "No data":
            print("No data")
        elif  count == 23:
            count = 0
            daily_med.append([np.median(temp), row[0], monitoring_station])
            temp = []
        else:
            count +=1
            temp.append(row[pol_num])
    return daily_med

def hourly_average(data:list, monitoring_station:str, pollutant:str)->list:
    """
    Parameters: 
    -                                               
    - data = 2d array
    - monitoring_station = String of the name of the monitoring station
    - polluntant = "no" = Nitric Oxide "PM10" = Inhalable partical matter <= 10µm  "PM25" = Inhalable partical matter <= 2.5µm 
    \n
    Code: 
    - 
    - Call function to get pollutant row number
    - Initializes:
        - hourly_average array
        - hours array empty 2d array with 24 rows
        - counter
    - Loops through each line and adds hourly values too corresponding columns
    - Loops through rows of hours and appends their median to hourly_average
    """
    pol_num = pollutant_num(pollutant)
    hourly_average=[]
    hours = [[]*24]
    count = 1

    for row in data:
        # Possible issues with modulos function
        hours.append([count%24,row[pol_num]])
    
    for row in hours:
        hourly_average.append(np.average(row), row[1], monitoring_station,)
    print(hourly_average)

    return hourly_average


def monthly_average(data:list, monitoring_station:str, pollutant:str)->list:
    """Your documentation goes here"""
    
    ## Your code goes here
def peak_hour_date(data:list, date:str, monitoring_station:str, pollutant:str)->str:
    """Your documentation goes here"""
    
    ## Your code goes here

def count_missing_data(data:list, monitoring_station:str, pollutant:str)->int:
    """Your documentation goes here"""
    
    ## Your code goes here

def fill_missing_data(data:list, new_value,  monitoring_station:str, pollutant:str):
    """Your documentation goes here"""
    
    ## Your code goes here

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
    - The next() function ireturns the next item in the csvread variable
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