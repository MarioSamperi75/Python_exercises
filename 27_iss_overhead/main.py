import smtplib
import time

import requests
from datetime import datetime

MY_LAT = 59.329323 # Your latitude
MY_LONG = 18.068581 # Your longitude

MY_EMAIL = "samperimario75@gmail.com"
PASSWORD = "not_shared_sorry"


def is_iss_near():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    print(iss_latitude, iss_longitude)

    return abs(iss_latitude - MY_LAT) <= 5 and abs(iss_longitude - MY_LONG) <= 5

def is_dark():
    time_now = datetime.now()
    if time_now.hour < sunrise or time_now.hour > sunset:
        return True
    return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


while True:

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


    if is_iss_near() and is_dark():
        connection = smtplib.SMTP("smtp.gmail.com", port=587)
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="mariosamperi75@outlook.it",
                            msg=f"Subject:Prova APP\n\nLOOK UP!")
        connection.close()
    else:
        print("not visible yet")

    time.sleep(60)






#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.