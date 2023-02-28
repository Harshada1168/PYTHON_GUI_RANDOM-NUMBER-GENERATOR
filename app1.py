#random number genration in python gui
from random import *
from tkinter import *
def random_generation():
    r=randint(1, 100)
    msg1=Label(App, text="Random Number generated is: ")
    msg1.pack()
    msg=Label(App, text=r)
    msg.pack()
App=Tk()
App.title("Random number generator")
App.geometry("250x250")
b=Button(App, text="Generate!", command=random_generation)
b.pack()
App.mainloop()

