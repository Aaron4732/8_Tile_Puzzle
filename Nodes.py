from Puzzle import puzzle

class nodes:
    def __init__(self, node_id, parent_id, heuristic_class, parent_cost=0, gameboard=None):
        """
        :param node_id: Unique ID for the node.
        :param parent_id: ID of the parent node
        :param heuristic_class: Heuristic class used to calculate the cost of reaching node.
        :param parent_cost: Accumulated cost from the initial state to the parent state.
        :param gameboard: The current state of the puzzle

        """
        self.node_id = node_id
        self.parent = parent_id
        self.puzzle = puzzle(gameboard)
        self.heuristic = heuristic_class
        self.children = []
        self.cost = heuristic_class.calculate(self.puzzle.gameboard, parent_cost)

    def add_child(self, child_id):
        """
        :param child_id: of the child node to be added
        """
        self.children.append(child_id)

