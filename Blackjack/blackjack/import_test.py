'''
Created on 18 Sep 2020

@author: Adam
'''
import blackjack

#if a blackjack is imported the attribute __name__ == "blackjack"
print(blackjack.__name__)

#__name__ inside of its own file is = to __main__ 
print(__name__)

blackjack.play()
print(blackjack.cards)

