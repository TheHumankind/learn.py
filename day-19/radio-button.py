from tkinter import *

window = Tk()
window.title('Win GUI')

food = ['pizza', 'hamburger', 'hotdog']
x = IntVar()

def order():
    if x.get() == 0:
        print('pizza')
    elif x.get() == 1:
        print('hamburger')
    else:
        print('hotdog')

for i in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[i],
                              variable=x,
                              value=i,
                              padx=25,
                              pady=25,
                              font=('Arial', 25),
                              compound='left',
                              indicatoron=True,
                              width=300,
                              command=order)
    radiobutton.pack(anchor=W)




window.mainloop()