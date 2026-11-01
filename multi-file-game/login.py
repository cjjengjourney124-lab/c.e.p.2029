import hashlib

"""Supports the site login and account creation flow."""

def hash_password(password):
    """Helper function to securely hash a password using SHA-256."""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def enter_username():
    """Prompts the user to enter a username."""
    return input("Enter username: ")

def enter_password():
    """Prompts the user to enter a password."""
    return input("Enter password: ")

def is_valid(username, password, accounts):
    """Returns True if the username and hashed password match the accounts data."""
    if username in accounts:
        # Hash the incoming login password to see if it matches the stored hash
        return accounts[username] == hash_password(password)
    return False

def needs_account():
    """Returns True if the user says they need to create a new account."""
    has_account = input("Do you already have an account (y/n)? ")
    return has_account.lower() in ["n", "no"]

def select_new_username(accounts):
    while True:
        newuser = enter_username()
        
        # If they want to go back, return a flag immediately
        if newuser.lower() == "back":
            return "back"
            
        if newuser in accounts:
            print("Username already taken. Try again.")
        else:
            return newuser


def select_new_password(min_length):
    """Prompts the user to enter a password for their new account."""
    password = enter_password()
    while len(password) < min_length:
        print(f"Password must have at least {min_length} characters.")
        password = enter_password()
    return password  # Returns plain text; gets hashed when added to 'accounts'
