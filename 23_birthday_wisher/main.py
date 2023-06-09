##################### Extra Hard Starting Project ######################
import random

# 1. Update the birthdays.csv

import pandas as pd
from tkinter import *
import datetime as dt
import smtplib
MS_DAY = 5000

my_email = "samperimario75@gmail.com"
password = "I_M_NOT_SHARING_THIS"


def get_new_record():
    new_record = {'name': name_entry.get(),
                  'email': email_entry.get(),
                  'year': year_entry.get(),
                  'month': month_entry.get(),
                  'day': day_entry.get()}
    return new_record


def reset_fields():
    name_entry.delete(0, END)
    email_entry.delete(0, END)
    year_entry.delete(0, END)
    month_entry.delete(0, END)
    day_entry.delete(0, END)


def add_new_record():
    record = get_new_record()
    data = pd.read_csv("birthdays.csv")
    birth_dict = data.to_dict(orient="records")
    birth_dict.append(record)

    df = pd.DataFrame.from_dict(birth_dict)
    df.to_csv("birthdays.csv", index=False)
    reset_fields()


def send_email(record):
    merged_letter = ""
    random_letter = random.randint(1,3)
    with open(f"./letter_templates/letter_{random_letter}.txt") as file:
        letter = file.read()
        merged_letter = letter.replace("[NAME]", record['name'])

    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="mariosamperi75@outlook.it",
                        msg=f"Subject:Happy birthday\n\n{merged_letter}")
    connection.close()


def find_birthdays():
    now = dt.datetime.now()
    data = pd.read_csv("birthdays.csv")
    birth_dict = data.to_dict(orient="records")
    for record in birth_dict:
        a_date = dt.datetime(int(record['year']), int(record['month']), int(record['day']))
        if now.month == a_date.month and now.day == a_date.day:
            send_email(record)
            windows.after(1000, find_birthdays)


# interface
windows = Tk()
windows.title("Birthday Wisher")
windows.config(padx=50, pady=50)


name_label = Label(text="Name:")
name_label.grid(row=1, column=0)
name_entry = Entry(width=34)
name_entry.grid(row=1, column=1, columnspan=5)
name_entry.focus()

email_label = Label(text="Email")
email_label.grid(row=2, column=0)
email_entry = Entry(width=34)
email_entry.grid(row=2, column=1, columnspan=5)

day_label = Label(text="day")
day_label.grid(row=3, column=0)
day_entry = Entry(width=7)
day_entry.grid(row=3, column=1)

month_label = Label(text="month")
month_label.grid(row=3, column=2)
month_entry = Entry(width=7)
month_entry.grid(row=3, column=3)

year_label = Label(text="year")
year_label.grid(row=3, column=4)
year_entry = Entry(width=7)
year_entry.grid(row=3, column=5)


add_button = Button(text="Add", width=14, command=add_new_record)
add_button.grid(row=4, column=1, columnspan=6)

# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.
windows.after(MS_DAY, find_birthdays)

windows.mainloop()


# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


# Instructor's code

# from datetime import datetime
# import pandas
# import random
# import smtplib
#
# MY_EMAIL = "YOUR EMAIL"
# MY_PASSWORD = "YOUR PASSWORD"
#
# today = datetime.now()
# today_tuple = (today.month, today.day)
#
# data = pandas.read_csv("birthdays.csv")
# birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# if today_tuple in birthdays_dict:
#     birthday_person = birthdays_dict[today_tuple]
#     file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
#     with open(file_path) as letter_file:
#         contents = letter_file.read()
#         contents = contents.replace("[NAME]", birthday_person["name"])
#
#     with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
#         connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs=birthday_person["email"],
#             msg=f"Subject:Happy Birthday!\n\n{contents}"
#         )













