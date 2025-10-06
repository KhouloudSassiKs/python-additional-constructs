# Define a simple binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x       # value of the node
        self.left = None   # left child
        self.right = None  # right child

def max_height_diff(root):
    # We use a list to hold max_diff so it can be updated inside the nested function
    max_diff = [0]

    # Recursive helper to compute the height of a subtree
    def height(node):
        if node is None:
            return 0  # base case: empty node has height 0
        
        # Recursively compute the heights of left and right subtrees
        left = height(node.left)
        right = height(node.right)

        # Calculate the difference in heights for this node
        diff = abs(left - right)

        # Update the maximum difference found so far
        max_diff[0] = max(max_diff[0], diff)

        # Height of this node = 1 (itself) + max(left height, right height)
        return 1 + max(left, right)    
    
    # Edge case: if the tree is empty
    if root is None:
        return 0

    # Trigger the recursive traversal to fill max_diff
    height(root)

    # Return the maximum difference found across all nodes
    return max_diff[0]

# Test samples
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(13)
root.right.right = TreeNode(17)

print(max_height_diff(root)) # Expected output: 1
