import csv

with open("weather_data.csv") as file:
    # concertivn reader bject to a list in order to use [1:]
    # and skip the frst line
    data = list(csv.reader(file))
    temperatures = []
    for row in data[1:]:
        temperatures.append(int(row[1]))

print(temperatures)
