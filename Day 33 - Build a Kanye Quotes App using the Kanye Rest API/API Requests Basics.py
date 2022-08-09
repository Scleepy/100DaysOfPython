import requests

url = "http://api.open-notify.org/iss-now.json"

response = requests.get(url) #requests.get(url="some url")
response.raise_for_status() #Returns exception if error occurs

data = response.json() 
print(data)

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)

print(iss_position)
