from tkinter import *

homeno3 =Tk()
homeno3.geometry("250x250")
#label
labelName= Label(homeno3,text="enter name")
labelName.grid(row=0,column=0)
#textbox
textName=Entry(homeno3)
textName.grid(row=0,column=1)


homeno3.mainloop()