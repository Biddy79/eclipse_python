high = 1000
low = 1

print(f"Please think of a number between {low} and {high}")
input("Please press enter to start")

guesses = 1

while True:
    print(f"\t Guesses in the range {low } - {high} ")
    
    #binary search algorithm 
    guess = low + (high - low) // 2
    
    high_low = input("My guess is {} Should I guess higher or lower?"
                     " Enter h, l or c if my guess was correct".format(guess)).casefold()
    if high_low == "h":
        #guess higher. The low end of the range becomes 1 greater than the guess
        low = guess + 1
    elif high_low == "l":
        #guess lower. The high end of the range becomes 1 less than the guess
        high = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses".format(guesses))
        break
    else:
        print("Please enter h, l or c")
        
    guesses = guesses + 1