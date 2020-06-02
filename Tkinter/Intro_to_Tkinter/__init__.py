#Tkinter is a Python GUI moduel

#importing module with exception. If Trying to import tkinter in Python2 this must be imported 
#with a capital T(Tkinter). This exception will try to import first in Python3 with lower 
#case t(tkinter). If this fails it will then import the moduel with the upper case T for python2
try:
    import tkinter
except  ImportError: #Pyhton2
    import Tkinter as tkinter
    
#gives current installed version of Tkinter 
print(tkinter.TkVersion)
print(tkinter.TclVersion)

#opens test gui window
#tkinter._test()

#opens gui tkinter window and sets it = to mainWindow variable   
mainWindow = tkinter.Tk()#(note lower case k()

#sets title 
mainWindow.title("Hello World")
#640x480 sets window size. +500+400 sets position 
mainWindow.geometry('640x480+500+400')#note we are passing a string not an int

#passes control over to tkinter.Tk() by calling the mainloop() method of our top window
#main loop method handles all event processors that a gui needs to work
mainWindow.mainloop()