import datetime as dt
import random
import smtplib

my_email = "samperimario75@gmail.com"
password = "sorry_not_available"
# Hotmail: smtp.live.com
# Yahoo: smtp.mail.yahoo.com


def send_quote(quote):
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="mariosamperi75@outlook.it",
                        msg=f"Subject:Daily Quote\n\n{quote}")
    connection.close()


now = dt.datetime.now()
# year = now.year
# month = now.month
# day = now.day

day_of_week = now.weekday()
# print(day_of_week)

if day_of_week == 0:

    with open("quotes.txt", "r") as my_file:
        data = my_file.readlines()
        random_quote = random.choice(data)
        print(random_quote)
        send_quote(random_quote)
else:
    print("Sarà per un altro giorno")







