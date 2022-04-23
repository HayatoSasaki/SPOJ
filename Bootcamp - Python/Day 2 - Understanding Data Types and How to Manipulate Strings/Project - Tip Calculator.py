print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What porcentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip = bill * (tip / 100)
pay = (bill + tip) / 7

print("Each person should pay", round(pay, 2))