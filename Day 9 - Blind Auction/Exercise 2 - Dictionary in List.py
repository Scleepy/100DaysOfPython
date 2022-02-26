travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country, visits, cities):
    new_log = {}
    new_log["country"] = country
    new_log["visits"] = visits
    new_log["cities"] = cities
    travel_log.append(new_log)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
