###
# A computer program analyses the price of a product in an online store
#

current_price = float(input('Enter current price of the product: '))
previous_price = float(input('Enter previous price of the product: '))

price_reduction_percentage = ((previous_price - current_price) / previous_price) * 100

if price_reduction_percentage >= 10:
    print('Buy the product!!')
    print(f'Product price reduced by {price_reduction_percentage}%')
else:
    print('No recommendation to buy.')