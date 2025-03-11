from tkinter import *

mywin =Tk()
#label
mywin.geometry("350x350")
labelnum =Label(mywin, text="enter number")
labelnum.grid(row=0, column=0)

#textbox
textboxnum =Entry(mywin)
textboxnum.grid(row=0,column=1)

submitBtn= Button(mywin, text ="click hee" )
submitBtn.grid(row=1 ,column=1)
mywin.mainloop()