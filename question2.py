class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited: Ksh {amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self._balance:
                self._balance -= amount
                print(f"Withdrew: Ksh {amount:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self._balance  # Provide a way to view the balance

# Demonstration of depositing and withdrawing money
account = BankAccount(1000)  # Starting with an initial balance of Ksh 1000
account.deposit(500)         # Depositing Ksh 500
account.withdraw(300)        # Withdrawing Ksh 300
account.withdraw(1500)       # Attempt to withdraw more than balance
print(f"Current Balance: Ksh {account.get_balance():.2f}")
