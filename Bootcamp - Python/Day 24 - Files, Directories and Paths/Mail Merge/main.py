# Starting Letter
with open('Bootcamp - Python/Day 24 - Files, Directories and Paths/Mail Merge/Input/Letters/starting_letter.txt') as _:
    letter = _.read()
# Invited Names
with open('Bootcamp - Python/Day 24 - Files, Directories and Paths/Mail Merge/Input/Names/invited_names.txt') as _:
    names = _.read().split('\n') # readLines().strip('\n') also works, I guess.
# Replace and Save
for name in names:
    new_letter = open(f'Bootcamp - Python/Day 24 - Files, Directories and Paths/Mail Merge/Output/ReadyToSend/{name} Letter.txt', 'w')
    new_letter.write(letter.replace('[name]', name))