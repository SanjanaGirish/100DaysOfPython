import requests
from datetime import datetime

PIXELA_END_POINT = "https://pixe.la/v1/users"
USERNAME = "* ENTER USENAME *"
TOKEN = "* ENTER RANDOM COMBINATION OF LETTERS *"
GRAPH_ID = "graph1"

pixela_parameters = {"token": TOKEN,
                     "username": USERNAME,
                     "agreeTermsOfService": "yes",
                     "notMinor": "yes"}
# response = requests.post(url=PIXELA_END_POINT, json=pixela_parameters)

GRAPH_ENDPOINT = f"{PIXELA_END_POINT}/{USERNAME}/graphs"
graph_params = {"id": GRAPH_ID,
                "name": "Study Graph",
                "unit": "hours",
                "type": "float",
                "color": "ajisai"}
# headers = {"X-USER-TOKEN": TOKEN}
# response = requests.post(url=GRAPH_ENDPOINT, json=graph_params,
# headers=headers)

today = datetime.now()

# POST A PIXEL
pixel_endpoint = f"{PIXELA_END_POINT}/{USERNAME}/graphs/graph1"
pixel_params = {"date": today.strftime("%Y%m%d"),
                "quantity": "3"}
headers = {"X-USER-TOKEN": TOKEN}
response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)

# UPDATE A PIXEL
# today = datetime(year=2021, month=7, day=29)
# date = today.strftime("%Y%m%d")
# pixel_endpoint = f"{PIXELA_END_POINT}/{USERNAME}/graphs/graph1/{date}"
# pixel_params = {"quantity": "1"}
# headers = {"X-USER-TOKEN": TOKEN}
# response = requests.put(url=pixel_endpoint, json=pixel_params, headers=headers)
# print(response.text)

# DELETE A PIXEL
# today = datetime(year=2021, month=7, day=29)
# date = today.strftime("%Y%m%d")
# pixel_endpoint = f"{PIXELA_END_POINT}/{USERNAME}/graphs/graph1/{date}"
# pixel_params = {"quantity": "1"}
# headers = {"X-USER-TOKEN": TOKEN}
# response = requests.delete(url=pixel_endpoint, headers=headers)
# print(response.text)
