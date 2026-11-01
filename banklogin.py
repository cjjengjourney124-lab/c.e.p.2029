class BankAccount:
    def __init__(self, username, balance=0.0):
        self.username = username
        self.balance = balance

    def view_balance(self):
        print(f"\n--- Current Balance: ${self.balance:.2f} ---")
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"\nSuccessfully deposited ${amount:.2f}.")
            self.view_balance()
        else:
            print("\nInvalid amount. Deposit must be greater than $0.")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"\nDeclined: Insufficient funds. You only have ${self.balance:.2f}.")
        elif amount <= 0:
            print("\nInvalid amount. Withdrawal must be greater than $0.")
        else:
            self.balance -= amount
            print(f"\nSuccessfully withdrew ${amount:.2f}.")
            self.view_balance()


# -------------------------------------------------------------------
# System Database & Simulation
# -------------------------------------------------------------------

# Dictionary storing user credentials: {username: {"password": password, "account": BankAccount_Object}}
users_db = {
    "alice": {"password": "password123", "account": BankAccount("alice", 500.0)},
    "bob": {"password": "securepwd", "account": BankAccount("bob", 100.0)}
}

def bank_menu(account):
    """Sub-menu for logged-in users."""
    while True:
        print(f"\n=== Welcome, {account.username} ===")
        print("1. View Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Log Out")
        
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == "1":
            account.view_balance()
        elif choice == "2":
            try:
                amt = float(input("Enter deposit amount: $"))
                account.deposit(amt)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == "3":
            try:
                amt = float(input("Enter withdrawal amount: $"))
                account.withdraw(amt)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == "4":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please pick 1-4.")

def main():
    """Main system entry point for Registering or Logging in."""
    while True:
        print("\n====== ATM PORTAL ======")
        print("1. Log In")
        print("2. Register New Account")
        print("3. Exit System")
        
        choice = input("Choose an option (1-3): ").strip()
        
        if choice == "1":
            username = input("Username: ").strip()
            password = input("Password: ").strip()
            
            # Verify credentials
            if username in users_db and users_db[username]["password"] == password:
                print("\nLogin successful!")
                # Pass the BankAccount object associated with this user into the menu
                bank_menu(users_db[username]["account"])
            else:
                print("\nIncorrect username or password. Please try again.")
                
        elif choice == "2":
            new_user = input("Create Username: ").strip()
            if not new_user:
                print("Username cannot be blank.")
                continue
                
            if new_user in users_db:
                print("That username already exists. Try logging in.")
            else:
                new_pass = input("Create Password: ").strip()
                try:
                    initial_deposit = float(input("Enter initial deposit amount (optional, enter 0 for none): $"))
                except ValueError:
                    initial_deposit = 0.0
                
                # Store credentials and instantiate a new BankAccount object for them
                users_db[new_user] = {
                    "password": new_pass,
                    "account": BankAccount(new_user, initial_deposit)
                }
                print(f"\nAccount created successfully for {new_user}!")
                
        elif choice == "3":
            print("\nThank you for banking with us. Goodbye!")
            break
        else:
            print("Invalid option. Please pick 1-3.")

if __name__ == "__main__":
    main()
