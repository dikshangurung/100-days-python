import requests
from datetime import datetime
pixela_endpoint = "https://pixe.la/v1/users"
Token = "a1a2a3e21e12e12"
User = "dikshan"
Graph_Id = "code"
user_params = {
    "token": Token,
    "username": User,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.request("Post",url=pixela_endpoint,json=user_params)
# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)
graph_endpoint = f"{pixela_endpoint}/{User}/graphs"
graph_config = {
    "id": Graph_Id,
    "name": "Coding",
    "unit": "hrs",
    "type": "float",
    "color": "ajisai"
}
headers={
    "X-USER-TOKEN": Token
}
current_day = datetime.now()

# response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)
pixel_endpoint = f"{pixela_endpoint}/{User}/graphs/{Graph_Id}"
pixel_config = {
    "date": current_day.strftime("%Y%m%d"),
    "quantity": "3.2",
}
# response = requests.post(url=pixel_endpoint,json=pixel_config,headers=headers)
# print(response.text)
#Updating hai guys

update_endpoint = f"{pixela_endpoint}/{User}/graphs/{Graph_Id}/{'20230113'}"
new_pixel_data = {
    "quantity": "2.1",
}
# response = requests.put(url=update_endpoint,json=new_pixel_data,headers=headers)
# print(response.text)
#delete hai ta

delete_endpoint = f"{pixela_endpoint}/{User}/graphs/{Graph_Id}/{'20230113'}"
response = requests.delete(url=delete_endpoint,headers=headers)
print(response.status_code)