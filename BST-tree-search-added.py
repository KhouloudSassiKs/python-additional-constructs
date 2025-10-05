class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    def __str__(self):
        return f'Node({self.val})'

def insert_BST(root, node):
    if root is None:
        return node

    if node.val < root.val:
        if root.left is None:
            root.left = node
        else:
            insert_BST(root.left, node)
    elif node.val > root.val:
        if root.right is None:
            root.right = node
        else:
            insert_BST(root.right, node)
    # if equal, do nothing (BST usually doesn’t store duplicates)
    return root

def search_BST(root, value): 
    """Search for a value in the BST. Returns Node or None."""
    if root is None:
        return None

    if root.val == value:
        return root
    elif value < root.val:
        return search_BST(root.left, value)
    else:
        return search_BST(root.right, value)
        
r = Node(50)
insert_BST(r, Node(20))
insert_BST(r, Node(70))
insert_BST(r, Node(10))
insert_BST(r, Node(30))
insert_BST(r, Node(60))
insert_BST(r, Node(80))

print(search_BST(r, 70)) # returns Node(70)
print(search_BST(r, 30)) # returns Node(30)
print(search_BST(r, 80)) # returns Node(80)
print(search_BST(r, 40)) # returns None
print(search_BST(r, 50)) # returns Node(50)
print(search_BST(r, 90)) # returns None
