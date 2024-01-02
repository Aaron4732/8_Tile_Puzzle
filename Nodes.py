from Puzzle import puzzle

class nodes:
    def __init__(self, node_id, parent_id, gameboard=None):
        self.node_id = node_id
        self.parent = parent_id
        self.puzzle = puzzle(gameboard)
        self.children = []
        self.cost = self.puzzle.get_cost()

    def add_child(self, child_id):
        self.children.append(child_id)

