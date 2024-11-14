def f(detector):
    count = 0
    max_count = 0

    for symbol in detector:
        if symbol == '+':
            count += 1
            max_count = max(max_count, count)
        elif symbol == '-':
            count -= 1
        if max_count >= 3:
            return True
    return max_count >= 3

print(f("+-+++-+---"))
print(f("+-+-+-+-"))
print(f("+-++-+--"))
print(f("+-++-++-+---"))