# ===============================
# PART I - BankAccount Class
# ===============================

class BankAccount:
    def __init__(self, username, password, balance=0):
        self.username = username
        self.password = password
        self.balance = balance
        self.authenticated = False

    def authenticate(self, username, password):
        if self.username == username and self.password == password:
            self.authenticated = True
            print("Authentication successful.")
        else:
            print("Authentication failed.")
            self.authenticated = False

    def deposit(self, amount):
        if not self.authenticated:
            raise Exception("Authentication required.")
        if amount <= 0:
            raise Exception("Deposit amount must be positive.")
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("Authentication required.")
        if amount <= 0:
            raise Exception("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise Exception("Insufficient funds.")
        self.balance -= amount
        print(f"Withdrew ${amount}. New balance: ${self.balance}")


# ============================================
# PART II - MinimumBalanceAccount Class
# ============================================

class MinimumBalanceAccount(BankAccount):
    def __init__(self, username, password, balance=0, minimum_balance=0):
        super().__init__(username, password, balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("Authentication required.")
        if amount <= 0:
            raise Exception("Withdrawal amount must be positive.")
        if self.balance - amount < self.minimum_balance:
            raise Exception(f"Cannot withdraw: minimum balance requirement of ${self.minimum_balance} not met.")
        self.balance -= amount
        print(f"Withdrew ${amount}. New balance: ${self.balance}")


# ===============================
# PART III - ATM Class
# ===============================

class ATM:
    def __init__(self, account_list, try_limit=2):
        # Validate account list
        if not isinstance(account_list, list) or not all(isinstance(acc, (BankAccount, MinimumBalanceAccount)) for acc in account_list):
            raise Exception("account_list must be a list of BankAccount or MinimumBalanceAccount instances.")

        # Validate try_limit
        if not isinstance(try_limit, int) or try_limit <= 0:
            raise Exception("try_limit must be a positive integer.")

        self.account_list = account_list
        self.try_limit = try_limit
        self.current_tries = 0

        self.show_main_menu()

    def show_main_menu(self):
        while True:
            print("\n--- ATM Main Menu ---")
            print("1. Log in")
            print("2. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                username = input("Enter username: ")
                password = input("Enter password: ")
                self.log_in(username, password)
            elif choice == "2":
                print("Exiting ATM. Goodbye!")
                break
            else:
                print("Invalid option.")

    def log_in(self, username, password):
        for account in self.account_list:
            if account.username == username and account.password == password:
                account.authenticate(username, password)
                self.show_account_menu(account)
                return

        self.current_tries += 1
        print(f"Login failed. Attempts left: {self.try_limit - self.current_tries}")
        if self.current_tries >= self.try_limit:
            print("Maximum login attempts reached. ATM shutting down.")
            exit()

    def show_account_menu(self, account):
        while True:
            print(f"\n--- Account Menu for {account.username} ---")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Log Out")
            choice = input("Choose an option: ")

            if choice == "1":
                try:
                    amount = float(input("Enter deposit amount: "))
                    account.deposit(amount)
                except Exception as e:
                    print(e)
            elif choice == "2":
                try:
                    amount = float(input("Enter withdrawal amount: "))
                    account.withdraw(amount)
                except Exception as e:
                    print(e)
            elif choice == "3":
                if account.authenticated:
                    print(f"Your balance is: ${account.balance}")
                else:
                    print("Authentication required.")
            elif choice == "4":
                print("Logging out...")
                account.authenticated = False
                break
            else:
                print("Invalid option.")


# ===============================
# PART IV - Testing the ATM
# ===============================

if __name__ == "__main__":
    # Create accounts
    acc1 = BankAccount("user1", "pass1", 1000)
    acc2 = MinimumBalanceAccount("user2", "pass2", 500, minimum_balance=100)

    # Launch ATM
    atm = ATM([acc1, acc2], try_limit=3)
