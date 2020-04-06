user_input = input("Enter some text here: ").casefold()

user_serch = input("Enter letter you are searching for: ").casefold()

#each letter in user_input separated into individual characters
characters = list(user_input) 

print(characters)

letter_search = "";

for i in characters:
    if user_serch == i:
        letter_search += i

print(f"Here are all the letters you where searching for {letter_search.split()} ")
    
