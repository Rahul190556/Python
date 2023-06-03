from tkinter import *

window=Tk()    #This imports the tkinter module and creates an instance of the Tk class, which represents the main window of the application.
def km_to_mile():
    print(e1_value.get())
    miles=float(e1_value.get()) * 1.6
    t1.insert(END,miles)

b1=Button(window,text="Execute",command=km_to_mile)
#This creates a button widget (b1) with the text "Execute" and associates it with the km_to_mile function using the 
# command parameter. The button is then placed in the grid layout using the grid() method with the specified row and column.

b1.grid(row=0,column=0)

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
#This creates an entry widget (e1) to accept user input. The StringVar variable e1_value is associated 
# with it using the textvariable parameter. The entry widget is placed in the grid layout.
e1.grid(row=0,column=1)

t1=Text(window,height=1,width=50)
t1.grid(row=0,column=2)
window.mainloop()

#This starts the main event loop of the application, which listens for user actions and 
# responds accordingly. It keeps the application window open until it is manually closed.