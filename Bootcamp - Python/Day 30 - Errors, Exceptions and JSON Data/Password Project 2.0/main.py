import tkinter as tk
import random
import json
import pyperclip
from tkinter import messagebox

path_img = "Bootcamp - Python/Day 29 - Password Manager GUI App with TKinter/logo.png"
path_passwords = "Bootcamp - Python/Day 30 - Errors, Exceptions and JSON Data/Password Project 2.0/passwords.json"

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
    pyperclip.copy(password.get())

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    new_data = {
        website.get(): {
            "email": login.get(),
            "password": password.get()
        }}
    
    if any([len(website.get()) == 0, len(login.get()) == 0, len(password.get()) == 0]):
        messagebox.showerror(title="Empty Fields!", message="Please don't leave any fields empty!")
        return # Is empty = True
    try:
        with open(path_passwords, "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        with open(path_passwords, "w") as data_file:
            json.dump(new_data, data_file, indent=4)
    else:
        data.update(new_data)        
        with open(path_passwords, "w") as data_file:
            json.dump(data, data_file, indent=4)
    finally:
        website.delete(0, tk.END)
        login.delete(0, tk.END)
        password.delete(0, tk.END)

# ---------------------------- FIND PASSWORD -------------------------- #
def find_password():
    site = website.get()
    try:
        with open(path_passwords) as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if site in data:
            email = data[site]["email"]
            passw = data[site]["password"]
            pyperclip.copy(passw)
            messagebox.showinfo(title=site, message=f"Email: {email}\nPassword: {passw}\n\nPassword copied!")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {site} exists.")

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=30)

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
website = tk.Entry(width=22) # Web | Entry
website.grid(column=1, row=1) #website.insert(1, "EMAIL")
website.focus()
login = tk.Entry(width=35) # Login | Entry
login.grid(column=1, row=2, columnspan=2, pady=5)
password = tk.Entry(width=22) # Password | Entry
password.grid(column=1, row=3)

# Buttons
generate_password = tk.Button(text="Generate", width=10, command=generate) # Generate Password | Button
generate_password.grid(column=2, row=3)
search_password = tk.Button(text="Search", width=10, command=find_password) # Search Password | Button
search_password.grid(column=2, row=1)
add = tk.Button(text="Add", width=30, command=save) # Add | Button
add.grid(column=1, row=4, columnspan=2, pady=15)

window.mainloop()