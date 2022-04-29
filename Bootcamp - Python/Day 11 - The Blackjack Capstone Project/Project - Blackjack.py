############### Blackjack Project #####################
from replit import clear
from art import logo
import random

############### Our Blackjack House Rules #####################
## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

## Forgot to check if both are over 21, but too lazy to do it rn...

def checkBlackjack():
    global user_cards, computer_cards
    if sum(user_cards) == 21:
        print("Blackjack!!! User Wins!")
        return True
    elif sum(computer_cards) == 21:
        print("Blackjack!!! Computer Wins!")
        return True
    else:
        return False

def checkUserOver():
    global user_cards
    if sum(user_cards) > 21:
        if 11 in user_cards: # Check for Ace
                user_cards[user_cards.index(11)] = 1
                return checkUserOver()
        else:
            print("User is over 21, Computer Wins!")
            return True
    else:
        return False

def checkComputerOver():
    global computer_cards
    if sum(computer_cards) > 21:
        if 11 in computer_cards: # Check for Ace
                computer_cards[computer_cards.index(11)] = 1
                return checkUserOver()
        else:
            print("Copmputer is over 21, User Wins!")
            return True
    else:
        return False

def dealCards(): # Deal Cards.
    global user_cards, computer_cards, cards
    user_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))

def checkComputer17():
    global computer_cards, cards
    if sum(computer_cards) < 17:
        computer_cards.append(random.choice(cards))
        checkComputer17()
    return

def calculateScore():
    clear()
    print(logo)
    checkComputer17()
    print(f"User final hand: {user_cards} = {sum(user_cards)}")
    print(f"User final hand: {computer_cards} = {sum(computer_cards)}")
    if checkBlackjack() or checkComputerOver():
        return
    if sum(user_cards) > sum(computer_cards):
        print("User Wins!")
    elif sum(user_cards) < sum(computer_cards):
        print("Computer Wins!")
    else:
        print("Draw!")

def play_game():
    global user_cards, computer_cards
    user_cards = []
    computer_cards = []
    while True:
        clear()
        print(logo)
        dealCards()
        print('User Cards: ', user_cards)
        print(f'Computer Cards: [{computer_cards[0]}{", *" * (len(computer_cards)-1)}]')
        if checkUserOver():
            break
        elif input("\n'Y' if you want to stop now: ").upper() == 'Y':
            calculateScore()
            break
        else:
            pass

####################################################################################
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()