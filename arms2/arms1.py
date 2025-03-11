from tkinter import *
from bkarms1 import getInput

#my first classname
gi=getInput()
guiFrame = Tk()
guiFrame.title("myprogram")
guiFrame.geometry("500x450")
#place labels
label1 = Label(guiFrame, text="Procedings for process")
label1.grid(row=0,column=0)
label2 = Label(guiFrame, text= "lastnaUnder this agrment of the user and the provider user need to agree folling\n terms to enhance itse service" ,wraplength=200 )
label2.grid(row=1,column=0)
label3 =Label(guiFrame,text="Address")
label3.grid(row=2,column=0)





#textbox
textbox1 =Entry(guiFrame)
textbox1.grid(row=0,column=1)
textbox2 =Entry(guiFrame)
textbox2.grid(row=1, column=1)


#button
Submitbtn = Button(guiFrame, text="clickhere",command=lambda: gi.gettingVales(textbox1.get(), textbox2.get()))

Submitbtn.grid(row=2,column=1) 
guiFrame.mainloop()




