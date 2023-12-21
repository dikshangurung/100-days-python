import math

# with open("./weather_data.csv",mode="r") as data_file:
#     weather_info = data_file.readlines()
# print(weather_info)
# import csv
# with open("./weather_data.csv",mode="r") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] == "temp":
#             pass
#         else:
#             temperatures.append(int(row[1]))
#         print(row)
#
# print(temperatures)

import pandas
# data_frame = pandas.read_csv("weather_data.csv")
# data_series = data_frame["temp"]
#
# data_dict = data_frame.to_dict()
# data_list = data_series.to_list()
# # print(data_dict)
# print(data_list)
# print(round(sum(data_list)/len(data_list),2))
# print(data_series.max())

# Getting data in row
# print(data_frame[data_frame.day == "Monday"])
# print(data_frame[data_frame.temp == data_series.max()])
#
# monday = data_frame[data_frame.day == "Monday"]
# print(monday.temp)
# ok_dict = {
#     "students" : ["Dikshan","Ram","Shyam"],
#     "marks" : [90,80,90]
# }
# data = pandas.DataFrame(ok_dict)
# print(data)
# data.to_csv("new_data.csv")

# data_frame = pandas.read_csv("./Squirrel_data.csv")
# data_series = data_frame["Primary Fur Color"]
# gray_count = len(data_frame[data_frame["Primary Fur Color"] == "Gray"])
# red_count = len(data_frame[data_frame["Primary Fur Color"] == "Cinnamon"])
#
# print(gray_count)











#Solution 2
# data_lists = data_series.to_list()
# print(data_lists)
# grey_count = 0
# red_count = 0
# black_count = 0
# for color in data_lists:
#     # print(color)
#     if color == "Gray":
#         grey_count += 1
#     elif color == "Cinnamon":
#         red_count += 1
#     elif color == "Black":
#         black_count += 1
# squirrel_color = {
#     "Fur Color" : ["Gray","Red","Black"],
#     "Count" : [grey_count,red_count,black_count]
# }
# data = pandas.DataFrame(squirrel_color)
# # print(squirrel_color)
# data.to_csv("squirrel_count.csv")