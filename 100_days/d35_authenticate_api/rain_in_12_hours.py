import requests

endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "b36106f5dfc5b0ab3249578c216007ce"

weather_params = {
    "lat": 28.380211,
    "lon": 75.609169,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(endpoint, params=weather_params)
response.raise_for_status()

weather_data = response.json()
# print(weather_data)

weathers = weather_data["list"]
for i in weathers:
    ids = i["weather"][0]["id"]
    if ids < 700:
        print("Bring the Umbrella")
        break
else:
    print("No need, NO rain in 12 hours")