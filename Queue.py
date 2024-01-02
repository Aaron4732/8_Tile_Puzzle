from Nodes import nodes
from Puzzle import puzzle

class queue:
    def __init__(self):
        self.nodes = {}
        self.next_node_id = 0
        self.open_nodes = {}
        self.path = []

    def reset(self):
        self.nodes = {}
        self.next_node_id = 0
        self.open_nodes = {}
        self.path = []



    def set_first_node(self):
        self.nodes[self.next_node_id] = nodes(self.next_node_id, None)
        self.open_nodes[self.next_node_id] = self.nodes[self.next_node_id]
        self.next_node_id += 1

    def find_cheapest_node(self):
        cheapest_node = None
        cheapest_node_id = None
        for node_id, node in self.open_nodes.items():
            if cheapest_node is None or node.cost < cheapest_node.cost:
                cheapest_node = node
                cheapest_node_id = node_id
        return cheapest_node_id
    
    def add_node(self, parent_id, puzzle: puzzle):
        self.nodes[self.next_node_id] = nodes(self.next_node_id, parent_id, puzzle)
        self.nodes[parent_id].add_child(self.next_node_id)
        self.open_nodes[self.next_node_id] = self.nodes[self.next_node_id]
        self.next_node_id += 1

    def expand_node(self, node_id):
        self.open_nodes.pop(node_id)
        node = self.nodes[node_id]
        for gameboard in node.puzzle.generate_posible_gameboards():
            if not node.puzzle.compare_gameboards(gameboard):
                self.add_node(node_id, node.puzzle)

        self.open_nodes.pop(node_id)
    
    def get_path(self, node_id):
        path = []
        while node_id is not None:
            path.append(node_id)
            node_id = self.nodes[node_id].parent
        return path[::-1]
    
    def print_path(self):
        for node_id in self.path:
            print(self.nodes[node_id].puzzle.gameboard)

    def find_solution(self):
        self.reset()

        self.set_first_node()
        if self.nodes[0].puzzle.is_solvable() == False:
            return None
        
        cheapest_node_id = 0
        
        while True:
            if cheapest_node_id is None:
                return None
            if self.nodes[cheapest_node_id].puzzle.reach_goalstate():
                self.path = self.get_path(cheapest_node_id)
                return None
            self.expand_node(cheapest_node_id)
            cheapest_node_id = self.find_cheapest_node()