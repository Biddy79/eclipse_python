import shelve

# with shelve.open('car.bin') as car:
#     car['make'] = "B.M.W"
#     car['model'] = "m5"
#     car['seat number'] = 5
#     
# now shelve file as be create we can comment code out so we do not keep creating over 

#opening car.bin and creating car object to work with car.bin
car = shelve.open('car.bin')

#adding a new key and value to car.bin
car['colour'] = "black"

#printing out car colour
print(car['colour'])

print("-" * 30)

#shelve dose not return values in order there for we can rap shelve in list and use sort() function 

#unordered
for c in car:
    print(f"{c} - {car[c]}")
    
print("-" * 30)

#ordered 
ordered_keys = list(car.keys())
ordered_keys.sort()

for c in ordered_keys:
    print(f"{c} - {car[c]}")
    
print("-" * 30)    

#we can also test to see if a key is in a shelve
while True:
    dick_key = input("Enter key value: ")
    if dick_key == "quit":
        break
    
    if dick_key in car:
        description = car[dick_key]
        print(description)
    else:
        print(f"We do not have {dick_key} value")

#must no remember to close file as we used open and not with block!!!
car.close()

