class Node:
    """A node in a singly linked list."""
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    """A simple singly linked list implementation."""
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, data):
        """
        Insert a new node with the given data at the end of the list.
        """
        if not self.head:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(data)
        self.size += 1

    def delete(self, data):
        """
        Delete the first node with the specified data.
        """
        temp = self.head
        prev = None
        while temp:
            if temp.data == data:
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                self.size -= 1
                break
            prev = temp
            temp = temp.next


if __name__ == "__main__":
    # Example usage
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    print("Size of the linked list after insertions:", linked_list.size)  
    # Expected output: 3

    linked_list.delete(2)
    print("Size of the linked list after deletion:", linked_list.size)  
    # Expected output: 2
