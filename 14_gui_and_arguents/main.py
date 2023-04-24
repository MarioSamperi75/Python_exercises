import tkinter

from tkinter import *

def try_button_listener():
    # print("listener works")
    # my_label['text'] = "Button got clicked"
    my_input = my_entry.get()
    my_label['text'] = my_input


windows = Tk()
windows.title("Mi first GUI program")
windows.minsize(width=80, height=60)
# windows.config(padx=100, pady=100)

# label
my_label = Label(text="I am a label", font=("Garamond", 24, "bold"))
my_label['text'] = "New Text"
my_label.config(text='New Text2', background='yellow')
# my_label.pack()
my_label.grid(row=0, column=0)
my_label.config(pady=50, padx=50)
# more commands? check https://tcl.tk/man/tcl8.6/TkCmd/label.htm

# button
my_button = Button(text="CLIKKA QUI", command=try_button_listener)
# my_button.pack()
# my_button.pack(side='left')
# my_button.place(x=300, y=300)
my_button.grid(row=1, column=1)

new_button = Button(text="Submit")
new_button.grid(row=0, column=2)

# entry
my_entry = Entry(width=10)
# my_entry.pack()
my_entry.grid(row=2, column=3)

windows.mainloop()
