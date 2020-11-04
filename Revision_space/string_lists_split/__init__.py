numbers = "102938 0988"

number = numbers[0]
print(number)

#when storing a string in a variabel you can index each char with array brackets []
my_list = "I like winter"
print(my_list[2])

my_list1 = "I,like,winter"
#split() will remove what ever char is passed as parameter. No parameter will defalt to a space
#Here we have split the string by ',' This removes all commas and separates each word between them
#into its own index which can then be selected using []
print(my_list1.split(',')[1])

my_list2 = ["I like Winter".split()]
print(my_list2[0][2])
print(len(my_list2))

