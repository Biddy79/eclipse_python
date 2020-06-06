try:
    import tkinter
except ImportError:
    import Tkinter as tkinter
    
#.grid() uses row and column to set grid lay out over mainWindow
#.grid() also uses stick. this sets position using, north, south, east, and west ('n','s','e','w')
    
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

mainWindow.mainloop()