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

#NOTE: docs and inline comments finished
def get_live_data_pollutant_plot(site_code='MY1',start_date=None,end_date=None):
    """
    Return data from the LondonAir API using its AirQuality API. 
    
    *** This function is provided as an example of how to retrieve data from the API. ***
    It requires the `requests` library which needs to be installed. 
    In order to use this function you first have to install the `requests` library.
    This code is provided as-is. 
    """
    #sets start date if no data if passed in
    start_date = datetime.date.today() if start_date is None else start_date
    #sets end date if no data is passed in
    end_date = start_date + datetime.timedelta(days=1) if end_date is None else end_date
    #url endpoint for api
    endpoint = "http://api.erg.ic.ac.uk/AirQuality/Data/Site/SiteCode={site_code}/StartDate={start_date}/EndDate={end_date}/Json"
    #formatter for url
    url = endpoint.format(
        site_code = site_code,
        start_date = start_date,
        end_date = end_date
    )
    # gets data from url
    res = requests.get(url)
    # returns data in json format
    return res.json()

#NOTE: docs and inline comments finished
def get_live_data_from_api_hourly():
    """
    Code:
    - 
    - Url for the api
    - requests the data from the api
    - returns json data
    """
    # url for api
    url ="http://api.erg.ic.ac.uk/AirQuality/Hourly/MonitoringIndex/GroupName=London/Json"
    #gets data
    res = requests.get(url)
    #returns data in json format
    return res.json()

#NOTE: docs and inline comments finished
def get_live_data_from_api_radar(site_code_1 = None, site_code_2 = None):
    """
    Code:
    - 
    - Url for the api
    - requests the data from the api
    - returns json data
    """
    # Default site codes are BG1 and MY1
    site_code_1 = "BG1" if site_code_1 is None else site_code_1
    site_code_2 = "MY1" if site_code_2 is None else site_code_2
    #gets data from the api for the first station
    url_1 ="https://api.erg.ic.ac.uk/AirQuality/Daily/MonitoringIndex/Latest/SiteCode="+site_code_1+"/Json"
    res_1 = requests.get(url_1)
    #gets data from the api for the second station
    url_2 ="https://api.erg.ic.ac.uk/AirQuality/Daily/MonitoringIndex/Latest/SiteCode="+site_code_2+"/Json"
    res_2 = requests.get(url_2)
    #returns the json data
    return res_1.json(), res_2.json()

#NOTE: docs and inline comments finished
def pollutant_plot(site_code=None, start=None, end=None, species_code=None,):
    """
    Code:
    -
    - Initializes variables
    - Gets data from the api
    - Loops through the data
    - Grabs info for the correct species
    - gets the values and dates of the variables
    - plots the data
    - shows the plotted data
    """
    #sets background to dark
    plt.style.use('dark_background')
    #initializes variables
    site_code = "MY1" if site_code is None else site_code
    start = datetime.date.today() if start is None else start
    end = start + datetime.timedelta(days=1) if end is None else end
    species_code = "NO2" if species_code is None else species_code
    variables = {'values':[],'dates':[]}
    #gets data from the api
    api_data = get_live_data_pollutant_plot(site_code,start,end)
    #loops through the data
    for i in api_data['AirQualityData']['Data']:
        #grabs info for the correct species
        if i['@SpeciesCode'] == species_code:
            #adds the values and dates to the variables
            variables['values'].append(i['@Value'])
            variables['dates'].append(i['@MeasurementDateGMT'])
    #plots the data
    plt.title(f'Site: {site_code} Pollutant: {species_code}')
    plt.xticks(ticks=range(len(variables['dates'])) , rotation=90)
    plt.xlabel('Time')
    plt.ylabel('Concentration')
    plt.plot(variables['dates'], variables['values'])
    plt.show()

#NOTE: docs and inline comments finished
def hourly_data()->dict:
    """
    Code:
    -
    - Grabs all hourly data from the api and returns it as a dictionary
    """
    #initializes dictionary to store data from the api
    data = {}
    #gets raw data from the api
    api_data = get_live_data_from_api_hourly()
    #loops through the local authorities
    for i in api_data['HourlyAirQualityIndex']['LocalAuthority']:
        #Checks if their are monitoring sites in the local authority
        if 'Site' in i.keys():
            #if the site is a list loop through the list
            if type(i['Site']) == list:
                for j in i['Site']:
                    #creates temporary dictionary to store data from the site
                    temp = {}
                    #if the site is a list loop through the list
                    if type(j['Species']) == list:
                        #loops through the items in species
                        for x in j['Species']:
                            #adds the species to the temporary dictionary
                            temp[x['@SpeciesCode']] = x['@AirQualityBand']
                    else:
                        #adds the species to the temporary dictionary
                        temp[j['Species']['@SpeciesCode']] = j['Species']['@AirQualityBand']
                    #adds the temporary dictionary to the data dictionary
                    data[j['@SiteName']+" "+j['@SiteCode']] = temp
            #if the site is a dictionary
            elif type(i['Site']) == dict:
                #creates temporary dictionary to store data from the site
                temp = {}
                #loops through species
                for k in i['Site']['Species']:
                    #adds the species to the temporary dictionary
                    temp[k['@SpeciesCode']] = k['@AirQualityBand']
                #adds the temporary dictionary to the data dictionary
                data[i['Site']['@SiteName']+" "+i['Site']['@SiteCode']] = temp
    return data

