import queue

# Function to convert a natural number to binary using a stack
def to_binary(n):
    # Create an empty stack using LifoQueue
    stack = queue.LifoQueue()
    
    # Continue dividing by 2 and pushing remainders to the stack
    while n > 0:
        remainder = n % 2  # Get remainder
        stack.put(remainder)  # Push remainder to stack
        n = n // 2  # Divide n by 2
    
    # Pop and print the binary digits from the stack
    binary_number = ""
    while not stack.empty():
        binary_number += str(stack.get())  # Pop from the stack and append to the binary result
    
    return binary_number

# Main program
n = int(input("Enter a natural number: "))  # Take user input
binary = to_binary(n)

print(f"Natural number: {n}")
print(f"Binary number: {binary}")
