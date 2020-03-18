
#tupel 
t = "a", "b", "c"
print(t)

# this is also a tuple note extras brackets ()
print(("a", "b", "c"))

#this is not a tuple
print("a", "b", "c")

print("==" *20)
#tuples can be created with variables of different types. below are tuples which use
#both string and int type

# more tuples giving vehicle model, make, number of seats, and year
car1 = "BMW", "Z3", "2 SEATS", 1996
car2 = "VW", "T5", "6 SEATS", 2003
car3 = "FORD", "RANGER", "5 SEATS", 2015

#prints all items in car1 tuple
print(car1)
#can also access items with in a tuple using array braket's
print(car1[2])

print("==" *20)

#tuples are immutable (cannot be changed once created)!!!!
#this can offer protection and lead to less bugs 
##############car1[2] = "5 SEATS"#################
#This gives error 'tuple' object does not support item assignment

#We can pull out the items in a tuple ## UNPACKING THE TUPLE
make, model, seat_number, year = car3

print(make)
print(model)
print(seat_number)
print(year)

print("==" *20)

######### REMINDER EXPRESSION ARE READ LEFT TO RIGHT ##################
a, b = 12, 13
print(a, b)
a, b = b, a
print(f"{a} {b}")

print("==" *20)

### We can however assign the object car1 with a new variables 
car1 = car1[0], car1[1], "5 SEATS"
print(car1)

print("==" *20)

###############lists are mutable (items can be changed)##########
car4 = ["FORD", "FOCUS" , "5 SEATS", 2019]
print(car4)

print("==" *20)

## item 2 in list CAN be changed using array braket's
car4[3] = 2017
print(car4)
