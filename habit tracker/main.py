from datetime import datetime

import requests

PIXELA_ENDPOINT = "https://pixe.la//v1/users"
USERNAME = "yourNameHere"
TOKEN = "youTokenHere"
user_parameters = {
    "token": TOKEN,  # you can write anything between 8-128 chars
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# send post request
# response = requests.post(url=PIXELA_ENDPOINT, json=user_parameters)
# print(response.text)
"""
    After creating an account. We can commit out account post request code.
"""

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
headers = {
    "X-USER-TOKEN": TOKEN
}
GRAPH_ID = "booktracker5"
date = datetime.now()
today = str(date.year)+str(date.month)+str(date.day)

user_graph_parameters = {
    "id": GRAPH_ID,
    "name": "reading tracker",
    "unit": "pages",
    "type": "int",
    "color": "sora"
}
# response = requests.post(url=GRAPH_ENDPOINT, json=user_graph_parameters, headers=headers)
# print(response)
"""
    Once you create graph you can comment out request part.
"""


# posting a pixel
PIXEL_POSTING_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"
pixel_post_parameters = {
    "date": today,
    "quantity": "20"
}

# send post request to store
# response_pixel_post = requests.post(url=PIXEL_POSTING_ENDPOINT, json=pixel_post_parameters, headers=headers)
# print(response_pixel_post)


# update pixel
date_to_update = "20231217"
UPDATE_PIXEL_ENDPOINT = f"{PIXEL_POSTING_ENDPOINT}/{date_to_update}"
update_pixel_parameters = {
    "quantity": "24"
}

# response_update_pixel = requests.put(url=UPDATE_PIXEL_ENDPOINT, json=update_pixel_parameters, headers=headers)
# print(response_update_pixel)


# delete a pixel
date_to_delete = "20231218"
DELETE_PIXEL_ENDPOINT = f"{PIXEL_POSTING_ENDPOINT}/{date_to_delete}"
response_delete_pixel = requests.delete(url=DELETE_PIXEL_ENDPOINT, headers=headers)
print(response_delete_pixel.text)
