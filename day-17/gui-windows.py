from tkinter import *

window = Tk()
window.geometry('1280x720')
window.title('Win GUI')

icon = PhotoImage(file='icon.png')

window.iconphoto(True, icon)
window.config(background='#404040')

window.mainloop()