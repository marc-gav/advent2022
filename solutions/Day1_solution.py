from solutions.SolutionBaseClass import AdventSolution

class Solution(AdventSolution):
    def __init__(self):
        super().__init__(day=1)

    def create_input(self, number_cases: int):
        assert number_cases > 0, "Number of cases must be greater than 0"
        problem_string = self.problem_string
        # problem unit
        problem_unit = problem_string.split('\n\n')[0]
        new_problem = [problem_unit] * number_cases
        return '\n\n'.join(new_problem)

    def reader_parser(self, problem_string) -> list:
        return [list(map(int, elf.split('\n'))) for elf in problem_string.split('\n\n')]

    def part1(self, problem_string) -> int:
        elfs_snacks = self.reader_parser(problem_string)
        snack_count = [sum(snack) for snack in elfs_snacks]
        return max(snack_count)

    def part2(self, problem_string) -> int:
        elfs_snacks = self.reader_parser(problem_string)
        snack_count = [len(set(snack)) for snack in elfs_snacks]
        return max(snack_count)
    
    def original_length(self):
        return len(self.problem_string)