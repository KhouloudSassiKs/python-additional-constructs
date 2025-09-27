def are_brackets_balanced(s):
    """
    Check if brackets in the string are balanced.
    Supports (), [], {} and ignores non-bracket characters.
    """
    bracket_map = {"(": ")", "[": "]", "{": "}"}
    open_brackets = set(["(", "[", "{"])
    stack = []

    for char in s:
        if char not in open_brackets and char not in bracket_map.values():
            continue
        elif char in open_brackets:
            stack.append(char)
        elif stack and char == bracket_map[stack[-1]]:
            stack.pop()
        else:
            return False

    return len(stack) == 0


if __name__ == "__main__":
    print(are_brackets_balanced("(abc[d]{fg})"))      # Expected: True
    print(are_brackets_balanced("(a[bcd{fg}h]i)"))    # Expected: True
    print(are_brackets_balanced("(abc{d[fg]h)i"))     # Expected: False
    print(are_brackets_balanced("({a[bcd]})"))        # Expected: True
