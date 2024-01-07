# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import statistics

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

    manhattan_memory_values = []
    manhattan_time_values = []
    hamming_memory_values = []
    hamming_time_values = []

    for i in range(runs):
        x = queue(Heuristic.manhattan_distance(puzzle.goalstate, 11))
        x.find_solution()
        manhattan_memory_values.append(x.memory_usage)
        manhattan_time_values.append(x.get_time())

    for i in range(runs):
        x = queue(Heuristic.hamming_distance(puzzle.goalstate, 11))
        x.find_solution()
        hamming_memory_values.append(x.memory_usage)
        hamming_time_values.append(x.get_time())

    manhattan_memory_deviation = statistics.stdev(manhattan_memory_values)
    manhattan_time_deviation = statistics.stdev(manhattan_time_values)
    hamming_memory_deviation = statistics.stdev(hamming_memory_values)
    hamming_time_deviation = statistics.stdev(hamming_time_values)


    print(f"Average memory usage for Manhattan: {manhattan_memory_sum/runs}")
    print(f"Average time usage for Manhattan: {manhattan_time_sum/runs}")
    print(f"Manhattan Memory Standard Deviation: {manhattan_memory_deviation}")
    print(f"Manhattan Time Standard Deviation: {manhattan_time_deviation}")
    print(f"Average memory usage for Hamming: {hamming_memory_sum/runs}")
    print(f"Average time usage for Hamming: {hamming_time_sum/runs}")
    print(f"Hamming Memory Standard Deviation: {hamming_memory_deviation}")
    print(f"Hamming Time Standard Deviation: {hamming_time_deviation}")

if __name__ == "__main__":
    main()