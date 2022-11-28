
import utils
import reporting
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
    """Your documentation goes here"""
    choice = input("Monitoring Menu:"
                +"\nChoice: ").upper()

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

    if choice == "DA":
        data = utils.csvs_to_dict()
        print(reporting.daily_average(data,monitoring_station,pollutant)) #type: ignore
    elif choice == "DM":
        reporting.daily_median()  # type: ignore
    elif choice == "HA":
        reporting.hourly_average()  # type: ignore
    elif choice == "MA":
        reporting.monthly_average()  # type: ignore
    elif choice == "PH":
        reporting.peak_hour_date()  # type: ignore
    elif choice== "M":
        main_menu()
    else:
        print("Error please try again\nRemember to use uppercase letters")
        reporting_menu()

def intelligence_menu():
    """Your documentation goes here"""
    choice = input("Intelligence Menu:"
                +"\nChoice:").upper()

def about():
    """Your documentation goes here"""
    print("Module: ECM1400 \nCandidate Number: ???")
    return main_menu()

def quit():
    """Your documentation goes here"""
    exit()


if __name__ == '__main__':
    main_menu()