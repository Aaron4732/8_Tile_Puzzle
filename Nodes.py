from Puzzle import puzzle

class nodes:
    def __init__(self, node_id, parent_id, heuristic_class, parent_cost=0, gameboard=None):
        self.node_id = node_id
        self.parent = parent_id
        self.puzzle = puzzle(gameboard)
        self.heuristic = heuristic_class
        self.children = []
        self.cost = heuristic_class.calculate(self.puzzle.gameboard, parent_cost)

    def add_child(self, child_id):
        self.children.append(child_id)

