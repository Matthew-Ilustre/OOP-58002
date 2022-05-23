from tkinter import *

window = Tk()
window.title("Find the Smallest Number")
window.geometry("450x200")

def findLeast():
 S= []
 S.append(eval(conOfent2.get()))
 S.append(eval(conOfent3.get()))
 S.append(eval(conOfent4.get()))
 conOfLeast.set(min(S))


lbl1 = Label(window, text = "SMALLEST NUMBER IDENTIFIER", font='BOLD',bg = 'white')
lbl1.grid(row=0, column=1, columnspan=2,sticky=EW)


lbl2 = Label(window,text = "Enter the first number:", font='TimesNewRoman',bg = 'white')
lbl2.grid(row=1, column = 0,sticky=W)
conOfent2 = StringVar()


ent2 = Entry(window,bd=3,textvariable=conOfent2)
ent2.grid(row=1, column = 1)


lbl3 = Label(window,text = "Enter the second number:", font='TimesNewRoman',bg = 'white')
lbl3.grid(row=2, column=0)
conOfent3=StringVar()


ent3 = Entry(window,bd=3,textvariable=conOfent3)
ent3.grid(row=2,column=1)


lbl4 = Label(window,text="Enter the third number:", font='TimesNewRoman',bg = 'white')
lbl4.grid(row=3,column =0, sticky=W)
conOfent4 = StringVar()


ent4 = Entry(window,bd=3,textvariable=conOfent4)
ent4.grid(row=3, column=1)


btn1 = Button(window,text = "Find the Least number",command=findLeast , font='TimesNewRoman',bg = 'white')
btn1.grid(row=4, column = 1)


lbl5 = Label(window,text="The Least number:", font='TimesNewRoman',bg = 'white')
lbl5.grid(row=5,column=0,sticky=W)
conOfLeast = StringVar()


ent5 = Entry(window,bd=3,state="readonly",textvariable=conOfLeast, font='TimesNewRoman',bg = 'white')
ent5.grid(row=5,column=1)

mainloop()
