from tkinter import *
from bkarms import getInput

#my first classname
gi=getInput()
guiFrame = Tk()
guiFrame.title("myprogram")
guiFrame.geometry("500x450")
#place labels
label1 = Label(guiFrame, text="firstname")
label1.grid(row=0,column=0)
label2 = Label(guiFrame, text= "lastname"  )
label2.grid(row=1,column=0)
label3 =Label(guiFrame,text="Address")
label3.grid(row=2, column=0)
label4 =Label(guiFrame,text="Tel no")
label4.grid(row=3, column=0)
#label5 =Label(guiFrame,text="Gender")
#label5.grid(row=4, column=0)
#label6 =Label(guiFrame,text="Gender")
#label6.grid(row=5, column=0)
#label5 =Label(guiFrame,text="Gender")
#label5.grid(row=3, column=0)




#textbox
textbox1 =Entry(guiFrame)
textbox1.grid(row=0,column=1)

#textbox2 =Entry(guiFrame)
#textbox2.grid(row=1,column=1)

#textbox3 =Entry(guiFrame)
#textbox3.grid(row=3,column=3)
#button
Submitbtn = Button(guiFrame, text="clickhere",command=lambda: gi.gettingVales(textbox1.get()))
Submitbtn.grid(row=2,column=1) 
guiFrame.mainloop()



