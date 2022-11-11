
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
    - Match statement handles user input of the menu and redirects to corresponding choice, if there is a error it calls the function again
    """
    choice = input("Main Menu:"
                +"\n\tR - Access to PR module"
                +"\n\tI - Access to MI module"
                +"\n\tM - Access to RM module"
                +"\n\tA - Print the about text"
                +"\n\tQ - Quit"
                +"\nChoice: ").upper()
    match(choice):
        case "R":
            reporting_menu()
        case "I":
            intelligence_menu()
        case "M":
            monitoring_menu()
        case "A":
            about()
        case "Q":
            quit()
        case _ :
            print("Error please try again\nRemember to us uppercase letters")
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
    - Monitoring station is choosen by the user and represented byb a number
    - Match statement sets monitoring station to string value
    - Pollutant is chosen by the the user and +2 is added to represent its column number in csv file
    - Match statement handles user input of the menu and redirects to corresponding choice, if there is a error it calls the function again
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
    
    match(station):
        case 0:
            monitoring_station = "London Harlington"
        case 1:
            monitoring_station = "London Marlylebone"
        case 2:
            monitoring_station = "London N Kensington"

    pollutant = input("Choose Pollutant:"
        +"\n\t0 - Nitric Oxide"
        +"\n\t1 - PM10"
        +"\n\t2 - PM25"
        +"\nChoice: ") +2


    match(choice):
        case "DA":
            data = utils.csv_to_array("Pollution-"+monitoring_station+".csv")

            print(reporting.daily_average(data,monitoring_station,pollutant))
        case "DM":
            reporting.daily_median()
        case "HA":
            reporting.hourly_average()
        case "MA":
            reporting.monthly_average()
        case "PH":
            reporting.peak_hour_date()
        case "M":
            main_menu()
        case _ :
            print("Error please try again\nRemember to us uppercase letters")
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