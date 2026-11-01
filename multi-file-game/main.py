import login
import users

logged_in_user = None

# Wrap everything in a loop so we can restart it if they choose "back"
while not logged_in_user:
    
    if login.needs_account():
        print("--- Create an account ---")
        print("(Type 'back' at the username prompt to return)")
        
        new_username = login.select_new_username(users.accounts)
        
        # Check if the user wanted to go back
        if new_username == "back":
            print("\nReturning to main menu...\n")
            continue  # Restarts the while loop from the very beginning
            
        new_password = login.select_new_password(8)
        users.accounts[new_username] = login.hash_password(new_password)
        
        logged_in_user = new_username
        print(f"\nWelcome, {logged_in_user}!")

    else:
        # Users have three login attempts before they're locked out.
        for attempt in range(3):
            print("--- Log in ---")
            username = login.enter_username()
            password = login.enter_password()

            if login.is_valid(username, password, users.accounts):
                logged_in_user = username
                print(f"\nWelcome back, {logged_in_user}!")
                break
        else:
            print("\nToo many failed attempts. You are locked out.")
            break # Breaks the outer while loop because they are locked out

# Core application behavior goes here
if logged_in_user:
    print(f"\n[Dashboard] Active session: {logged_in_user}")
