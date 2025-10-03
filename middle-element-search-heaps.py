"""
MiddleElementFinder using two heaps.
Author: Your Name
Description:
    Maintains a running collection of numbers and efficiently
    finds the middle element using a max-heap and min-heap.
"""

import heapq
from typing import Optional


class MiddleElementFinder:
    """
    Maintains two heaps to efficiently find the middle element:
    - small: max-heap (stores the smaller half, using negated values)
    - large: min-heap (stores the larger half)
    """

    def __init__(self):
        self.heaps = [], []  # small, large

    def add_num(self, num: int) -> None:
        """
        Add a number to the data structure.

        Args:
            num (int): The number to add.
        """
        small, large = self.heaps
        # Push to large first, then move smallest to small (negated for max-heap)
        heapq.heappush(small, -heapq.heappushpop(large, num))
        # Rebalance if small has more elements than large
        if len(large) < len(small):
            heapq.heappush(large, -heapq.heappop(small))

    def middle_element(self) -> Optional[int]:
        """
        Return the current middle element.

        Returns:
            int or None: The middle element if available, else None.
        """
        small, large = self.heaps
        if not large and not small:
            return None
        if len(large) > len(small):
            return large[0]
        return max(large[0], small[0])  # small stores negatives


def main():
    """Example usage of MiddleElementFinder."""
    estimate_finder = MiddleElementFinder()
    numbers = [5, 10, 3, 1, 7]

    for num in numbers:
        estimate_finder.add_num(num)

    print("Middle element:", estimate_finder.middle_element())  # Expected output: 5


if __name__ == "__main__":
    main()
