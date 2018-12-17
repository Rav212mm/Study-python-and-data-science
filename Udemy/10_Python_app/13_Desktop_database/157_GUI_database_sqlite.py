from tkinter import *

window = Tk()

l1 = Label(window, text='Title', width=7)
#l1.pack(side='right')
l1.grid(row=0, column=1)

t1 = Text(window, height=1, width=15)
t1.grid(row=0, column=2)

l2 = Label(window, text='Author', width=7)
#l2.pack(side='right')
l2.grid(row=0, column=3)

t2 = Text(window, height=1, width=15)
t2.grid(row=0, column=4)

l3 = Label(window, text='Year', width=7)
#l3.pack(side='right')
l3.grid(row=1, column=1)

t3 = Text(window, height=1, width=15)
t3.grid(row=1, column=2)

l4 = Label(window, text='ISBN', width=7)
#l4.pack(side='right')
l4.grid(row=1, column=3)

t4 = Text(window, height=1, width=15)
t4.grid(row=1, column=4)

t4 = Text(window, height=6, width=35)
t4.grid(row=2, column=1)

window.mainloop()
