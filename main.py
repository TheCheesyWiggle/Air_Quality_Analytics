
from colours import fg,bg,decor
import reporting, monitoring, intelligence, utils
# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification

#NOTE:docs and inline comments finished
def main_menu():
    """
    Code:
    -
    - choice variable stores user input
    - if else statement handles user input of the menu and redirects to corresponding choice, if there is a error it calls the function again
    """
    # User input for the menu
    choice = input(fg.pink + decor.bold+"Main Menu:"+ decor.reset+ fg.cyan
                +"\n\tR - Access to PR module"
                +"\n\tI - Access to MI module"
                +"\n\tM - Access to RM module"
                +"\n\tA - Print the about text"
                +"\n\tQ - Quit" + fg.pink+ decor.bold
                +"\nChoice: " + decor.reset+fg.lightgreen).upper()
    # resets teminal colours
    print(decor.reset)
    # If else statement to handle user input
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
        # prints error message and resets terminal colours
        print(fg.red+decor.bold+"Error please try again"+decor.reset+fg.red+decor.italic+"\nRemember to use uppercase letters"+ decor.reset)
        # returns to the main menu
        main_menu()

#NOTE:docs and inline comments finished
def monitoring_menu():
    """
    Code:
    -
    - choice variable stores user input
    - if else statement handles user input of the menu and redirects to corresponding choice, if there is a error it calls the function again
    - during th eif else statement the user is asked for the site code, start date, end date and species code 
    - this input is then passed into the functions
    """
    # User input for the menu
    choice = input(fg.pink + decor.bold+"Monitoring Menu:"+ decor.reset+ fg.cyan
        +"\n\t1 - Graph"
        +"\n\t2 - Hourly data"
        +"\n\t3 - Radar Graphs"+fg.pink + decor.bold
        +"\nChoice: "+ fg.lightgreen).upper()
    
    # If else statement to handle user input
    if choice == "1":
        site_code = input(fg.pink + decor.bold+"Please enter the site code: "+ decor.reset+fg.lightgreen).upper()
        start = input(fg.pink + decor.bold+"Please enter the start date (yyyy-mm-dd): "+decor.reset+ fg.lightgreen)
        end = input(fg.pink + decor.bold+"Please enter the end date (yyyy-mm-dd): "+ decor.reset+fg.lightgreen)
        species_code = input(fg.pink + decor.bold+"Please enter the species code: "+ decor.reset+fg.lightgreen).upper()
        print(decor.reset)
        monitoring.pollutant_plot(site_code,start,end,species_code)
    elif choice == "2":
        # User input for variables needed for the function
        site_code = input(fg.pink + decor.bold+"Please enter the site code: "+ decor.reset+fg.lightgreen).upper()
        species_code = input(fg.pink + decor.bold+"Please enter the species code: "+ decor.reset+fg.lightgreen).upper()
        # resets terminal colours
        print(decor.reset)
        # Calls the function to print the formatted hourly data
        monitoring.hourly_formatted(monitoring.hourly_data(),site_code,species_code)
    elif choice == "3":
        # User input for variables needed for the function
        site_code_1 = input(fg.pink + decor.bold+"Please enter the site code for the first station: "+ decor.reset+fg.lightgreen).upper()
        site_code_2 = input(fg.pink + decor.bold+"Please enter the site code for the second station: "+ decor.reset+fg.lightgreen).upper()
        # resets terminal colours
        print(decor.reset)
        # Calls the function to plot the radar chart
        monitoring.plot_radar_chart(monitoring.radar_chart_data(site_code_1,site_code_2))
    else:
        # prints error message and resets terminal colours while returning to the main menu
        print(decor.reset+fg.red+decor.bold+"Error please try again"+decor.reset+fg.red+decor.italic+"\nRemember to double check the data entered is correct"+ decor.reset)
        print(decor.reset)
        monitoring_menu()

