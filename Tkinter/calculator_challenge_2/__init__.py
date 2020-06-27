#Calculator_2  
#This is my second attempt at building a calculator using for loop

try:
    import tkinter
except ImportError:
    import TKinter as tkinter
    
mainWindow = tkinter.Tk()

mainWindow.geometry('300x375-1200-850')
mainWindow.title("Calculator")

mainWindow.minsize('200', '250')

mainWindow['padx'] = 2

#result_box added
result_box = tkinter.Entry(mainWindow)
result_box.grid(row=0, column=0, columnspan=4)

#list of text for buttons on key pad
button_list = [['C','CE'],
               ['7', '8', '9', '+'],
               ['4', '5', '6', '-'],
               ['1', '2', '3', '*'],
               ['0', '=', '/']]

#iterate over buttons_list 0 to 4 (note result box is first starting at 0)         
for row in range(len(button_list)):
    print(f"row:{row}") #this show rows
    #iterate over each column in each row
    for col in range(len(button_list[row])):
        #create buttons addeing text from button_list
        buttons = tkinter.Button(mainWindow, text=button_list[row][col])
        print(f"row:{row}, col:{col}") #this shows rows and column
        #set each buttons position (added 1 to row to account for result_box!)
        buttons.grid(row=row+1, column=col, sticky='ew')
      
                
                        
mainWindow.mainloop()
                             

