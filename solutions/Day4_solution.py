from solutions.SolutionBaseClass import AdventSolution
from pprint import pprint as pp


class Solution(AdventSolution):
    def __init__(self):
        super().__init__(day=4)


    def part1(self, problem_string) -> int:
        problem = self.reader_parser(problem_string)
        # we need to find if interval1 is subset of interval2 or viceversa
        # if interval1 is subset of interval2, then interval1[0] >= interval2[0] and interval1[1] <= interval2[1]
        # if interval2 is subset of interval1, then interval2[0] >= interval1[0] and interval2[1] <= interval1[1]
        is_sub_interval = [
            (interval1[0] >= interval2[0] and interval1[1] <= interval2[1]) or (interval2[0] >= interval1[0] and interval2[1] <= interval1[1])
            for interval1, interval2 in problem
        ]
        return sum(is_sub_interval)

    def part2(self, problem_string) -> int:
        problem = self.reader_parser(problem_string)
        # now we need to find if they overlap
        # if they overlap then interval1[0] <= interval2[1] and interval1[1] >= interval2[0]
        # or viceversa
        is_overlap = [
            (interval1[0] <= interval2[1] and interval1[1] >= interval2[0]) or (interval2[0] <= interval1[1] and interval2[1] >= interval1[0])
            for interval1, interval2 in problem
        ]
        return sum(is_overlap)
        
    
    def reader_parser(self, problem_string):
        p = [a.split(',') for a in problem_string.splitlines()]
        p = [(interval1.split('-'), interval2.split('-')) for interval1,interval2 in p]
        # map all to int
        p = [((int(interval1[0]), int(interval1[1])), (int(interval2[0]), int(interval2[1]))) for interval1,interval2 in p]
        return p

    def original_length(self):
        # number of lines
        return len(self.problem_string.splitlines())

    def create_input(self, number_cases: int):
        # get a random line
        unit_problem = self.problem_string.splitlines()[0]
        return '\n'.join([unit_problem] * number_cases)
    