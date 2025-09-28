from typing import List

def days_until_cooler(temps: List[int]) -> List[int]:
    """
    For each day, compute the number of days until a cooler temperature occurs.
    
    Args:
        temps (List[int]): List of daily temperatures.
    
    Returns:
        List[int]: List where each element is the number of days until a cooler temperature.
                   If no cooler day exists, the value is -1.
    """
    result = [-1] * len(temps)
    stack = []  # stores indices of days

    # Traverse from right to left
    for i in range(len(temps) - 1, -1, -1):
        # Pop indices of days that are not cooler
        while stack and temps[stack[-1]] >= temps[i]:
            stack.pop()

        if stack:
            result[i] = stack[-1] - i  # days until cooler

        stack.append(i)

    return result


if __name__ == "__main__":
    # Example test cases
    print(days_until_cooler([30, 60, 90, 120, 60, 30]))  
    # Expected: [-1, 4, 2, 1, 1, -1]

    print(days_until_cooler([100, 95, 90, 85, 80, 75]))  
    # Expected: [1, 1, 1, 1, 1, -1]

    print(days_until_cooler([1]))  
    # Expected: [-1]
