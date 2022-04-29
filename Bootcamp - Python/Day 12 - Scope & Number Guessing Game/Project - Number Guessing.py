from random import randint

def game(attemps, number):
    for tries in range(attemps-1):
        print(f"You have {attemps-tries} remaining to guess the number.")        
        guess = int(input("Make a guess: "))
        if guess == number:
            return True
        elif guess > number:
            print("Too high!")
        elif guess < number:
            print("Too low!")
    return False

number = randint(1, 100)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
while True:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        if game(10, number) == False:
            print("You've run out guesses. You Lose!")
        else:
            print(f"You got it! The answer was {number}")
        break
    elif difficulty == 'hard':
        if game(5, number) == False:
            print("You're out of attemps. You Lose!")
        else:
            print(f"You got it! The answer was {number}.")
        break
    else:
        print("Choose a valid difficulty.")