def string_end(strng, n):
    """
    Reverse the input string using a stack
    and return the first n characters of the reversed string.
    """
    stack = list(strng)
    result = ''

    # Pop characters to reverse the string
    for _ in range(len(stack)):
        result += stack.pop()

    return result[:n]


if __name__ == "__main__":
    print(string_end("ijkshgegassem tnatropmi", 17))  # Expected: important message
    print(string_end("ffsfatad", 4))                  # Expected: data
    print(string_end("IA", 2))                        # Expected: AI
