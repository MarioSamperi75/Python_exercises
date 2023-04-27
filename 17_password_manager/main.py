from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    f = open("data.txt", "a")
    f.write(f"{website_entry.get()} | {username_entry.get()} | {password_entry.get()}\n")
    f.close()

    website_entry.delete(0, END)
    password_entry.delete(0, END)





# ---------------------------- UI SETUP ------------------------------- #
windows = Tk()
windows.title("Password Manager")
windows.config(padx=50, pady=50)

lock_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_entry = Entry(width=52)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)
username_entry = Entry(width=52)
username_entry.insert(0, "samperimario75@gmail.com")
username_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password")
password_label.grid(row=3, column=0)
password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)
password_btn = Button(text="Generate Password")
password_btn.grid(row=3, column=2)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2)







windows.mainloop()

