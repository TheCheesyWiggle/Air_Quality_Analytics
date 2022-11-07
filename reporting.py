import numpy
# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification


def daily_average(data, monitoring_station:str, pollutant:str):
    """
    Parameters:                                                
    - data = array 2D?
    - monitoring_station = String of the name of the monitoring station
    - polluntant = "no" = Nitric Oxide "PM10" = Inhalable partical matter <= 10µm  "PM25" = Inhalable partical matter <= 2.5µm        
    """
    
    match(pollutant):
        case "no":
            pol_num = 2
        case "PM10":
            pol_num = 3
        case "PM25":
            pol_num = 4

    daily_avg = []
    count, calc_avg, no_data= 0,0,0
    for row in data:
        if row[pol_num]== "No data":
            print("No data")
            no_data += 1
        elif count == 23:
            count,no_data = 0,0
            print(calc_avg)
            daily_avg.append(calc_avg/(24-no_data))
            calc_avg =float(row[pol_num])
        else:
            count += 1
            calc_avg += float(row[pol_num])
    print(daily_avg)

    return daily_avg
    ## Your code goes here

def daily_median(data, monitoring_station, pollutant):
    """Your documentation goes here"""
    
    ## Your code goes here
def hourly_average(data, monitoring_station, pollutant):
    """Your documentation goes here"""
    
    ## Your code goes here
def monthly_average(data, monitoring_station, pollutant):
    """Your documentation goes here"""
    
    ## Your code goes here
def peak_hour_date(data, date, monitoring_station,pollutant):
    """Your documentation goes here"""
    
    ## Your code goes here

def count_missing_data(data,  monitoring_station,pollutant):
    """Your documentation goes here"""
    
    ## Your code goes here

def fill_missing_data(data, new_value,  monitoring_station,pollutant):
    """Your documentation goes here"""
    
    ## Your code goes here



