class MaxStack:
    """
    Stack data structure that supports retrieving the maximum element in O(1) time.
    """
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, x):
        """
        Push an element onto the stack.
        Update the max_stack if necessary.
        """
        if self.max_stack:
            if x >= self.max_stack[-1]:
                self.max_stack.append(x)
        else:
            self.max_stack.append(x)
        self.stack.append(x)
    
    def pop(self):
        """
        Pop the top element from the stack.
        Update the max_stack if the popped element was the current maximum.
        """
        if self.max_stack and self.stack[-1] == self.max_stack[-1]:
            self.max_stack.pop()
        return self.stack.pop()

    def top(self):
        """Return the top element of the stack without removing it."""
        return self.stack[-1] if self.stack else None

    def get_max(self):
        """Return the current maximum element in the stack."""
        return self.max_stack[-1] if self.max_stack else None


if __name__ == "__main__":
    # Example usage
    stack = MaxStack()
    stack.push(5)
    print(stack.get_max())  # Expected: 5
    stack.push(1)
    print(stack.get_max())  # Expected: 5
    stack.push(6)
    print(stack.get_max())  # Expected: 6
    stack.pop()
    print(stack.get_max())  # Expected: 5
