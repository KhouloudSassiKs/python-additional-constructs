class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        
    def add_child(self, child_value):
        self.children.append(Node(child_value))
        
    def depth_first_search(self, visited=None):
        if visited is None:
            visited = set()
        visited.add(self.value)
        print(self.value, end=' -> ')
        for child in self.children:
            if child.value not in visited:
                child.depth_first_search()

# Construct an imitation of a planet hierarchy
root_node = Node('Earth')
root_node.add_child('Africa')
root_node.add_child('Asia')

# Expand upon the countries in Africa
africa = root_node.children[0]
africa.add_child('Nigeria')
africa.add_child('South Africa')
africa.add_child('Tunisia')
africa.add_child('Algeria')

# Expand upon the countries in Asia
asia = root_node.children[1]
asia.add_child('China')
asia.add_child('India')

# Perform a depth-first search traversal starting from the root node
print("DFS Traversal of Planet's Continents:")
root_node.depth_first_search()
print("end")