#NOTE:docs and inline comments finished
#NOTE: Use regex to check if the user input is a valid date
def reporting_menu():
    """
    Code:
    -
    - choice variable stores user input
    - if else statement sets monitoring station to string value
    - Pollutant is chosen by the the user 
    - if else statement handles user input of the menu and redirects to corresponding choice, if there is a error it calls the function again
    """
    # User input for the menu
    choice = input(fg.pink + decor.bold+"Reporting Menu:"+ decor.reset+ fg.cyan
        +"\n\tDA - Access to daily average"
        +"\n\tDM - Access to daily median"
        +"\n\tHA - Access to hourly average"
        +"\n\tMA - Access to monthly average"
        +"\n\tPH - Access to peak hour of polution for a given date"
        +"\n\tDA - Access to daily average"
        +"\n\tM - Main Menu" + fg.pink + decor.bold
        +"\nChoice: "+decor.reset+fg.lightgreen).upper()
    # Checks validaty of the data entered
    if choice != ("DA" or "DM" or "HA" or "MA" or "PH" or "M"):
        print(fg.red+decor.bold+"Error please try again"+decor.reset+fg.red+decor.italic+"\nRemember to double check your input"+ decor.reset)
        reporting_menu()
    # User input for the monitoring station
    station = input(fg.pink + decor.bold+"Choose Monitoring Station:"+ decor.reset+ fg.cyan
        +"\n\t0 - London Harlington"
        +"\n\t1 - London Marlylebone"
        +"\n\t2 - London N Kensington"+ fg.pink + decor.bold
        +"\nChoice: "+decor.reset+fg.lightgreen)
    # If else statement to set the monitoring station to a string value
    if station == "0":
        monitoring_station = "London Harlington"
    elif station == "1":
        monitoring_station = "London Marlylebone"
    elif station == "2":
        monitoring_station = "London N Kensington"
    else:
        # sets monitoring station to error  to prevent unkown errors
        monitoring_station = "ERROR"
        # error message
        print(fg.red+decor.bold+"Error please try again"+decor.reset+fg.red+decor.italic+"\nRemember to only use numbers"+ decor.reset)
        #returns to the menu
        reporting_menu()
    
    #grabs pollutant as a lower case string so it can be used to compare to the csv headers
    pollutant = input(fg.pink + decor.bold+"Choose Pollutant:"+ decor.reset+ fg.cyan
        +"\n\tNO - Nitric Oxide"
        +"\n\tPM10 - PM10"
        +"\n\tPM25 - PM25"+ fg.pink + decor.bold
        +"\nChoice: "+decor.reset+fg.lightgreen).lower()
    
    # if else statement to check if the pollutant data is valid
    if pollutant != "no" and pollutant != "pm10" and pollutant != "pm25":
        #error message
        print(fg.red+decor.bold+"Error please try again"+decor.reset+fg.red+decor.italic+"\nRemember to use lowercase letters"+ decor.reset)
        # if invalid it returns to the menu
        reporting_menu()
    # resets terminal colours
    print(decor.reset)
    # calls the function to convert the csvs to a dictionary
    data = utils.csvs_to_dict()
    #  if else statement to handle the user input and redirect to the corresponding function
    if choice == "DA":
        print(reporting.daily_average(data, monitoring_station, pollutant))
    elif choice == "DM":
        reporting.daily_median(data, monitoring_station, pollutant)
    elif choice == "HA":
        reporting.hourly_average(data, monitoring_station, pollutant)
    elif choice == "MA":
        reporting.monthly_average(data, monitoring_station, pollutant) 
    elif choice == "PH":
        # enetered date is stored in the date variable
        date = input(fg.pink + decor.bold+"Please enter the date (yyyy-mm-dd): "+decor.reset+fg.lightgreen)
        reporting.peak_hour_date(data, date, monitoring_station, pollutant) 
    elif choice== "M":
        main_menu()
    else:
        #error message
        print(fg.red+decor.bold+"Error please try again"+decor.reset+fg.red+decor.italic+"\nRemember to use uppercase letters"+ decor.reset)
        reporting_menu()

