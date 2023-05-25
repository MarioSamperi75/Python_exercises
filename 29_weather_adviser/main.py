# pip install python-dotenv
# Create file.env
# API_KEY=fhajdkhaklsjhlasfjh
# and so on
import os
from dotenv import load_dotenv

load_dotenv()

print(os.getenv("API_KEY"))
print(os.getenv("ACCOUNT_SID"))
print(os.getenv("AUTH_TOKEN"))

# --------------------------------------------------------------

import requests as requests
from twilio.http.http_client import TwilioHttpClient
from twilio.rest import Client

# TWILIO_TEL_NUM = "---"
# VALID_TEL_NUM = "000123456"  # to validate in twilio account
#
# weather_params = {
#     "lat": 71.193813,
#     "lon": 15.554015,
#     "appid": API_KEY,
#     "exclude": "current,minutely,daily"
# }
#
# # url = f"https://api.openweathermap.org/data/2.5/onecall?lat={LATITUDE}&lon={LONGITUDE}&appid={API_KEY}"
# url = "https://api.openweathermap.org/data/2.5/onecall"
#
# response = requests.get(url=url, params=weather_params)
# response.raise_for_status()
# weather_data = response.json()
#
# will_rain = False
# weather_12h = weather_data['hourly'][:12]
# for hour in weather_12h:
#     condition_code = hour['weather'][0]['id']
#     will_rain = True
#
# if will_rain:
#     proxy_client = TwilioHttpClient()
#     proxy_client.session.proxies = {'https': os.environ['https_proxy']}
#
#     client = Client(ACCOUNT_SID, AUTH_TOKEN, http_client=proxy_client)
#     message = client.messages \
#         .create(
#         body="It's going to rain today. Remember to bring an ☔️",
#         from_="YOUR TWILIO VIRTUAL NUMBER",
#         to="YOUR TWILIO VERIFIED REAL NUMBER"
#     )
#     print(message.status)
