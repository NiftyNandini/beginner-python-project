import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password():
    length = length_var.get()
    include_special = special_var.get()
    include_numbers = number_var.get()

    if length <= 0:
        messagebox.showerror("Error", "Please enter a valid length.")
        return

    characters = string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_password():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# Create the main window
root = tk.Tk()
root.title("Colorful Password Generator")
root.geometry("400x250")
root.configure(bg="#2E4053")

# Create variables
length_var = tk.IntVar(value=12)
special_var = tk.BooleanVar(value=True)
number_var = tk.BooleanVar(value=True)

# Styling the widgets
label_style = {"bg": "#2E4053", "fg": "#F7F9F9", "font": ("Arial", 12)}
button_style = {"bg": "#5DADE2", "fg": "white", "font": ("Arial", 12), "bd": 0, "width": 20}
entry_style = {"bg": "#F7F9F9", "fg": "#2E4053", "font": ("Arial", 12), "bd": 1}

# Create and place widgets
tk.Label(root, text="Password Length:", **label_style).grid(row=0, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=length_var, **entry_style).grid(row=0, column=1, padx=10, pady=10)

tk.Checkbutton(root, text="Include Special Characters", variable=special_var, bg="#2E4053", fg="#F7F9F9", selectcolor="#2E4053", font=("Arial", 12)).grid(row=1, column=0, columnspan=2)
tk.Checkbutton(root, text="Include Numbers", variable=number_var, bg="#2E4053", fg="#F7F9F9", selectcolor="#2E4053", font=("Arial", 12)).grid(row=2, column=0, columnspan=2)

generate_button = tk.Button(root, text="Generate Password", command=generate_password, **button_style)
generate_button.grid(row=3, column=0, columnspan=2, pady=10)

password_entry = tk.Entry(root, width=30, **entry_style)
password_entry.grid(row=4, column=0, padx=10, pady=10, columnspan=2)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_password, **button_style)
copy_button.grid(row=5, column=0, padx=10, pady=10, columnspan=2)

# Run the main loop
root.mainloop()
