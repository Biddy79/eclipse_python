from player import Player

Adam = Player("Adam")

#printing out all attributes of Player class
print(Adam.name)
print(Adam.lives)
print(Adam.level)
print(Adam.score)

#printing out lives attribute using _get_lives method
print(Adam._get_lives())

#setting number of lives using _set lives attribute
Adam._set_lives(300)
print(Adam.lives)

#Using the lives property() method in Player class which encapsulates instance attributes
#of _get_lives and _set_lives Take note this is not the same attribute as underscore _lives !!!
Adam.lives -= 10
#Agine printing out the lives attribute
print(Adam.lives)

#trying to set lives to negative number using _set_lives method. this will give a priinted warrning
#This is implemented in Player class inside of _set_lives method
Adam._set_lives(-5)


#printin Adam object. Method __str__  is implemented in Player class
print(Adam)
