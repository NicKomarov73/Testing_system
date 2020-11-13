from tkinter import *

global open_fr
open_fr = TRUE

# creating window
window = Tk()
window.title("Test")
window.geometry('300x390')
window.resizable(False, False)

# some funcions
def com1():
    fr.pack_forget()

def com2():
    fr.pack(side=TOP)

# creating buttons
btn = Button(window, text='Close', command=com1)
btn.pack(side=TOP)
btn2 = Button(window, text='OpenUp', command=com2)
btn2.pack(side=RIGHT)

# creating frame
fr = Frame(window, bg='red', bd=5)
btn_fr1 = Button(fr, text='l', width=5, height=2)
btn_fr2 = Button(fr, text='o', width=5, height=2)
btn_fr3 = Button(fr, text='l', width=5, height=2)
btn_fr1.pack()
btn_fr2.pack()
btn_fr3.pack()
fr.pack(side=TOP)

window.mainloop()
