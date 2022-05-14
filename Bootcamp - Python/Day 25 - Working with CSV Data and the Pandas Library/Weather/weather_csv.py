import csv

with open('Bootcamp - Python/Day 25 - Working with CSV Data and the Pandas Library/Weather/weather_data.csv') as _:
    data = csv.reader(_)
    temperatures = []
    for row in data:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))

    print(f'{temperatures}')