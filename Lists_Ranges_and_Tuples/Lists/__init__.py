#List of string
names = ["Bob", "Sue", "John", "David" ,"Nick"]

for name in names:
    print(name + ", ", end = '')
    
print()
#New_Name must be a list and not str type so that We can append this to names
#Don't do this New_Name = "Rob" !!!!!!!!! it must be a list type ["Rob"]
New_Name = ["Rob"]

New_Name_List = names + New_Name

for name in New_Name_List:
    print(name + ", ", end = '')

print()
#A better way to add a name to the names list is using names.append() function
names.append("Jack")

for name in names:
    print(name + ", ", end = '')

print()

#list of int type
even = [2,4,6,8,]
odd = [1,3,5,7,9]

numbers = even + odd

#sort() function
print(numbers.sort()) # this will out put None as it returns null

#we must use sort() on numbers before printing 
numbers.sort()
print(numbers)

#sorted function will arrange numbers is order
print(sorted(numbers)) 

#or save numbers into a variable (number_in_order) after using sorted()
numbers_in_order = sorted(numbers)
print(numbers_in_order)