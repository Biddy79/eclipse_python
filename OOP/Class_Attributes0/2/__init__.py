#using underscores in classes

#Attributes that start with a single underscaore are for internal class use only

class computer():
    _cpu = "i7"
    
    
print(computer._cpu)

#you can still name veriables out side of the class with the underscore convention
#but this is discurage as it will lead to confusion regarding nameing and breaks 
#encapsulation 

_cpu = "i5"
print(_cpu)
print(computer._cpu)

#NAME MANGLING
#Attributes that start with two underscores will be non public to the class but the 
#name can still be used to declare veriables out side of the class
#pyhton will intrpret them as separate veriables/attributes 
#This is used when sub classing

#make attribute declared inside class car with in double underscore
class car():
    __make = "B.M.W"

myCar = car
#to access __make we must use object then class name 
print(myCar._car__make)

#we can see using __dict__ on class car
#that car class as created its own attribute called _car__make
#This happens when we declared inside class car with in double underscore line 25
print(car.__dict__)

#we can now create variable out side of the class with the same name __make this will be seen 
#its own veriable although it shares the same name 
__make = "V.W"
print(__make)







    

