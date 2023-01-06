import requests

pixela_endpoint = "https://pixe.la/v1/users"
token = ""
username = "mario"
user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
response = requests.post()(url=pixela_endpoint, json=user_params)
print(response.text)

