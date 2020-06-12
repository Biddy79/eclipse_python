from aptdaemon.loop import mainloop
from pkg_resources._vendor.packaging.markers import Variable
try:
    import tkinter
except ImportError:
    import TKinter as tkinter

import os

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
fileList.grid(row=1,column=0, sticky='nsew',rowspan=2)#rowspan sets number of rows to span
fileList.config(border=2, relief='raised')

#inserting directory of file to fileList box
for zone in os.listdir('/usr/bin'): # '/Windows/System32' 
    fileList.insert(tkinter.END, zone) #tkinter.END specify order to add list items
    
#adding scroll bar to fileList
#parameter: orient=tkinter.VERTICAL: sets scroll bar vertical or horizontal
#parameter: command=fileList.yview: sets movement orientation of items in list vertical or horizontal
listScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=fileList.yview)
#position listScroll inside mainWindow
listScroll.grid(row=1, column=1, sticky='nsw', rowspan=2)
#allows fileList to call set method each time list is moved (by mouse) or new items added
fileList['yscrollcommand'] = listScroll.set  

#frame for radio buttons
optionFrame = tkinter.LabelFrame(mainWindow, text="File Details")
#position optionFrame inside mainWindow
optionFrame.grid(row=1, column=2, sticky='ne')

#setting radioButton value. 
rbValue = tkinter.IntVar()
#All buttons will shear the same value so only one can be selected at a time
rbValue.set(3)
#Adding radio buttons to optionsFrame created on line 54
#Parameter: value=1 sets a value for each button so we can determine which button is selected
#Parameter: variable=rbValue: attaches button to rbValue 
radio1 = tkinter.Radiobutton(optionFrame, text="Filename", value=1, variable=rbValue)
radio2 = tkinter.Radiobutton(optionFrame, text="path", value=2, variable=rbValue)
radio3 = tkinter.Radiobutton(optionFrame, text="Timestamp", value=3, variable=rbValue)

#positioning radio buttons inside of optionFrame
radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')


mainWindow.mainloop()

#retrieving radio button selected and printing out to console
print(rbValue.get()) #NOTE THIS IS DONE OUT SIDE OF mineWindow,mainloop()





