# static methods, much like class methods, 
# are methods that are bound to a class rather than its object. 
# They do not require a class instance creation.
# So, they are not dependent on the state of the object
from _ast import With

# Below is a class Pesron that has attributes age and name.
# It also has an ID attribute which value is set by calling a set_id method
# set_id then calls staticmethod _random_id() 

# Static methods in pyhton can be called by objects (NOT like in other programing
# languages (c, c++, java). This is NOT!! the intended uses of static methods 
# as they should be used from inside the class and are called by there class name. 
# In this case Person._random_id().
# Also take note that it is common to prefix static methods With an underscore and the 
# @staticmethod above 



import random

class Person():
    def __init__(self, age, name):
        self.age = age
        self.name = name
        self.ID = 0
    
    #Generates random number
    @staticmethod
    def _random_id():
        ran_num = random.randint(1, 100)
        return ran_num
        
    
    def set_id(self):
        self.ID = Person._random_id() 
        print(f"your id is {self.ID}")

        
if __name__ == "__main__":
    
    
    Adam = Person(41, "Adam")
    Adam.set_id()
    
    Tim = Person(32, "Tim")
    Tim.set_id() 
