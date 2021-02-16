'''
Created on 16 Feb 2021

@author: Adam
'''
#Polymorphism is the ability of an object to take on many forms



class Duck():
    
    def walk(self):
        print("Waddle, waddle ,waddle")
        
    def swim(self):
        print("Come on in the water is lovely")
        
    def quack(self):
        print("Quack, quack")
        

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

    print("-" * 40)
    
    percy = Penguin()
    #Methods from Penguin will be called
    test_class(percy)
    
    
    
    
    
    
    