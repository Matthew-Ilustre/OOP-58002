from tkinter import *
from tkinter import ttk

from tkinter import *

from tkinter import ttk

win = Tk()
win.geometry("500x200+10+20")
win.title("Midterm in OOP")

lbl1 = Label(win, text="Enter your fullname: ", fg="red", font=("times new roman", 14))
lbl1.place(x=50, y=50)

name = Entry(win, font=("times new roman", 12), bd=5)
name.place(x=250, y=50)

btn = Button(win, text="Click to display your Fullname", fg="red", bg="white", font=("times new roman", 10))
btn.place(x=50, y=100)

lbl2 = Label(win,text= name, fg="red", font=("times new roman", 14))
lbl2.place(x=250, y=100)

win.mainloop()