#NOTE: docs and inline comments finished
def hourly_formatted(data:dict, site_code:str, species_code:str):
    """
    Parameters:
    -
    - data: The data from the api
    - site_code: The site code for the station
    - species_code: The species code for the pollutant
    Code:
    -
    - Formats the hourly data from the api
    """
    #loops through the data
    for i in data:
        #Grabs the site code and comapres it to the site code given
        if i[-3:] == site_code:
            #check if the data is valid
            if "No data" == data[i][species_code]:
                #error message
                print("Unfortunately there is no data for this site and pollutant")
            else:
                #outputs data
                print("The air quality band for this site is:",data[i][species_code])

#NOTE: docs and inline comments finished
def radar_chart_data(site_code_1:str, site_code_2:str,):
    """
    Parameters:
    -
    - site_code_1: The site code for the first station
    - site_code_2: The site code for the second station
    Code:
    -
    - Gets data fromm api and stores it in a dictionary
    - Returns stations data
    """
    #Creates a dictionarys to store the data
    stations={}
    # grabs api data for both stations
    data_1, data_2= get_live_data_from_api_radar(site_code_1, site_code_2)

    ## creates dictionary with both stations
    stations[data_1['DailyAirQualityIndex']['LocalAuthority']['Site']['@SiteName']] = get_values(data_1)
    stations[data_2['DailyAirQualityIndex']['LocalAuthority']['Site']['@SiteName']] = get_values(data_2)

    # returns the dictionary with the stations
    return stations

#NOTE: docs and inline comments finished
def get_values(data:dict)->dict:
    """
    Parameters:
    -  data: The data from the api
    Code:
    -
    - Returns a dictionary with the species and their air quality index
    """
    #creates a temporary dictionary to store the data
    temp = {}
    #loops through the species
    for i in data['DailyAirQualityIndex']['LocalAuthority']['Site']['Species']:
        #adds the species to the temporary dictionary
        temp[i['@SpeciesCode']] = i['@AirQualityBand']
    #returns the temporary dictionary
    return temp

#NOTE: docs and inline comments finished
def plot_radar_chart(stations:dict):
    """
    Code:
    - 
    - Plots the 2 stations on a radar chart
    """

    # style of the plot
    plt.style.use('dark_background')
    # grabs keys from the dictionary
    keys = stations.keys()
    station_name_1, station_name_2 = list(keys)[0], list(keys)[1]
    # grabs values from the dictionary
    station_1, station_2 = list(stations[station_name_1].values()), list(stations[station_name_2].values())
    # fills in missing data with no data values
    station_1, station_2 = fill_missing_data(station_1), fill_missing_data(station_2)
    print(station_1, station_2)
    # starts at 0 and goes to 2pi ==360 degrees
    pollutants = ['CO', 'NO2', 'O3', 'PM10', 'PM25', 'SO2']
    angles = np.linspace(0,2*np.pi,len(pollutants), endpoint=False)
    angles=np.concatenate((angles,[angles[0]]))
    # makes data circular for consistancy when plotting
    pollutants.append(pollutants[0])
    station_1.append(station_1[0])
    station_2.append(station_2[0])
    # creates the plot
    fig=plt.figure(figsize=(7,7))
    ax=fig.add_subplot(polar=True)
    #plotting station 1
    ax.plot(angles, station_1)
    ax.plot(angles,station_1, 'o-', color='cyan', label= station_name_1)
    ax.fill(angles, station_1, alpha=0.25, color='cyan')
    #plotting station 2
    ax.plot(angles, station_2)
    ax.plot(angles,station_2, 'o-', color='magenta', label= station_name_2)
    ax.fill(angles, station_2, alpha=0.25, color='magenta')
    #making scale
    ax.plot(angles, ["No data","Low","Mid","High","Low","Mid","High"], color='white', alpha=0)
    # sets the labels/plot features
    ax.set_thetagrids(angles * 180/np.pi, pollutants)# type: ignore
    # sets y axis labels
    ax.set_yticklabels(["No data","Low","Mid","High"])
    # sets title
    plt.title(station_name_1+" VS "+station_name_2)
    # creates grid lines
    plt.grid(True)
    # provides automatic padding to subplot
    plt.tight_layout()
    # automatically handles labels
    plt.legend()
    # shows plot
    plt.show()

#NOTE: docs and inline comments finished
def fill_missing_data(station_list:list)->list:
    """
    Parameters:
    - 
    - station_list: The list of the station data
    Code:
    -
    - Fills in missing data with no data values
    """
    for i in range(1, 7-len(station_list)):
        station_list.append("No data")
    return station_list


if __name__ == '__main__':
    plot_radar_chart(radar_chart_data("MY1","BG2"))
