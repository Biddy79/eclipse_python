'''
Created on 16 Feb 2021

@author: Adam
'''
#Polymorphism is the ability of an object to take on many forms
#We can see that on lines 58-61 that pyhtons use of obj arg in the 
#test_class function is changed dependent upon which class instance
#is passed in. On line 69 we pass in a instance of a Duck. Therfor
#all methods from Duck class will be called. like wise on
#line 77 we use a instance of a Penguin and therfor all Penguin
#methods will be called. 
#So we can see that obj arg in test_class function (line 64) as the ability 
#to change becoming POLYMORPHIC


#Composition is when a Class contains instances objects from an other Class
#Below on line 27-28 In the Duck class __init__ 
#We set a veriable _wing equal to Wing(1.8) Class creating a Wing obj 
#We then use this veriable _wing to call fly() method in Wing Class on 
#line 42

class Wing():
    
    def __init__(self, ratio):
        self.ratio = ratio
    
    def fly(self):
        if self.ratio > 1:
            print("weee, This is fun")
        elif self.ratio ==  1:
            print("This is hard work, but Im flying")
        else:
            print("Ithink I'll just walk")
            

class Duck():
    #_wing set equal to new obj of Wing class in __init__
    def __init__(self):
        self._wing = Wing(1.8)
    
    def walk(self):
        print("Waddle, waddle ,waddle")
        
    def swim(self):
        print("Come on in the water is lovely")
        
    def quack(self):
        print("Quack, quack")
    #fly method here calls fly method in Wing class as _wing is obj of Wing class
    def fly(self):
        self._wing.fly()

class Penguin():
    
    def walk(self):
        print("Waddle, waddle I waddle too")
        
    def swim(self):
        print("Come on in, but its a bit chilly this far South")
        
    def quack(self):
        print("Are you 'avin' a larf? Im a penguin!")
        
#In python obj type is not need when passing to a function like in c++/java
#Here we simply use obj to call fuction to relivent class passed in as arg no type declaration is needed
def test_class(obj):
    obj.walk()
    obj.swim()
    obj.quack()

if __name__ == '__main__':
    
    donald = Duck()
    #Methods from Duck class will be called
    test_class(donald)
    donald.fly()

    print("-" * 40)
    
    percy = Penguin()
    #Methods from Penguin will be called
    test_class(percy)
    
    
    
    
    
    
    