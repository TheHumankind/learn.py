from tkinter import *


def open_file():
    print('file opened')

def save_file():
    print('file saved')

def cut_file():
    print('file cuted')

def copy_file():
    print('file copied')

window = Tk()

menubar = Menu(window)
window.config(menu=menubar)


file_menu = Menu(menubar, tearoff=False, font=('MV Boli', 15))
menubar.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=quit)

edit_menu = Menu(menubar, tearoff=False)
menubar.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Copy', command=copy_file)
edit_menu.add_command(label='Cut', command=cut_file)
window.mainloop()