import random

# Cool Letters Generator in with ASCII >_<, hell no.
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
letters_ = int(input("How many letters would you like in your password?\n")) 
symbols_ = int(input(f"How many symbols would you like?\n"))
numbers_ = int(input(f"How many numbers would you like?\n"))

password_list = []
for char in range(1, letters_ + 1):
  password_list.append(random.choice(letters))

for char in range(1, symbols_ + 1):
  password_list += random.choice(symbols)

for char in range(1, numbers_ + 1):
  password_list += random.choice(numbers)

random.shuffle(password_list)
print("Your password is: " + ("".join(password_list)))