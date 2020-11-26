from tkinter import *

que_list = []
ans_list = []
correct_ans_list = []

def back(task_num):
    global que_label
    global btn_back
    global btn_next
    global btn_fin_test

    btn_next.pack_forget()
    btn_back.pack_forget()

    que_label.config(text = que_list[task_num-1])
    btn_back = Button(mini_menu_fr, text='back', command=lambda: back(task_num - 1))
    btn_next = Button(mini_menu_fr, text='next', command=lambda: forward(task_num - 1))

    btn_next.pack(side=RIGHT)
    btn_back.pack(side=RIGHT)

    if task_num - 1 == 0:
        btn_back.config(state=DISABLED)

    return

def forward(task_num):
    global que_label
    global btn_back
    global btn_next
    global btn_fin_test

    btn_next.pack_forget()
    btn_back.pack_forget()

    que_label.config(text=que_list[task_num + 1])
    btn_back = Button(mini_menu_fr, text='back', command=lambda: back(task_num + 1))
    btn_next = Button(mini_menu_fr, text='next', command=lambda: forward(task_num + 1))

    if task_num + 2 == len(que_list):
        btn_next.config(state=DISABLED)

    btn_next.pack(side=RIGHT)
    btn_back.pack(side=RIGHT)

    return

def to_test():
    main_fr.pack_forget()
    task_fr.pack(fill = BOTH, expand = 1)


# -------------read file------------------
test_lines = open("test/my_test.txt").readlines()

i = 0
while i < len(test_lines):
    question = test_lines[i]
    question = question[0:len(question)-4]
    que_list.append(question)

    while test_lines[i] != "(end)\n":
        i += 1
        answer = test_lines[i]

        if answer[len(answer)-4:] == "(+)\n":
            answer = answer[0:len(answer)-4]
            correct_ans_list.append(answer)
        else:
            answer = answer[0:len(answer) - 1]
        if answer != "(end)":
            ans_list.append(answer)
    i += 1

# -------------creating window------------------
window = Tk()
window.title("Testing system")
window.geometry('500x700')
window.update()
#window.resizable(False, False)


# -------------creating start menu------------------
main_fr = Frame(window, bg='grey')
main_fr.pack(expand = 1)

# creating buttons on start menu
st_btn = Button(main_fr, text='Start', bg='blue', fg='white', width=15, height=3, command = to_test)
st_btn.pack(expand=1, side=TOP)

sett_btn = Button(main_fr, text='Settings', bg='blue', fg='white', width=15, height=3)
sett_btn.pack(side=TOP)

info_btn = Button(main_fr, text='Info', bg='blue', fg='white', width=15, height=3)
info_btn.pack(side=TOP)

exit_btn = Button(main_fr, text='Exit', bg='blue', fg='white', width=15, height=3,  command=window.quit)
exit_btn.pack(side=TOP)


# -------------creating tasks frame------------------
task_fr = Frame(window, bg = 'grey')

quest_fr = Frame(task_fr)
quest_fr.pack(side=TOP, fill='x', padx = 10)
quest_fr.config(bg = 'black')

que_label = Message(quest_fr, text=que_list[0], justify = CENTER, width = window.winfo_width() - 20)
que_label.pack(side=TOP, pady=10, padx=14, fill='x')
que_label.bind("<Configure>", lambda e: que_label.configure(width=e.width-10))

ans_fr = Frame(task_fr)
ans_fr.pack(side=TOP, fill=BOTH, padx = 10, expand=1)
ans_fr.config(bg='red')

ans = Listbox(ans_fr)
ans.pack(expand=1)


mini_menu_fr = Frame(task_fr)
mini_menu_fr.pack(side=BOTTOM, fill='x', padx = 10)
mini_menu_fr.config(bg='black')

btn_back = Button(mini_menu_fr, text='back', state = DISABLED, command = lambda: back(0))
btn_next = Button(mini_menu_fr, text='next', command = lambda: forward(0))
btn_fin_test = Button(mini_menu_fr, text='Finish test')
btn_exit = Button(mini_menu_fr, text='Exit', command=window.quit)

btn_exit.pack(side=LEFT)
btn_fin_test.pack(side=LEFT)
btn_next.pack(side=RIGHT)
btn_back.pack(side=RIGHT)



window.mainloop()
