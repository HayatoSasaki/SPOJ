import pandas as pd

data = pd.read_csv('Bootcamp - Python/Day 25 - Working with CSV Data and the Pandas Library/Squirrel Census Data Analysis/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')['Primary Fur Color'].to_list()

data_dict = {
    'Fur Color': ['Grey', 'Cinnamon', 'Black'],
    'Count': [data.count('Gray'), data.count('Cinnamon'), data.count('Black')]
}
pd.DataFrame(data_dict).to_csv('Bootcamp - Python/Day 25 - Working with CSV Data and the Pandas Library/Squirrel Census Data Analysis/census01.csv')