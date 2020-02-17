pack_list = ["Tooth Brush", "Jacket", "Shirt", "Shorts", "Trainners"]


# for items in pack_list:
#     if items != "Shirt":
#         print(f"pack {items}")

# same way of writing above code using keword continue
for items in pack_list:
    if items == "Shirt":
        continue
    print(f"pack {items}")

print("-" *25)

item_to_find = "Shirt"
found_at = None

for index in range(len(pack_list)):
    if pack_list[index] == item_to_find:
        found_at = index
        break # adding break will make code more efficient as the loop will not continue !!
        
print(f"Item found at index {found_at}")
        
print("-" *25) 
    




colours = "Red Green Blue"
  
for character in colours:
    print(character)
      
print("-" * 20)
 
#rang in for loop will iterate over loop between given range NOT INCLUDING LAST VALUE
for i in range(20,26):
    print(f"i is now {i}")
     
print("-" * 20)
 
#range where no start value is given start default is 0
for i in range (10):
    print(f"i is now {i}")
 
print("-" * 20)
 
#range steps can be added as a 3rd argument to range function
for i in range(1,10,2):
    print(f"i is now {i}")
     
print("-" * 20)
 
#range negative step can be added START MUST BE GRATER THEN END
for i in range(10,0,-2):
    print(f"i is now {i}")
     
print("-" * 20)
 
#range can be used to test if values are in a range
age = int(input("enter your age: "))
if age in range(16, 66):
    print("you are aged between 16 and 65")
else:
    print("you are younger than 16 or older then 65")
     
print("-" * 20)
 
      
#number = "992, 47: 36;38 875;1123"
numbers = (input("Enter numbers"))
separators = ""
  
for char in numbers:
    if not char.isnumeric(): # isnumeric() checks for numbers in string
        separators = separators + char
          
print(separators)
  
values = "".join(char if char not in separators else " " for char in numbers).split()
print(sum([int(val)for val in values]))
 
 
print("-" * 20)
 
quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""
caps = ""
 
for letters in quote:
    if letters.isupper():
        caps = caps + letters
 
print(caps)

#program that print out numbers between 0 - 100 divisible by 7
num = 0
for i in range(0, 101):
    if i % 7 == 0:
        num = i
        print(num)

#Nested for loop
for i in range(1,13):
    for j in range(13):
        print(f"{j} x {i} = {j*i}")
    print("-" * 25)
    