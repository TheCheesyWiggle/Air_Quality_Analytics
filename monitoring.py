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
    """
    Code:
    - 
    - Url for the api
    - requests the data from the api
    - returns json data
    """
    url ="http://api.erg.ic.ac.uk/AirQuality/Hourly/MonitoringIndex/GroupName=London/Json"
    res = requests.get(url)
    return res.json()

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

def hourly_data()->dict:
    """
    Code:
    -
    - Grabs all hourly data from the api and returns it as a dictionary
    """
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

def hourly_formatted(data:dict, site_code:str, species_code:str):

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

def api_formatted_for_radar_chart(site_code_1:str, site_code_2:str,):
    #initializes variables
    site_code_1 = "MY1" if site_code_1 is None else site_code_1
    site_code_2 = "BG1" if site_code_2 is None else site_code_2
    # grabs api data for both stations
    api_data_1 = get_live_data_pollutant_plot(site_code_1)
    api_data_2 = get_live_data_pollutant_plot(site_code_2)
    #NOTE:loops through variables and gets site name, species code and values
    
    
def plot_radar_chart(pollutants, station_1, station_2):
    #NOTE: Take stations as a dictionary then you can store site names too
    #NOTE: list of pollutants is the same for both stations
    # starts at 0 and goes to 2pi ==360 degrees
    angles = np.linspace(0,2*np.pi,len(pollutants), endpoint=False)
    angles=np.concatenate((angles,[angles[0]]))
    # makes data circular for consistancy when plotting
    pollutants.append(pollutants[0])
    station_1.append(station_1[0])
    station_2.append(station_2[0])
    # plotting station 1
    fig=plt.figure(figsize=(6,6))
    ax=fig.add_subplot(polar=True)
    ax.plot(angles, station_1)
    ax.plot(angles,station_1, 'o-', color='cyan', label='Station name')
    ax.fill(angles, station_1, alpha=0.25, color='cyan')
    #plotting station 2
    ax.plot(angles, station_2)
    ax.plot(angles,station_2, 'o-', color='magenta', label='Station name')
    ax.fill(angles, station_2, alpha=0.25, color='magenta')
    ax.set_thetagrids(angles * 180/np.pi, pollutants)# type: ignore
    plt.grid(True)
    plt.tight_layout()
    plt.legend()
    plt.show()

