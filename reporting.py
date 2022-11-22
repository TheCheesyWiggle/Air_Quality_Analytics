import utils
import numpy as np

# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification


def daily_average(data:dict, monitoring_station:str, pollutant:str) -> list:
    """
    Parameters: 
    -                                               
    - data = Dictionary
    - monitoring_station = String of the name of the monitoring station
    - polluntant = "no" = Nitric Oxide "PM10" = Inhalable partical matter <= 10µm  "PM25" = Inhalable partical matter <= 2.5µm 
    \n
    Code:
    - Grabs station data for intended station
    - initialises empty arrays for later use
    - initalizes count so we can track what hour we are one
    - loops for every value on the no nested dict
    - If statement checks if there is data and if we havent iterated through the day yet and performs operation accordingly
   """
    station = data[monitoring_station]
    poll_val = station[pollutant]
    daily_avg, temp = [], []
    count = 0
    for i in poll_val:
        if i == "No data":
            print("No data")
        elif count == 23:
            count= 0
            daily_avg.append(np.average(temp))
            temp =[]
        else:
            count += 1
            temp.append(float(i))
    return daily_avg

def daily_median(data:dict, monitoring_station:str, pollutant:str) -> list:
    """
    Parameters: 
    -                                               
    - data = Dictionary
    - monitoring_station = String of the name of the monitoring station
    - polluntant = "no" = Nitric Oxide "PM10" = Inhalable partical matter <= 10µm  "PM25" = Inhalable partical matter <= 2.5µm 
    \n
    Code: 
    - Grabs all the data for the intended station
    - Initalizes empty arrays ffor later use
    - initalizes count so we can track what hour we are one
    - loops for every value in the poll_val variable
    - If statement checks if there is data and if we havent iterated through the day yet and performs operation accordingly
    """
    station = data[monitoring_station]
    poll_val = station[pollutant]
    daily_med, temp = [], []
    count = 0
    for i in poll_val:
        if i == "No data":
            print("No data")
        elif count == 23:
            count= 0
            daily_med.append(np.median(temp))
            temp = []
        else:
            count += 1
            temp.append(float(i))
    return daily_med

def hourly_average(data:dict, monitoring_station:str, pollutant:str)->list:
    """
    Parameters: 
    -                                               
    - data = Dictionary
    - monitoring_station = String of the name of the monitoring station
    - polluntant = "no" = Nitric Oxide "PM10" = Inhalable partical matter <= 10µm  "PM25" = Inhalable partical matter <= 2.5µm 
    \n
    Code: 
    - 
    """
    station = data[monitoring_station]
    poll_val = station[pollutant]
    hourly_average=[]
    #get the keys of each hour in the time key
    # uses these keys to find the corresponing values ion the correct pollutant column
    return hourly_average

def monthly_average(data:dict, monitoring_station:str, pollutant:str)->list:
    """
    Parameters: 
    -                                               
    - data = Dictionary
    - monitoring_station = String of the name of the monitoring station
    - polluntant = "no" = Nitric Oxide "PM10" = Inhalable partical matter <= 10µm  "PM25" = Inhalable partical matter <= 2.5µm 
    \n
    Code: 
    -
    """
    station = data[monitoring_station]
    poll_val = station[pollutant]
    monthly_avg = []
    #get the keys of each month in the date key
    # uses these keys to find the corresponing values ion the correct pollutant column
    return monthly_avg

def peak_hour_date(data:dict, date:str, monitoring_station:str, pollutant:str)->str:
    """
    Parameters: 
    -                                               
    - data = Dictionary
    - monitoring_station = String of the name of the monitoring station
    - polluntant = "no" = Nitric Oxide "PM10" = Inhalable partical matter <= 10µm  "PM25" = Inhalable partical matter <= 2.5µm 
    \n
    Code:
    -
    """
    # grab all values form one day and compare
    station = data[monitoring_station]
    poll_val = station[pollutant]
    values =[]
    return utils.maxvalue(values)

def count_missing_data(data:dict, monitoring_station:str, pollutant:str)->int:
    """
    Parameters: 
    -                                               
    - data = 2d array
    - monitoring_station = String of the name of the monitoring station
    - polluntant = "no" = Nitric Oxide "PM10" = Inhalable partical matter <= 10µm  "PM25" = Inhalable partical matter <= 2.5µm 
    \n
    Code:
    - Initializes empty array values
    - Loops through the dictionary
    - Appends just the pollutant value to values
    - Returns countvalue in utils with values and 'No data' as parameters
    """
    ## loop through dict to find missing data
    station = data[monitoring_station]
    poll_val = station[pollutant]
    values =[]
    for i in poll_val:
        values.append(i)
    return utils.countvalue(values, "No data")

def fill_missing_data(data:dict, new_value:any,  monitoring_station:str, pollutant:str):
    """
    Parameters: 
    -                                               
    - data = Dictionary
    - monitoring_station = String of the name of the monitoring station
    - polluntant = "no" = Nitric Oxide "PM10" = Inhalable partical matter <= 10µm  "PM25" = Inhalable partical matter <= 2.5µm 
    \n
    Code:
    - 
    """
    station = data[monitoring_station]
    poll_val = station[pollutant]

print(daily_median(utils.csvs_to_dict(),"London Harlington","no"))