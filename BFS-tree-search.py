from collections import deque

# Graph represented as an adjacency list
PLANET_GRAPH = {
    'Mars':     ['Jupiter', 'Saturn'],
    'Jupiter':  ['Mars', 'Neptune', 'Uranus'],
    'Saturn':   ['Mars', 'Venus', 'Mercury'],
    'Neptune':  ['Jupiter'],
    'Uranus':   ['Jupiter', 'Earth'],
    'Venus':    ['Saturn'],
    'Mercury':  ['Saturn'],
    'Earth':    ['Uranus']
}

def bfs(graph, start_node):
    """
    Perform a breadth-first search (BFS) traversal starting from start_node.

    Args:
        graph (dict): adjacency list representing the graph
        start_node (str): starting node for BFS

    Returns:
        list: order of visited nodes
    """
    visited = set()
    order = []
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(f"{node} has been visited")
            visited.add(node)
            order.append(node)
            # enqueue unvisited neighbors
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)
    return order

def main():
    traversal_order = bfs(PLANET_GRAPH, 'Mars')
    print("\nOrder of visited planets:", traversal_order)

if __name__ == "__main__":
    main()
