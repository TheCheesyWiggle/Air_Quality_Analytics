
from colours import fg,bg,decor
import reporting, monitoring, intelligence, utils
# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification


def main_menu():
    """
    Code:
    -
    - choice variable stores user input
    - if else statement handles user input of the menu and redirects to corresponding choice, if there is a error it calls the function again
    """
    choice = input(fg.pink + decor.bold+"Main Menu:"+ decor.reset+ fg.cyan
                +"\n\tR - Access to PR module"
                +"\n\tI - Access to MI module"
                +"\n\tM - Access to RM module"
                +"\n\tA - Print the about text"
                +"\n\tQ - Quit" + fg.pink+ decor.bold
                +"\nChoice: " + decor.reset+fg.lightgreen).upper()
    print(decor.reset)
    if choice == "R":
        reporting_menu()
    elif choice == "I":
        intelligence_menu()
    elif choice == "M":
        monitoring_menu()
    elif choice == "A":
        about()
    elif choice == "Q":
        quit()
    else:
        print(fg.red+decor.bold+"Error please try again"+decor.reset+fg.red+decor.italic+"\nRemember to use uppercase letters"+ decor.reset)
        main_menu()

def monitoring_menu():
    """
    Code:
    -
    - choice variable stores user input
    - if else statement handles user input of the menu and redirects to corresponding choice, if there is a error it calls the function again
    - during th eif else statement the user is asked for the site code, start date, end date and species code 
    - this input is then passed into the functions
    """
    choice = input(fg.pink + decor.bold+"Monitoring Menu:"+ decor.reset+ fg.cyan
        +"\n\t1 - Graph"
        +"\n\t2 - Hourly data"+fg.pink + decor.bold
        +"\nChoice: "+ fg.lightgreen).upper()
    
    if choice == "1":
        site_code = input(fg.pink + decor.bold+"Please enter the site code: "+ decor.reset+fg.lightgreen).upper()
        start = input(fg.pink + decor.bold+"Please enter the start date (yyyy-mm-dd): "+decor.reset+ fg.lightgreen)
        end = input(fg.pink + decor.bold+"Please enter the end date (yyyy-mm-dd): "+ decor.reset+fg.lightgreen)
        species_code = input(fg.pink + decor.bold+"Please enter the species code: "+ decor.reset+fg.lightgreen).upper()
        print(decor.reset)
        monitoring.pollutant_plot(site_code,start,end,species_code)
    elif choice == "2":
        site_code = input(fg.pink + decor.bold+"Please enter the site code: "+ decor.reset+fg.lightgreen).upper()
        species_code = input(fg.pink + decor.bold+"Please enter the species code: "+ decor.reset+fg.lightgreen).upper()
        print(decor.reset)
        monitoring.hourly_formatted(monitoring.hourly_data(),site_code,species_code)
    else:
        print(decor.reset+fg.red+decor.bold+"Error please try again"+decor.reset+fg.red+decor.italic+"\nRemember to double check the data entered is correct"+ decor.reset)
        print(decor.reset)
        monitoring_menu()

def reporting_menu():
    """
    Code:
    -
    - choice variable stores user input
    - if else statement sets monitoring station to string value
    - Pollutant is chosen by the the user 
    - if else statement handles user input of the menu and redirects to corresponding choice, if there is a error it calls the function again
    """
    choice = input(fg.pink + decor.bold+"Reporting Menu:"+ decor.reset+ fg.cyan
        +"\n\tDA - Access to daily average"
        +"\n\tDM - Access to daily median"
        +"\n\tHA - Access to hourly average"
        +"\n\tMA - Access to monthly average"
        +"\n\tPH - Access to peak hour of polution for a given date"
        +"\n\tDA - Access to daily average"
        +"\n\tM - Main Menu" + fg.pink + decor.bold
        +"\nChoice: "+decor.reset+fg.lightgreen).upper()
    
    if choice != ("DA" or "DM" or "HA" or "MA" or "PH" or "M"):
        print(fg.red+decor.bold+"Error please try again"+decor.reset+fg.red+decor.italic+"\nRemember to use uppercase letters"+ decor.reset)
        reporting_menu()

    station = input(fg.pink + decor.bold+"Choose Monitoring Station:"+ decor.reset+ fg.cyan
        +"\n\t0 - London Harlington"
        +"\n\t1 - London Marlylebone"
        +"\n\t2 - London N Kensington"+ fg.pink + decor.bold
        +"\nChoice: "+decor.reset+fg.lightgreen)
    
    if station == "0":
        monitoring_station = "London Harlington"
    elif station == "1":
        monitoring_station = "London Marlylebone"
    elif station == "2":
        monitoring_station = "London N Kensington"
    else:
        monitoring_station = "ERROR"
        print(fg.red+decor.bold+"Error please try again"+decor.reset+fg.red+decor.italic+"\nRemember to only use numbers"+ decor.reset)
        reporting_menu()
    
    #grabs pollutant as a lower case string so it can be used to compare to the csv headers
    pollutant = input(fg.pink + decor.bold+"Choose Pollutant:"+ decor.reset+ fg.cyan
        +"\n\tNO - Nitric Oxide"
        +"\n\tPM10 - PM10"
        +"\n\tPM25 - PM25"+ fg.pink + decor.bold
        +"\nChoice: "+decor.reset+fg.lightgreen).lower()
    
    if pollutant != "no" and pollutant != "pm10" and pollutant != "pm25":
        print(fg.red+decor.bold+"Error please try again"+decor.reset+fg.red+decor.italic+"\nRemember to use lowercase letters"+ decor.reset)
        reporting_menu()
    print(decor.reset)
    data = utils.csvs_to_dict()

    if choice == "DA":
        print(reporting.daily_average(data, monitoring_station, pollutant))
    elif choice == "DM":
        reporting.daily_median(data, monitoring_station, pollutant)
    elif choice == "HA":
        reporting.hourly_average(data, monitoring_station, pollutant)
    elif choice == "MA":
        reporting.monthly_average(data, monitoring_station, pollutant) 
    elif choice == "PH":
        date = input(fg.pink + decor.bold+"Please enter the date (yyyy-mm-dd): "+decor.reset+fg.lightgreen)
        reporting.peak_hour_date(data, date, monitoring_station, pollutant) 
    elif choice== "M":
        main_menu()
    else:
        print(fg.red+decor.bold+"Error please try again"+decor.reset+fg.red+decor.italic+"\nRemember to use uppercase letters"+ decor.reset)
        reporting_menu()

