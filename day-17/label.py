from tkinter import *

window = Tk()
window.geometry('1280x720')
window.title('Win GUI')
icon = PhotoImage(file='icon.png')
window.iconphoto(True, icon)

label = Label(window,
              text='Hello!!!',
              font=('Arial', 36, 'bold'),
              fg='#404040',
              relief=RAISED,
              bd=5,
              image=icon,
              compound='bottom')

label.pack()
#label.place(x=0, y=0)
window.mainloop()