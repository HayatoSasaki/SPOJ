import turtle
from state import State

# Screen | Window/Background
image = "Bootcamp - Python/Day 25 - Working with CSV Data and the Pandas Library/U.S. States Game Project/blank_states_img.gif"
screen = turtle.Screen()
screen.title('U.S. States Game')
screen.addshape(image)
turtle.shape(image)

# States | Data/Pandas
state = State() 
guessed_states = []

# Game
while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 | Guess the State", prompt="What's another state's name?").title()
    if state.check(answer):
        guessed_states.append(answer)
    elif answer == 'Exit':
        state.missing(guessed_states) # Create CSV with missing states.
        break # Close the game / loop.
    
    turtle.mainloop() # Keeps the window open.