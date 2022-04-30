import art
from game_data import data
from random import randint
from replit import clear

def generate():
    global a, b
    a = randint(0, len(data))
    b = randint(0, len(data))
    if a == b:
        y = randint(0, len(data))
        generate()

score = 0
while True:
    generate()
    print(f"{art.logo}\nCompare A: {data[a]['name']}, {data[a]['description']}, from {data[a]['country']}.")
    print(f"{art.vs}\nAgainst B: {data[b]['name']}, {data[b]['description']}, from {data[b]['country']}.")

    choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    clear()
    if choice == 'A' and data[a]['follower_count'] > data[b]['follower_count']:
        score += 1
        print(f"You're right! Current score: {score}.")
    elif choice == 'B' and data[a]['follower_count'] < data[b]['follower_count']:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        break