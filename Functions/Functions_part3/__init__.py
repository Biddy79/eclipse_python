#writing center_text() function to a file 

def center_text(*args, sep=' ', end='\n', file=None, flush=False):
    text = ""
    for arg in args:
        text += str(arg) + sep #adding sep parameter to end of text
    left_margin = (80 - len(text)) // 2
    #setting print parameters = to center_text function arguments
    print(" " * left_margin, text, end=end, file=file, flush=flush)
    
text = "I am learning python"

#copying center_text functiontoa file
with open("centered", mode='w') as centerd_file:
    #call to center_text function
    center_text("Hello world", file = centerd_file)
    center_text(text, file = centerd_file)
    center_text(1,2,3,sep=':', file = centerd_file)
    
#writing center_text2() function to a file using return key word 

def center_text2(*args, sep=' '):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    #return: will return text after left_margin times by width of a blank space 
    return " " * left_margin + text

with open("centered2", mode='w') as centered_file2:
    #setting s1 = to return value of center_text2
    s1 = center_text2("Hello world")
    #printing s1 to file
    print(s1, file=centered_file2)
    #printing string directly in to file
    print(center_text2("I am learning pyhton"), file=centered_file2)
    #setting s3 = to return value of center_text2
    s3 = center_text2(1,2,3, sep=':')
    #printing s3 to file 
    print(s3, file=centered_file2)
    