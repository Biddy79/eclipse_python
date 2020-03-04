set_num1 = range(0,100,5)
print(set_num1)
set_num2 = set_num1[::5]
print(set_num2)

for i in set_num1:
    print(i)
    
print("=" *20)

for i in set_num2:
    print(i)
    
print("=" *20)
    
mylist = range(100,0,-2)
set_num3 = mylist[::]

for i in set_num3:
    print(i)

set_num4 = mylist[::-1]

print("=" *20)

for i in set_num4:
    print(i)
    
print("=" *20)    

new_list = list(range(50,0,-3))
print(new_list[::])

revers_new_list = new_list[::-1]
print(revers_new_list)

my_string = "hello"
print(my_string)

revers_my_string = my_string[::-1]
print(revers_my_string)

string_list = list("goodBuy")
print(string_list[::])

for i in string_list:
    print(i, end = '')
    
print()
    
for i in string_list[::-1]:
    print(i, end = '')



