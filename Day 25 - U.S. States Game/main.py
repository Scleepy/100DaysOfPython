# USING CSV LIBRARY
# import csv

# with open("weather-data.csv") as weather_data:
#     new_data = csv.reader(weather_data)
#     temperatures = []
#     for row in new_data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

# print(temperatures)

# USING PANDAS 
import pandas as pd

data = pd.read_csv("weather-data.csv")
#print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# print(data["temp"].mean())
# print(data["temp"].max())

# # BOTH WORKS
# print(data["condition"])
# print(data.condition)

# print(data[data["day"] == "Monday"])
# print(data[data["temp"] == data["temp"].max()])

# monday = data[data["day"] == "Monday"]
# monday_temp = int(monday["temp"])

# monday_temp_F = monday_temp * 9/5 + 32

# print(monday_temp_F)

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pd.DataFrame(data_dict)
data.to_csv("new_data.csv")