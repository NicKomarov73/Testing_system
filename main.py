from tkinter import *

que_list = [
    "какойто первый вопрос",
    "какойто второй вопрос",
    "какойто третий вопрос"
]

def back(task_num):
    global que_label
    global btn_back
    global btn_next
    global btn_fin_test

    if task_num + 2 != len(que_list):
        btn_fin_test.pack_forget()

    que_label.config(text = que_list[task_num-1])
    btn_back = Button(task_fr, text='back', command=lambda: back(task_num - 1))
    btn_next = Button(task_fr, text='next', command=lambda: forward(task_num - 1))

    btn_back.place(relx=.1, rely=.9)
    btn_next.place(relx=.9, rely=.9)

    if task_num - 1 == 0:
        btn_back.config(state=DISABLED)

    return

def forward(task_num):
    global que_label
    global btn_back
    global btn_next
    global btn_fin_test

    que_label.config(text=que_list[task_num + 1])
    btn_back = Button(task_fr, text='back', command=lambda: back(task_num + 1))
    btn_next = Button(task_fr, text='next', command=lambda: forward(task_num + 1))

    if task_num + 2 == len(que_list):
        btn_next.config(state=DISABLED)
        btn_fin_test.pack(side=RIGHT )

    btn_back.place(relx=.1, rely=.9)
    btn_next.place(relx=.9, rely=.9)

    return

def to_test():
    main_fr.pack_forget()
    task_fr.pack(fill = BOTH, expand = 1)



# -------------creating window------------------
window = Tk()
window.title("Testing system")
window.geometry('700x900')
window.resizable(False, False)


# -------------creating start menu------------------
main_fr = Frame(window, bg='grey')
main_fr.pack(fill = BOTH, expand = 1)

# creating buttons on start menu
st_btn = Button(main_fr, text='Start', bg='blue', fg='white', width=15, height=3, command = to_test)
st_btn.pack(anchor = CENTER)

sett_btn = Button(main_fr, text='Settings', bg='blue', fg='white', width=15, height=3)
sett_btn.pack()

info_btn = Button(main_fr, text='Info', bg='blue', fg='white', width=15, height=3)
info_btn.pack()

exit_btn = Button(main_fr, text='Exit', bg='blue', fg='white', width=15, height=3,  command=window.quit)
exit_btn.pack()


# -------------creating tasks frame------------------
task_fr = Frame(window, bg = 'grey')

que_label = Label(task_fr, text=que_list[0], justify = CENTER)
que_label.pack(side=TOP, pady=10, padx=14, fill='x')

btn_back = Button(task_fr, text='back', state = DISABLED, command = lambda: back(0))
btn_next = Button(task_fr, text='next', command = lambda: forward(0))
btn_fin_test = Button(task_fr, text='Finish test')

btn_back.place(relx=.1, rely=.9)
btn_next.place(relx=.9, rely=.9)

window.mainloop()