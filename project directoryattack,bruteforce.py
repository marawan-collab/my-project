#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import itertools
import string
import os

# Hardcoded correct password
CORRECT_PASSWORD = "P@ssw0rd123!"

def dictionary_attack(username, dictionary_path):
    """Attempts to find the password using a dictionary file."""
    
    # Debug: Check if file exists
    if not os.path.exists(dictionary_path):
        return f"Error: Dictionary file '{dictionary_path}' not found. Please check the file path."

    try:
        with open(dictionary_path, "r", encoding="utf-8") as file:
            for password in file:
                password = password.strip()  # Remove spaces and newlines
                
                # Debug: Print each password being tested
                print(f"Trying password: '{password}'")
                
                if password == CORRECT_PASSWORD:
                    return f"Success! User '{username}' logged in with password: '{password}' (Dictionary Attack)"
    except Exception as e:
        return f"Error reading the file: {e}"
    
    return None  # Dictionary attack failed

def brute_force_attack(username):
    """Performs a brute force attack by generating all possible 5-letter passwords."""
    chars = string.ascii_letters  # Uppercase and lowercase letters
    for password_tuple in itertools.product(chars, repeat=5):
        password = "".join(password_tuple)
        if password == CORRECT_PASSWORD:
            return f"Success! User '{username}' logged in with password: '{password}' (Brute Force Attack)"
    return "Failed to crack the password."  # Should not happen with a 5-letter limit

# Prompt user for username
username = input("Enter username: ")

dictionary_file_path = "Directory.txt"  # Ensure this file exists!

# Run dictionary attack first
result = dictionary_attack(username, dictionary_file_path)
if result:
    print(result)
else:
    print("Dictionary attack failed. Trying brute force...")
    print(brute_force_attack(username))


# In[ ]:




