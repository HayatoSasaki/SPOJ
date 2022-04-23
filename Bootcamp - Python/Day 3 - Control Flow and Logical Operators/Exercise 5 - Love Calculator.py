def lovecalculator(name: str):
    score = [0, 0]
    for letter in "TRUE":
        score[0] += name.count(letter)
    for letter in "LOVE":
        score[1] += name.count(letter)     
    return int(str(score[0]) + str(score[1]))

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

score = sum(map(lovecalculator, [name1.upper(), name2.upper()]))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")