class computer():
    memory_size = 128 #This is an attribute of class computer
    

work_computer = computer
#printing attribute of work computer
print(work_computer.memory_size)

#changing memory_size 
work_computer.memory_size = 500
print(f"Work computer memory size as now been changed to {work_computer.memory_size}")

#note although we have created a new instance of the class computer 
#memory size is still set as 500 as this was changed above
home_computer = computer
print(f"home computer has the changed value of work computer: {home_computer.memory_size}")

#We can add new attributes to any instance these of the class
home_computer.external_memory = 1000
print(f"New external memory add to computer class of:  {home_computer.external_memory}")
#and the will be made avalible to all instances of that class
print(f"work computer also as access to external memory of: {work_computer.external_memory}")

print("-" * 30)

#list all attributes and methods of a class using .__dict__ function
print(work_computer.__dict__)
print(home_computer.__dict__)

print("-" * 30)

#Setting new attributes ram using CLASS!! name
computer.ram = 16

print(work_computer.ram)
print(home_computer.ram)
#showing attributes using __dict__
print(work_computer.__dict__)
print(work_computer.__dict__)

home_computer.ram = 8
print(work_computer.ram)
print(home_computer.ram)




