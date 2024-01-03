import random

class puzzle:

    goalstate = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def __init__(self, gameboard=None):
        self.gameboard = gameboard

        if gameboard is None:
            self.fill_gameboard()

    # Fill gameboard with randomized numbers
    def fill_gameboard(self):
        # Creating 3x3 array for the gameboard
        self.gameboard = [[0] * 3 for _ in range(3)]
        # Shuffle numbers until solvable
        is_solvable = False

        while not is_solvable:

            self.numbers = [1,2,3,4,5,6,7,0,8]
            random.shuffle(self.numbers)
            for i in range(3):
                for j in range(3):
                    # Pop first number from shuffled list and assign it to gameboard
                    self.gameboard[i][j] = self.numbers.pop(0)

            # Check if puzzle is solvable
            is_solvable = self.is_solvable()

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
            for k, tile in enumerate(row):
                if tile == 0:
                    return i, k
                
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
        return self.gameboard == puzzle.goalstate
    

    def get_cost_simple(self):
        cost = 0
        for i in range(3):
            for j in range(3):
                if self.gameboard[i][j] != puzzle.goalstate[i][j]:
                    cost += 1
        return cost
    
    def get_cost(self):
        cost = 0
        for i in range(3):
            for j in range(3):
                if self.gameboard[i][j] != puzzle.goalstate[i][j]:
                    for k in range(3):
                        for l in range(3):
                            if self.gameboard[i][j] == puzzle.goalstate[k][l]:
                                cost += abs(i - k) + abs(j - l)
        return cost