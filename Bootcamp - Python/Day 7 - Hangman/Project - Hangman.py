from random import choice
from replit import clear
import HangmanResources as art

def guess(guess_):
    if len(guess_) != 1:
        print("One letter pls.")
        return
    clear()
    global lives
    if guess_ not in chosen_word:
        print(f"{art.logo}\n\nYou guessed {guess_}, that's not in the word. You lose a life.")
        lives -= 1
    else:
        if guess_ in blanks_:
            print(f"{art.logo}\n\nYou've already guessed {guess_}")
            lives -= 1
        else:
            print(f"{art.logo}\n\nYou've guessed {guess_}, there is {chosen_word.count(guess_)} in the word.")
            for x in [letter for letter in range(len(chosen_word)) if guess_ == chosen_word[letter]]:
                blanks_[x] = guess_
# -----------------------------------------------------------------------------------------------
lives = 6
chosen_word = choice(art.word_list).upper()
blanks_ = ["_"] * len(chosen_word)
clear()
print(f'{art.logo}')
while True:
    print(f'{art.stages[lives]}\n', "".join(blanks_))
    if "_" not in blanks_:
        print("You Win!")
        break
    elif lives == 0:
        print(f"You Lose! The word was {chosen_word.lower()}.")
        break
    else:
        guess(input("\nGuess a letter: ").upper())