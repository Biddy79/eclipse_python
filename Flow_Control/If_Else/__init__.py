name = input("Please enter you Name: ")
age = int(input("Hello {0} Please enter your age: ".format(name)))
  
if age <= 18:
    print("sorry {0} You are not old enough to vote Please come back in {1} Years".format(name, 18 - age))
else:
    print(f"Hi {name} you are old enough to vote. ")
 
 
# pin = 959
# guess = int(input("Please enter your pin"))
#   
#  
# if guess > pin:
#     print(f"you entered {guess}. pin is a lower number!!!")
#     guess = int(input("please enter pin"))
#     if guess == pin:
#         print("pin correct")
#     else: print("Sorry pin is incorrect")
# elif guess < 959:
#     print(f"you entered {guess}. pin is a higher number !!! ")
#     guess = int(input("please enter pin"))
#     if guess == pin:
#         print("pin correct")
#     else: print("Sorry pin is incorrect")
# else:
#     print("pin correct !!!")

#better way!!!!!!!!!!!!!!!!!!!!!!!!!!!!

pin = 959
guess = int(input("Please enter your pin: "))

if guess == pin:
    print("pin correct")
else:
    if guess < pin:
        print("pin is a higher number")
    else:
        print("pin is a lower number")
    guess = int(input("please enter pin again"))
    if guess == pin:
        print("pin correct")
    else:
        print("sorry pin still incorrect!!!")

    
        

    
    
    