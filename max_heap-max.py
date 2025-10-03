"""
MaxHeap operations using Python's heapq.
Author: Your Name
Description:
    Demonstrates how to insert and delete elements in a max-heap
    using Python's heapq (which only provides a min-heap by default).
"""

import heapq

# Create an empty max-heap (simulated using negatives)
maxHeap = []


def insert(nodes):
    """
    Insert values into the max heap.

    Args:
        nodes (iterable): A list or iterable of integers to insert.
    """
    for node in nodes:
        heapq.heappush(maxHeap, -node)
    print(f"Max Heap after insertion: {[-x for x in maxHeap]}")


def delete():
    """
    Remove the largest element from the max heap.

    Returns:
        int: The removed largest element.
    """
    if not maxHeap:
        raise IndexError("delete from empty heap")
    largest = -heapq.heappop(maxHeap)
    print(f"Max Heap after deletion of largest node: {[-x for x in maxHeap]}")
    return largest


# Example usage
numbers = [28, 14, 35, 55, 68, 72, 47, 19, 11, 32]

insert(numbers)   # Insert elements
delete()          # Remove the largest element
