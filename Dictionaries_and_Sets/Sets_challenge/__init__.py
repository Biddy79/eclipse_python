# Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
#
# You can either enter the text from the keyboard or
# initialise a string variable with the string.

user_input = input("Enter text here: ").casefold()

vowels = frozenset("aeiou")

finalset = set(user_input).difference(vowels)
print(finalset)

finalist = sorted(finalset)
print(finalist)










    

