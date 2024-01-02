import random

class puzzle:
    def __init__(self):

        self.goalstate = [1, 2, 3], [4, 5, 6], [7, 8, 0]

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
        
    def copy_gameboard(self):
        new_gameboard = []
        for row in self.gameboard:
            new_gameboard.append(row.copy())
        return new_gameboard
    
    def compare_gameboards(self, gameboard):
        return self.gameboard == gameboard
    
    def get_empty_field(self):
        for i, row in enumerate(self.gameboard):
            for tile in row:
                if tile == 0:
                    return i, tile
                
    def generate_posible_gameboards(self):
        row, tile = self.get_empty_field()
        posible_gameboards = []
        
        if row > 0:
            new_gameboard = self.copy_gameboard()
            new_gameboard[row][tile], new_gameboard[row - 1][tile] = new_gameboard[row - 1][tile], new_gameboard[row][tile]
            posible_gameboards.append(new_gameboard)
        if row < 2:
            new_gameboard = self.copy_gameboard()
            new_gameboard[row][tile], new_gameboard[row + 1][tile] = new_gameboard[row + 1][tile], new_gameboard[row][tile]
            posible_gameboards.append(new_gameboard)
        if tile > 0:
            new_gameboard = self.copy_gameboard()
            new_gameboard[row][tile], new_gameboard[row][tile - 1] = new_gameboard[row][tile - 1], new_gameboard[row][tile]
            posible_gameboards.append(new_gameboard)
        if tile < 2:
            new_gameboard = self.copy_gameboard()
            new_gameboard[row][tile], new_gameboard[row][tile + 1] = new_gameboard[row][tile + 1], new_gameboard[row][tile]
            posible_gameboards.append(new_gameboard)
        
        return posible_gameboards
    
    def reach_goalstate(self):
        return self.gameboard == self.goalstate
    

    def get_cost(self):
        cost = 0
        for i in range(3):
            for j in range(3):
                if self.gameboard[i][j] != self.goalstate[i][j]:
                    cost += 1
        return cost