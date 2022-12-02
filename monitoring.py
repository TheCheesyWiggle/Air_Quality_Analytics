# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification.
# 
# This module will access data from the LondonAir Application Programming Interface (API)
# The API provides access to data to monitoring stations. 
# 
# You can access the API documentation here http://api.erg.ic.ac.uk/AirQuality/help
# 
#overlay a contour map on a image of london
#change map for different pollutants
#change map for different days
#
import requests
import datetime
import json
import numpy as np
import utils
import matplotlib.pyplot as plt

def get_live_data_pollutant_plot(site_code='MY1',start_date=None,end_date=None):
    """
    Return data from the LondonAir API using its AirQuality API. 
    
    *** This function is provided as an example of how to retrieve data from the API. ***
    It requires the `requests` library which needs to be installed. 
    In order to use this function you first have to install the `requests` library.
    This code is provided as-is. 
    date format yyyy-mm-dd
    """
    start_date = datetime.date.today() if start_date is None else start_date
    end_date = start_date + datetime.timedelta(days=1) if end_date is None else end_date
    endpoint = "http://api.erg.ic.ac.uk/AirQuality/Data/Site/SiteCode={site_code}/StartDate={start_date}/EndDate={end_date}/Json"

    url = endpoint.format(
        site_code = site_code,
        start_date = start_date,
        end_date = end_date
    )
    
    res = requests.get(url)
    return res.json()

def get_live_data_from_api():
    url ="http://api.erg.ic.ac.uk/AirQuality/Hourly/MonitoringIndex/GroupName=London/Json"
    res = requests.get(url)
    return res.json()

def pollutant_plot(*args,**kwargs):
    """Your documentation goes here"""
    site_code= args[0]
    start = args[1]
    end = args[2]
    species_code = args[3]
    variables = {'values':[],'dates':[]}

    api_data = get_live_data_pollutant_plot(site_code,start,end)
    for i in api_data['AirQualityData']['Data']:
        if i['@SpeciesCode'] == species_code:
            variables['values'].append(i['@Value'])
            variables['dates'].append(i['@MeasurementDateGMT'])

    plt.title(f'Site: {site_code} Pollutant: {species_code}')
    plt.xticks(ticks=range(len(variables['dates'])) , rotation=90)
    plt.xlabel('Time')
    plt.ylabel('Concentration')
    plt.plot(variables['dates'], variables['values'])
    plt.show()


    


    
    

def rm_function_2(*args,**kwargs):
    """Your documentation goes here"""



def hourly_data(*args,**kwargs)->dict:
    """Your documentation goes here"""
    #initializes dictionary to store data from the api
    data = {}
    #gets raw data from the api
    api_data = get_live_data_from_api()
    #loops through the local authorities
    for i in api_data['HourlyAirQualityIndex']['LocalAuthority']:
        #Checks if their are monitoring sites in the local authority
        if 'Site' in i.keys():
            #if the site is a list loop through the list
            if type(i['Site']) == list:
                for j in i['Site']:
                    #creates 
                    temp = {}
                    if type(j['Species']) == list:
                        for x in j['Species']:
                            temp[x['@SpeciesCode']] = x['@AirQualityBand']
                    else:
                        temp[j['Species']['@SpeciesCode']] = j['Species']['@AirQualityBand']
                    data[j['@SiteName']+" "+j['@SiteCode']] = temp
            elif type(i['Site']) == dict:
                temp = {}
                for k in i['Site']['Species']:
                    temp[k['@SpeciesCode']] = k['@AirQualityBand']
                data[i['Site']['@SiteName']+" "+i['Site']['@SiteCode']] = temp
    return data
    
def rm_function_4(*args,**kwargs):
    """Your documentation goes here"""
    # Your code goes here


#pollutant_plot('BG1','2019-01-01','2019-01-02','SO2')
print(hourly_data())