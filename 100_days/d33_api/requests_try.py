import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response.status_code)
# print(response.json())

# if response.status_code != 200:
#     raise Exception("Bad request from ISS API.")

# if response.status_code == 404:
#     raise Exception("That resource doesn't exist")
# elif response.status_code == 401:
#     raise Exception("You do not have permission to access this resource")

response.raise_for_status()

# data = response.json()["iss_position"]
# data = response.json()["iss_position"]["longitude"]

data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position)