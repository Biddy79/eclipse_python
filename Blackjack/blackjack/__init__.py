import random

try:
    import tkinter
except ImportError: #python 2
    import Tkinter as tkinter
    


def load_images(card_images):
    suits=['club', 'diamond', 'heart', 'spade']
    face_cards=['jack', 'queen', 'king']
    
    if tkinter.TkVersion >= 8.6:
        extension = 'png'
    else:
        extension = 'ppm'
        
    # for each suit, retrieve the image from the cards
    for suit in suits:
        #first the number card 1 to 10
        for card in range(1, 11):
            name = 'C:\\Users\\Adam\\src\\eclipse_python\\Blackjack\\blackjack\\cards\\{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image,))
            
            
        #next the face cards
        for card in face_cards:
            name = 'C:\\Users\\Adam\\src\\eclipse_python\\Blackjack\\blackjack\\cards\\{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image,))


def deal_card(frame):
    #pop the next card off the top of the deck
    next_card = deck.pop(0)
    #and add it to back of pack
    deck.append(next_card)
    #add the image to the label and display the the label
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    #now return the card's face value
    return next_card
    
def score_hand(hand):
    #calculate the total score of all cards in the list
    #Only one ace can have a value 11, and this will be reduced to 1 if the hand would bust.
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        #If bust, check if there is an ace and subtract 10
        if score > 21 and ace:
            score -= 10
            ace = False
    return score
    
    
def deal_dealer():
    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)
    
    player_score = score_hand(player_hand)
    if player_score > 21:
        result_text.set("Dealer wins!!")
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player wins!!")
    elif dealer_score > player_score:
        result_text.set("Dealer wins!!")
    else:
        result_text.set("Draw!")
    
def deal_player():
    player_hand.append(deal_card(player_card_frame))
    player_score = score_hand(player_hand)
    
    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer Wins!")
        
#     global player_score
#     global player_ace
#     card_value = deal_card(player_card_frame)[0]
#     if card_value == 1 and not player_ace:  
#         player_ace = True
#         card_value = 11
#     player_score += card_value
#     #if bust check for ace and subtract 1
#     if player_score > 21 and player_ace:
#         player_score -= 10
#         player_ace = False
#     player_score_label.set(player_score)
#     if(player_score > 21):
#         result_text.set("Dealer Wins!")
#     print(locals())


def initial_deal():
    deal_player()
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()

def rest_game():
    #declare global veriabels to gain access with in this function
    global dealer_card_frame
    global player_card_frame
    global dealer_hand
    global player_hand
    
    #destroy dealer and player card from to remove card image from card frame
    dealer_card_frame.destroy()
    player_card_frame.destroy()
    
    #re-define dealer and player card frame
    dealer_card_frame = tkinter.Frame(card_frame, background="green")
    dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)
    
    player_card_frame = tkinter.Frame(card_frame, background="green")
    player_card_frame.grid(row=2, column=1 , sticky='ew', rowspan=2)
    
    #Set result text to NULL
    result_text.set("")
    
    #create new dealer and player list
    dealer_hand = []
    player_hand = []
    initial_deal()
    
    

    
def shuffel():
    random.shuffle(deck)
    
def play():
    #Deal new hand
    initial_deal()
    mainWindow.mainloop()
    
    
mainWindow = tkinter.Tk()
        
#set up screen and frames for dealer nad player
mainWindow.title("Black Jack")
mainWindow.geometry("640x480")
mainWindow.configure(background='green')
    
result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)
    
card_frame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)
    
dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green", fg="white").grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg="white").grid(row=1, column=0)
#embeded frame to hold card images
dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)
    
player_score_label = tkinter.IntVar()
    
tkinter.Label(card_frame, text="player", background="green", fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg="white").grid(row=3, column=0)
#embeded frame to hold the card images 
player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1 , sticky='ew', rowspan=2)
    
button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')
    
dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_dealer)
dealer_button.grid(row=0, column=0)
    
player_button = tkinter.Button(button_frame, text="Player", command=deal_player)
player_button.grid(row=0, column=1)
    
new_game_button = tkinter.Button(button_frame, text="New game", command=rest_game)
new_game_button.grid(row=0, column=2)
    
shuffle_button = tkinter.Button(button_frame, text="Shuffle", command=shuffel)
shuffle_button.grid(row=0, column=3)
    
    
#load cards
cards = []
load_images(cards)
print(cards)
    
#Create a new deck of cards and shuffle them
deck = list(cards) #creates new deck each time not deck = cards
shuffel()
    
#Create list to store Dealer and Players hands
dealer_hand = []
player_hand = []

#The play() function is resposibel for starting the program.
#test to see if __name__ == "__main__"
#If TRUE play() will be executed and the program will start
#Therfor if file is imported it will not execute unless the play function is called and __name__ == "__main__"
if __name__ == "__main__":   
    #play() executes initial_deal() and mainWindow.mainloop() which start the program running
    play()
    

    
    
