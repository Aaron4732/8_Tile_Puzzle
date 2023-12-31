class Heuristic:
    @staticmethod
    def manhattan_distance(gameboard):
        manhattan_distance = 0

        for i in range(3):
            for j in range(3):
                tile = gameboard[i][j]
                if tile != 0:
                    # Calculate goal position for the tile
                    goal_i, goal_j = divmod(tile - 1, 3)
                    # Add the Manhattan distance for this tile
                    manhattan_distance += abs(goal_i - i) + abs(goal_j - j)
        return manhattan_distance


    @staticmethod
    def hamming_distance(gameboard):
        goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        hamming_distance = 0

        for i in range(3):
            for j in range(3):
                if gameboard[i][j] != goal_state[i][j] and gameboard[i][j] != 0:
                    hamming_distance += 1
        return hamming_distance