# with open("weather_data.csv") as data_file:
#      data = data_file.readlines()
#      print(data)
import csv

# import csv
#
# with open ("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(float(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()
# print(data_dict)
# "].mean())
# print(data["temp"].max())
#
# temp_list = data["temp"].tolist()
# print(temp_list)
#
# print(data["temp
# # Get Data in columns
# print(data["condition"])

# Row of data where the temp was at the maximum
# print(data[data.temp == data.temp.max()])
#
# #Create a data frame from scratch
# data_dict = {
#     "students": ["Amy", "James", "Halima"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# # to generate another new data file of csv
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
     "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")