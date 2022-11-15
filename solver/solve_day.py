import sys
sys.path.insert(0, '..')
from timer import Timer
from importlib.machinery import SourceFileLoader
from termcolor import colored


def solve_puzzles(day: str, part: str | None, input_filename: str, is_testing: bool):
    _print_title(day, is_testing)

    if part:
        _solve_part(part, input_filename, is_testing)
    else:
        _solve_part('1', input_filename, is_testing)
        _solve_part('2', input_filename, is_testing)
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


def _solve_part(part: str, input_filename: str, is_testing: bool):
    print(colored(f"\n--- Part {part} ---\n", 'magenta'))

    main_path, input_path = _get_file_paths(day, input_filename)
    main = _import_main(main_path)
    timer = Timer()

    timer.start()
    puzzle_solver = main.DayPuzzleSolver(input_path)
    puzzle_solver.print_solution_for(part)
    timer.stop()

    if not is_testing:
        print(colored(f"\nTime: {timer.elapsed_sec:.2f} seconds.\n", 'blue'))


def _import_main(main_path):
    return SourceFileLoader("main.py", main_path).load_module()


def _get_file_paths(day, input_filename):
    directory = _get_directory_name(day)
    main_path = directory + "main.py"
    input_path = directory + input_filename
    return main_path, input_path


def _get_directory_name(day):
    return "../day_" + _normalize_day(day) + "/"


def _normalize_day(arg):
    return arg if len(arg) > 1 else "0" + arg


if __name__ == '__main__':
    day = sys.argv[1]
    input_filename = sys.argv[2]
    part = sys.argv[3] if len(sys.argv) > 3 else None
    is_testing = "test" in input_filename

    solve_puzzles(day, part, input_filename, is_testing)
