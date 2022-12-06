from solutions.SolutionBaseClass import AdventSolution

class Solution(AdventSolution):
    def __init__(self):
        super().__init__(day=6)

    def create_input(self, number_cases: int):
        pass


    def provide_example(self):
        return 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'

    def reader_parser(self, problem_string):
        return problem_string

    def part1(self, problem_string) -> int:
        for i in range(len(problem_string) - 3):
            if len(set(problem_string[i:i+14])) == 4:
                return i + 4
        
        raise Exception("No window of 4 characters found")
    
    def part2(self, problem_string) -> int:
        for i in range(len(problem_string) - 13):
            if len(set(problem_string[i:i+14])) == 14:
                return i + 14
        
        raise Exception("No window of 14 characters found")

    def original_length(self):
        return len(self.problem_string)