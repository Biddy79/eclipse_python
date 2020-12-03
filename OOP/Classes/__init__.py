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
#and is used to access instence variables that belongs to the class.

class dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.vicious = False
        
    #Adding new method to class dog
    def attack(self):
        self.vicious = True
        
        
#Instantiate and instance of dog. seting Rover = to template of dog() 
#passing in values name and age
Rover = dog("Rover", 2)
#printing out return values of name and age from defiined obejct Rover
print(Rover.name)
print(Rover.age)

#now creating another instence of class dog

billy = dog("Billy", 11)

print(f"Dogs name is {billy.name} and he is {billy.age} years old")

print("-" * 30)

#printing vicious attribute set in constructor on line 28
print(billy.vicious)
#calling method attack on line 31 which changes attribute of vicious to True
billy.attack()
#printing out vicious after status being changed
print(billy.vicious)

print("-" * 30)

#We can also add instance variables to class from out side of initial definition 
Rover.colour = "brown"
print(Rover.colour)
#Take note not ever instance of dog class will have attribute colour!!!
#Cannot do billy.colour !!!!!



    

