from tkinter import  *
from  tkinter import messagebox

answer = ''

def click():
    # messagebox.showinfo(title='info box', message='u call a box')
    # messagebox.showwarning(title='warning', message='u have a virus')
    # messagebox.showerror(title='error', message=':(')
    # if  messagebox.askokcancel(title='ok or cancel', message='do u want?'):
    #     print(True)
    # else:
    #     print(False)
    # messagebox.askyesno()
    # messagebox.askretrycancel()
    # answer = messagebox.askquestion(title='hi', message='do u like pies?')
    # print(answer)
    messagebox.askyesnocancel()

window = Tk()

button = Button(window, text='call', command=click)
button.pack()


window.mainloop()