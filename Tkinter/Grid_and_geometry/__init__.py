try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

#Note!    
#.grid() uses row and column to set grid lay out over mainWindow
#.grid() also uses stick. this sets position using, north, south, east, and west ('n','s','e','w')

#careful not to confuse columnconfigure() with config()  

    
mainWindow = tkinter.Tk()

mainWindow.geometry('800x600+200+000')

mainWindow.title("Hello world")

label = tkinter.Label(mainWindow, text="Welcome")
label.grid(row=0, column=0)

leftFrame = tkinter.Frame(mainWindow)
leftFrame.grid(row=1, column=1)

canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
canvas.grid(row=1, column=0)

rightFrame = tkinter.Frame(mainWindow)
rightFrame.grid(row=1, column=2, stick='n')

button1 = tkinter.Button(rightFrame, text="button1")
button2 = tkinter.Button(rightFrame, text="button2")
button3 = tkinter.Button(rightFrame, text="button3")
button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)

#configure the columns in mainWindow. Adding weight to columns will populate empty space in column 
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.grid_columnconfigure(2, weight=1) #grid_columnconfigure is the same as columnconfigure

#config() sets options. In this case options are a sunken boarder for: 
#leftFrame which is in row=1 column=1 and rightFrame in row=1 column=2 of mainWindow
leftFrame.config(relief='sunken', borderwidth=1)
rightFrame.config(relief='sunken', borderwidth=1)

#grid(sticky= ) is used here to stretch the sunken boarder
#using the compass references points: 'ns', 'new' 
leftFrame.grid(sticky='ns')
rightFrame.grid(sticky='new')

#NOTE ! weight options must be set inside of a cell first in some cases 
#as some options like sticky may not work.

#setting weight options for rightFrame using columnconfigure   
rightFrame.columnconfigure(0, weight=1)

#now weight as been set above on line 53 we can use grid(sticky='ew') to stretch buttons
button2.grid(sticky='ew') 


mainWindow.mainloop()



