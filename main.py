# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from Queue import queue
import time
import Heuristic
from Puzzle import puzzle

def main():
    test_queus = [
        queue(Heuristic.manhattan_distance(puzzle.goalstate, 11)),
        queue(Heuristic.hamming_distance(puzzle.goalstate, 11))
    ] 

    times = []

    for test in test_queus:
        start_time = time.time()
        test.find_solution()
        #test.print_path()
        print("##################################################")
        times.append(time.time() - start_time)

    for i in range(len(times)):
        print("Time for solution with " + test_queus[i].heuristic_class.__class__.__name__ + " heuristic: " + str(times[i]) + "number of moves: " + str(test_queus[i].number_of_moves))

if __name__ == "__main__":
    main()
