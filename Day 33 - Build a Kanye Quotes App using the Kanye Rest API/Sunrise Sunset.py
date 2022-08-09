import requests
from datetime import datetime

url = "http://api.sunrise-sunset.org/json"

params = {
    "lat":51.507351,
    "lng": -0.127758,
    "formatted": 0
}

response = requests.get(url, params) #requests.get(url="some url")
response.raise_for_status() #Returns exception if error occurs

json_data = response.json()

sunrise = json_data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = json_data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now = datetime.now()

print(time_now.hour)
