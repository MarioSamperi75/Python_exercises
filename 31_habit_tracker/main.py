import os
from dotenv import load_dotenv
import requests
load_dotenv()

TOKEN = os.getenv("TOKEN")
USERNAME = os.getenv("NOMEUTENTE")
pixela_endpoint = "https://pixe.la/v1/users"
graph_id = "graph1"


# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
#
# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)

# -------------------------------------------------------------------

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
# graph_config = {
#     "id": "graph1",
#     "name": "Python graph",
#     "unit": "min",
#     "type": "int",
#     "color": "ajisai"
# }
#
headers = {
    "X-USER-TOKEN": TOKEN
}
#
# response = requests.post(url=graph_endpoint, headers=headers, json=graph_config)

post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}"

post_pixel_config = {
    "date": "20230422",
    "quantity": "15",
}

response = requests.post(url=post_pixel_endpoint, headers=headers, json=post_pixel_config)


print(response.text)

