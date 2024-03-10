from tkinter import *

window = Tk()

x = IntVar()

def display():
    if x.get() == 1:
        print('agree')
    else:
        print('disagree')

check_btn = Checkbutton(window,
                        text='i agree to smth',
                        font=('Arial', 20),
                        variable=x,
                        onvalue=1,
                        offvalue=0,
                        command=display,
                        fg='#00ff00',
                        bg='#000000',
                        activeforeground='#00ff00',
                        activebackground='#000000',
                        padx=20,
                        pady=10)
check_btn.pack()



window.mainloop()


