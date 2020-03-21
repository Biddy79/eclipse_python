computer_parts = {"cpu": "central processing unit ",
                  "mother board": "main circuit board",
                  "ram": "random access memory",
                  "hard drive": "data storage device"}

# .keys() and .values() return list like objects
#new dict_ objects are created each time dictionaries are update (adding or removing)

print(computer_parts.keys()) # returns a dict_keys object 
print(computer_parts.values())# return a dict_values object

print("-" * 30)

# .items() return dict_items object
print(computer_parts.items())

print("-" * 30)

#dict_iteams can be stored in a tuple variable  
c_tuple = tuple(computer_parts.items())
print(c_tuple)

print("-" * 30)

#the tuple can be use in the usual way
for parts in c_tuple:
    items, description = parts
    print(items + "-" + description)