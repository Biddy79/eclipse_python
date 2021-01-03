'''
Created on 31 Dec 2020

@author: Adam
'''
from ctypes.test.test_pickling import name


class Player(object):
    ''' Simpel player class to demonstrate using getters and setters within python 
    
        although setters and getters are not really nessesery in pyhton as we have direct
        access to attributes inside of a class they can be useful to validate or check infromation 
        regarding an attribute before changing or manipulating data
        
        This class will validate that lives are grater than 0 giving a print warning that 
        lives cannot be negative and lives will be set to 0 inside of the _set_lives method
        if any attempts are made to do so
        
    '''

    def __init__(self, name):
        '''Constructor
           Attributes:
               name (str) name of player passed in as arg
               _lives (int) number of lives player has
               _level (int) _level of player 
               score (int) score of player
               
               NOTE that _lives is prefixed with underscore. Tis will stop 
               recursion when lives is passed to _set_lives method as they will 
               be separate attributes!!!!
        '''
        self.name = name
        self._lives = 3
        self._level = 1
        self.score = 0
        
    def _get_lives(self):
        '''Simpel getter method that returs players lives attribute
        '''
        return self._lives
    
    def _set_lives(self, lives):
        '''simple setter method which sets the lives attribute of the player
        to the number passed in as: arg (int) lives
        
        If attempts are made to set lives to a negative number a printed warrning 
        will be given and lives will be set to zero
        '''
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives cannot be negative")
            self._lives = 0
     
    
    
    def _get_level(self):
        return self._level
    
    def _set_level(self, level):
        if level > 0:
            delta = level - self._level
            self.score += delta * 1000
            self._level = level
        else:
            print("Level cannot be less than 1")
            
            
            
    #The property() method in Python provides an interface to instance attributes.
    #It encapsulates instance attributes and provides a property. 
    #The property() method takes the get, set and delete methods as arguments
    #and returns an object of the property class.
    #We can now make calls to the _get and _set methods by just using lives or level
    #and therfore we go loger need to use () brackes to call the methods 
    
    lives = property(_get_lives, _set_lives)
    level = property(_get_level, _set_level)        
        
    
    
    def __str__(self):
        ''' __str__ method that prints attributs within a Class
            When printing an object pyhton will look for this method
            
            arg: (self) Class passed as arg
            
            
        '''
        return f"Name {self.name}, Lives {self.lives}, Level {self._level}, Score {self.score}"
        
        
        
    
    
    
    
    
    