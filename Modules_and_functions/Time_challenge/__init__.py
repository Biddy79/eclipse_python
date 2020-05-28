# Create a program that allows a user to choose one of
# up to 9 time zones from a menu. You can choose any
# zones you want from the all_timezones list.
#
# The program will then display the time in that timezone, as
# well as local time and UTC time.
#
# Entering 0 as the choice will quit the program.
#
# Display the dates and times in a format suitable for the
# user of your program to understand, and include the
# timezone name when displaying the chosen time.

import datetime
import pytz
    
countrys = {"1": 'Mexico/BajaNorte',
            "2": 'Pacific/Easter',
            "3": 'US/Central',
            "4": 'Hongkong',
            "5": 'GB',
            "6": 'Europe/Rome',
            "7": 'Europe/Paris',
            "8": 'Europe/Monaco',
            "9": 'Canada/Central'}

for x in countrys:
    
    print(f"{x}: {countrys[x]}")
    


while True:
    user_input = input("\nEnter 1 to 9 to select a country from the list. 0 will quit the program")
    if user_input not in dict.keys(countrys):
        print("you have made an invalid entry") 
    elif user_input == "0":
        print("Goodbuy.")
        break
print(countrys[user_input])
    


    