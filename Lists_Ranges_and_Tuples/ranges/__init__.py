
print(range(0,100))
#creating a list using list constructor and giving a rage of 1 to 100
my_list = list(range(1,10))
#printint my_list index each item in list to be printed 
print(my_list)

#list can take a range with start, end, and increment postions 
odd = list(range(1, 10, 2))
even = list(range(0, 10, 2))

print(odd)
print(even)

# range(1,10) and range(1,100000) will use the same amount of memory. Only when creating a list 
# will more memory be used in the larger ranges

my_string = "abcdefghijklmnopqrstuvwxyz"
#.index() takes a item from list as argument and returns index of item
print(my_string.index('c'))
# we can also give and index in arry brakets to select an item in list
print(my_string[2])

#NOTE creating a range not a list of ranges
odd_range = range(1,10000,2)

sevens = range(7,100000,7)
x = int(input("Enter a positive number less than one million: "))
if x in sevens:
    print(f"{x} is divisabel by seven")
else:
    print(f"{x} is not divisabel by seven")
    
my_range = range(0,10)
print(my_range)

new_range = my_range[::2]
print(new_range.index(4))

print("=" * 20)


nums = range(0,100)
num_set = nums[::3]

for i in num_set:
    print(i)
    
print("=" * 20)

for i in range(0,100,3):
    print(i)

#both have the same value in list
print(num_set == range(0,100,3))
#but both are not the same list object
print(num_set is range(0,100,3))
