import requests
from twilio.rest import Client

endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "b36106f5dfc5b0ab3249578c216007ce"
account_sid = "AC0a738ad623d71c971e335453b765398c"
auth_token = "7ee2087c1c20224ff83d5f9989206445"


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
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body="Its going to rain today.",
            from_= "+13347817769",
            to=""
        )
        break
else:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Not gonna rain today.",
        from_="+13347817769",
        to = ""
    )

print(message.status)