from collections import deque
from typing import List

def interleave_queues(queue1: deque, queue2: deque) -> List[int]:
    """
    Interleave two queues of equal length by alternating their elements.

    Args:
        queue1 (deque): First input queue.
        queue2 (deque): Second input queue.

    Returns:
        List[int]: A list containing elements from both queues interleaved.
    """
    interleave_queue = deque()

    while queue1:
        interleave_queue.append(queue1.popleft())
        interleave_queue.append(queue2.popleft())

    return list(interleave_queue)


if __name__ == "__main__":
    # Test cases
    print(interleave_queues(deque([1, 2, 3, 4, 5]), deque([6, 7, 8, 9, 10])))
    # Expected output: [1, 6, 2, 7, 3, 8, 4, 9, 5, 10]

    print(interleave_queues(deque([1]), deque([2])))
    # Expected output: [1, 2]

    print(interleave_queues(deque([1, 3, 5]), deque([2, 4, 6])))
    # Expected output: [1, 2, 3, 4, 5, 6]
