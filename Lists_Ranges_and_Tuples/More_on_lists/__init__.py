
list1 = []
#creating a list using list constructor
list2 = list()
print(list1)
print(list2)

#prints each character separately
print(list("The list are equal"))

odd = [1,3,5,7,9,]
even = list([2,4,6,8,])

#list of lists
numbers = [odd, even]
print(numbers)

#seting a variabel called new numbers the point to the same values as numbers
new_numbers = numbers
#list in new_numbrs point to the list in numbers
if new_numbers == numbers:
    print("true")
else:
    print("false")
#new_nubers is  the same list therefore is the same     
if new_numbers is numbers:
    print("true")
else:
    print("false")
#using list constructor to create a new list passing numbers into the constructor
new_new_numbers = list(numbers)

print("-" * 20)

#new_new_nubers is its own copy of numbers therefore new_new_numbers is not numbers
if new_new_numbers is numbers:
    print("true")
else:
    print("false")
#But!! new_new_nubers is equal to the values in the numbers list as it point 
#to the same list
if new_new_numbers == numbers:
    print("true")
else:
    print("false")

#revrsing the order of new_numbers
new_numbers.sort(reverse=True)
print(new_numbers)
#NOTE this also reverser the order of numbers as they point to the same list
print(numbers)

#new_new_nubers remains in order as it is its own list
#created using the constructor List()
print(new_new_numbers)
