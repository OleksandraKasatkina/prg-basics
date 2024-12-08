array = [15, 38, 7, 23, 14]

def occurs(number, array):
    for element in array:
        if element == number:
            return True
    return False

number = int(input("Enter a number to check: "))

result = occurs(number, array)

print("Number:", number)
print("Array:", *array)
if result:
    print(f"Result: number {number} appears in the array")
else:
    print(f"Result: number {number} does not appear in the array")