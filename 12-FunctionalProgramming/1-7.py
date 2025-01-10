is_even = lambda number: number % 2 == 0

test_numbers = [1, 2, 3, 4, 5, 10, 15, 20]

for number in test_numbers:
    if is_even(number):
        print(f'{number} is even')
    else:
        print(f'{number} is odd')