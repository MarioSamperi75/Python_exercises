import tkinter

from tkinter import *

windows = Tk()
windows.title("Mi first GUI program")
windows.minsize(width=800, height=600)

# label
my_label = Label(text="I am a label", font=("Garamond", 24, "bold"))
my_label.pack()
my_label['text'] = "New Text"
my_label
my_label.config(text='New Text2', background='yellow')
# more commands? check https://tcl.tk/man/tcl8.6/TkCmd/label.htm


def try_button_listener():
    # print("listener works")
    # my_label['text'] = "Button got clicked"
    my_input = my_entry.get()
    my_label['text'] = my_input


my_button = Button(text="CLIKKA QUI", command=try_button_listener)
my_button.pack()

my_entry = Entry(width=10)
my_entry.pack()


windows.mainloop()
