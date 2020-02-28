string = "1234567890"

# for char in string:
#     print(char)
    
my_iterator = iter(string)
print(my_iterator) #prints the obj type <str_iterator> and memory location in hex
print(next(my_iterator)) #prints next item in string list 
print(next(my_iterator)) #and so on....
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator)) #till last item in list 

#print(next(my_iterator)) if continued this would return error as off end of list

print("-" * 20)

# for char in string:
#     print(char)
#     

#this is same as above but creating iterator our selfs 
for char in iter(string):
    print(char)

print("-" * 20)

#CHALLENGE
#
#Create a list of items (either string or numbers)
#then create an iterator using iter() function
#
#use a for loop "n" times, where n is the number of items in your list
#Each time round the loop, use next() on your list to print the next item.
#
#hitn: use the len() function rather than counting the number of items in the list

quote_list= ["Better", "to", "remain", "silent", "and",
              "be", "though", "a", "fool", "than", "to", "speak",
              "and", "remove", "all", "doubt"]

quote_iterator = iter(quote_list)
    
for i in range(0, len(quote_list)):
    print(next(quote_iterator),end = (' '))    



