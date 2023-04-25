from tkinter import *

def calculate():
    miles = float(miles_input.get())
    km_label_2.config(text=miles*1.60934)


windows = Tk()
windows.title("Miles to Km Converter")
windows.minsize(width=200, height=120)
windows.config(padx=50, pady=50)


miles_input = Entry(width=10)
miles_input.grid(row=0, column=1)

miles_label = Label(width=10, text="Miles")
miles_label.grid(row=0, column=2)

km_label_1 = Label(width=10, text="is equal to")
km_label_1.grid(row=1, column=0)

km_label_2 = Label(width=10)
km_label_2.grid(row=1, column=1)

km_label_3 = Label(width=10, text="Km")
km_label_3.grid(row=1, column=2)

calculate_btn = Button(text="Calculate", command=calculate)
calculate_btn.grid(row=2, column=1)









windows.mainloop()