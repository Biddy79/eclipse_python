from aptdaemon.loop import mainloop
try:
    import tkinter
except ImportError:
    import TKinter as tkinter
    
mainWindow = tkinter.Tk()

mainWindow.geometry('800x580-1200-400')
mainWindow.title("Grid Demo")

label = tkinter.Label(mainWindow, text="Tkinter Grid Demo")
label.grid(row=0,column=0, columnspan=3)# columnspan sets number of columns to span over

#setting weight in row or column will cores the cell area within
#to populate more space (IF FREE).
#The higher the weight number the grater president it as over the other cell's
#This will then cores items with in the area to appear larger

#set weight in each column
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=3)
mainWindow.columnconfigure(3, weight=3)
mainWindow.columnconfigure(4, weight=3)
#set weight in each row
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)
mainWindow.rowconfigure(4, weight=3)

#adding list box
fileList = tkinter.Listbox(mainWindow)
fileList.grid(row=1,column=0, sticky='nsew',rowspan=3)#rowspan sets number of rows to span
fileList.config(border=2, relief='raised')



mainWindow.mainloop()