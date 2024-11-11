###
# A program that finds N leading prime numbers

N = int(input('Enter the number of prime numbers you want to find: '))

count = 0
number = 2
prime_numbers = []

while count < N:
    is_prime = True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(number)
        count += 1
    number += 1

print('Prime numbers:', ' '.join(map(str, prime_numbers)))