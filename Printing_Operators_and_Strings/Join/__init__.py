#this is NOT an efficient way to join !!!!!
myList = ["a", "b", "c", "d"]

newString_0 = ""
#this is because a new string is creating each time around the loop
for c in myList:
    newString_0 += c + ", "
#note the trailing comma at the end of the string
print(newString_0)

#A better way is to use the  .join() function
newString_1 = ""

newString_1 = ", ".join(myList) 
print(newString_1)

#we can use any sequence type with join(). below we pass a string instead of a list
letters = "abcdefghijklmnopqrstuvwxyz"

newString_1 = "".join(letters)
print(newString_1)

#Also what ever is added before the join in this case mississippi will be added after each 
#item that is to be joined
numbers = "12345678910"
numbers_string = " mississippi ".join(numbers)
print(numbers_string)
