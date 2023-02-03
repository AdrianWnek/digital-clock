from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title('My Clock')

def time():
    string = strftime('%H:%M:%S %p\n   %x')
    lbl.config(text=string)
    lbl.after(1000, time)

lbl = Label(root, font=('calibr', 100, 'bold'),
                background='black',
                foreground='green')

lbl.pack(anchor='center')
time()

mainloop()