def intelligence_menu():
    """
    Code:
    - Choice variable stores user input which service the want
    - if else statement handles user input of the menu and redirects to corresponding choice, if there is a error it calls the function again
    - second choice variable stores user input which colour pixels they want attributed for the service
    - if else statement handles user input of the menu and redirects to corresponding choice, if there is a error it calls the function again
    
    """
    
    choice = input(fg.pink + decor.bold+"Intelligence Menu:"+ decor.reset+ fg.cyan
        +"\n\tFP - Find Pixels"
        +"\n\tFC - Find Connected Components"
        +"\n\tSC - Sort Connected Components"+ fg.pink + decor.bold
        +"\nChoice: "+decor.reset+fg.lightgreen).upper()

    if choice == "FP":
        choice2 = input(decor.reset+ fg.cyan+"R - Red Pixels"
            +"\n\tC - Cyan Pixels"+ fg.pink + decor.bold
            +"\nChoice: "+decor.reset+fg.lightgreen).upper()
        print(decor.reset)
        if choice2 == "R":
            intelligence.find_red_pixels("data//map.png",upper_threshold=100,lower_threshold=50)
        elif choice2 == "C":
            intelligence.find_cyan_pixels("data//map.png",upper_threshold=100,lower_threshold=50)
        else:
            intelligence_menu()
    elif choice == "FC":
        choice2 = input(decor.reset+ fg.cyan+"R - Red Pixels"
            +"\n\tC - Cyan Pixels"+ fg.pink + decor.bold
            +"\nChoice: "+decor.reset+fg.lightgreen).upper()
        print(decor.reset)
        if choice2 == "R":
            intelligence.detect_connected_components(intelligence.find_red_pixels("data//map.png",upper_threshold=100,lower_threshold=50))
        elif choice2 == "C":
            intelligence.detect_connected_components(intelligence.find_cyan_pixels("data//map.png",upper_threshold=100,lower_threshold=50))
        else:
            intelligence_menu()
    elif choice == "SC":
        choice2 = input(decor.reset+ fg.cyan+"R - Red Pixels"
            +"\n\tC - Cyan Pixels"+ fg.pink + decor.bold
            +"\nChoice: "+decor.reset+fg.lightgreen).upper()
        print(decor.reset)
        if choice2 == "R":
            intelligence.detect_connected_components_sorted(intelligence.detect_connected_components(intelligence.find_red_pixels("data//map.png",upper_threshold=100,lower_threshold=50)))
        elif choice2 == "C":
            intelligence.detect_connected_components_sorted(intelligence.detect_connected_components(intelligence.find_cyan_pixels("data//map.png",upper_threshold=100,lower_threshold=50)))
        else:
            intelligence_menu()
    else:
        intelligence_menu()
        
def about():
    """
    Code:
    - Prints the module and candidate number
    """
    print(decor.reset+ fg.cyan+"Module: ECM1400 \nCandidate Number: 720019013"+decor.reset)
    return main_menu()

def quit():
    """
    Code:
    - Exits the program
    """
    exit()

if __name__ == '__main__':
    main_menu()