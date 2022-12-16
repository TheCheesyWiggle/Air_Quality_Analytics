import utils
import numpy as np

# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification

#NOTE: docs and inline comments finished
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
    # loops through pollutant values
    for i in poll_val:
        # checks if we have looped the entire day
        if count == 23:
            # resets count 
            count= 0
            # added the mean value to daily_avg
            daily_avg.append(np.average(temp))
            #resets temporary array
            temp =[]
        #checks of there is data 
        elif i != "No data":
            count += 1
            temp.append(float(i))
        # if there isnt data just increment count by 1
        else:
            count += 1
    return daily_avg

#NOTE: docs and inline comments finished
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
    # loops through pollutant values
    for i in poll_val:
        # checks if we have looped the entire day
        if count == 23:
            # resets count
            count= 0
            # adds daily median too daily med
            daily_med.append(np.median(temp))
            # resets temp array
            temp =[]
        #checks if there is data
        elif i != "No data":
            # increment counter to keep track of the days
            count += 1
            #adds value too temporary array
            temp.append(float(i))
        else:
            # increments counter
            count += 1
    return daily_med

#NOTE: docs and inline comments finished
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
    - Grabs all the data and puts it into an hour dictionary
    - Averages the arrays in the dictionary
    - Returns average for each hour across the entire dataset
    """
    #gets data for specified monitoring station
    station = data[monitoring_station]
    # grabs the time data from the time column
    time = station["time"]
    #grabs all the pollutant values
    poll_val = station[pollutant]
    #sets up a dictionary with arrays with the hours so we can easily add the hours in
    hours={"01":[],"02":[],"03":[],"04":[],"05":[],"06":[], "07":[], "08":[], "09":[], "10":[], "11":[], "12":[], "13":[], "14":[], "15":[], "16":[], "17":[], "18":[], "19":[], "20":[], "21":[], "22":[], "23":[], "24":[]}
    #sets up final emtpy array
    avg = []*24
    #loops through time while giving an index for the equivalent in the pollant list
    for count, hour in enumerate(time):
        # checks if the pollutant value has data
        if poll_val[count] != "No data":
            # adds the data value
            hours[hour[:2]].append(float(poll_val[count]))
    # adds the mean values to the fianl array   
    for hr in hours:
        avg.append(float(np.average(hours[hr])))
    #returns array of mean values
    return avg

#NOTE: docs and inline comments finished
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
    - Gets all the data from the api and sorts it by month
    """
    # grabs the correct stations data
    station = data[monitoring_station]
    # grabs all the pollutant values
    poll_val = station[pollutant]
    # grabs date valeus
    date = station["date"]
    # dictionary of months
    months = {"01":[],"02":[],"03":[],"04":[],"05":[],"06":[], "07":[], "08":[], "09":[], "10":[], "11":[], "12":[]}
    # sets up empty array with 12 values
    monthly_avg = []*12
    #sets month to jan
    prev_month = "01"
    # loops through the data
    for index, month  in enumerate(date):
        #gets the month from the date
        month = month.split("-")[1]
        # checks if there is data
        if poll_val[index] != "No data":
            #checks if we are in the same month
            if month == prev_month:
                #adds value to the dictionary
                months[month].append(float(poll_val[index]))
            else:
                # changes month
                prev_month = month
                # adds value to the dictionary
                months[month].append(float(poll_val[index]))      
        else:

            months[month].append(float(0))
    # loops through dictionary and gets mean values for the arraysd
    for m in months:
        monthly_avg.append(float(np.average(months[m])))
    
    return monthly_avg

#NOTE: docs and inline comments finished
def peak_hour_date(data:dict, date:str, monitoring_station:str, pollutant:str)->float:
    """
    Parameters: 
    -                                               
    - data = Dictionary
    - monitoring_station = String of the name of the monitoring station
    - polluntant = "no" = Nitric Oxide "PM10" = Inhalable partical matter <= 10µm  "PM25" = Inhalable partical matter <= 2.5µm 
    \n
    Code:
    -
    - Gets all the data for the day and puts it in an array
    - Gets the max value from the array
    """
    # grabs required station data
    station = data[monitoring_station]
    # grabs required polluntant data
    poll_val = station[pollutant]
    # empty array
    values =[]
    # loops through the data
    for index, day in enumerate(station["date"]):
        # checks date
        if day == date:
            # adds values to the empty array
            values.append(float(poll_val[index]))
    # returns max values
    return utils.maxvalue(values)

#NOTE: docs and inline comments finished
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
    # gets all the data for the required station
    station = data[monitoring_station]
    # gets all pollutant data
    poll_val = station[pollutant]
    # sets up empty array
    values =[]
    # loops through pollutant values
    for i in poll_val:
        #adds value to empty array
        values.append(i)
    #counts values through utils function
    return utils.countvalue(values, "No data")

#NOTE: docs and inline comments finished
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
    - Finds values equal to No data
    - Overwrites values with new data
    """
    # gets all data for the required station
    station = data[monitoring_station]
    # gets data for the pollutants
    poll_val = station[pollutant]
    # loops through pollutants
    for index, value in enumerate(poll_val):
        # checks if there is data
        if value == "No data":
            # Overwrites the data in poll_val
            poll_val[index] = new_value
    # overwites data in station[pollutant] structure
    station[pollutant] = poll_val
    # overwrites data in the data[monitoring station] structure
    data[monitoring_station] = station
    #returns data
    return data

if __name__ == '__main__':
    dic = utils.csvs_to_dict()
    print(peak_hour_date(dic,"2021-09-01","London N Kensington", "pm25"))