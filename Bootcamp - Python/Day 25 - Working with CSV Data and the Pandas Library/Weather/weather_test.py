import pandas as pd

# Just testing stuff...
data = pd.read_csv('Bootcamp - Python/Day 25 - Working with CSV Data and the Pandas Library/Weather/weather_data.csv')
average_temps = data.temp.mean() # same as: sum(data['temp'].to_list()) / len(data['temp'])
max_temp = data.temp.max()

print(f'Average: {round(average_temps, 1)}C \nMax: {max_temp}C')

print(data[data.temp == max_temp])

monday = data[data.day == 'Monday']
print(monday.condition)

