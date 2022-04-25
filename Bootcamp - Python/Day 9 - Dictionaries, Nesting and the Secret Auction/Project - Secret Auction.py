from replit import clear
from art import logo

def highest():
    winner = ""
    for bidder in bids:
        if bids[bidder] > winner:
            winner = bidder
    print("Winner is", winner)

bids = {}
print(logo)

while True:
    name = input("What is your name? ")
    price = input("What is your bid? $")
    bids[name] = price
    loop = input("Are there any other bidders? If so, type 'yes'").lower()
    if loop != 'yes':
        break
    clear
highest()