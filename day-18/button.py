from tkinter import *

window = Tk()
window.geometry('1280x720')
window.title('Win GUI')
icon = PhotoImage(file='../day-17/icon.png')
window.iconphoto(True, icon)

def click():
    print('u are so cool')


button = Button(window, text='click me', command=click, image=icon)
button.pack()

window.mainloop()