#NOTE:docs and inline comments finished
def intelligence_menu():
    """
    Code:
    - Choice variable stores user input which service the want
    - if else statement handles user input of the menu and redirects to corresponding choice, if there is a error it calls the function again
    - second choice variable stores user input which colour pixels they want attributed for the service
    - if else statement handles user input of the menu and redirects to corresponding choice, if there is a error it calls the function again
    
    """
    # User input for the menu
    choice = input(fg.pink + decor.bold+"Intelligence Menu:"+ decor.reset+ fg.cyan
        +"\n\tFP - Find Pixels"
        +"\n\tFC - Find Connected Components"
        +"\n\tSC - Sort Connected Components"+ fg.pink + decor.bold
        +"\nChoice: "+decor.reset+fg.lightgreen).upper()
    # if statement redirects to the corresponding function
    if choice == "FP":
        # User input for colour of pixels
        choice2 = pixel_colour()
        # resets terminal colours
        print(decor.reset)
        # if else statement redirects to the corresponding function
        if choice2 == "R":
            intelligence.find_red_pixels("data//map.png",upper_threshold=100,lower_threshold=50)
        elif choice2 == "C":
            intelligence.find_cyan_pixels("data//map.png",upper_threshold=100,lower_threshold=50)
        else:
            # Error message
            print(fg.red+decor.bold+"Error please try again"+decor.reset+fg.red+decor.italic+"\nRemember to double check your input"+ decor.reset)
            intelligence_menu()
    elif choice == "FC":
        # User input for colour of pixels
        choice2 = pixel_colour()
        # resets terminal colours
        print(decor.reset)
        # if else statement redirects to the corresponding function
        if choice2 == "R":
            intelligence.detect_connected_components(intelligence.find_red_pixels("data//map.png",upper_threshold=100,lower_threshold=50))
        elif choice2 == "C":
            intelligence.detect_connected_components(intelligence.find_cyan_pixels("data//map.png",upper_threshold=100,lower_threshold=50))
        else:
            # Error message
            print(fg.red+decor.bold+"Error please try again"+decor.reset+fg.red+decor.italic+"\nRemember to double check your input"+ decor.reset)
            intelligence_menu()
    elif choice == "SC":
        # User input for colour of pixels
        choice2 = pixel_colour()
        # resets terminal colours
        print(decor.reset)
        # if else statement redirects to the corresponding function
        if choice2 == "R":
            intelligence.detect_connected_components_sorted(intelligence.detect_connected_components(intelligence.find_red_pixels("data//map.png",upper_threshold=100,lower_threshold=50)))
        elif choice2 == "C":
            intelligence.detect_connected_components_sorted(intelligence.detect_connected_components(intelligence.find_cyan_pixels("data//map.png",upper_threshold=100,lower_threshold=50)))
        else:
            # Error message
            print(fg.red+decor.bold+"Error please try again"+decor.reset+fg.red+decor.italic+"\nRemember to double check your input"+ decor.reset)
            intelligence_menu()
    else:
        # Error message
        print(fg.red+decor.bold+"Error please try again"+decor.reset+fg.red+decor.italic+"\nRemember to double check your input"+ decor.reset)
        intelligence_menu()

#NOTE:docs and inline comments finished
def pixel_colour():
    """
    Code:
    -
    - User input for colour of pixels
    """
    choice = input(decor.reset+ fg.cyan+"R - Red Pixels"
            +"\nC - Cyan Pixels"+ fg.pink + decor.bold
            +"\nChoice: "+decor.reset+fg.lightgreen).upper()
    return choice

#NOTE:docs and inline comments finished
def about():
    """
    Code:
    - Prints the module and candidate number
    """
    print(decor.reset+ fg.cyan+"Module: ECM1400 \nCandidate Number: 720019013"+decor.reset)
    return main_menu()

#NOTE:docs and inline comments finished
def quit():
    """
    Code:
    - Exits the program
    """
    exit()

if __name__ == '__main__':
    main_menu()