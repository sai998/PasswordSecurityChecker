import re

def check_password_strength(password):
    strength = 0
    
    # Check for length
    if len(password) >= 8:
        strength += 1
    
    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength += 1
    
    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength += 1
    
    # Check for digits
    if re.search(r'\d', password):
        strength += 1
    
    # Check for special characters
    if re.search(r'[^A-Za-z0-9]', password):
        strength += 1
    
    return strength

password = input("Enter a password: ")
strength = check_password_strength(password)
if strength >= 5:
    print("Strong Password...")
else :
    print("Weak Password...")


