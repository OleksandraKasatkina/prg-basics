class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0.0  # Initial balance is PLN 0.00
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: PLN {amount:.2f}")
        else:
            print("Deposit amount must be greater than 0.")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds on the account.")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrew: PLN {amount:.2f}")
        else:
            print("Withdrawal amount must be greater than 0.")

    def display_account_info(self):
        formatted_balance = f"{self.balance:,.2f}"  # Format the balance with commas
        # Manually format account number with spaces every 4 digits
        formatted_account_number = (self.account_number[:2] + ' ' + 
                                    self.account_number[2:6] + ' ' + 
                                    self.account_number[6:10] + ' ' + 
                                    self.account_number[10:14] + ' ' + 
                                    self.account_number[14:18] + ' ' + 
                                    self.account_number[18:22] + ' ' + 
                                    self.account_number[22:26])
        
        print(f"Bank Account No: {formatted_account_number}")
        print(f"Balance: PLN {formatted_balance}")