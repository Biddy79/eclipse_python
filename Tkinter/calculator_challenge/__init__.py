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
import tkinter
from PIL.TiffImagePlugin import ROWSPERSTRIP

try:
    import tkinter
except ImportError:
    import TKinter as tkinter
    
mainWindow = tkinter.Tk()

mainWindow.geometry('500x600-1200-400')
mainWindow.title("Calculator")

mainWindow.rowconfigure(0, weight=10)
mainWindow.rowconfigure(1, weight=0)
mainWindow.rowconfigure(2, weight=500)

mainWindow.columnconfigure(0, weight=0)
mainWindow.columnconfigure(1, weight=0)
mainWindow.columnconfigure(2, weight=500)
mainWindow.columnconfigure(3, weight=500)


resultBox = tkinter.Entry(mainWindow)
resultBox.grid(row=0, column=0, sticky='nsew', columnspan=3)

C_Button = tkinter.Button(mainWindow, text='C')
C_Button.grid(row=1, column=0, sticky='w')

CE_Button = tkinter.Button(mainWindow, text='CE')
CE_Button.grid(row=1, column=1, sticky='w')





mainWindow.mainloop()
    
    
    