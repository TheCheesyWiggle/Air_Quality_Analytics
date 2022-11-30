# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification.
# 
# This module will access data from the LondonAir Application Programming Interface (API)
# The API provides access to data to monitoring stations. 
# 
# You can access the API documentation here http://api.erg.ic.ac.uk/AirQuality/help
#
import requests
import datetime
import json

def get_live_data_from_api(*args,**kwargs):
    """
    Return data from the LondonAir API using its AirQuality API. 
    
    *** This function is provided as an example of how to retrieve data from the API. ***
    It requires the `requests` library which needs to be installed. 
    In order to use this function you first have to install the `requests` library.
    This code is provided as-is. 
    """
    
    url = "http://api.erg.ic.ac.uk/AirQuality/Hourly/MonitoringIndex/GroupName=London/Json"
    
    res = requests.get(url)
    #print(json.dumps(res.json(), indent=4))
    return res.json()


def rm_function_1(*args,**kwargs):
    """Your documentation goes here"""
    # Your code goes here
    
    

def rm_function_2(*args,**kwargs):
    """Your documentation goes here"""
    # Your code goes here

def rm_function_3(*args,**kwargs):
    """Your documentation goes here"""
    api_data = get_live_data_from_api()
    #print(api_data.keys())
    #print(api_data['HourlyAirQualityIndex'].keys())
    #print(api_data['HourlyAirQualityIndex']['LocalAuthority'][0])
    for i in api_data['HourlyAirQualityIndex']['LocalAuthority']:
        if 'Site' in i.keys():
            if type(i['Site']) == list:
                for j in i['Site']:
                    print(j['@SiteName'])
            elif type(i['Site']) == dict:
                print(i['Site']['@SiteName'])
    
def rm_function_4(*args,**kwargs):
    """Your documentation goes here"""
    # Your code goes here

#print(get_live_data_from_api('MY1', 'NO'))
rm_function_3()