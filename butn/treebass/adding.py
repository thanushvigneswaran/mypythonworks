from tkinter import *
#from gettingfile import getInput

#gi =getInput()
guiFrame = Tk()
guiFrame.title("mypro")
guiFrame.geometry("500x250")
#labels
label1 = Label(guiFrame,text ="firstname")
label1.grid(row=0 ,column=0)
label2 =Label(guiFrame,text ="lastname")
label2.grid(row=1, column=0)

textbox1 =Entry(guiFrame)
textbox1.grid(row=0, column=1)
textbox2 =

guiFrame.mainloop()