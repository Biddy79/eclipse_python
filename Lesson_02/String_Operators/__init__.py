string1 = ("Hello ")
string2 = ("my name ")
string3 = ("is ")
string4 = ("Adam")

print(string1 + string2 + string3 + string4)

print(string1 * 5) #print hello 5 times

# print(string1 * 5 + 4) // gives error TypeError: must be str, not int

print(string1 * (5 + 4)) # Remember operator Precedence () will first do 5 + 4 

#in = bool type true or false

print("my" in string2) #print true if "my" is in string2  
print("Adam" in string2) #print false if "Adam" is in string2
print("Parrot" in "dog") #false

#printing parts of a string in a string list 
computer_parts = ["CPU", "RAM", "HardDrive"]
print(computer_parts[1][1])
print(computer_parts[2][4]) 
print(computer_parts[1][-2])
print(computer_parts[1][2])