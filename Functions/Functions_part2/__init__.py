#modifying center_text function to take more than one argument using *
#we can aslo set parameter values inside fuction brackets() using =
#also adding parameters found in print function 
#two function that have the same parameters are said to have the same signatuer
def center_text(*args, sep=' ', end='\n', file=None, flush=False):
    text = ""
    for arg in args:
        text += str(arg) + sep #adding sep parameter to end of text
    left_margin = (80 - len(text)) // 2
    #setting print parameters = to center_text function arguments
    print(" " * left_margin, text, end=end, file=file, flush=flush)
    
    
center_text("Hello world")
center_text("I ", "Am ", "learing " , "python")
center_text(1, 2, 3, sep=":")# setting sep parameter as : 