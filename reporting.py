import utils
import numpy as np

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
    - Initalizes empty array to store daily averages and initalises counters for the loop/ if statement
    - Loops through data row by row
    - If statement checks if there is data and if we havent iterated through the day yet and performs operation accordingly
    - Returns array with daily averages
    """
    daily_avg = []
    temp =[]

    for row in data:
        if row[pollutant]== "No data":
            print("No data")
        elif count == 23:
            count= 0
            daily_avg.append([np.average(temp), row[0], monitoring_station])
            temp =[]
        else:
            count += 1
            temp.append(float(row[pollutant]))
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
    daily_med = []
    temp= []
    count = 0

    for row in data:
        if row[pollutant]== "No data":
            print("No data")
        elif  count == 23:
            count = 0
            daily_med.append([np.median(temp), row[0], monitoring_station])
            temp = []
        else:
            count +=1
            temp.append(row[pollutant])
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
    hourly_average=[]
    hours = [[]*24]
    count = 1

    for row in data:
        # Possible issues with modulos function
        hours.append([count%24,row[pollutant]])
    
    for row in hours:
        hourly_average.append(np.average(row), row[1], monitoring_station,)
    print(hourly_average)

    return hourly_average

def monthly_average(data:list, monitoring_station:str, pollutant:str)->list:
    """
    Parameters: 
    -                                               
    - data = 2d array
    - monitoring_station = String of the name of the monitoring station
    - polluntant = "no" = Nitric Oxide "PM10" = Inhalable partical matter <= 10µm  "PM25" = Inhalable partical matter <= 2.5µm 
    \n
    Code: 
    - Initializes:
        - monthly_avg as empty array
        - pev_month as a january
        - temporary array
    - If statement checks if the current rows month is the same as the previous
    - If true we add pollutant value to the temporary array
    - Else we add the average of the temp array to the monthly_avg
    - Clear the temp array
    - set the new month while 
    - Add the current value to the new temp array
    - Return list of averages
    """
    monthly_avg = []
    prev_month = "01"
    temp=[]

    for row in data:
        if row[0][4:6] == prev_month:
            temp.append(row[pollutant])
        else:
            monthly_avg.append(np.average(temp))
            temp=[]
            prev_month = row[0][4:6]
            temp.append(row[pollutant])

    return monthly_avg

def peak_hour_date(data:list, date:str, monitoring_station:str, pollutant:str)->str:
    """
    Parameters: 
    -                                               
    - data = 2d array
    - monitoring_station = String of the name of the monitoring station
    - polluntant = "no" = Nitric Oxide "PM10" = Inhalable partical matter <= 10µm  "PM25" = Inhalable partical matter <= 2.5µm 
    \n
    Code:
    -
    - Initializes empty values array
    - Loops through the rows in data
    - Check if the row is equal to the specified date
    - Returns the result of values passed through the maxvalues function in utils.py
    """
    values =[]
    for row in data:
        if row[0] == date:
            values.append(row[pollutant])
    
    return utils.maxvalue(values)

    

def count_missing_data(data:list, monitoring_station:str, pollutant:str)->int:
    """
    Parameters: 
    -                                               
    - data = 2d array
    - monitoring_station = String of the name of the monitoring station
    - polluntant = "no" = Nitric Oxide "PM10" = Inhalable partical matter <= 10µm  "PM25" = Inhalable partical matter <= 2.5µm 
    \n
    Code:
    - Initializes empty array values
    - Loops through each row in the data
    - Appends just the pollutant value to values
    - Returns countvalue in utils with values and 'No data' as parameters
    """
    values =[]
    for row in data:
        values.append(row[pollutant])
    return utils.countvalue(values, "No data")

def fill_missing_data(data:list, new_value:any,  monitoring_station:str, pollutant:str):
    """
    Parameters: 
    -                                               
    - data = 2d array
    - monitoring_station = String of the name of the monitoring station
    - polluntant = "no" = Nitric Oxide "PM10" = Inhalable partical matter <= 10µm  "PM25" = Inhalable partical matter <= 2.5µm 
    \n
    Code:
    - Loops through each row in the data
    - If statement checks if the value equals 'No data' 
    - Replaces row[pollutant] with new_value
    - Write to csv file
    """
    for row in data:
        if row[pollutant]== "No data":
            row[pollutant] = new_value
            #write row to csv file
    
    ## Your code goes here
