# Python Script to Implement and Manipulate Linked List in Python

# Node class
class Node:
    """A node in a singly linked list."""
    def __init__(self, data):
        self.data = data  # Node data
        self.next = None  # Reference to the next node


# LinkedList class
class LinkedList:
    """A simple singly linked list implementation."""
    def __init__(self):
        self.head = None

    def push(self, new_data):
        """
        Add a new node with `new_data` at the beginning of the linked list.
        """
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_node(self, new_data, insert_data):
        """
        Insert a new node with `new_data` immediately after the first node
        containing `insert_data`.

        Args:
            new_data: Data for the new node.
            insert_data: Data of the node after which the new node will be inserted.
        """
        new_node = Node(new_data)
        current_node = self.head
        while current_node:
            if current_node.data == insert_data:
                next_node = current_node.next
                current_node.next = new_node
                new_node.next = next_node
                break
            current_node = current_node.next

    def print_list(self):
        """Print the linked list from head to tail."""
        current_node = self.head
        while current_node:
            print(current_node.data, end="->")
            current_node = current_node.next
        print("END")


if __name__ == "__main__":
    # Create a linked list representing the alien communication network
    llist = LinkedList()
    llist.push("Zog")                # Add node at the beginning
    llist.insert_node("Zak", "Zog")  # Insert after "Zog"

    # Print the network
    llist.print_list()  # Expected output: Zog->Zak->END
