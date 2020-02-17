#basic while loop
i = 0

while i < 10:
    i += 1
    print(i)
    
direction = ["North", "East"]

chosen = ""

while chosen not in direction:
    #chosen set to user input
    chosen = input("choose a different direction ")
    #if user enters Quit the program will exit the loop. 
    #.casefold() is used to convert all character to lower case if user enters upper case      
    if chosen.casefold() == "quit":
        print("you have chosen to stay where you are")
        break
   
#this line executes if chosen is set = to a direction in direction list
print("you are heading in the right direction")