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

# Write a program to print out all the numbers from 0 to 20 that aren't divisible by 3 or 5
# Zero is considered divisible by everthing (Zero should not appear in the output)
for i in range (0, 20):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print(i)
        
#TODO: can added here thing needed to do using the special todo comment makes a file with lsit

print("-" * 25)

# Modify the code inside this loop to stop when i is exactly divisible by 11
for i in range(0, 100, 7):
    print(i)
    if i / 11 == 7.0:
        break

       
    
    
    
    
    