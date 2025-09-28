class Node:
    """A node in a singly linked list."""
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    """A singly linked list with a tail pointer."""
    def __init__(self):
        self.head = None
        self.tail = None  # Extra pointer to the last node

    def add_node(self, data):
        """
        Add a node with the given data to the end of the linked list.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node  # Tail points to the first node
        else:
            self.tail.next = new_node
            self.tail = new_node  # Update tail to the new node

    def length_parity(self):
        """
        Determine if the length of the linked list is even or odd.

        Returns:
            str: "Even" if length is even, "Odd" if length is odd.
        """
        length = 0
        current_node = self.head
        while current_node:
            length += 1
            current_node = current_node.next

        return "Even" if length % 2 == 0 else "Odd"


if __name__ == "__main__":
    # Test cases
    linked_list = LinkedList()
    linked_list.add_node(1)
    linked_list.add_node(2)
    linked_list.add_node(3)
    print(linked_list.length_parity())  # Expected: 'Odd'

    linked_list = LinkedList()
    linked_list.add_node(10)
    linked_list.add_node(20)
    linked_list.add_node(30)
    linked_list.add_node(40)
    print(linked_list.length_parity())  # Expected: 'Even'

    linked_list = LinkedList()
    print(linked_list.length_parity())  # Expected: 'Even'
