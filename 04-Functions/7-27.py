def f(dice):
    if not dice:
        return None

    max_count = 1
    max_digit = dice[0]

    current_count = 1
    current_digit = dice[0]

    for i in range(1, len(dice)):
        if dice[i] == current_digit:
            current_count += 1
        else:
            if current_count > max_count:
                max_count = current_count
                max_digit = current_digit
            current_digit = dice[i]
            current_count = 1

    if current_count > max_count:
        max_digit = current_digit

    return int(max_digit)

print(f("5233165554211"))
print(f("2133"))
