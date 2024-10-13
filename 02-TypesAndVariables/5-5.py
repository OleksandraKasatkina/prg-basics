###
# A program that allows you to enter the product price and discount.
# Print the product price, discount, discounted product price,
# and the difference between the product price before and after the discount.
price = input('Enter the price: ')
price = float(price)
discount_percent = input('Enter the discount: ')
discount_percent = float(discount_percent)
discount_amount = price * (discount_percent / 100)
price_with_discount = price - discount_amount
print(f'Price: {price}')
print(f'discount %: {discount_percent}')
print(f'Price with discount: {price_with_discount}')
print(f'Reduction: {discount_amount}')