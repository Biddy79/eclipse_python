#sets
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









