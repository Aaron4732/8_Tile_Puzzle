from Nodes import nodes
import time
import psutil
import tracemalloc
import resource

class queue:
    def __init__(self, heuristic_class):
        """
        :param heuristic_class: heuristic class used for node cost calculation
        """
        self.nodes = {}
        self.next_node_id = 0
        self.open_nodes = {}
        self.path = []
        self.number_of_moves = 0

        self.heuristic_class = heuristic_class

        self.end_time = 0

        self.memory_usage = 0
    def reset(self):
        """
        :return: Resets queue to its initial state
        """
        self.nodes = {}
        self.next_node_id = 0
        self.open_nodes = {}
        self.path = []



    def set_first_node(self):
        self.nodes[self.next_node_id] = nodes(self.next_node_id, None, self.heuristic_class, 0)
        self.open_nodes[self.next_node_id] = self.nodes[self.next_node_id]
        self.next_node_id += 1

    def find_cheapest_node(self):
        """
        :return: ID of cheapest node
        """
        cheapest_node = None
        cheapest_node_id = None
        for node_id, node in self.open_nodes.items():
            if cheapest_node is None or node.cost < cheapest_node.cost:
                cheapest_node = node
                cheapest_node_id = node_id
        return cheapest_node_id
    
    def add_node(self, parent_id, gameboard):
        """
        :param parent_id:ID of the parent node.
        :param gameboard: Gameboard state of the new node
        """
        self.nodes[self.next_node_id] = nodes(self.next_node_id, parent_id, self.heuristic_class, self.nodes[parent_id].cost, gameboard)
        self.nodes[parent_id].add_child(self.next_node_id)
        self.open_nodes[self.next_node_id] = self.nodes[self.next_node_id]
        self.next_node_id += 1

    def check_if_node_exists(self, gameboard):
        """
        :param gameboard: Gameboard state to check.
        :return: True if node exists, False otherwise.
        """
        for node_id, node in self.nodes.items():
            if node.puzzle.compare_gameboards(gameboard):
                return True
        return False

    def expand_node(self, node_id):
        """
        :param node_id: ID of the node to expand.
        """
        self.open_nodes.pop(node_id)
        parent_node = self.nodes[node_id]
        for gameboard in parent_node.puzzle.generate_posible_gameboards():
            if not parent_node.puzzle.compare_gameboards(gameboard):
                if not self.check_if_node_exists(gameboard):
                    self.add_node(node_id, gameboard)
    
    def get_path(self, node_id):
        """
        :param node_id: ID of the ending node.
        :return: List of node IDs representing the path from start to end.
        """
        path = []
        while node_id is not None:
            path.append(node_id)
            node_id = self.nodes[node_id].parent
        self.number_of_moves = len(path) - 1
        return path[::-1]
    
    def print_path(self):
        previous_gameboard = None

        for node_id in self.path:
            current_gameboard = self.nodes[node_id].puzzle.gameboard

            if previous_gameboard is not None:
                print()
                for i in range(len(current_gameboard)):
                    for j in range(len(current_gameboard[i])):
                        if current_gameboard[i][j] != previous_gameboard[i][j]:
                            print("\033[31m{}\033[00m".format(current_gameboard[i][j]), end=' ')
                        else:
                            print(current_gameboard[i][j], end=' ')
                    print()
            
            else:
                for row in current_gameboard:
                    for item in row:
                        print(item, end=' ')
                    print()

            previous_gameboard = current_gameboard

        
        #print(f"Number of moves: {self.number_of_moves}")
        

    def find_solution(self):
        self.reset()

        self.start_time = time.time()
        tracemalloc.start()

        self.set_first_node()
        cheapest_node_id = 0

        run = 0
        
        while True:
            run += 1
            if cheapest_node_id is None:
                return None
            if self.nodes[cheapest_node_id].puzzle.reach_goalstate():
                self.path = self.get_path(cheapest_node_id)
                tracemalloc.stop()
                self.end_time = time.time()
                self.memory_usage = psutil.virtual_memory().used

                return None
            self.expand_node(cheapest_node_id)
            cheapest_node_id = self.find_cheapest_node()

            #print("Current node: " + str(cheapest_node_id) + " with cost: " + str(self.nodes[cheapest_node_id].cost) + "parent: " + str(self.nodes[cheapest_node_id].parent) + "run: " + str(run) + "current_cost: " + str(self.nodes[cheapest_node_id].puzzle.get_cost()) + "current_open_nodes: " + str(len(self.open_nodes)))
            #self.nodes[cheapest_node_id].puzzle.print_gameboard()

    def get_time(self):
        """
        :return: Time duration in seconds.
        """
        return self.end_time - self.start_time
