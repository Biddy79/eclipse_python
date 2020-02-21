#write a program to print a number of options, and allow the user to select an option from
#the list. There must be more than 4 options and less than 9. 

#The program should continue looping, allowing the user to choose one of the options each 
#time round.

#The loop should only terminate when the user chooses 0.

#If the user makes a valid choice, the program should print a short message.
#The message should include the value that they typed
#Don't print a different message for each choice - the only thing that should change is the 
#number they typed.  

#If their choice isn't one in the list of options nothing should be printed (although you
#should see there input on the screen)

#As optional extra, modify the program so the menu is printed again if they choose an 
#invalid option. Do this without duplicating the print lines


options = ["1: seconds", "2: minutes", "3: hours", "4: days", "5: weeks", "6: months", "7: years"]

user_selection = ""
list = ""
exit = "0"

while user_selection != exit:
    for option in options:
        print(option)
    user_selection = input("Please select how long you would like to rent the item for: ").casefold()
    list += user_selection + " "
    


print(list)