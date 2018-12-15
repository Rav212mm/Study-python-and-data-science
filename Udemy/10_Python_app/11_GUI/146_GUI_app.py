from tkinter import *

window = Tk()

def km_to_miles():
    grams = round((int(e1_value.get()) * 1000),2)
    t1.delete("1.0", END)
    t1.insert(END, grams)
    pounds = round((int(e1_value.get()) * 2.20462),2)
    t2.delete("1.0", END)
    t2.insert(END, pounds)
    ounces = round((int(e1_value.get()) * 35.274), 2)
    t3.delete("1.0", END)
    t3.insert(END, ounces)

l1 = Label(window, text = 'kg', )
l1.pack(side='bottom')
l1.grid(row=0, column=0)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value, width=10)
e1.grid(row=0, column=1)

b1=Button(window, text = 'Convert', command=km_to_miles)
b1.grid(row =0, column =2)

t1 = Text(window, height=1, width=7)
t1.grid(row=1, column=0)

t2 = Text(window, height=1, width=7)
t2.grid(row=1, column=1)

t3 = Text(window, height=1, width=7)
t3.grid(row=1, column=2)

window.mainloop()
