import pandas as pd
path = "Bootcamp - Python/Day 26 - Comprehension and the NATO Alphabet/NATO Project/nato_phonetic_alphabet.csv"

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data = pd.read_csv(path)
nato = {row.letter:row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = list(input("Digit your name: ").upper())
print(' '.join([nato[x] for x in name]))