# Python Script to Implement and Traverse a Binary Tree

# Node class
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Define a binary tree using the Node class
house_tree_head = TreeNode("Entrance")

room_node1 = TreeNode("Living Room")
room_node2 = TreeNode("Bedroom")
room_node3 = TreeNode("Kitchen")

room_node11 = TreeNode("Sofa")
room_node12 = TreeNode("TV")
room_node13 = TreeNode("Bed")

# Build the binary tree
house_tree_head.left = room_node1
house_tree_head.right = room_node2

room_node1.left = room_node11
room_node1.right = room_node12

room_node2.right = room_node13
house_tree_head.right.right = room_node3


# In-order traversal
def print_in_order(node):
    if node is None:
        return
    print_in_order(node.left)
    print(f"Position -> {node.value}")
    print_in_order(node.right)


# Print the nodes of the binary tree
print_in_order(house_tree_head)
