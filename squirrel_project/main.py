# importing datas from the file
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperature = int(row[1])
#             temperatures.append(temperature)
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# average = sum(temp_list) / len(temp_list)
# print(average)
#
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data.condition)

# # Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9 / 5 + 32
# print(monday_temp_F)

# Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data=data_dict)
# data.to_csv("new_data.csv")


# squirrel task
initial_data = pandas.read_csv("squirrel_count.csv")

squirrel_fur_color = initial_data["Primary Fur Color"]
grey_count = squirrel_fur_color.value_counts()["Gray"]
red_count = squirrel_fur_color.value_counts()["Cinnamon"]
black_count = squirrel_fur_color.value_counts()["Black"]

# Create a dataframe
squirrel_data = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [grey_count, red_count, black_count]
}

output_data = pandas.DataFrame(data=squirrel_data)
output_data.to_csv("squirrel_count_new.csv")
