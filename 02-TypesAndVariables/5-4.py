###
# A program that reads an amount from the keyboard
# Then, it calculates and prints both the amount and its VAT
VAT_rate = 0.23
amount = input('Enter the amount: ')
amount = float(amount)
VAT_amount = amount * VAT_rate
print(f'Amount: {amount} ')
print(f'23% VAT of this amount: {VAT_amount}')