sing_in_record = "D.K ", 21, ([])
#unpacking the tuple
company, location, time_in_out = sing_in_record
    
print(sing_in_record)

#company, location these values cannot be changed as the are tuples

#these values can be changed as they are list inside of tuple
time_in = float(input(print("Enter Time in: ")))
time_out = float(input(print("Enter Time out: ")))

#below are two different ways of setting values in a list within a tuple
sing_in_record[2].append((time_in))

time_in_out.append((time_out))

#iterating of items in tuple 
for info in sing_in_record:
    print(f"{info}", end = "")

print("\n")

#can also access list in tuple like this
print(sing_in_record[2][0])
#or like this
print(time_in_out[1])
    





    
