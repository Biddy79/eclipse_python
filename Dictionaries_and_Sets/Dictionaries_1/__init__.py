computer_parts = {"cpu": "central processing unit ",
                  "mother board": "main circuit board",
                  "ram": "random access memory",
                  "hard drive": "data storage device"}

# while True:
#     dict_key = input("enter a computer part")
#     if dict_key == "quit":
#         break
#     #computer_parts.get(dict_key) will return None if key dose not exist
#     elif dict_key in computer_parts:
#         description = computer_parts.get(dict_key)
#         print(description)
#     else:
#         print("we dont have a " + dict_key)


#Below adding second parameter to method computor_parts.get() 

while True:
    dict_key = input("Enter computer part: ")
    if dict_key == "quit":
        break
    description = computer_parts.get(dict_key, f"{dict_key} is not in list of components" )
    print(description)
    
#pyhton2 also has computer_parts.has_key() method. Has_key will check if key exist's


#Iterating over dictionaries
for parts in computer_parts:
    print(computer_parts[parts])
    
#order of dictionaries can change with each iteration. Hashing. 
#Note The behaviour changed in Python3.6!! But ordering keys first is still advised
for i in range(10):
    print("-" * 30)
    for parts in computer_parts:
        print(parts + " is " + computer_parts[parts])
        
print("-" * 30)
        
#order dictionaries keys in a list to order dictionaries

#Creating a list so we can use .sort() and storing it in ordered_key 
#.keys() will return all keys in dictionaries 
ordered_key = list(computer_parts.keys())
#sorting list of keys into order
ordered_key.sort()
#iterating over computer_parts by checking parts in ordered_key
for p in ordered_key:
    print(p + " - " + computer_parts[p])
    
print("-" * 30)

#ordering dictionaries same as above but short hand. 
#remember to use sorted() and not .sort() as .sort() returns null and must be used after
ordered_key2 = sorted(list(computer_parts.keys()))
for p in ordered_key2:
    print(p + " - " + computer_parts[p])
    
print("-" * 30)
    
#if only using ordered_key to print out and not for testing this can be shorted further
for p in sorted(computer_parts.keys()):
    print(p + " - " + computer_parts[p])
    

    
#get values of dictionaries using .values() method this will give us just the values
for val in computer_parts.values():
    print(val)
    
print("-" * 30)
    
#using the key to do this more efficient than above
for key in computer_parts:
    print(computer_parts[key])
    
print("-" * 30)

# .keys() and .values() return list like objects
#new dict_ objects are created each time dictionaries are update (adding or removing)
print(computer_parts.keys()) # returns a dict_keys object 
print(computer_parts.values())# return a dict_values object







    