###
# A program that prints a lottery coupon (numbers from 1 to 49)

for i in range(1, 8):
    for j in range(i, 50, 7):
        print(f"{j:2}", end=" ")
    print()