import requests

pixela_endpoint = "https://pixe.la/v1/users"
token = "ajnj24j453n3jkgöhöl64"
username = "mario"
graph_id = "graph1"
pixel_create_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}"

user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Cycling",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}
# response = requests.post(url=graph_endpoint, json=graph_config)

pixel_data = {}

