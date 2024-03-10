from tkinter import *


def show():
    print(scale.get())

window = Tk()

scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL,
              font=('Arial', 20),
              tickinterval=10,
              troughcolor='#00ff00',
              showvalue=False,
              resolution=5,
              fg='#00ff00',
              bg='#000000')
scale.pack()

button = Button(window, text='submit', command=show)
button.pack()

window.mainloop()