def leapyear(year):
    if year % 4 == 0:
        return True
    elif year % 100 == 0:
        if year % 400 == 0:
            return False
        return True
    else:
        return False

if leapyear(int(input("Which year do you want to check? "))):
    print("Leap year.")
else:
    print("Not leap year.")

def days_in_month(y, m):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    if m == 2 and leapyear(y):
        return 29
    else:
        return month_days[m-1]

#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)