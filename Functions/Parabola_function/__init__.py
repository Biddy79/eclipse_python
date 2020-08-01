#Parabola function displayed using tkinter
import math

try:
    import tkinter
except ImportError: # python2
    import Tkinter as tkinter


def parabola(page, size):
    for x in range(size):
        y = x*x / size
        plot(page, x, y)
        plot(page, -x, y)
        
#No need to pass colour argument as colour as a defalut value of "red" 
def circle(page, radius, g, h, colour="red"):
    page.create_oval(g + radius, h + radius, g - radius, h - radius, outline=colour , width=2)
    
    #for x in range(g* 100, (g + radius) * 100):
        #x /= 100
        #y = h + (math.sqrt(radius ** 2 - ((x-g) ** 2)))
        #plot(page, x, y)
        #plot(page, x, 2 * h - y)
        #plot(page, 2 * g - x, y)
        #plot(page, 2 * g - x, 2 * h - y)
    
def draw_axes(page):
    page.update()
    x_origin = page.winfo_width() / 2
    y_origin = page.winfo_height() /2
    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin ))
    page.create_line(-x_origin, 0, x_origin, 0, fill="black")
    page.create_line(0, y_origin, 0, -y_origin, fill="black")
    #locals() function returns all variables that have been defined with ina function
    #Note locals() must be used within a function
    print(locals())
    
def plot(page, x ,y):
    page.create_line(x, -y, x+1, -y+1, fill="red")
    
mainWindow = tkinter.Tk()

mainWindow.title("Parabola")
mainWindow.geometry("640x480-1200-650")

canvas = tkinter.Canvas(mainWindow, width=640, height = 480)
canvas.grid(row=0, column=0)

#repr() function prints object name ant type
print(repr(canvas))

draw_axes(canvas)

parabola(canvas, 100)
parabola(canvas, 200)

circle(canvas, 100, 100, 100, "blue")
circle(canvas, 100, 100, -100, "yellow")
circle(canvas, 100, -100, 100, "black")
circle(canvas, 100, -100, -100, "green")

#Note we do not need to pass colour argument to circle function call as it as a 
#default value of "red" diffined on line 16 
circle(canvas, 10, 30, 30)
circle(canvas, 10, 30, -30)
circle(canvas, 10, -30, 30)
circle(canvas, 10, -30, -30)

circle(canvas, 10, 0, 0)


    
mainWindow.mainloop()
    
