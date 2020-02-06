name = input("Please enter you Name: ")
age = int(input("Hello {0} Please enter your age: ".format(name)))
 
if age <= 18:
    print("sorry {0} You are not old enough to vote Please come back in {1} Years".format(name, 18 - age))
else:
    print(f"Hi {name} you are old enough to vote. ")


pin = int(input("Please enter your pin"))

if pin == 959:
    print(f"you entered {pin}. pin correct !!!")
elif pin > 959:
    print(f"you entered {pin}. pin is a lower number!!!")
else:
    print(f"you entered {pin}. pin is a higher number !!! ")
    