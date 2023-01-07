from datetime import datetime

import requests

pixela_endpoint = "https://pixe.la/v1/users"
token = "felianfilian"
username = "darian63"
graph_id = "graph1"
pixel_create_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}"

user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

headers = {
    "X-USER-TOKEN": token
}

response = requests.post(url=pixela_endpoint, json=user_params, headers=headers)

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Cycling",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)


today = datetime(year=2022, month=7, day=23)
actual_date = today.strftime("%Y%m%d")

pixel_data = {
    "date": actual_date,
    "quantity": "10",
}

response = requests.post(url=pixel_create_endpoint, json=pixel_data, headers=headers)

print(response.text)
