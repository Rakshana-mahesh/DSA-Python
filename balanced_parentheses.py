def is_balanced(expression):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in '([{':
            stack.append(char)                    # opening bracket -> push
        elif char in ')]}':
            if not stack or stack.pop() != pairs[char]:
                return False                       # mismatch or empty stack
    return len(stack) == 0                         # all opens must be matched


if __name__ == "__main__":
    tests = ["{[()]}", "([)]", "((()))", "{[}]", "()[]{}"]

    for expr in tests:
        print(f"{expr:10} -> {'Balanced' if is_balanced(expr) else 'Not Balanced'}")