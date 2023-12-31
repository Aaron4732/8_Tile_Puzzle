import random

class Puzzle:
    def __init__(self):
        # Creating 3x3 array for the gameboard
        self.gameboard = [[0] * 3 for _ in range(3)]

        # Create array for numbers 0-8 and shuffle order
        self.numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        random.shuffle(self.numbers)

    # Fill gameboard with randomized numbers
    def fill_gameboard(self):
        for i in range(3):
            for j in range(3):
                # Pop first number from shuffled list and assign it to gameboard
                self.gameboard[i][j] = self.numbers.pop(0)

    # Print gameboard
    def print_gameboard(self):
        for row in self.gameboard:
            print(row)

    # Define goal state of gameboard
    def goalstate(self):
        self.goalstate = [1, 2, 3], [4, 5, 6], [7, 8, 0]

    def is_solvable(self):
        """ Check if the puzzle is solvable. """
        flattened_puzzle = [tile for row in self.gameboard for tile in row if tile != 0]
        inversions = 0

        for i in range(len(flattened_puzzle)):
            for j in range(i + 1, len(flattened_puzzle)):
                if flattened_puzzle[i] > flattened_puzzle[j]:
                    inversions += 1

        if len(self.gameboard) % 2 != 0:  # Odd grid
            return inversions % 2 == 0
        else:  # Even grid
            blank_row = next(row for row, tiles in enumerate(self.gameboard)
                             if 0 in tiles)
            return (blank_row % 2 == 0) == (inversions % 2 != 0)