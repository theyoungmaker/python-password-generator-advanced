import tkinter as tk
from generate_password import gui_generate_password 

def on_button_clicked():
    website = website_entry.get()
    login_id = login_id_entry.get()
    include_uppercase = uppercase_var.get()
    include_lowercase = lowercase_var.get()
    include_special_char = special_char_var.get()
    include_numbers = numbers_var.get()
    password_length = password_length_entry.get()

    gui_generate_password(website=website, login_id=login_id, include_uppercase=include_uppercase, include_lowercase=include_lowercase, include_special_char=include_special_char, include_numbers=include_numbers,password_length=password_length)

window = tk.Tk()
window.title("Password Generator")

# Website Label and Entry widget
tk.Label(window, text="Website:").pack()
website_entry = tk.Entry(window)
website_entry.pack(padx=20)

# Login Id Label and Entry widget
tk.Label(window, text="Login ID:").pack()
login_id_entry = tk.Entry(window)
login_id_entry.pack(padx=20)

# Include numbers/digits Checkbox widget
numbers_var = tk.BooleanVar()
tk.Checkbutton(window, text="Include Numbers", variable=numbers_var).pack(padx=20)

# Include uppercase Checkbox widget
uppercase_var = tk.BooleanVar()
tk.Checkbutton(window, text="Include Uppercase", variable=uppercase_var).pack(padx=20)

# Include lowercase Checkbox widget
lowercase_var = tk.BooleanVar()
tk.Checkbutton(window, text="Include Lowercase", variable=lowercase_var).pack(padx=20)

# Include special characters Checkbox widget
special_char_var = tk.BooleanVar()
tk.Checkbutton(window, text="Include Special Characters", variable=special_char_var).pack(padx=20)

# Password Length
tk.Label(window, text="Password Length:").pack()
password_length_entry = tk.Entry(window)
password_length_entry.pack()

# Button to Generate Password
generate_button = tk.Button(window, text="Generate Password", command=on_button_clicked)
generate_button.pack()

window.mainloop()