class TreeNode:
    """Node of a Binary Search Tree (BST)."""
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def bst_insert(root, node):
    """Insert a node into the BST."""
    if root is None:
        return node

    if node.val < root.val:
        if root.left is None:
            root.left = node
        else:
            bst_insert(root.left, node)
    else:
        if root.right is None:
            root.right = node
        else:
            bst_insert(root.right, node)
    return root


def bst_traversal_inorder(root):
    """Inorder traversal of BST (Left, Root, Right)."""
    if root:
        bst_traversal_inorder(root.left)
        print(root.val, end=" ")
        bst_traversal_inorder(root.right)


def insert_value(root, val):
    """Helper function to insert a value directly (wraps TreeNode)."""
    return bst_insert(root, TreeNode(val))


if __name__ == "__main__":
    # Example usage
    root = TreeNode(50)
    insert_value(root, 30)
    insert_value(root, 20)
    insert_value(root, 40)
    insert_value(root, 70)
    insert_value(root, 60)
    insert_value(root, 80)

    print("Inorder Traversal of BST:")
    bst_traversal_inorder(root)
    print()
