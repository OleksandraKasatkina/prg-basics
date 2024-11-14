def f(number):
    number_str = str(number)
    repeated_digits = set()
    sum_repeats = 0
    
    for i in range(len(number_str)):
        if number_str[i] in repeated_digits:
            continue
        if number_str[i] in number_str[i+1:]:
            sum_repeats += int(number_str[i])
            repeated_digits.add(number_str[i])
    return sum_repeats

print(f(1027))
print(f(230335))
print(f(513553007))