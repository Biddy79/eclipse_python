try:
    import tkinter
except ImportError:
    import TKinter as tkinter

import os

mainWindow = tkinter.Tk()

mainWindow.geometry('800x580-200-100')
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
for zone in os.listdir('/usr/bin'): # '/Windows/System32' or '/usr/bin'
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

#results label
resultLabel = tkinter.Label(mainWindow, text='Result')
resultLabel.grid(row=2, column=2, sticky='nw')
#result box
result = tkinter.Entry(mainWindow)
result.grid(row=2, column=2, sticky='sw')

#Frame for time spinners
timeFrame = tkinter.LabelFrame(mainWindow, text='Time')
#positioning timeFrame inside mainWindow
timeFrame.grid(row=3, column=0, sticky='new')

#time spinners 
hourSpinner = tkinter.Spinbox(timeFrame, width=2, values=tuple(range(0,24)))
minuteSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59) #from is a key word 
secondSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59) #so we use _from

#positioning time spinner inside timeFrame
hourSpinner.grid(row=0, column=0)
tkinter.Label(timeFrame, text=':').grid(row=0, column=1)#setting ':' between each time spinner
minuteSpinner.grid(row=0, column=2) 
tkinter.Label(timeFrame, text=':').grid(row=0, column=3)#setting ':' between each time spinner
secondSpinner.grid(row=0,column=4)
#adding padding 
timeFrame['padx'] = 36 #'padx' adds padding on x axis, 'pady' adds padding on y axis  

#Frame for date spinners
dateFrame = tkinter.Frame(mainWindow)
#position dateFrame inside mainWinow
dateFrame.grid(row='4', column='0', sticky='new')

#date labels
dayLabel = tkinter.Label(dateFrame, text='Day')
monthLabel = tkinter.Label(dateFrame, text='Month')
yearLabel = tkinter.Label(dateFrame, text='Year')
#position day month year labels inside of dateFrame
dayLabel.grid(row=0, column=0, sticky='w')
monthLabel.grid(row=0, column=1, sticky='w')
yearLabel.grid(row=0, column=2, sticky='w')

#date spinners added to dateFrame 
daySpin = tkinter.Spinbox(dateFrame, width=5, from_=1, to=31)
monthSpin = tkinter.Spinbox(dateFrame, width=5, from_=1, to=12)
yearSpin = tkinter.Spinbox(dateFrame, width=5, from_=2000, to=2099)
#position day month year Spinbox inside dateFrame
daySpin.grid(row=1, column=0)
monthSpin.grid(row=1, column=1)
yearSpin.grid(row=1, column=2)


mainWindow.mainloop()

#retrieving radio button selected and printing out to console
print(rbValue.get()) #NOTE THIS IS DONE OUT SIDE OF mineWindow,mainloop()





