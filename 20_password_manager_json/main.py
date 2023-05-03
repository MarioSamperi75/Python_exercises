import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    random_letters = [random.choice(letters) for _ in range(nr_letters)]
    random_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    random_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = random_letters + random_numbers + random_symbols

    random.shuffle(password_list)

    random_password = "".join(password_list)
    pyperclip.copy(random_password)
    password_entry.insert(0, random_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website:
            {
                "email": username,
                "password": password
            }
    }

    is_valid = len(website) > 0 and len(username) > 0 and len(password) > 0
    # messagebox.showinfo(title="La Divina Commedia", message="Nel mezzo del cammin di nostra vita...")

    if not is_valid:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            data = new_data
        else:
            data.update(new_data)
        finally:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

            website_entry.delete(0, END)
            password_entry.delete(0, END)


def search():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website not in data:
            messagebox.showinfo(title="Error", message="No details for the website exists")
        else:
            email = data[website]["email"]
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f"email : {email}\npassword: {password}")


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
website_entry = Entry(width=34)
website_entry.grid(row=1, column=1)
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
password_btn = Button(text="Generate Password", command=generate_password)
password_btn.grid(row=3, column=2)

search_button = Button(text="Search", width=14, command=search)
search_button.grid(row=1, column=2)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2)

windows.mainloop()
