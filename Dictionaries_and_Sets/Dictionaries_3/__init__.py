#update and copy methods in dictionaries

computer_parts = {"cpu": "central processing unit ",
                  "mother board": "main circuit board",
                  "ram": "random access memory",
                  "hard drive": "data storage device"}

print(computer_parts)

print("-" *30)

computer_price = {"intel i9": 499,
                 "Asus Rog": 250,
                 "32gb corse air": 140,
                 "samsung m.4 2tb": 230}

#update will combine two dictionaires together NOTE update returns null
computer_parts.update(computer_price)
print(computer_parts)

print("-" *30)

#use copy when you want a new dictionaries that containes keys and values form a dictionaries
#Note copy also return null
new_computer = computer_parts.copy()
#now we have a new dictionaries new_computer made from a copy of computers_parts
print(new_computer)

