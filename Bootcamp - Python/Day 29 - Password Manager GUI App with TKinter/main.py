import tkinter as tk
from tkinter import messagebox
import random

path_img = "Bootcamp - Python/Day 29 - Password Manager GUI App with TKinter/logo.png"
path_passwords = "Bootcamp - Python/Day 29 - Password Manager GUI App with TKinter/passwords.txt"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    password.delete(0, tk.END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    # Random Letters (8-10) | # Random Symnols (2-4) | # Random Numbers (2-4)
    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))] + [random.choice(symbols) for _ in range(random.randint(2, 4))] + [random.choice(numbers) for _ in range(random.randint(2, 4))]
    random.shuffle(password_list)
    
    password.insert(0, "".join(password_list))

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    if any([len(website.get()) == 0, len(login.get()) == 0, len(password.get()) == 0]):
        messagebox.showerror(title="Empty Fields!", message="Please don't leave any fields empty!")
        return # Is empty = True
    if not messagebox.askokcancel(title=website.get(), message=f"These are the details entered: \nLogin: {login.get()}\nPassword: {password.get()}\nIs it ok to save?"):
        return # Check Button = False/Cancel
    
    with open(path_passwords, "a") as data:
        data.write(f"{website.get()} | {login.get()} | {password.get()}\n")
            
        website.delete(0, tk.END)
        login.delete(0, tk.END)
        password.delete(0, tk.END)

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Logo | Canvas
canvas = tk.Canvas(width=200, height=200)
logo_img = tk.PhotoImage(file=path_img)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = tk.Label(text="Website:") # Website | Label
website_label.grid(column=0, row=1)
login_label = tk.Label(text='Email/Username:') # Login | Label
login_label.grid(column=0, row=2)
password_label = tk.Label(text='Password:') # Password | Label
password_label.grid(column=0, row=3)

# Entries
website = tk.Entry(width=35) # Web | Entry
website.grid(column=1, row=1, columnspan=2) #website.insert(1, "EMAIL")
website.focus()
login = tk.Entry(width=35) # Login | Entry
login.grid(column=1, row=2, columnspan=2)
password = tk.Entry(width=21) # Password | Entry
password.grid(column=1, row=3)

# Buttons
generate_password = tk.Button(text="Generate", width=10, command=generate) # Generate Password | Button
generate_password.grid(column=2, row=3)
add = tk.Button(text="Add", width=32, command=save) # Add | Button
add.grid(column=1, row=4, columnspan=2)

window.mainloop()