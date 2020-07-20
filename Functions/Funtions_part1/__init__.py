#define a function
def python_food():
    print("Spam and eggs")

#call to function python_food
python_food()

#call function python_food. 
#Using print will print functions return value which in this case is None
print(python_food())

print("-" * 30)

#function defined to print text in center of screen (if screen is 80 characters wide)
#center_text also takes a parameter called text
def center_text(text):
    text = str(text)#text is cast too a string in case a number is passed in as argument
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)

text = "Im learning pyhton"
#calling funtion center text and passing in a string as a argument 
center_text("Hello world")
#calling funtion center text and passing in a variable text (which holds a string)
center_text(text)
#calling funtion center text and passing in a int
center_text(12)

#note on line 16 text is cast to string. 
#int dose not have character lenght so (80 - len(text)) // 2 can not be caculated
#consider ints in computers are stored in binary or hex thefore 12 would be 1100 in binary