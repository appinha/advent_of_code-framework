from termcolor import colored


class PuzzleSolver:
    def __init__(self, input_filename: str, delimiter: str):
        self.is_testing = "test" in input_filename
        self.raw_input = self._get_raw_input(input_filename, delimiter)

    def get_input_into_self(self, raw_input):
        raise NotImplementedError()

    def solve_part_1(self):
        raise NotImplementedError()

    def solve_part_2(self):
        raise NotImplementedError()

    def print_solution_for(self, part: str):
        solving_function = self.solve_part_1 if part == "1" else self.solve_part_2

        def print_solution(label: str, raw_input: str, solution: str | None=None):
            self.get_input_into_self(raw_input)
            print(
                colored(label, 'cyan'),
                solving_function(),
                colored("(" + str(solution) + ")" if solution else "", 'green')
            )

        if self.is_testing:
            for i, test in enumerate(self.raw_input[part]):
                print_solution(f"Test {i + 1} =", test["raw_input"], test["solution"])
        else:
            print_solution("Solution =", self.raw_input)

    def _get_raw_input(self, input_filename: str, delimiter: str):
        with open(input_filename, 'r') as f:
            file_content = f.read()

        if self.is_testing:
            return self._get_tests_raw_input(file_content, delimiter)
        return self._split_raw_input(file_content, delimiter)

    def _split_raw_input(self, file_content: str, delimiter: str):
        return list(map(str, (file_content.split(delimiter)))) if delimiter else file_content

    def _get_tests_raw_input(self, file_content: str, delimiter: str):

        def separate_parts(file_content: str):
            if "<===>" in file_content:
                parts = file_content.split("\n\n<===>\n\n")
            else:
                parts = [file_content, file_content]
            return {"1": parts[0], "2": parts[1]}

        def get_tests(raw_tests):
            tests = []
            for raw_test in raw_tests:
                string, solution = raw_test.split("\n:-> solution=")
                test = {
                    "raw_input": self._split_raw_input(string, delimiter),
                    "solution": solution.replace(" <-:", "")
                }
                tests.append(test)
            return tests

        string_by_part = separate_parts(file_content)
        tests_by_part = {}
        for part, string in string_by_part.items():
            raw_tests = string.split("\n\n<--->\n\n")
            tests_by_part[part] = get_tests(raw_tests)
        return tests_by_part
