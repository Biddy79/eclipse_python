#Parabola function displayed using tkinter
try:
    import tkinter
except ImportError: # python2
    import Tkinter as tkinter

def parabola(x):
    y = x*x / 100
    return y
    
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
    
def plot(canvas, x ,y):
    canvas.create_line(x, y, x+1, y+1, fill="red")
    
mainWindow = tkinter.Tk()

mainWindow.title("Parabola")
mainWindow.geometry("840x680-1200-650")

canvas = tkinter.Canvas(mainWindow, width=420, height = 680)
canvas.grid(row=0, column=0)

canvas2 = tkinter.Canvas(mainWindow, width=420, height = 680, background="blue")
canvas2.grid(row=0, column=1)

#repr() function prints object name ant type
print(repr(canvas), repr(canvas2))

draw_axes(canvas)
draw_axes(canvas2)

for x in range(-100, 100):
    y = parabola(x)
    plot(canvas, x, -y)


    
mainWindow.mainloop()
    
