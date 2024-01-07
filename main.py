# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from Queue import queue
import time
import Heuristic
from Puzzle import puzzle

def main():

    manhattan_memory_sum = 0
    manhattan_time_sum = 0
    hamming_memory_sum = 0
    hamming_time_sum = 0

    runs = 100

    for i in range(runs):
        x = queue(Heuristic.manhattan_distance(puzzle.goalstate, 11)) 
        x.find_solution()
        print(x.get_time())
        print(x.memory_usage)
        manhattan_memory_sum += x.memory_usage
        manhattan_time_sum += x.get_time()

    for i in range(runs):
        x = queue(Heuristic.hamming_distance(puzzle.goalstate, 11))
        x.find_solution()
        print(x.get_time())
        print(x.memory_usage)
        hamming_memory_sum += x.memory_usage
        hamming_time_sum += x.get_time()

    print(f"Average memory usage for Manhattan: {manhattan_memory_sum/runs}")
    print(f"Average time usage for Manhattan: {manhattan_time_sum/runs}")
    print(f"Average memory usage for Hamming: {hamming_memory_sum/runs}")
    print(f"Average time usage for Hamming: {hamming_time_sum/runs}")

if __name__ == "__main__":
    main()
