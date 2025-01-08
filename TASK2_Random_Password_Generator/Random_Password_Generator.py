## RANDOM PASSWORD GENERATOR IN BEGINNER LEVEL

import random
import string

# Define the character set
letters = string.ascii_letters  # This includes a-z and A-Z
# Ask the user for the password length
length = int(input("Enter the password length: "))
# Generate a random password
password = ''.join(random.choice(letters) for _ in range(length))
# Display the generated password
print("Your Password:", password)


# Define the character set
letters = string.ascii_letters  # a-z and A-Z
numbers = string.digits  # 0-9
symbols = string.punctuation  # !, @, #, $, etc.
# Combine all characters
all_characters = letters + numbers + symbols
# Ask the user for the password length
length = int(input("Enter the password length: "))
# Generate a random password
password = ''.join(random.choice(all_characters) for _ in range(length))
# Display the generated password
print("Your Password:", password)


# Define the character set
letters = string.ascii_letters  # a-z and A-Z
numbers = string.digits  # 0-9
symbols = string.punctuation  # !, @, #, $, etc.
all_characters = letters + numbers + symbols
# Loop to allow generating multiple passwords
while True:
    # Ask the user for the password length
    length = int(input("Enter the password length: "))

    # Generate a random password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    # Display the generated password
    print("Your Password:", password)
    # Ask the user if they want to generate another password
    repeat = input("Do you want to generate another password? (yes/no): ").strip().lower()
    if repeat != 'yes':
        print("Goodbye!")
        break


import re
def check_password_strength(password):
    # Check length
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."
    # Check for at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return "Weak: Password must contain at least one uppercase letter."
    # Check for at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return "Weak: Password must contain at least one lowercase letter."
    # Check for at least one digit
    if not re.search(r'[0-9]', password):
        return "Weak: Password must contain at least one digit."
    # Check for at least one special character
    if not re.search(r'[@#$%^&+=]', password):
        return "Weak: Password must contain at least one special character."
    # Check for common patterns (optional)
    common_patterns = ["password", "123456", "qwerty", "abc123"]
    if any(pattern in password.lower() for pattern in common_patterns):
        return "Weak: Password contains common patterns."
    return "Strong: Your password is strong."
# Example usage:
password = input("Enter a password to check its strength: ")
print(check_password_strength(password))


## RANDOM PASSWORD GENERATOR IN ADVANCED LEVEL

import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip  # To copy password to clipboard

# Function to generate the password based on selected options
def generate_password():
    try:
        length = int(length_entry.get())  # Get the password length entered by the user
        
        # Validate the input for length
        if length < 8:
            raise ValueError("Password length should be at least 8 characters for security.")
        
        # Build character set based on selected checkboxes
        all_characters = ""
        if include_uppercase.get():
            all_characters += string.ascii_uppercase
        if include_lowercase.get():
            all_characters += string.ascii_lowercase
        if include_digits.get():
            all_characters += string.digits
        if include_symbols.get():
            all_characters += string.punctuation

        # Ensure at least one character type is selected
        if not all_characters:
            raise ValueError("You must select at least one character type (uppercase, lowercase, digits, symbols).")
        
        # Generate password
        password = ''.join(random.choice(all_characters) for _ in range(length))
        
        # Display the password
        password_label.config(text=f"Your Password: {password}")

        # Update strength label based on password complexity
        strength = password_strength(password)
        strength_label.config(text=f"Password Strength: {strength}")

    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))

# Function to evaluate the password strength
def password_strength(password):
    strength = "Weak"
    
    # Check length
    if len(password) >= 12:
        strength = "Strong"
    elif len(password) >= 8:
        strength = "Medium"
    
    # Check for complexity
    if (any(char.isdigit() for char in password) and
        any(char.isupper() for char in password) and
        any(char.islower() for char in password) and
        any(char in string.punctuation for char in password)):
        strength = "Very Strong"
    
    return strength

# Function to copy the password to the clipboard
def copy_to_clipboard():
    password = password_label.cget("text")  # Get the current password displayed
    if password != "":
        pyperclip.copy(password.split(": ")[1])  # Copy the password part to clipboard
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("No Password", "Please generate a password first.")

# Function to check the password strength from the clipboard
def check_clipboard_password_strength():
    password = pyperclip.paste()  # Get the password from clipboard
    if password:
        strength = password_strength(password)
        messagebox.showinfo("Password Strength", f"Password is {strength}")
    else:
        messagebox.showwarning("No Password", "Please copy a password first.")

# Function to clear all entries and labels
def clear_all():
    length_entry.delete(0, tk.END)
    password_label.config(text="")
    strength_label.config(text="Password Strength:")
    include_uppercase.set(True)
    include_lowercase.set(True)
    include_digits.set(True)
    include_symbols.set(True)

# Create the main window
root = tk.Tk()
root.title("Advanced Password Generator")

# Add widgets for password length input
tk.Label(root, text="Enter Password Length (minimum 8):").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

# Add checkboxes for character type selection
include_uppercase = tk.BooleanVar(value=True)
include_lowercase = tk.BooleanVar(value=True)
include_digits = tk.BooleanVar(value=True)
include_symbols = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Uppercase Letters", variable=include_uppercase).pack(anchor="w")
tk.Checkbutton(root, text="Include Lowercase Letters", variable=include_lowercase).pack(anchor="w")
tk.Checkbutton(root, text="Include Digits", variable=include_digits).pack(anchor="w")
tk.Checkbutton(root, text="Include Symbols", variable=include_symbols).pack(anchor="w")

# Create the "Generate Password" button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Label to display the generated password
password_label = tk.Label(root, text="", fg="blue")
password_label.pack(pady=5)

# Label to display password strength
strength_label = tk.Label(root, text="Password Strength:", fg="green")
strength_label.pack(pady=5)

# Create the "Copy to Clipboard" button
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=10)

# Create the "Check Clipboard Password Strength" button
check_clipboard_button = tk.Button(root, text="Check Clipboard Password Strength", command=check_clipboard_password_strength)
check_clipboard_button.pack(pady=10)

# Create the "Clear" button to reset the form
clear_button = tk.Button(root, text="Clear", command=clear_all)
clear_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()


















