### 
# A program that prints numbers from 1 to 30
# If the number is divisible by 3 then the program prints the word 'THREE'
# Next, if the number is divisible by 5 then the program prints the word 'FIVE'
# Finally, if the number is divisible by both 3 and 5 then the program prints the word 'BINGO'

for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print('BINGO', end=' ')
    elif i % 5 == 0:
        print('FIVE', end=' ')
    elif i % 3 == 0:
        print('THREE', end=' ')
    else: 
        print(i, end=' ')