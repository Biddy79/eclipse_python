string1 = ("Hello ")
string2 = ("my name ")
string3 = ("is ")
string4 = ("Adam")

print(string1 + string2 + string3 + string4)

print()

print(string1 * 5) #print hello 5 times

print()

# print(string1 * 5 + 4) // gives error TypeError: must be str, not int
print(string1 * (5 + 4)) # Remember operator Precedence () will first do 5 + 4 

print()

#in = bool type true or false
print("my" in string2) #print true if "my" is in string2  
print("Adam" in string2) #print false if "Adam" is in string2
print("Parrot" in "dog") #false

print()

#printing parts of a string in a string list 
computer_parts = ["CPU", "RAM", "HardDrive"]
print(computer_parts[1][1])
print(computer_parts[2][4]) 
print(computer_parts[1][-2])
print(computer_parts[1][2])

print()

#string replacement fields and .format()
age = 40
print("may age is " + str(age)) 
print("may age is {0} ".format(age))

print()

print("there are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, and {7},"
     .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))

print()
      
for i in range(1,13):
    print("No. {0} squared is {1} and cubed is {2}".format(i, 1 ** 2, i ** 3))
    
print()

#
for i in range(1,13):
    # {0:2} note the second :2 will set the width of reserved spaces 
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))
    







