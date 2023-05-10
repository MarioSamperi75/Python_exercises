import smtplib

my_email = "samperimario75@gmail.com"
password = "nothing_to_share"
# Hotmail: smtp.live.com
# Yahoo: smtp.mail.yahoo.com

connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="mariosamperi75@outlook.it", msg="Subject:Hello\n\nThis is the body of the email")
connection.close()




