
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
# Zero is considered divisible by everything (Zero should not appear in the output)
for i in range (0, 20):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print(i)
         
#TODO: can added here thing needed to do using the special to do comment makes a file with list
 
print("-" * 25)
 
# Modify the code inside this loop to stop when i is exactly divisible by 11
for i in range(0, 100, 7):
    print(i)
    if i / 11 == 7.0:
        break
    
print("-" * 25)

#Guessing game
import random
highest = 10
answer = random.randint(1, highest)

guess = None
Quit = 0

while guess != answer:
    guess = int(input(f"Please enter a number between 1 and {highest}. If you would rather not play please enter 0:  "))
    if guess == 0:
        print("You have chosen to quit good buy ")
        break
    elif guess < answer:
        print("Number is higher")
    elif guess > answer:
        print("Number is lower !!!")
    elif guess == answer:
        print("You are correct !!")
        break

    
    
    
    
    