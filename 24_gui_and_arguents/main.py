import tkinter

windows = tkinter.Tk()
windows.title("Mi first GUI program")
windows.minsize(width=800, height=600)

# label
my_label = tkinter.Label(text="I am a label", font=("Garamond", 24, "bold"))

my_label.pack()









windows.mainloop()