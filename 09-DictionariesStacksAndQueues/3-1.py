import queue

# Create a stack
stack = queue.LifoQueue()

# Perform operations: Push elements onto the stack
stack.put(2)
stack.put(3)
stack.put(7)
stack.put(4)
stack.put(1)
stack.put(9)
stack.put(8)

# Sum the last two numbers of the stack
last_num = stack.get()  # Get the top element (8)
second_last_num = stack.get()  # Get the next element (9)
last_two_sum = last_num + second_last_num
print("Sum of the last two numbers:", last_two_sum)

# Calculate the sum of the remaining elements in the stack
remaining_sum = 0
while not stack.empty():
    remaining_sum += stack.get()

print("Sum of the remaining elements:", remaining_sum)
