def pepperoni():
    if input("Do you want pepperoni? Y or N ") == "Y":
        return True
    else:
        return False

def cheese(order):
    if input("Do you want extra cheese? Y or N ") == "Y":
        return order + 1
    else:
        return order

def size(order):
    if order == "S":
        order = 15
        if pepperoni():
            order += 2
        order = cheese(order)
    elif order == "M":
        order = 20
        if pepperoni():
            order += 3
        order = cheese(order)
    else:
        order = 25
        if pepperoni():
            order += 3
        order = cheese(order)
    return order

print("Welcome to Python Pizza Deliveries!")
order = size(input("What size pizza do you want? S, M, or L "))
print(f"Your final bill is: ${order}.")