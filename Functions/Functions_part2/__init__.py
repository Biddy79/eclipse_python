#modifying center_text function to take more than one argument

def center_text(text):
    text = str(text)#text is cast too a string in case a number is passed in as argument
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)
    
center_text("Hello world")