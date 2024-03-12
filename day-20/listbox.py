from tkinter import  *

def submit():
    food = []
    for i in listbox.curselection():
        food.insert(i, listbox.get(i))
    print(food)
def add():
    listbox.insert(listbox.size(), entry.get())
    listbox.config(height=listbox.size())
    entry.delete(0, END)

def delete():
    for i in reversed(listbox.curselection()):
        listbox.delete(i)
    listbox.config(height=listbox.size())



window = Tk()

listbox = Listbox(window, bg='#f7ffde', font=('Constantia', 18), width=12, selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1, 'pizza')
listbox.insert(2, 'hotdog')
listbox.insert(3, 'garlic bread')
listbox.insert(4, 'soup')
listbox.insert(5, 'salad')

listbox.config(height=listbox.size())

entry = Entry(window)
entry.pack()

add_item = Button(window, text='add item', command=add)
add_item.pack()


submit_btn = Button(window, text='Submit', command=submit)
submit_btn.pack()

delete_btn = Button(window, text='delete', command=delete)
delete_btn.pack()

window.mainloop()