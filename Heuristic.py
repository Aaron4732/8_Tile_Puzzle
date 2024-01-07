class manhattan_distance:

    def __init__(self, goal_state, cost_exponent=3):
        """
        :param goal_state: The goal state of the puzzle.
        :param cost_exponent: The exponent used to amplify the cost (default is 3).
        """
        self.goal_state = goal_state
        self.cost_exponent = cost_exponent

    def calculate(self, gameboard, parent_cost):
        """
        :param gameboard: The current state of the puzzle.
        :param parent_cost: The accumulated cost from the initial state to the parent state.
        :return: The calculated heuristic cost for the current gameboard.
        """
        cost = 0
        # Summing the distance for each tile from its goal position
        for i in range(3):
            for j in range(3):
                if gameboard[i][j] != self.goal_state[i][j]:
                    cost += 1
        return cost ** self.cost_exponent + parent_cost

class hamming_distance:

    def __init__(self, goal_state, cost_exponent=3):
        """
        :param goal_state: The goal state of the puzzle.
        :param cost_exponent: The exponent used to amplify the cost (default is 3).
        """
        self.goal_state = goal_state
        self.cost_exponent = cost_exponent

    def calculate(self, gameboard, parent_cost):
        """
        :param gameboard: The current state of the puzzle.
        :param parent_cost: The accumulated cost from the initial state to the parent state.
        :return: The calculated heuristic cost for the current gameboard.
        """
        cost = 0
        # Calculating the sum of the distances of the tiles from their goal positions
        for i in range(3):
            for j in range(3):
                if gameboard[i][j] != self.goal_state[i][j]:
                    for k in range(3):
                        for l in range(3):
                            if gameboard[i][j] == self.goal_state[k][l]:
                                cost += abs(i - k) + abs(j - l)
        return cost ** self.cost_exponent  + parent_cost
