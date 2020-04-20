#import pickle lib
import pickle

#creating a tuple to write to bin_file
computer = ('CPU RAM HARD DRIVE MOTHERBOARD',
            (('cpu', 'AMD Ryzen 9'), ('ram', 'Corsair 32gb'),
            ('hard drive', 'Samsung 1td ssd'), ('motherboard', 'ASUS ROG STRIX')))
 
computer_parts, computer_spec = computer



#using pickle.dump() to save computer tuple as a bin file
# with open("computer.bin", 'wb') as pickle_file:
#     #parameter   tuple    file variable             
#     pickle.dump(computer, pickle_file)


####code above commented out as file as now been created so no need to create again############
    
    
#using pickle.load() to read computer.bin in readable format #parameters  file variable
with open("computer.bin", 'rb') as computer_pickled:           
    computer = pickle.load(computer_pickled)
    
#print(computer)

#unpacking computer tuple that as now been read using pickle.load()
computer_description, computer_parts = computer

#printing out unpacked tuple
print(computer_description)

for parts in computer_parts:
    description, part = parts
    print(description, part)
    
print("-" * 30)

#variables created to add to computer.bin file
stock_left = [12, "Manchester", 10, "Sheffield", 2, "Newcastle"]

#using dump to now add stock_left list to computer.bin
#pickled.dump() parameters: item to be saved, file name, and protocol
with open("computer.bin", 'wb') as pickle_file:
    pickle.dump(computer, pickle_file)
    pickle.dump(stock_left, pickle_file)
    #we can also just add a variable here
    total_stock = stock_left[0] + stock_left[2] + stock_left[4]
    pickle.dump(total_stock, pickle_file)
    
#now reading computer.bin after dump of new items
#when reading items must be loaded in same order they where dump() into file
with open("computer.bin", 'rb') as computer_pickled:
    computer = pickle.load(computer_pickled)
    stock_and_area = pickle.load(computer_pickled)
    total_stock = pickle.load(computer_pickled)

#unpacking tuple
computer_description, computer_parts = computer

#printing out tuple 
print(computer_description)

for parts in computer_parts:
    description, part = parts
    print(description, part)

#printing out new item stock_left that was added with dump() on line 46
print(stock_and_area)

#printing out new variable that was added on lines 48 and 49
print(total_stock)
    

#note protocols are not backwards compatible and there are safety concerns when loading pickled files
#from unknown source as this could have system commands with in 
    
    
    





    
      
