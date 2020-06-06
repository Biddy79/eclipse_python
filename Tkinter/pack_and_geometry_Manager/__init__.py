try: 
    import tkinter
except ImportError:
    import Tkinter as tkinter
    
#Notes on some parameters:
#fill=tkinter.Y will fill virticaly 
#fill=tkinter.X Will fill horizantly 
#Note expand=True is only need with some positions to fill the window

#anchor will place using compass reference points anchor='n' 's' 'e' 'w' 'ne' 'nw' ect.....
    
mainWindow = tkinter.Tk()

mainWindow.title("hello world")        

mainWindow.geometry('800x600+250+000')        

#creates a label 
label = tkinter.Label(mainWindow, text="Welcome")
#pack sets the label placement inside mainWindow
label.pack(side='top')

#creating a frame inside of maineWindow
leftFrame = tkinter.Frame(mainWindow)
#positioning frame inside of mainWindow
leftFrame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)

#creates a raised canvas inside leftFrame
canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
#pack sets the canvase position inside mainWindow
canvas.pack(side='left', anchor='n')

#adding right frame
rightFrame = tkinter.Frame(mainWindow)
#positioning right frame inside mainWindow
rightFrame.pack(side='right', anchor='n', expand=True)

#adding buttons to rightFrame
button1 = tkinter.Button(rightFrame, text="Button1")
button2 = tkinter.Button(rightFrame, text="Button2")
button3 = tkinter.Button(rightFrame, text="Button3")

#positioning buttions inside right frame.
button1.pack(side='top')
button2.pack(side='top')
button3.pack(side='top')



mainWindow.mainloop()