# f string should be used.

age = int(input("What is your current age?"))

months = (90 - age) * 12
weeks = (90 - age) * 52
days = (90 - age) * 365

print(f"You have {days} days, {weeks} weeks, and {months} months left.")