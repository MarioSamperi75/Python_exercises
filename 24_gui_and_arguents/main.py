import tkinter

windows = tkinter.Tk()
windows.title("Mi first GUI program")
windows.minsize(width=800, height=600)

# label
my_label = tkinter.Label(text="I am a label", font=("Garamond", 24, "bold"))
my_label.pack()
my_label['text'] = "New Text"
my_label
my_label.config(text='New Text2', background='yellow')
# more commands? check https://tcl.tk/man/tcl8.6/TkCmd/label.htm












windows.mainloop()