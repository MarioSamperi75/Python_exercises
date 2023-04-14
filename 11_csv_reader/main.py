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

import pandas

data = pandas.read_csv("weather_data.csv")
# printing the wole dataframe
print(data)

# printing a series
temp_series = data["temp"]
print(temp_series)

# converting a dataframe to  dictionary
print(data.to_dict())

# converting a series to a list
temp_list = temp_series.to_list()
print(temp_list)

# average
average_teperature = sum(temp_list) / len(temp_list)
print(int(average_teperature))
# alternative
average_teperature = temp_series.mean()
print(int(average_teperature))

# max & min look at https://pandas.pydata.org/docs/reference/series.html
print(temp_series.max())
print(temp_series.min())

# key notation or object notation - does not matter!
print(data['temp'])
print(data.temp)

# select one or more rows
print(data[data.day == "Monday"])
print(data[data.condition == "Sunny"])

# print the row with the max temp
print(data[data.temp == data.temp.max()])

#convert to farenheit
monday = data[data.day == "Monday"]
temp_fahrenheit = int(monday.temp) * 9/5 + 32
print(temp_fahrenheit)








