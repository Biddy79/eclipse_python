'''
Created on 18 Sep 2020

@author: Adam
'''
import blackjack

#if a file is imported the attribute __name__ == "__main__" and the program will exectue inside of the imported file


#__name__ is = to __main__ inside of Blackjack main file
print(__name__)
blackjack.play()
print(blackjack.cards)
