class manhattan_distance:

    def __init__(self, goal_state, cost_exponent=3):
        self.goal_state = goal_state
        self.cost_exponent = cost_exponent

    def calculate(self, gameboard, parent_cost):
        cost = 0
        for i in range(3):
            for j in range(3):
                if gameboard[i][j] != self.goal_state[i][j]:
                    cost += 1
        return cost ** self.cost_exponent + parent_cost

class hamming_distance:

    def __init__(self, goal_state, cost_exponent=3):
        self.goal_state = goal_state
        self.cost_exponent = cost_exponent

    def calculate(self, gameboard, parent_cost):
        cost = 0
        for i in range(3):
            for j in range(3):
                if gameboard[i][j] != self.goal_state[i][j]:
                    for k in range(3):
                        for l in range(3):
                            if gameboard[i][j] == self.goal_state[k][l]:
                                cost += abs(i - k) + abs(j - l)
        return cost ** self.cost_exponent  + parent_cost
