#opening file using open() function. parameters are path location and in this case we use 'r' for read only
#Declaring variable python_description and setting this = to open function

# python_description = open("/home/adam/src/eclipse_python/Input_Output/Python_Description.txt", 'r')
# 
# #Basic reading of .txt file using a for loop  
#  
# for line in python_description:
#     print(line)



# #using for loop to only print lines of the file with the word "language" 
# for line in python_description:
#     if "language" in line.lower():
#         print(line, end='')
#           
#  
# #must remember to close file
# python_description.close()


##################Note code above had to be commented out our below would not print###################


#Here is another way to read a file using with() function, this was added after pyhton2
#note this time close() is not needed
#with also will terminate the program is there is an error
with open("/home/adam/src/eclipse_python/Input_Output/Python_Description.txt", 'r') as python_description:
    for line in python_description:
        if "PYTHON" in line.upper():
            print(line, end='')
            
print("-" * 30)

##################Note code above did NOT need commenting out ####################################
##################As using with() function lets open and print file multiple times###############           
with open("/home/adam/src/eclipse_python/Input_Output/Python_Description.txt", 'r') as python_description:
    line = python_description.readline()
    #using while here will check if file is empty and if so would not processed
    while line:
        print(line, end='')
        #we must then set line = to next line in file using readline() function()
        line = python_description.readline()
        
print("-" * 30)

#reading file as a list using readlines() function. NOTE THIS IS LINES 'S' NOT LINE
with open("/home/adam/src/eclipse_python/Input_Output/Python_Description.txt", 'r') as python_description:
    line = python_description.readlines()   
print(line)

print("-" * 30)

#we can now uses array assignment to iterate over the list of lines
print(line[1])
#or (also take note of the \n at the end of every line when we printed as list on line 51)
for lines in line:
    print(lines, end='')
    
print("-" * 30)

#note we are back to using read() not readline() or readlineS()
with open("/home/adam/src/eclipse_python/Input_Output/Python_Description.txt", 'r') as python_description:
    lines = python_description.read()
#we can then use range [::-1] in this case to print out the file in reverse
for line in lines[::-1]:
    print(line, end='')



######################summary of function when reading a flie###############################
#READ
#read() reads the entire file (and if it is a text file) returns a string containing the contents of the file

#READ LINE #####IS RECOMENDED FOR READING LARGE FILES####
#readline() reads a single line from a file and returns a string

#READ LINES
#readlines() reads the entire file and returns a list of strings


     