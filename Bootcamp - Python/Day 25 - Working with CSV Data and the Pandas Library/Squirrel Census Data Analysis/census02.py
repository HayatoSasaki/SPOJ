import pandas as pd

data = pd.read_csv('Bootcamp - Python/Day 25 - Working with CSV Data and the Pandas Library/Squirrel Census Data Analysis/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

grey_count = len(data[data['Primary Fur Color'] == 'Gray'])
red_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_count = len(data[data['Primary Fur Color'] == 'Black'])

data_dict = {
    'Fur Color': ['Grey', 'Cinnamon', 'Black'],
    'Count': [grey_count, red_count, black_count]
}
pd.DataFrame(data_dict).to_csv('Bootcamp - Python/Day 25 - Working with CSV Data and the Pandas Library/Squirrel Census Data Analysis/census02.csv')