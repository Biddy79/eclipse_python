

#when storing a string in a variabel you can index each char with array brackets []
my_list = "I like winter"
print(my_list[2])

numbers = "102938 0988"
#split() will remove what ever is passed as parameter. No parameter will defalt to a space
#here we split number by space
number = numbers.split()
#now we print number by index as it now a list with two elements 
print(number[1])

my_list1 = "I,like,winter"
#Here we have split the string by ',' This removes all commas and separates each word between them
#creating a list, index can then be selected using [] 
print(my_list1.split(',')[1])

#this is a LIST OF string with two string elements.
#the first string in split by the space between the words 
my_list2 = ["I like Winter".split(), "and summer too"]
#We now select the first string using [0] then the words int that string using[2]
print(my_list2[0][2])
#we can also select the sceond sentance from my_list2
print(my_list2[1])
#this can then be broken down further to give the letter from the second string
print(my_list2[1][4])

#len(function desplays the lenght of a list
print(len(my_list2))

