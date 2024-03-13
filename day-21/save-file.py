from  tkinter import *
from tkinter import filedialog

def save_file():
    file = filedialog.asksaveasfile(title='open file for me',
                                    defaultextension='.txt',
                                    filetypes=[('text file', '.txt'), ('html file', '.html'), ('all files', '.*')])
    file_text = str(text.get(1.0, END))
    file.write(file_text)
    file.close()

window = Tk()


text = Text(window)
text.pack()
button = Button(window, text='save', command=save_file)
button.pack()

window.mainloop()