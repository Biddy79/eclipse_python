#sets
#for more info:        https://docs.python.org/2/library/sets.html


#sets are not orded 
Farm_animals = {"sheep", "cow", "pig"}
print(Farm_animals)

for animals in Farm_animals:
    print(animals)
    
print("-" * 30)

#creating a set using constructor note list brakets [] used 
Wild_animals = set(["Tiger", "lion", "panther", "snake"])
print(Wild_animals)

#if creating an empty set you must use set constructor empty_set = set()


for animals in Wild_animals:
    print(animals)

print("-" * 30)

#add() function adding to set
Farm_animals.add("horse")
print(Farm_animals)

print("-" *30)

#remove and discard
Farm_animals.discard("horse")#removes horse
print(Farm_animals)
Farm_animals.remove("pig")
print(Farm_animals)#removes pig

#discard wil not through error if iteam not in set 
Farm_animals.discard("chicken") # no error
#remove will through error if not in set
try:
    Farm_animals.remove("chicken")
except KeyError:
    print("The animal is not in Farm animels")

print("-" * 30)

#range can be used in a set
even = set(range(0,40,2))
print(even)

#set can also take tuples, lists or other as a parameter but must use set constructor 
squares_tuple = (4, 6, 9, 16, 25)
#set constructor usse to create set of tuple
squares = set(squares_tuple)
print(squares)

print("-" * 30)

print(even)
print(len(even))

print(squares)
print(len(squares))

print("-" * 30)

#using union() function
#Union of two given sets is the smallest set which contains all the elements of both the sets.
#Union of two given sets A and B is a set which consists of all 
#the elements of A and all the elements of B such that no element is repeated.

#union will add all itemes form a set that are not already part of that given set
#in this case 6 and 9 are added to even set 
print(even.union(squares))
print(len(even.union(squares)))

print("-" * 30)

#intersection() function will give itemes that are in both sets 
#in this case 6, 4, 16 are in both even and squares sets
print(even.intersection(squares))
#this gives the same out put
print(even & squares)

print("-" * 30)

#difference() function removes items from set a in set b 
#we will also sort the order to make it easy to read

#even minus squares
print(squares)
print(sorted(even.difference(squares)))
#this can also be writen print(even - squares)

print("-" * 30)

#squares minus even
print(even)
print(sorted(squares.difference(even)))
#print(squares - even)

print("-" *30)

#symmetric difference
#elements present in either of the two sets, but not common to both the sets
set_A = {1,2,3,4,5}
set_B = {1,3,5,6,9}
#2,4,6,9 will be returned as they are not in both sets
print(set_A.symmetric_difference(set_B))
#symmetric_difference() can also be written as ^ this is same as above
print(set_A ^ set_B)

print("-" * 30)

set_C = {5,10,15,20}
set_D = {5,10,15,20,25,30}

#issuperset
#The issuperset() method returns True if a set has every elements of another set
#(but it may also contain other elements).
#(passed as an argument).
#If not, it returns False.

# here True is retured as set_D as all elements of set_B (include extra elements 25,30)
print(set_D.issuperset(set_C)) 

#issubset
#The issubset() method returns True if all items in the set
#exists in the specified set, otherwise it retuns False.

#here False is returned as set_D dose not have all the elements of set_C
print(set_D.issubset(set_C))

print("-" * 30)

#frozen set

set_E = frozenset(range(0,10,3))
#frozanset is immutabel. we can NOT add or remove from a frozan set 
print(set_E)

#set_E.add(12) will trown error: 'frozenset' object has no attribute 'add'












