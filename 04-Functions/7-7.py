def f(amount_to_pay):
    coin_count = 0

    coin_count += amount_to_pay // 5
    amount_to_pay %= 5

    coin_count += amount_to_pay // 2
    amount_to_pay %= 2

    coin_count += amount_to_pay

    return coin_count

print(f(23))
print(f(8))
print(f(2))
print(f(0))