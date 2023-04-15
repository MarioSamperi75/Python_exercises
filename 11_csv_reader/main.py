# import csv
#
# with open("weather_data.csv") as file:
#     # concertivn reader bject to a list in order to use [1:]
#     # and skip the frst line
#     data = list(csv.reader(file))
#     temperatures = []
#     for row in data[1:]:
#         temperatures.append(int(row[1]))
#
# print(temperatures)

# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # printing the wole dataframe
# print(data)
#
# # printing a series
# temp_series = data["temp"]
# print(temp_series)
#
# # converting a dataframe to  dictionary
# print(data.to_dict())
#
# # converting a series to a list
# temp_list = temp_series.to_list()
# print(temp_list)
#
# # average
# average_teperature = sum(temp_list) / len(temp_list)
# print(int(average_teperature))
# # alternative
# average_teperature = temp_series.mean()
# print(int(average_teperature))
#
# # max & min look at https://pandas.pydata.org/docs/reference/series.html
# print(temp_series.max())
# print(temp_series.min())
#
# # key notation or object notation - does not matter!
# print(data['temp'])
# print(data.temp)
#
# # select one or more rows
# print(data[data.day == "Monday"])
# print(data[data.condition == "Sunny"])
#
# # print the row with the max temp
# print(data[data.temp == data.temp.max()])
#
# #convert to farenheit
# monday = data[data.day == "Monday"]
# temp_fahrenheit = int(monday.temp) * 9/5 + 32
# print(temp_fahrenheit)
#
# # Createind a dataframe from scratch
# data_dict = {
#     "students": ["Mario", "Ellen", "Sofia", "Alexander"],
#     "scores": [30, 80, 100, 100]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
#
# # creating CSV file from
# data.to_csv("new_data.csv")

import pandas

data = pandas.read_csv("squirrel_data.csv")

fur_color_series = data["Primary Fur Color"]

gray_ones = data[data["Primary Fur Color"] == "Gray"]
total_gray = len(gray_ones)
# total_gray = gray_ones.get("Primary Fur Color").count()

black_ones = data[data["Primary Fur Color"] == "Black"]
total_black = len(black_ones)
# total_black = black_ones.get("Primary Fur Color").count()

red_ones = data[data["Primary Fur Color"] == "Cinnamon"]
total_red = len(red_ones)
# total_red = red_ones.get("Primary Fur Color").count()

data_dict = {
    "fur_color": ["Grey", "Black", "Red"],
    "count": [total_gray, total_black, total_red]
}

data = pandas.DataFrame(data_dict)

data.to_csv("squirrel_count.csv")













