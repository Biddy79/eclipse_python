#import key word will import modules or (library)
import time # here we imported the module time

#we can now use functions from the time module time.time() and time.ctime() 
t = time.time()
print(time.ctime(t))


print('-' * 30)

#If we do not want to put the module name before each method we can us key words from 
from time import time, ctime  #warning is telling us time as already been imported 

#now we can just call the methods
t = time()
print(ctime(t))

print('-' * 30)

# we can also use * with from to import all the methods in a module
from time import * 

#again we do not need to add time to the beginning of each method call 
t = time()
print(ctime(t))

#this could lead to potential errors if we where to make a variable with the same name
time = "Do you have the time please. "
t = time()
print(ctime(t))

