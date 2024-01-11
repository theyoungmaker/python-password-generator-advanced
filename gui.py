import tkinter as tk
from generate_password import gui_generate_password 

def on_generate_clicked():
    website = website_entry.get()
    login_id = login_id_entry.get()
    include_uppercase = uppercase_var.get()
    include_lowercase = lowercase_var.get()
    include_special_char = special_char_var.get()
    include_numbers = numbers_var.get()
    password_length = password_length_entry.get()

    gui_generate_password(website=website, login_id=login_id, include_uppercase=include_uppercase, include_lowercase=include_lowercase, include_special_char=include_special_char, include_numbers=include_numbers,password_length=password_length )

root = tk.Tk()
root.title("Password Generator")

# Labels and Entry Fields
tk.Label(root, text="Website:").grid(row=0)
website_entry = tk.Entry(root)
website_entry.grid(row=0, column=1)

tk.Label(root, text="Login ID:").grid(row=1)
login_id_entry = tk.Entry(root)
login_id_entry.grid(row=1, column=1)

# Checkboxes for Password Options
numbers_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).grid(row=2, columnspan=2)

uppercase_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Uppercase", variable=uppercase_var).grid(row=3, columnspan=2)

lowercase_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Lowercase", variable=lowercase_var).grid(row=4, columnspan=2)

special_char_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Special Characters", variable=special_char_var).grid(row=5, columnspan=2)

# Password Length
tk.Label(root, text="Password Length:").grid(row=6)
password_length_entry = tk.Entry(root)
password_length_entry.grid(row=6, column=1)

# Button to Generate Password
generate_button = tk.Button(root, text="Generate Password", command=on_generate_clicked)
generate_button.grid(row=7, columnspan=2)

root.mainloop()


