###
# A program that calculates the amount to be paid for online shopping
#
number_of_products = int(input('Enter the number of purchased products: '))
product_price = float(input('Enter price of the product: '))

if number_of_products <= 2:
    amount_to_pay = number_of_products * product_price
elif number_of_products > 2:
    full_price_amount = 2 * product_price
    discounted_price = product_price * 0.75
    amount_to_pay = full_price_amount + ((number_of_products - 2) * discounted_price)
elif number_of_products <= 0:
    print('Number of products can not be negative or 0')

print(f'Amount to pay: {amount_to_pay}')