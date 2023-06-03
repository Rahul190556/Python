from tkinter import *

window=Tk()
b1=Button(window,text="Execute")
# b1.pack()                   #we dont used pack to define postion of buttion
b1.grid(row=0,column=0)

e1=Entry(window)
e1.grid(row=0,column=1)

t1=Text(window,height=1,width=50)
t1.grid(row=0,column=2)
window.mainloop()

