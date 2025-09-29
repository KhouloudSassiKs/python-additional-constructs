# Python Script: Company Hierarchy as a Non-Binary Tree

class TreeNode:
    """A node in a non-binary tree representing a company hierarchy."""
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        """Add a child node."""
        self.children.append(child_node)
    
    def remove_child(self, child_node):
        """Remove a specific child node."""
        self.children = [child for child in self.children if child is not child_node]


# Build the Company Hierarchy
company_hierarchy_root = TreeNode("CEO")

vp_marketing = TreeNode("VP Marketing")
vp_finance = TreeNode("VP Finance")
vp_engineering = TreeNode("VP Engineering")

company_hierarchy_root.add_child(vp_marketing)
company_hierarchy_root.add_child(vp_finance)
company_hierarchy_root.add_child(vp_engineering)

# Add Directors and Engineers
director_marketing = TreeNode("Director Marketing")
vp_marketing.add_child(director_marketing)

engineer = TreeNode("Engineer")
vp_engineering.add_child(engineer)

senior_engineer = TreeNode("Senior Engineer")
product_manager = TreeNode("Product Manager")
vp_engineering.add_child(senior_engineer)
vp_engineering.add_child(product_manager)

# Move "Engineer" under "Senior Engineer"
vp_engineering.remove_child(engineer)
senior_engineer.add_child(engineer)


def print_company_hierarchy(node):
    """
    Print the company hierarchy using pre-order traversal.
    """
    if node is None:
        return
    print(f'Position -> {node.value}')
    for child in node.children:
        print_company_hierarchy(child)


# Display the company hierarchy
if __name__ == "__main__":
    print_company_hierarchy(company_hierarchy_root)
