class MovingAverage:
    """
    Class to calculate the moving average of word lengths over a fixed window size.
    """
    def __init__(self, size):
        self.queue = []
        self.size = size
        self.total = 0

    def calculate_moving_average(self, word):
        """
        Add a word to the queue and calculate the moving average of word lengths.

        Args:
            word (str): The new word to add.

        Returns:
            float: The moving average of word lengths, rounded to 2 decimal places.
        """
        word_size = len(word)
        self.queue.append(word)
        self.total += word_size

        # Remove oldest word if window exceeds size
        if len(self.queue) > self.size:
            removed_word = self.queue.pop(0)
            self.total -= len(removed_word)

        return round(self.total / len(self.queue), 2)


if __name__ == "__main__":
    # Test samples
    ma = MovingAverage(3)
    print(ma.calculate_moving_average('one'))    # Expected: 3.0
    print(ma.calculate_moving_average('two'))    # Expected: 3.0
    print(ma.calculate_moving_average('three'))  # Expected: 3.67
    print(ma.calculate_moving_average('four'))   # Expected: 4.0
    print(ma.calculate_moving_average('five'))   # Expected: 4.33
    print(ma.calculate_moving_average('six'))    # Expected: 3.67
