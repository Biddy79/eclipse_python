# Write a GUI program to create a simple calculator
# layout that looks like the screenshot.
#
# Try to be as Pythonic as possible - it's ok if you
# end up writing repeated Button and Grid statements,
# but consider using lists and a for loop.
#
# There is no need to store the buttons in variables.
#
# As an optional extra, refer to the documentation to
# work out how to use minsize() to prevent your window
# from being shrunk so that the widgets vanish from view.
#
# Hint: You may want to use the widgets .winfo_height() and
# winfo_width() methods, in which case you should know that
# they will not return the correct results unless the window
# has been forced to draw the widgets by calling its .update()
# method first.
#
# If you are using Windows you will probably find that the
# width is already constrained and can't be resized too small.
# The height will still need to be constrained, though.

try:
    import tkinter
except ImportError:
    import TKinter as tkinter
    
mainWindow = tkinter.Tk()

mainWindow.geometry('300x375-1200-400')
mainWindow.title("Calculator")

mainWindow.minsize('200', '250')

mainWindow['padx'] = 2

mainWindow.rowconfigure(0, weight=0)
mainWindow.rowconfigure(1, weight=0)
mainWindow.rowconfigure(2, weight=0)
mainWindow.rowconfigure(3, weight=0)
mainWindow.rowconfigure(4, weight=0)
mainWindow.rowconfigure(5, weight=0)
mainWindow.rowconfigure(6, weight=100)

mainWindow.columnconfigure(0, weight=0)
mainWindow.columnconfigure(1, weight=0)
mainWindow.columnconfigure(2, weight=0)
mainWindow.columnconfigure(3, weight=0)
mainWindow.columnconfigure(4, weight=100)


resultBox = tkinter.Entry(mainWindow)
resultBox.grid(row=0, column=0, sticky='ew', columnspan=4)

C_Button = tkinter.Button(mainWindow, text='C')
C_Button.grid(row=1, column=0)

CE_Button = tkinter.Button(mainWindow, text='CE')
CE_Button.grid(row=1, column=1, sticky='ew')

Button_7 = tkinter.Button(mainWindow, text='7')
Button_7.grid(row=2, column=0)

Button_8 = tkinter.Button(mainWindow, text='8')
Button_8.grid(row=2, column=1, sticky='ew')

Button_9 = tkinter.Button(mainWindow, text='9')
Button_9.grid(row=2, column=2)

Button_plus = tkinter.Button(mainWindow, text='+')
Button_plus.grid(row=2, column=3, sticky='ew')

Button_4 = tkinter.Button(mainWindow, text='4')
Button_4.grid(row=3, column=0)

Button_5 = tkinter.Button(mainWindow,text='5')
Button_5.grid(row=3, column=1, sticky='ew')

Button_6 = tkinter.Button(mainWindow, text='6')
Button_6.grid(row=3, column=2)

Button_sub = tkinter.Button(mainWindow, text='-')
Button_sub.grid(row=3, column=3, sticky='ew')

Button_1 = tkinter.Button(mainWindow, text='1')
Button_1.grid(row=4, column=0)

Button_2 = tkinter.Button(mainWindow, text='2')
Button_2.grid(row=4, column=1, sticky='ew')

Button_3 = tkinter.Button(mainWindow, text='3')
Button_3.grid(row=4, column=2)

Button_mult = tkinter.Button(mainWindow, text='*')
Button_mult.grid(row=4, column=3, sticky='ew')

Button_0 = tkinter.Button(mainWindow, text='0')
Button_0.grid(row=5, column=0)

Button_equal = tkinter.Button(mainWindow, text='=')
Button_equal.grid(row=5, column=1, sticky='ew', columnspan=2)


Button_slash = tkinter.Button(mainWindow, text='/')
Button_slash.grid(row=5, column=3, sticky='ew')

#Calculator 2 using for loop 

mainWindow_2 = tkinter.Tk()

mainWindow_2.geometry('300x375-1200-850')
mainWindow_2.title("Calculator")

mainWindow_2.minsize('200', '250')

mainWindow_2['padx'] = 2


button_list = [['C','CE'],
               ['7', '8', '9', '+'],
               ['4', '5', '6', '-'],
               ['1', '2', '3', '*'],
               ['0', '=', '/']]

#below is just some of my working out
# buttons = None
# for button_list_array in button_list:
#     for buttons in button_list_array:
#         buttons = tkinter.Button(mainWindow_2, text=buttons)
#         print(type(buttons))
        
for row in range(len(button_list)):
    #print(row) my working out
    for col in range(len(button_list[row])):
        buttons = tkinter.Button(mainWindow_2, text=button_list[row][col])
        #print(f"row: {row}, col: {col}")my working out
        buttons.grid(row=row, column=col, sticky='ew')
        
        
                
                                   


mainWindow.mainloop()

mainWindow_2.mainloop()
    
    
    