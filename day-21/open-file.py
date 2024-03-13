from  tkinter import *
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename(title='open file for me', filetypes=[('text files','*.txt'), ('all', '*.*')])
    file = open(file_path, 'r')
    print(file.read())
    file.close()


window = Tk()

button = Button(window, text='open', command=open_file)
button.pack()

window.mainloop()