#Parabola function displayed using tkinter
try:
    import tkinter
except ImportError: # python2
    import Tkinter as tkinter

mainWindow = tkinter.Tk()

mainWindow.title("Parabola")
mainWindow.geometry("940x680-1200-650")

canvas = tkinter.Canvas(mainWindow, width=940, height= 680)
canvas.grid(row=0, column=0)

def parabola(x):
    y = x*x 
    return y

for x in range(-100, 100):
    y = parabola(x)
    print(y)
    
mainWindow.mainloop()
    
