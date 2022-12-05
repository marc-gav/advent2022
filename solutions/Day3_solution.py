from solutions.SolutionBaseClass import AdventSolution
from pprint import pprint as pp


class Solution(AdventSolution):
    def __init__(self):
        super().__init__(day=3)

        # list from a to Z
        alphabet = [chr(i) for i in range(ord("a"), ord("z") + 1)] + [
            chr(i) for i in range(ord("A"), ord("Z") + 1)
        ]
        self.priorities = {
            letter: priority
            for priority, letter in zip(range(1, 53), alphabet)
        }


    def part1(self, problem_string) -> int:
        problem = self.reader_parser(problem_string)
        repeated_elements = [list(set(a) & set(b))[0] for a, b in problem]
        return sum([self.priorities[repeated] for repeated in repeated_elements])

    def part2(self, problem_string) -> int:
        problem = self.reader_parser(problem_string)
        problem = [rucksack_left + rucksack_right for rucksack_left, rucksack_right in problem]
        # group it by 3 consecutive elements
        problem = [problem[i : i + 3] for i in range(0, len(problem), 3)]

        # find the repeated elements
        repeated_elements = [
            list(set(a) & set(b) & set(c))[0] for a, b, c in problem 
        ]

        return sum([self.priorities[repeated] for repeated in repeated_elements])
    
    def reader_parser(self, problem_string):
        return [
            (line[len(line) // 2 :], line[: len(line) // 2])
            for line in problem_string.splitlines()
        ]
    
    def original_length(self):
        # number of lines divided by 3
        return len(self.problem_string.splitlines()) // 3
    
    def create_input(self, number_cases: int):
        # three first lines
        problem_unit = '\n'.join(self.problem_string.splitlines()[:3])
        # repeat the three first lines
        new_problem = [problem_unit] * number_cases
        return '\n'.join(new_problem)