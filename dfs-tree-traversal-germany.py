class Area:
    def __init__(self, name):
        """
        Initialize an Area with a name and an empty list of subareas.
        """
        self.name = name
        self.subareas = []
        
    def add_sub_area(self, area_name):
        """
        Add a new subarea (child Area) by name.
        """
        self.subareas.append(Area(area_name))  
    
    def dfs_traversal(self, visited=None):
        """
        Perform a depth-first search (DFS) traversal through the area hierarchy.
        - visited: keeps track of already visited areas to avoid repetition.
        """
        if visited is None:
            visited = set()
        
        # Mark this area as visited
        visited.add(self.name)
        
        # Print the current area
        print(self.name, end=" -> ")
        
        # Visit each subarea recursively
        for subarea in self.subareas:
            if subarea.name not in visited:
                subarea.dfs_traversal(visited)


# ---------------------------
# Build the city structure
# ---------------------------

# Root area
root_area = Area("Germany")

# Add top-level areas
root_area.add_sub_area("Hessen")
root_area.add_sub_area("Offfenbach")

# Add districts under Hessen
hessen = root_area.subareas[0]
hessen.add_sub_area("Ostend")
hessen.add_sub_area("Westend")
hessen.add_sub_area("Innenstadt")
hessen.add_sub_area("Sued")

# ---------------------------
# Run DFS traversal
# ---------------------------
print("Germany traversal:")
root_area.dfs_traversal()
print("end")
