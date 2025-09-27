class Stack:
    """
    A simple stack implementation with a maximum size limit.
    Supports push, pop, peek, size, and empty-check operations.
    """

    def __init__(self, max_size=10):
        self.stack = []
        self.max_size = max_size

    def push(self, item):
        """Push an item onto the stack if not full."""
        if len(self.stack) < self.max_size:
            self.stack.append(item)
            print(f"Pushed {item} to the stack")
        else:
            raise Exception("Stack Overflow: Cannot push more items.")

    def pop(self):
        """Remove and return the top item from the stack."""
        if self.stack:
            popped_element = self.stack.pop()
            print(f"Popped element: {popped_element}")
            return popped_element
        else:
            raise Exception("Stack Underflow: The stack is empty.")

    def peek(self):
        """View the top element of the stack without removing it."""
        if self.stack:
            peeked_element = self.stack[-1]
            print(f"Peeked element: {peeked_element}")
            return peeked_element
        else:
            raise Exception("Stack Underflow: The stack is empty.")

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def get_size(self):
        """Return the current size of the stack."""
        return len(self.stack)


if __name__ == "__main__":
    my_stack = Stack()

    # Push elements onto the stack
    for i in range(1, 7):
        my_stack.push(i)

    print("\nOperations after pushing elements:")
    my_stack.peek()  # Peek top element
    my_stack.pop()   # Pop top element
    my_stack.peek()  # Peek new top element

    print("\nOperations when popping all elements:")
    while not my_stack.is_empty():
        my_stack.pop()
        if not my_stack.is_empty():
            my_stack.peek()

    print("\nFinal check on empty stack:")
    if my_stack.is_empty():
        print("The stack is empty.")
    else:
        print("The stack is not empty.")
