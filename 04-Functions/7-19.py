def f(n):
    count = 0
    candidate = 2

    while True:
        is_prime = True
        for i in range(2, int(candidate**0.5) + 1):
            if candidate % i == 0:
                is_prime = False
                break

        if is_prime:
            count += 1
            if count == n:
                return candidate

        candidate += 1

print(f(1))
print(f(5))