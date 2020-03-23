#write a program to print a number of options, and allow the user to select an option from
#the user_description. There must be more than 4 options and less than 9. 

#The program should continue looping, allowing the user to choose one of the options each 
#time round.

#The loop should only terminate when the user chooses 0.

#If the user makes a valid choice, the program should print a short message.
#The message should include the value that they typed
#Don't print a different message for each choice - the only thing that should change is the 
#number they typed.  

#If their choice isn't one in the user_description of options nothing should be printed (although you
#should see there input on the screen)

#As optional extra, modify the program so the menu is printed again if they choose an 
#invalid option. Do this without duplicating the print lines


options = ["second", "minute", "hour", "day", "month", "year"]

user_selection = ""
user_description = ""
exit = "0"
print("select the format of time / date form user_description below")
while user_selection != exit:
    for option in options:
        print(option)
    user_selection = input("Enter your selection. Or type 0 to exit: ").casefold()
    if user_selection == exit:
        break
    elif user_selection in options:
        print(f"{user_selection} added to your user_description \n Please make another selection: ")
        user_description += user_selection + " " 
    else:
        print(f"{user_selection} is not a valid selection. please type one of the following")
    
    
print(f"You have selected the following time / date format: {user_description}")