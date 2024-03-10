from tkinter import *

window = Tk()
window.title('Win GUI')
icon = PhotoImage(file='../day-17/icon.png')
window.iconphoto(True, icon)

def submit():
    username = entry.get()
    print('Hello ' + username)

def delete():
    entry.delete(0, END)

def backspace():
    entry.delete(len(entry.get()) - 1, END)


submit_button = Button(window, text='submit', command=submit, font=('Arial', 20))
submit_button.pack(side=RIGHT)
delete_button = Button(window, text='delete', command=delete, font=('Arial', 20))
delete_button.pack(side=RIGHT)
backspace_button = Button(window, text='back', command=backspace, font=('Arial', 20))
backspace_button.pack(side=RIGHT)

entry = Entry(window,
              font=('Arial', 20),
              show='*')
entry.pack()

window.mainloop()
