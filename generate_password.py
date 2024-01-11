import string
import random
from tkinter import messagebox

def gui_generate_password(website, login_id, include_uppercase, include_lowercase, include_special_char, include_numbers, password_length):
    characters = ""
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_special_char:
        characters += string.punctuation
    if include_numbers:
        characters += string.digits

    if not characters:
        messagebox.showerror("Error", "Please select at least one character type.")
        return

    try:
        password_length = int(password_length)
    except ValueError:
        messagebox.showerror("Error", "Invalid password length. Please enter a number.")
        return

    password = ''.join(random.choice(characters) for i in range(password_length))

    # Save to file
    with open("passwords.txt", "a") as file:
        file.write(f"Website: {website}, Login ID: {login_id}, Password: {password}\n")

    messagebox.showinfo("Generated Password", f"Your password: {password}")
