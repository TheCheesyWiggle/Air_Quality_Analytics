
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
    choice = input("Main Menu:"
                +"\n\tR - Access to PR module"
                +"\n\tI - Access to MI module"
                +"\n\tM - Access to RM module"
                +"\n\tA - Print the about text"
                +"\n\tQ - Quit"
                +"\nChoice: ").upper()

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
        print("Error please try again\nRemember to use uppercase letters")
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
    choice = input("Monitoring Menu:"
        +"\n\t1 - Graph"
        +"\n\t2 - Hourly data"
        +"\nChoice: ").upper()
    
    if choice == "1":
        site_code = input("Please enter the site code: ").upper()
        start = input("Please enter the start date (yyyy-mm-dd): ")
        end = input("Please enter the end date (yyyy-mm-dd): ")
        species_code = input("Please enter the species code: ").upper()
        monitoring.pollutant_plot(site_code,start,end,species_code)
    elif choice == "2":
        site_code = input("Please enter the site code: ").upper()
        species_code = input("Please enter the species code: ").upper()
        monitoring.hourly_formatted(monitoring.hourly_data(),site_code,species_code)

def reporting_menu():
    """
    Code:
    -
    - choice variable stores user input
    - if else statement sets monitoring station to string value
    - Pollutant is chosen by the the user 
    - if else statement handles user input of the menu and redirects to corresponding choice, if there is a error it calls the function again
    """
    choice = input("Reporting Menu:"
        +"\n\tDA - Access to daily average"
        +"\n\tDM - Access to daily median"
        +"\n\tHA - Access to hourly average"
        +"\n\tMA - Access to monthly average"
        +"\n\tPH - Access to peak hour of polution for a given date"
        +"\n\tDA - Access to daily average"
        +"\n\tM - Main Menu"
        +"\nChoice: ").upper()

    station = input("Choose Monitoring Station:"
        +"\n\t0 - London Harlington"
        +"\n\t1 - London Marlylebone"
        +"\n\t2 - London N Kensington"
        +"\nChoice: ")
    
    if station == "0":
        monitoring_station = "London Harlington"
    elif station == "1":
        monitoring_station = "London Marlylebone"
    elif station == "2":
        monitoring_station = "London N Kensington"
    else:
        monitoring_station = "ERROR"
        print("Error please try again\nRemember to use only numbers")
        monitoring_menu()

    pollutant = input("Choose Pollutant:"
        +"\n\tNO - Nitric Oxide"
        +"\n\tPM10 - PM10"
        +"\n\tPM25 - PM25"
        +"\nChoice: ").lower()
    
    if pollutant != "no" and pollutant != "pm10" and pollutant != "pm25":
        print("Error please try again\nRemember to use uppercase letters")
        reporting_menu()

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
        date = input("Please enter the date (yyyy-mm-dd): ")
        reporting.peak_hour_date(data, date, monitoring_station, pollutant) 
    elif choice== "M":
        main_menu()
    else:
        print("Error please try again\nRemember to use uppercase letters")
        reporting_menu()

def intelligence_menu():
    """
    Code:
    - Choice variable stores user input which service the want
    - if else statement handles user input of the menu and redirects to corresponding choice, if there is a error it calls the function again
    - second choice variable stores user input which colour pixels they want attributed for the service
    - if else statement handles user input of the menu and redirects to corresponding choice, if there is a error it calls the function again
    
    """
    
    choice = input("Intelligence Menu:"
        +"\n\tFP - Find Pixels"
        +"\n\tFC - Find Connected Components"
        +"\n\tSC - Sort Connected Components"
        +"\nChoice: ").upper()

    if choice == "FP":
        choice2 = input("R - Red Pixels"
            +"\n\tC - Cyan Pixels")
        if choice2 == "R":
            intelligence.find_red_pixels("data//map.png",upper_threshold=100,lower_threshold=50)
        elif choice2 == "C":
            intelligence.find_cyan_pixels("data//map.png",upper_threshold=100,lower_threshold=50)
        else:
            intelligence_menu()
    elif choice == "FC":
        choice2 = input("R - Red Pixels"
            +"\n\tC - Cyan Pixels")
        if choice2 == "R":
            intelligence.detect_connected_components(intelligence.find_red_pixels("data//map.png",upper_threshold=100,lower_threshold=50))
        elif choice2 == "C":
            intelligence.detect_connected_components(intelligence.find_cyan_pixels("data//map.png",upper_threshold=100,lower_threshold=50))
        else:
            intelligence_menu()
    elif choice == "SC":
        choice2 = input("R - Red Pixels"
            +"\n\tC - Cyan Pixels")
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
    print("Module: ECM1400 \nCandidate Number: 720019013")
    return main_menu()

def quit():
    """
    Code:
    - Exits the program
    """
    exit()


if __name__ == '__main__':
    main_menu()