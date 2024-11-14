def f(product_code):
    if len(product_code) != 4 or not product_code.isdigit():
        return False

    first_three_digits = product_code[:3]
    control_digit = int(product_code[3])

    digit_sum = sum(int(digit) for digit in first_three_digits)

    remainder = digit_sum % 7

    return control_digit == remainder

print(f("1082"))
print(f("2035"))
print(f("1114"))
print(f("7071"))