from turtle import Turtle
import pandas as pd

data = pd.read_csv("Bootcamp - Python/Day 25 - Working with CSV Data and the Pandas Library/U.S. States Game Project/50_states.csv")
path = 'Bootcamp - Python/Day 25 - Working with CSV Data and the Pandas Library/U.S. States Game Project/states_to_learn.csv'

class State(Turtle):
    
    def __init__(self):
        super().__init__()
        
    def write_(self, name):
        state = data[data.state == name]
        self.hideturtle()
        self.penup()
        self.goto(int(state.x), int(state.y))
        self.write(f'{name}', align="center", font=("Courier", 9, "normal"))

    def check(self, answer):
        if answer in data.state.to_list():
            self.write_(answer)
            return True
        return False
    
    def missing(self, guessed):
        missing_states = [x for x in data.state.to_list() if x not in guessed]
        pd.DataFrame(missing_states).to_csv(path)