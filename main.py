import sys
import reporting
import csv
import os
# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification


def main_menu():
    """
    -  User input assigned to the choice variable
    -  Match statement checks each case and executes accordingly and if the input doesnt match it outputs an error message and returns to main menu
    """
    choice = input("Main Menu:"
                +"\n\tR - Access to PR module"
                +"\n\tI - Access to MI module"
                +"\n\tM - Access to RM module"
                +"\n\tA - Print the about text"
                +"\n\tQ - Quit"
                +"\nChoice:").upper()
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
                +"\nChoice:").upper()

def reporting_menu():
    """Your documentation goes here"""
    choice = input("Reporting Menu:"
        +"\n\tDA - Access to daily average"
        +"\n\tDM - Access to daily median"
        +"\n\tHA - Access to hourly average"
        +"\n\tMA - Access to monthly average"
        +"\n\tPH - Access to peak hour of polution for a given date"
        +"\n\tDA - Access to daily average"
        +"\n\tM - Main Menu"
        +"\nChoice:").upper()
    match(choice):
        case "DA":
            monitoring_station = input("Input monitoring station: ")
            pollutant = input("Input polluntant: ")
            data = csv_to_array("Pollution-"+monitoring_station+".csv")

            reporting.daily_average(data,monitoring_station,pollutant)
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
    sys.exit()

def csv_to_array(filename):
    """
    Turns csv file into array
    """
    cwd = os.getcwd()
    rows = []
    with open(cwd+'\\data\\'+filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        for row in csvreader:
            columns = []
            for col in row:
                columns.append(col)
            rows.append(columns)
    return rows

if __name__ == '__main__':
    main_menu()