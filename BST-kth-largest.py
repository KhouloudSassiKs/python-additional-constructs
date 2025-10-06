# Define a Node for the BST
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val        # value of the node
        self.left = left      # left child
        self.right = right    # right child

def kthLargest(root, k):    
    # Counter to track how many nodes we've visited
    # Result will hold the kth largest value once found
    count = [0]
    result = [None]

    # Helper function: reverse inorder traversal (Right → Root → Left)
    def reverse_inorder(node):
        # Base case: if node is None or we've already found the result, stop
        if not node or result[0] is not None:
            return
        
        # First, go right (larger values in BST)
        reverse_inorder(node.right)

        # Visit current node
        count[0] += 1
        if count[0] == k:
            result[0] = node.val  # Found kth largest
            return
        
        # Then, go left (smaller values)
        reverse_inorder(node.left)

    # Start traversal from root
    reverse_inorder(root)

    # Return the kth largest value
    return result[0]
    

# ---- Testing ----

# Creating the BST
root = Node(50) 
root.left = Node(20)
root.right = Node(60) 
root.left.left = Node(10) 
root.left.right = Node(30)
root.right.left = Node(55)
root.right.right = Node(70)
root.left.right.left = Node(25)
root.left.right.right = Node(35)
root.right.right.left = Node(65)
root.right.right.right = Node(80)

# Test cases
print(kthLargest(root, 1))   # Expected output: 80 (largest element)
print(kthLargest(root, 5))   # Expected output: 55
print(kthLargest(root, 10))  # Expected output: 20
print(kthLargest(root, 3))   # Expected output: 65
print(kthLargest(root, 7))   # Expected output: 35
