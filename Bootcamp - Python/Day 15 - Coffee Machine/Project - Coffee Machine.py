import data

def turnoff():
    global engine
    engine = False

def report():
    print(f"Water: {data.resources['water']}ml\nMilk: {data.resources['milk']}ml\nCoffee: {data.resources['coffee']}g\n")

def resources(flavour):
    return set([data.MENU[flavour]["ingredients"][item] <= data.resources[item] for item in data.resources]) == {True} # data.MENU[flavour] <= data.resources

def makecoffee():
    global input_
    for item in data.resources:
        data.resources[item] -= data.MENU[input_]["ingredients"][item]
    print(f"Here is your, {input_}. Enjoy!\n")

def accountant(price):
    global profit
    money = 0
    print("Please insert coins.")
    for coins in data.coinsvalue:
        money += int(input(f"How many {coins}? ")) * data.coinsvalue[coins]

    if money >= price:
        if money > price:
            print(f"Here is ${round(money-price, 2)} dollars in change.")
        profit += price
        makecoffee()
    else:
        print("Sorry that's not enough money. Money refunded.")

###########################################
profit = 0
commands_ = {
    "off": turnoff,
    "report": report
}

engine = True
while engine:
    input_ = input("What would you like? (espresso/latte/cappuccino): ")

    if input_ in commands_:
        commands_[input_]()

    elif input_ in data.MENU:
        if resources(input_):
            accountant(data.MENU[input_]["cost"])
    else:
        print("Insert a valid flavour.")