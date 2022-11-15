
import sys
sys.path.insert(0, '..')
from aoc_framework.solver.puzzle_solver import PuzzleSolver
from pprint import pprint


delimiter = ""


class DayPuzzleSolver(PuzzleSolver):
    def __init__(self, input_filename):
        PuzzleSolver.__init__(self, input_filename, delimiter)

    def get_input_into_self(self, raw_input):
        ...

    def solve_part_1(self):
        return

    def solve_part_2(self):
        return
