from _overlapped import NULL

parrot = "Norwegian Blue"

print(parrot) 

print()

#print out we win (each carictor on a new line)

print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

print()

#same as befor this time using negative indexing

print(parrot[-11])
print(parrot[-1])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

print()

#same as before this time subtracting to give correct index

print(parrot[3 - 14])
print(parrot[4 - 14])
print(parrot[9 - 14])
print(parrot[3 - 14])
print(parrot[6 - 14])
print(parrot[8 - 14])

print()

#slicing using :

print(parrot[0:6]) # Norweg  #prints from value 0 upto BUT NOT INCLUDE 6 !!!!!
print(parrot[3:5]) # we      #prints from vale 3 upto BUT NOT INCLUDING 5 !!!!
print(parrot[:9])  # Norwegian Note if no start index is give 0 is default 
print(parrot[10:14]) # Blue
print(parrot[10:]) # Blue same as befor but if last value it will defalut to end value null ptr 

#slicing can be used with mathmatical oparotors 
print(parrot[:6] + parrot[6:]) # prints lines 0 to 6 + line 6 to 14 Norwegian Blue
print(parrot[:]) #prints from the begining of the string to the end

print()

#print we win using negative slicing

# 01234567890123
# Norwegian Blue

print(parrot[-11:-10])
print(parrot[-1:])
print(parrot[-5:-6])
print(parrot[-11:-10])
print(parrot[-8:-7])
print(parrot[-6:-5])

print()

#print blue using negative slicing
print(parrot[-4:])


#slicing 

num = "100,200,300,400,500"
print(num[0:18:4])



