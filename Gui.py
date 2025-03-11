from tkinter import *

guiFrame=Tk()
guiFrame.title("my first program")

guiFrame.geometry("400x400")
label_1 = Label(guiFrame,text="my first gi program!")
label_1.grid(row=0,column=0)
label_2 =Label(guiFrame, text= "my gui own")
label_2.grid(row=1,column=1)


guiFrame.mainloop()