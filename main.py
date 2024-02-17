import requests
from datetime import datetime


current_date = datetime.now()
current_date_formatted = current_date.strftime("%Y%m%d")

TOKEN = "Enter your pixela account token here"
USERNAME = "Enter your pixela account username here"

graph_id = "Enter the id of your graph here"
pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}"
update_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}/{current_date_formatted}"

headers = {
    "X-USER-TOKEN": TOKEN
}
user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_config = {
    "id": graph_id,
    "name": "Coding Time Graph",
    "unit": "h",
    "type": "float",
    "color": "sora"
}

post_config = {
    "date": current_date_formatted,
    "quantity": "3.0"
}

change_config = {
    "quantity": "5.5"
}

# Creating a pixela account:
account_response = requests.post(url=pixela_endpoint, json=user_parameters)
print(account_response.text)

# Creating our own graph (go to https://pixe.la/v1/<username>/a-know/graphs/<graphID> to see the graph after creation:
graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(graph_response.text)

# Posting value to your graph:
value_response = requests.post(url=post_endpoint, json=post_config, headers=headers)
print(value_response.text)

# Changing an existing value on your graph:
change_response = requests.put(url=update_delete_endpoint, json=change_config, headers=headers)
print(change_response.text)

# To delete an existing value on your graph:
delete_response = requests.delete(url=update_delete_endpoint, headers=headers)
print(delete_response.text)
