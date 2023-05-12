import requests
import datetime as dt

params = {
    "lat": 38.1937571,
    "lng": 15.5542082,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=params)
response.raise_for_status()
data = response.json()

print(data)
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

time_now = dt.datetime.now()
print(time_now.hour)


