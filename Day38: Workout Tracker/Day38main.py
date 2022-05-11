import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth
import os

APP_ID = os.environ["NT_APP_ID"]
API_KEY = os.environ["NT_API_KEY"]
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = os.environ["SHEET_ENDPOINT"]
SHEETY_USERNAME = os.environ['SHEET_USER']
SHEETY_PWD = os.environ['SHEET_PWD']

# Getting Today's info
today = datetime.now()
formatted_date = today.strftime("%d/%m/%Y")
formatted_time = today.strftime("%H:%M:%S")

# Setting Up Nutritionix API
user_input = input("Tell me which exercises you did: ")
exercise_parameters = {"query": user_input,
                       "gender": "female",
                       "weight_kg": 56.6,
                       "height_cm": 160,
                       "age": 19}
header = {"x-app-id": APP_ID,
          "x-app-key": API_KEY,
          "Content-Type": "application/json"}
response = requests.post(url=EXERCISE_ENDPOINT, json=exercise_parameters,
                         headers=header)
exercise_output = response.json()

# Interpreting Nutritionix Data
for exercise in exercise_output['exercises']:
    exercise_name = exercise['name'].title()
    exercise_mins = exercise['duration_min']
    exercise_cals = exercise['nf_calories']

    # Using Sheety to update Google Document
    sheety_params = {
        "workout": {
            "date": formatted_date,
            "time": formatted_time,
            "exercise": exercise_name,
            "duration": exercise_mins,
            "calories": exercise_cals
        }
    }
    final_response = requests.post(url=SHEETY_ENDPOINT, json=sheety_params,
                                   auth=HTTPBasicAuth(SHEETY_USERNAME,
                                                      SHEETY_PWD))
    print(final_response.text)


