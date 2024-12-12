import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

def brackets_ok(expression):
   # Dictionary for matching brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    # Stack for storing opening brackets
    stack = queue.LifoQueue()

    for char in expression:
        # Push opening brackets onto the stack
        if char in "({[":
            stack.put(char)
        # Check for closing brackets
        elif char in ")}]":
            if stack.empty() or stack.get() != bracket_map[char]:
                return False  # Mismatched or unmatched bracket

    # If stack is empty, all brackets matched; otherwise, some were unmatched
    return stack.empty()

# Test and print results
if brackets_ok(expression1):
    print(f"Expression 1: Brackets are correct")
else:
    print(f"Expression 1: Brackets are not correct")

if brackets_ok(expression2):
    print(f"Expression 2: Brackets are correct")
else:
    print(f"Expression 2: Brackets are not correct")

if brackets_ok(expression3):
    print(f"Expression 3: Brackets are correct")
else:
    print(f"Expression 3: Brackets are not correct")