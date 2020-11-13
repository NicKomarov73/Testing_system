from tkinter import *

# creating window
window = Tk()
window.title("Test")
window.geometry('300x390')
window.resizable(False, False)

# creating  menu frame
menu_fr = Frame(window, bg='#3E4048')
menu_fr.pack(fill=BOTH, expand=1)

# add buttons to menu frame
start_btn = Button(menu_fr, bg = 'black', text = 'Start', fg = 'white')
start_btn.pack(expand = 1)

window.mainloop()
