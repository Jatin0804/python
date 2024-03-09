import requests
from datetime import datetime

APP_ID = "09f0f267"
API_KEY = "b0cca154a1ed374a58b7b82cfb7e79db"

GENDER = "male"
WEIGHT = 75
HEIGHT = 175
AGE = 20

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/7a88bb70db8698ac1500e01ba8dd047f/wokoutTry/sheet1"

text = input("What exercises you did : ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
# print(result)
print(f"Nutritionix API call: \n {result} \n")

today = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    print(sheet_response.json())