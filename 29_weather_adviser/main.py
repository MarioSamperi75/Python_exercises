import requests as requests

#LATITUDE = 18.193813
#LONGITUDE = 15.554015
API_KEY = "69f04e4613056b159c2761a9d9e664d2"

weather_params = {
    "lat": 71.193813,
    "lon": 15.554015,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}


#url = f"https://api.openweathermap.org/data/2.5/onecall?lat={LATITUDE}&lon={LONGITUDE}&appid={API_KEY}"
url = "https://api.openweathermap.org/data/2.5/onecall"

response = requests.get(url=url, params=weather_params)
response.raise_for_status()
weather_data = response.json()

for i in range(12):
    condition_code = weather_data['hourly'][i]['weather'][0]['id']

    if condition_code < 700:
        print("Prendi l'ombrello")
        break





