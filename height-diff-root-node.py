class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def max_height_diff(root):
    def height(node):
        if node is None:
            return 0
        return 1 + max(height(node.left), height(node.right))    
        # implement this
        
    if root is None:
        return 0
    left_height = height(root.left)
    right_height = height(root.right)
    # implement this
    return abs(left_height - right_height)

# Test samples
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(13)
root.right.right = TreeNode(17)

print(max_height_diff(root)) # Expected output: 1
