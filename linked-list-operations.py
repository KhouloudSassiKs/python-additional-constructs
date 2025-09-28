# Python Script to Practice Manipulation of a Doubly Linked List

# Node class
class Node:
    """A node in a doubly linked list."""
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


# DoublyLinkedList class
class DoublyLinkedList:
    """A simple implementation of a doubly linked list."""
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        """
        Insert a new node with the given data at the end of the list.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def delete(self, data):
        """
        Delete the first node found with the given data.
        """
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                if current_node.next is not None:
                    current_node.next.prev = current_node.prev
                else:
                    self.tail = current_node.prev

                if current_node.prev is not None:
                    current_node.prev.next = current_node.next
                else:
                    self.head = current_node.next
                return
            current_node = current_node.next

    def display_forward(self):
        """
        Display the elements of the list from head to tail.
        """
        current_node = self.head
        while current_node:
            print(current_node.data, end=" <-> ")
            current_node = current_node.next
        print("END")

    def display_backward(self):
        """
        Display the elements of the list from tail to head.
        """
        current_node = self.tail
        while current_node:
            print(current_node.data, end=" <-> ")
            current_node = current_node.prev
        print("END")


if __name__ == "__main__":
    # Create a doubly linked list
    dList = DoublyLinkedList()

    # Insert some elements
    dList.insert('Mars')
    dList.insert('Jupiter')
    dList.insert('Saturn')

    # Remove a node
    dList.delete('Jupiter')

    # Display the elements
    dList.display_forward()   # Output: Mars <-> Saturn <-> END
    dList.display_backward()  # Output: Saturn <-> Mars <-> END
