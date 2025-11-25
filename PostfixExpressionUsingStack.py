
def apply_operation(op1, op2, operator):
    if operator == '+':
        return op1 + op2
    elif operator == '-':
        return op1 - op2
    elif operator == '*':
        return op1 * op2
    elif operator == '/':
        return op1 // op2   

def evaluate_postfix(expression):
    stack = []
    tokens = expression.split()

    for token in tokens:
        if token.isdigit():        
            stack.append(int(token))
        else:                     
            op2 = stack.pop()
            op1 = stack.pop()
            result = apply_operation(op1, op2, token)
            stack.append(result)

    return stack.pop()


expr = input("Enter postfix expression (use spaces): ")
print("Result =", evaluate_postfix(expr))
