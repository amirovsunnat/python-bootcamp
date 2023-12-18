from datetime import datetime

import requests

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access your variables
app_id = os.getenv("APP_ID")
api_key = os.getenv("API_KEY")
auth_token = os.getenv("AUTH_TOKEN")


API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id": app_id,
    "x-app-key": api_key
}
GENDER = "male"
WEIGHT_KG = 60
HEIGHT_CM = 173
AGE = 19

sentence = input("Tell me which exercise you did? ")
parameters = {
    "query": sentence,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=API_ENDPOINT, json=parameters, headers=headers)
response.raise_for_status()
data = response.json()
print(response.json())

# set up sheety api
SHEETY_ENDPOINT = "https://api.sheety.co/d78a84bb057cdba2d3da100fb0de03f5/workoutTracking/workouts"
workout_parameters = {
    "workout": data
}

sheety_headers = {
    "Authorization": auth_token
}

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=SHEETY_ENDPOINT, json=sheet_inputs, headers=sheety_headers)

    print(sheet_response.text)
