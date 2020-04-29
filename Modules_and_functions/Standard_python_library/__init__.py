#Python standard library dose not need to be imported as this is done automatically

#dir() is a powerful inbuilt function in Python3, 
#which returns list of the attributes and methods of any object 

print(dir()) #here dir() will print a list of the built in standard library
#['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
# '__name__', '__package__', '__spec__']
#any imported modules would also be added to this list after import

print('-' * 30)

#dir() used to print out all of __builtin__  #using for loop to print out more clearly 
for m in dir(__builtins__):
    print(m)

print('-' * 30)

import shelve 
#using dir() to see all attributes of shelve. remember we must import shelve first 
print(dir(shelve))

print('-' * 30)

#if we now use dir() to see all attributes of this program shelve will be added to the list
print(dir())
#['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
# '__name__', '__package__', '__spec__', 'm', 'shelve']

print('-' * 30)

#we can also see the objects of shelf class using dir() by filtering all underscore __ out 
for obj in dir(shelve.Shelf): #shelf is class in the shelve module 
    if obj[0] != '_':
        print(obj)

print('-' * 30)
        
#help() fuction can also give a lot of information about a class or object 
help(shelve)

#after adding a dot to shelve.Shelf the IED will show a list methods and variables of the shelf class
#holding Ctrl and left mouse clip will give a description and source code of class or module 





