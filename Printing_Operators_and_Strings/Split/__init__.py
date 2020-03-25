#dictionaries 
computer_parts = {"cpu": "central processing unit ",
                  "mother board": "main circuit board",
                  "ram": "random access memory",
                  "hard drive": "data storage device"}

print(computer_parts["cpu"])
#split() splits the dictionaries value in to a list separated by a comma 
print(computer_parts["cpu"].split())

print("-" * 30)

#We can then move up and down the list picking out items using array [1] 
print(computer_parts["cpu"].split()[1])

print("-" * 30)

print(computer_parts["cpu"])
#adding the parameter ", " to the split() function removes the comma creating a 
#a list of one item
print(computer_parts["cpu"].split(", "))

print("-" * 30)
#split is the opposite of join
#split and join can be used together 
print(' '.join(computer_parts["cpu"].split()))
