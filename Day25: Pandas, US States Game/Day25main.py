# weather_lst = []
# with open('weather_data.csv', 'r') as file:
#     weather_lst.append(file.readlines())
# print(weather_lst)

# import csv
#
# with open('weather_data.csv', 'r') as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#
# print(temperatures)

# USE PANDAS
# import pandas
# data = pandas.read_csv('weather_data.csv')

# DataFrame in pandas
# data_dict = data.to_dict()
# print(data_dict)

# Data Series in pandas
# data_lst = data['temp'].to_list()
# print(data_lst)

# Find average of temperatures
# print(data['temp'].mean())
# Finding max value in temperatures
# print(data['temp'].max())

# Get data from rows
# print(data[data.day == 'Monday'])

# Get data from the row which has the max temp
# print(data[data.temp == data.temp.max()])

# Create DataFrame from scratch
# data_dict = {"students":["Amy", "James", "Angela"],
#              "scores": [76, 65, 65]}
# data = pandas.DataFrame(data_dict)
# # Create csv file
# data.to_csv('new_data.csv')
# print(data)

# Find the number of grey, black and cinnamon squirrels
# in squirrel_data.csv
import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_colour_lst = data["Primary Fur Color"].to_list()
no_gray, no_black, no_cinnamon = 0, 0, 0
for item in fur_colour_lst:
    if item == 'Gray':
        no_gray += 1
    elif item == 'Cinnamon':
        no_cinnamon += 1
    elif item == 'Black':
        no_black += 1

squirrel_dict = {"Fur Color": ['Gray', 'Cinnamon', 'Black'],
                 "Count": [no_gray, no_cinnamon, no_black]}
data = pandas.DataFrame(squirrel_dict)
data.to_csv('squirrel_count.csv')
