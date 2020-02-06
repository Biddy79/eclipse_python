name = input("Please enter you Name: ")
age = int(input("Hello {0} Please enter your age: ".format(name)))

if age <= 18:
    print("sorry {0} You are not old enough to vote Please come back in {1} Years".format(name, 18 - age))
else:
    print("Hi {0} you are old enough to vote. ".format(name))

