#shelve is best used when working with lots of information as it dose not need to be loaded back into
#memory like you would have to when using pickel
  
#A shelve object is a lot like a Dictionaries in that it as key value pairs and uses the same functions()

#one big difference is that it sorts its values in a file and not memory and the values are pickle 
#when saved.

#again it is not wise to use shelve from untrusted source as it could contain system commands when loaded

#first we import the shelve lib
import shelve

with shelve.open('shelveTest') as computer:
    computer['cpu'] = "central processing unit"
    computer['ram'] = "random access memory" 
    computer['mother board'] = "main circuit board"
    computer['hard drive'] = "data storage device"
    computer['price'] = 1200
    
    #here we print out values inside the with shelve.open() block 
    print(computer['ram']) #still prints even after commented out above
    print(computer['cpu'])
    print(computer['price'])
    
#if we try opening out side of the block shelve is closed automatically as we are using with key word

#print(computer['ram'])
#print(computer['cpu'])

#this shows that shelve cannot be instantiated as dictionaries: my_dict = {1: "one", 2: "two" }

print('-' * 30)

with shelve.open('shelveTest') as computer:
    del computer['ram'] #to remove [ram] we must use del key word
    #we can now see ram as been removed from computer
    for key in computer:
        print(key)
    
