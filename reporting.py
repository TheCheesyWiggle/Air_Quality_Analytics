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
    # loops through pollutant values
    for i in poll_val:
        # checks if we have looped the entire day
        if count == 23:
            count= 0
            daily_avg.append(utils.meannvalue(temp))
            temp =[]
        elif i != "No data":
            count += 1
            temp.append(float(i))
        else:
            count += 1
            temp.append(float(0))
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
    # loops through pollutant values
    for i in poll_val:
        # checks if we have looped the entire day
        if count == 23:
            count= 0
            daily_med.append(np.median(temp))
            temp =[]
        elif i != "No data":
            count += 1
            temp.append(float(i))
        else:
            count += 1
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
            print(int(hour[:2]))
            # adds the data value
            hours[hour[:2]].append(float(poll_val[count]))

    # adds the mean values to the fianl array   
    for hr in hours:
        avg.append(float(utils.meannvalue(hours[hr])))
    #returns array of mean values
    print(avg)
    return avg

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
    # grabs the correct stations data
    station = data[monitoring_station]
    # grabs all the pollutant values
    poll_val = station[pollutant]
    # grabs date valeus
    date = station["date"]
    # dictionary of months
    months = {"01":[],"02":[],"03":[],"04":[],"05":[],"06":[], "07":[], "08":[], "09":[], "10":[], "11":[], "12":[]}
    #
    monthly_avg = []*12
    prev_month = "01"
    temp=[]

    for index, month  in enumerate(date):
        month = month.split("-")[1]
        if poll_val[index] != "No data":
            if month == prev_month:
                months[month].append(float(poll_val[index]))
            else:
                months[month].append(float(poll_val[index]))
                prev_month = month
        else:
            months[month].append(float(0))

    for m in months:
        monthly_avg.append(float(utils.meannvalue(months[m])))
    
    return monthly_avg

        
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

if __name__ == '__main__':
    dic = utils.csvs_to_dict()
    hourly_average(dic, "London Harlington","no")