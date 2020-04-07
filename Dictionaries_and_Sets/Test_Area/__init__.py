user_input = input("Enter some text here: ").casefold()
 
user_serch = input("Enter letter you are searching for: ").casefold()
 
#each letter in user_input separated into individual characters
characters = list(user_input) 
 
print(characters)
 
letter_search = "";
 
for i in characters:
    if user_serch == i:
        letter_search += i
 
print(f"Here are all the letters you where searching for {letter_search.split()} ")

print("-" * 20)  
     
tuple
transport_0 = "car", "plain", "boat"
transport_1 = "train", "car", "plain", "sub"

print(transport_0)
print(transport_1)

#unpacking the tupel
BMW, Boeing757, Cruies_Liner = transport_0 
print(f"Here are the types of transport in more detail "
    "car:{BMW}, plain:{Boeing757}, Boat:{Cruies_Liner}")

transport_0_set = set(transport_0)

#using difference function to show difference between sets
#note transport_1 is still a tuple but can be passed as a parameter
print(transport_0_set.difference(transport_1))


