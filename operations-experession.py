def evaluate_postfix_inverse(expression):
    """
    Evaluate a postfix expression (Reverse Polish Notation).
    Only supports +, -, *, / operators on integers.
    """
    stack = []
    for element in expression.split():
        if element.isdigit():
            stack.append(int(element))
        else:
            first = stack.pop()
            second = stack.pop()
            if element == '+':
                stack.append(second + first)
            elif element == '-':
                stack.append(second - first)
            elif element == '*':
                stack.append(second * first)
            elif element == '/':
                if first == 0:
                    print("Division by zero is not allowed!")
                    return None
                stack.append(second / first)
            else:
                raise ValueError(f"Unsupported operator: {element}")

    return stack.pop() if stack else None


if __name__ == "__main__":
    print(evaluate_postfix_inverse("2 3 -"))  # Expected: -1
    print(evaluate_postfix_inverse("2 3 +"))  # Expected: 5
    print(evaluate_postfix_inverse("6 3 *"))  # Expected: 18
    print(evaluate_postfix_inverse("0 8 /"))  # Expected: 0.0
    print(evaluate_postfix_inverse("8 2 /"))  # Expected: 4.0
