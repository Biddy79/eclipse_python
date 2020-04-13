# Write a program to append the times tables to our Python_Description
# in /home/adam/src/eclipse_python/Input_Output/Python_Description.txt We want the tables from 2 to 12 
#(similar to the output from the For loops part 2 lecture in section 6).
#
# The first column of numbers should be right justified. As an example,
# the 2 times table should look like this:
#   1 times 2 is 2
#   2 times 2 is 4
#   3 times 2 is 6
#   4 times 2 is 8
#   5 times 2 is 10
#   6 times 2 is 12
#   7 times 2 is 14
#   8 times 2 is 16
#   9 times 2 is 18
#  10 times 2 is 20
#  11 times 2 is 22
#  12 times 2 is 24
#  --------------------



#note we are using mode 'a' as the parameter with open function with will appened to the end of the file
#each time we run the program
with open("/home/adam/src/eclipse_python/Input_Output/Python_Description.txt", 'a') as pyhton_description:
    for i in range(1,13):
        print(f"{i:4} times 2 is {i*2}", file=pyhton_description)
         

        
with open("/home/adam/src/eclipse_python/Input_Output/Python_Description.txt", 'r') as pyhton_description:
    line = pyhton_description.read()
    print(line)
        
#look up file modes for Python 'r' 'w' 'b' 't' 'a' 'x' '+'