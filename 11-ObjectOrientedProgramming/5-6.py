from bank import BankAccount

def main():
    # Create a bank account with the given number
    my_account = BankAccount('12345655559090111100007722')

    print('Initial Account Info:')
    my_account.display_account_info()

    print('\nDepositing PLN 25,30')
    my_account.deposit(25.30)
    my_account.display_account_info()

    print('\nWithdrawing PLN 31,70')
    my_account.withdraw(31.70)
    my_account.display_account_info()

    print('\nWithdrawing PLN 14')
    my_account.withdraw(14)
    my_account.display_account_info()

if __name__ == "__main__":
    main()