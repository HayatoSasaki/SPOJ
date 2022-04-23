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