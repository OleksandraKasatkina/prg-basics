###
# A program showing any amount (natural number) 
# read from the keyboard with as few coins as possible

amount = int(input('Enter the amount in PLN: '))
amount1 = amount

five_pln_coins = 0
two_pln_coins = 0
one_pln_coins = 0

five_pln_coins = amount1 // 5
amount1 = amount1 % 5

two_pln_coins = amount1 // 2
amount1 = amount1 % 2

one_pln_coins = amount1

print(f'The amount of PLN {amount} in coins: ')
print(f'5 PLN coins: {five_pln_coins}')
print(f'2 PLN coins: {two_pln_coins}')
print(f'1 PLN coins: {one_pln_coins}')