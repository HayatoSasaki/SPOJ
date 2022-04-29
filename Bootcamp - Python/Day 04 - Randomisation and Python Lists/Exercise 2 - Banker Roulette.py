# Important: You are not allowed to use the choice() function.

import random

names = input("Give me everybody's names, separated by a comma. ").split(", ")
print(f"{names[random.randint(0, len(names)-1)]} is going to buy the meal today!")