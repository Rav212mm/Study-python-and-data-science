from tkinter import *
import backend

window = Tk()
window.title("Library master")

def dzialaj():
    print('Przycisk działa !')

l1 = Label(window, text='Title', width=7)
l1.grid(row=0, column=0)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value, width=15)
e1.grid(row=0, column=1)

l2 = Label(window, text='Author', width=7)
#l2.pack(side='right') inna metoda od grid
l2.grid(row=0, column=2)

e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value, width=15)
e2.grid(row=0, column=3)

l3 = Label(window, text='Year', width=7)
l3.grid(row=1, column=0)

e3_value = StringVar()
e3 = Entry(window, textvariable=e3_value, width=15)
e3.grid(row=1, column=1)

l4 = Label(window, text='ISBN', width=7)
l4.grid(row=1, column=2)

e4_value = StringVar()
e4 = Entry(window, textvariable=e4_value, width=15)
e4.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1 = Button(window, text='View all', width =12, command = dzialaj)
b1.grid(row=2, column=3)

b2 = Button(window, text='Search entry', width=12, command=print('View all working'))
b2.grid(row=3, column=3)

b3 = Button(window, text='Add entry', width=12, command=print('View all working'))
b3.grid(row=4, column=3)

b4 = Button(window, text='Update selected', width=12, command=print('View all working'))
b4.grid(row=5, column=3)

b5 = Button(window, text='Delete selected', width=12, command=print('View all working'))
b5.grid(row=6, column=3)

b6 = Button(window, text='Close', width=12, command=print('View all working'))
b6.grid(row=7, column=3)

window.mainloop()
