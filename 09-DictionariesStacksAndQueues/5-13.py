def calculate_rpn(expression):
    stack = []  # Stack to hold operands
    
    for token in expression.split():
        if token.isdigit() or (token.replace('.', '', 1).isdigit() and token.count('.') < 2):  # Check if the token is a number
            stack.append(float(token))  # Push the number onto the stack
        
        elif token in ('+', '-', '*', '/'):  # If it's an operator
            if len(stack) < 2:
                print("Error: Not enough operands.")
                return
            
            operand2 = stack.pop()  # Pop second operand
            operand1 = stack.pop()  # Pop first operand
            
            # Perform operation
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                if operand2 == 0:
                    print("Error: Division by zero.")
                    return
                result = operand1 / operand2
            
            stack.append(result)  # Push the result back onto the stack
        
        else:
            print("Invalid input. Please enter a valid number or operator.")
            return
    
    # After all tokens are processed, the final result should be on the stack
    if len(stack) == 1:
        return stack.pop()  # The final result
    else:
        print("Error: The RPN expression is invalid.")
        return

# Get the RPN expression from the user and evaluate it
def rpn_calculator():
    print("Enter your RPN expression (e.g. '2 3 + ='):")
    expression = input("Expression: ").strip()
    
    result = calculate_rpn(expression)
    if result is not None:
        print("Result:", result)

# Call the RPN calculator function to start the program
rpn_calculator()
