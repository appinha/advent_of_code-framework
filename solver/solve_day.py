import sys
sys.path.insert(0, '..')
import re
from importlib.machinery import SourceFileLoader
from termcolor import colored
from timer import Timer


def solve_puzzles(day: str, part: str | None, is_testing: bool):
    _print_title(day, is_testing)

    puzzle_solver = _get_puzzle_solver(day)
    puzzle_solver.raw_input = _get_raw_input(day, is_testing, puzzle_solver.delimiter)
    puzzle_solver.solutions = _get_solutions(day)

    if part:
        _solve_part(puzzle_solver, part, is_testing)
    else:
        _solve_part(puzzle_solver, '1', is_testing)
        _solve_part(puzzle_solver, '2', is_testing)
    print()


def _print_title(day: str, is_testing: bool):
    if is_testing:
        title = "Running tests"
        color = "red"
    else:
        title = f"Solution(s) for Day {day}"
        color = "green"
    print(
        colored("\n\n*** ", 'yellow'),
        colored(title, color),
        colored(" ***\n", 'yellow')
    )


def _get_puzzle_solver(day: str):

    def import_main(main_path):
        return SourceFileLoader("main.py", main_path).load_module()

    main = import_main(_build_main_path(day))
    return main.DayPuzzleSolver()


def _get_raw_input(day: str, is_testing: bool, delimiter: str):

    def get_file_content():
        input_path = _build_input_path(day, is_testing)
        with open(input_path, 'r') as f:
            file_content = f.read()
        return file_content

    def split_raw_input(file_content: str):
        return list(map(str, (file_content.split(delimiter)))) if delimiter else file_content

    def separate_parts(file_content: str):
        if "<===>" in file_content:
            parts = file_content.split("\n\n<===>\n\n")
        else:
            parts = [file_content, file_content]
        return {"1": parts[0], "2": parts[1]}

    def get_tests(string):
        raw_tests = string.split("\n\n<--->\n\n")
        tests = []
        for raw_test in raw_tests:
            string, solution = raw_test.split("\n:-> solution=")
            test = {
                "raw_input": split_raw_input(string),
                "solution": solution.replace(" <-:", "")
            }
            tests.append(test)
        return tests

    file_content = get_file_content()
    if is_testing:
        parts = separate_parts(file_content)
        return {part: get_tests(string) for part, string in parts.items()}
    return split_raw_input(file_content)


def _get_solutions(day: str):
    filename = _build_solutions_path(day)
    try:
        with open(filename, 'r') as f:
            file_content = f.read()
            return re.findall(r'"(.+?)"',file_content)
    except:
        return None


def _solve_part(puzzle_solver, part: str, is_testing: bool):
    print(colored(f"\n--- Part {part} ---\n", 'magenta'))

    timer = Timer()

    timer.start()
    _print_solution_for_part(puzzle_solver, part, is_testing)
    timer.stop()

    if not is_testing:
        print(colored(f"\nTime: {timer.elapsed_sec:.2f} seconds.\n", 'blue'))


def _print_solution_for_part(solver, part: str, is_testing: bool):
    solving_function = solver.solve_part_1 if part == "1" else solver.solve_part_2

    def print_solution(label: str, raw_input: str, solution: str | None=None):
        print(
            colored(label, 'cyan'),
            solving_function(raw_input),
            colored("(" + str(solution) + ")" if solution else "", 'green')
        )

    if is_testing:
        for i, test in enumerate(solver.raw_input[part]):
            print_solution(f"Test {i + 1} =", test["raw_input"], test["solution"])
    else:
        solution = solver.solutions[int(part) - 1] if solver.solutions else None
        print_solution("Solution =", solver.raw_input, solution)


def _build_input_path(day: str, is_testing: bool):
    directory = _get_directory_name(day)
    input_filename = "input_test.txt" if is_testing else "input.txt"
    return directory + input_filename


def _build_solutions_path(day: str):
    directory = _get_directory_name(day)
    return directory + "solutions.txt"


def _build_main_path(day: str):
    directory = _get_directory_name(day)
    return directory + "main.py"


def _get_directory_name(day: str):

    def normalize_day(arg: str):
        return arg if len(arg) > 1 else "0" + arg

    return "../day_" + normalize_day(day) + "/"


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage examples:")
        print("$ make day=01")
        print("$ make day=04 part=1")
        print("$ make test day=08")
        print("$ make test day=12 part=2")
        print("$ make new day=01")
    else:
        is_testing = sys.argv[1] == "testing"
        day = sys.argv[2]
        part = sys.argv[3] if len(sys.argv) > 3 else None

        solve_puzzles(day, part, is_testing)
