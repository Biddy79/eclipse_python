#first we must understand that in python underscores are used before the nameing of 
#methods. They act just the same as methods/functions below is and example of this

a = 12
b = 4
print(a + b)
# __add__ is a function which works the same as the + operator take note of the dot
# notation before calling and () at the end which takes parameter .__add__()
print(a.__add__(b))

print('-' * 30)



#Classes are used to build a template of objects
#class name is dog and we pass objects as a parameter. dog(object)

#"__init__" is a reseved method in python classes.
#It is called as a constructor in object oriented terminology

#The self parameter is a reference to the current instance of the class, 
#and is used to access variables that belongs to the class.

class dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.vicious = False
        
#Instantiate and instance of dog. seting Rover = to template of dog() 
#passing in values name and age
Rover = dog("Rover", 2)
#printing out return values of name and age from defiined obejct Rover
print(Rover.name)
print(Rover.age)

#now creating another instence of class dog

billy = dog("Billy", 11)

print(f"Dogs name is {billy.name} and he is {billy.age} years old")


