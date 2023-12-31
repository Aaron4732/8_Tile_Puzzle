# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from Puzzle import Puzzle
from Heuristic import Heuristic

def main():
    puzzle_instance = Puzzle()
    puzzle_instance.fill_gameboard()
    print("Gameboard:")
    puzzle_instance.print_gameboard()

    if puzzle_instance.is_solvable():
        print("The puzzle is solvable.")
    else:
        print("The puzzle is not solvable.")


if __name__ == "__main__":
    main()
