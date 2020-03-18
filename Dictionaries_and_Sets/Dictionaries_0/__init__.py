#Dictionaries
computer_parts = {"cpu": "central processing unit ",
                  "mother board": "main circuit board",
                  "ram": "random access memory",
                  "hard drive": "data storage device"}


#print all keys with variables
print(computer_parts)
#index computer_parts with key inside[]  again use []!!
print(computer_parts["mother board"])

#keys can be of different type objects but must be immutable therefore we carn't us a list but 
#can use a tuple 

#We can add to a dictionaries
computer_parts["storage capacity gb"] = 500
print(computer_parts)
#there is no append() method for dictionaries

#Dictionaries items can be updated using same key
computer_parts["storage capacity gb"] = 1000
print(computer_parts["storage capacity gb"])

#you can use duplicate keys. the last entry will be updated for that key
#below hard drive is updated to ssd

# computer_parts = {"cpu": "central processing unit ",
#                   "mother board": "main circuit board",
#                   "ram": "random-access memory",
#                   "hard drive": "data storage device",
#                   "hard drive": "ssd"}


#del command will delete an enter

del computer_parts["hard drive"]
print(computer_parts)

#del will also delete the dictionaries 
#del computer parts
#computer_parts.clear() will remove all items and keys from dictionaries


#looking if a entry exist's in  dictionaries

while True:
    dict_key = input("enter a computer part")
    if dict_key == "quit":
        break
    #computer_parts.get(dict_key) will return None if key dose not exist
    elif dict_key in computer_parts:
        description = computer_parts.get(dict_key)
        print(description)
    else:
        print("we dont have a " + dict_key)






