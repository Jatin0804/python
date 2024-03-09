import requests

endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "b36106f5dfc5b0ab3249578c216007ce"

weather_params = {
    "lat": 28.380211,
    "lon": 75.609169,
    "appid": api_key
}

response = requests.get(endpoint, params=weather_params)
# print(response.status_code)
# if 401, api not valid
# if 200, valid

# to get actual result
print(response.json())