import requests
from datetime import datetime
import os
USER_NAME = os.environ.get("USER_NAME")
PASSWORD = "okthisismypass123"
TOKEN = os.environ.get("Exercise_Token")
API_ID = "0be66d41"
API_KEY = "8b17ebce1afddd4a8d908d79aef92d40"
API_REMOTE_USER_ID = "0"
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
today_date = datetime.now().strftime("%Y/%m/%d")
now_time = datetime.now().strftime("%H:%M:%S")
# QUERY = input("What did you do today?: ")
# #sheety
# sheety_endpoint = "https://api.sheety.co/99febf72650bbd94b8342f71bd296feb/workouts/sheet1"
# headers = {
#     "x-app-id": API_ID,
#     "x-app-key": API_KEY
# }
# params = {
#     "query": QUERY,
#     "gender": "male",
#     "weight_kg": 64,
#     "height_cm": 165,
#     "age": 21
# }
# response = requests.post(url=exercise_endpoint,headers=headers,json=params)
# exercise_output = response.json()["exercises"]
#
#
# for result in exercise_output:
#     exercise = result["name"]
#     duration = result["duration_min"]
#     calorie = result["nf_calories"]
#     sheety_body = {
#         'sheet1': {
#             'date': today_date,
#             'time': now_time,
#             'exercise': exercise,
#             'duration': duration,
#             'calories': calorie
#         }
#     }
    # response_exercise = requests.post(url=sheety_endpoint, json=sheety_body)
    # With basic Authentication
    # response_exercise = requests.post(url=sheety_endpoint, json=sheety_body,auth=(USER_NAME,PASSWORD))
    # With Bearer Token Authentication
#     head = {
#         "Authorization": f"Bearer {TOKEN}"
#     }
#     response_exercise = requests.post(url=sheety_endpoint, json=sheety_body,headers=head)
#     print(response_exercise.json())
# #
# sheety_body = {
#     'sheet1': {
#         'date': today_date,
#         'time': now_time,
#         'exercise': 'Bycicle',
#         'duration': "25",
#         'calories': "120"
#     }
# }
# response = requests.post(url=sheety_endpoint,json=sheety_body)
# print(response.status_code)
# print(response.json())

