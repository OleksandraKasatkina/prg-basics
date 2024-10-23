###
# Credit card payment 
#
account_balance = 500
total_payment = int(input('Enter total value of purchases: '))

if total_payment <= account_balance:
    print('Payment completed')
else:
    print('No funds')