from collections import deque


def bfs(graph, root):
    """
    Perform a breadth-first search (BFS) starting from a root node.

    Args:
        graph (dict): Graph represented as an adjacency list.
        root (str): The starting node.

    Returns:
        dict: A dictionary mapping each node to its level
              (distance from the root).
    """
    visited = []
    queue = deque([root])
    level = {root: 0}  # Root starts at level 0

    while queue:
        vertex = queue.popleft()
        visited.append(vertex)

        level_of_vertex = level[vertex]

        for child in graph[vertex]:
            if child not in visited and child not in level:
                queue.append(child)
                level[child] = level_of_vertex + 1  # Child is one deeper

    print("\nTraversing completed!")
    return level


def main():
    """Example usage of bfs() with a sample graph."""
    graph = {
        '1': ['2', '3', '4'],
        '2': ['5', '6'],
        '3': ['7'],
        '4': ['8', '9'],
        '5': [],
        '6': ['10'],
        '7': ['11', '12'],
        '8': [],
        '9': [],
        '10': [],
        '11': [],
        '12': []
    }

    levels = bfs(graph, '1')
    print("Node levels:", levels)
