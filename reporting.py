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
        if count == 23:
            count= 0
            daily_avg.append(np.average(temp))
            temp =[]
        elif i != "No data":
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
    time = station["time"]
    poll_val = station[pollutant]
    hours={"01":[],"02":[],"03":[],"04":[],"05":[],"06":[], "07":[], "08":[], "09":[], "10":[], "11":[], "12":[], "13":[], "14":[], "15":[], "16":[], "17":[], "18":[], "19":[], "20":[], "21":[], "22":[], "23":[], "24":[]}
    hourly_avg = []*24

    for count, hour in enumerate(time):
        if poll_val[count] != "No data":
            hourly_avg[hour[:2]].append(float(poll_val[count]))
        
    for hr in hours:
        hourly_avg.append(utils.meannvalue(hours[hr]))

    return hourly_avg

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
    date = station["date"]
    monthly_avg = []
    prev_month = "01"
    temp=[]

    for index, month  in enumerate(date):
        month = month.split("-")[1]
        if poll_val[index] != "No data":
            if month == prev_month:
                temp.append(float(poll_val[index]))
            else:
                print(temp)
                monthly_avg.append(utils.meannvalue(temp))
                temp = []
                temp.append(poll_val[index])
                prev_month = month

    print(monthly_avg)
        
    #get the keys of each month in the date key
    # uses these keys to find the corresponing values ion the correct pollutant column
    return monthly_avg

def peak_hour_date(data:dict, date:str, monitoring_station:str, pollutant:str)->int:
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
    for index, day in enumerate(station["date"]):
        if day == date:
            values.append(poll_val[index])
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
    print(utils.countvalue(values, "No data"))
    return utils.countvalue(values, "No data")

def fill_missing_data(data:dict, new_value,  monitoring_station:str, pollutant:str):
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
    for index, value in enumerate(poll_val):
        if value == "No data":
            poll_val[index] = new_value
    station[pollutant] = poll_val
    data[monitoring_station] = station
    return data
