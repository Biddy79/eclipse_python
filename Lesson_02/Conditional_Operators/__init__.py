#c++      &&    ||  !
#python   and   or  not  in 


membership_points = 12
name = "Tom"
weekday  = False 

if (name == "Tom" and membership_points > 5) and weekday:
    print(f"Hi {name} you are eligibel for discount at the store you have {membership_points - 5 } rewards point remaining")
else:
    print(f"Hi {name} you have {membership_points} reward point but they can only be used on a weekend")


print("--" * 10)  

#thing that evaluate to true or false

# 0 evaluates to false
if 0:
    print("true")
else:
    print("false")

# empty string evaluates to false
if "":
    print("true")
else:
    print("false")

name2 = input("Enter your name: ")
if name2: # name != "" 
    print(f"Hello {name2}")
else:
    print("You did not enter anything....")
    
print("--" * 10)  
    
#in not in
pet_name = "Rover"

letter = input("Enter a letter: ")

if letter in pet_name:
    print(f"{letter} is in {pet_name}")
else:
    print(f"{letter} is not in {pet_name}")
    
print("--" * 10) 
    
day = input("What day are you available ")

#casefold(): will check case of string if not match then nothing output !!!!!!!!
# therefore if statement will not be run CHECK OUT OTHER str functions 
if "Friday" not in day.casefold():     
    print(f"sorry I am not available on {day}")
else:
    print(f"see you {day}")

    


