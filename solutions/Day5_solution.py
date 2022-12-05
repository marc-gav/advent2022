from solutions.SolutionBaseClass import AdventSolution
# import stack
from collections import deque

class Solution(AdventSolution):
    def __init__(self):
        super().__init__(day=5)

    def create_input(self, number_cases: int):
        pass


    def provide_example(self):
        stacks = [
            deque(['Z', 'N']), # 1
            deque(['M', 'C', 'D']), # 2
            deque(['P']), # 3
        ]
        moves = [
            (1, 2, 1),
            (3,1,3),
            (2,2,1),
            (1,1,2)
        ]

        return stacks, moves

    def reader_parser(self, problem_string):
        """
                [J]         [B]     [T]    
                [M] [L]     [Q] [L] [R]    
                [G] [Q]     [W] [S] [B] [L]
        [D]     [D] [T]     [M] [G] [V] [P]
        [T]     [N] [N] [N] [D] [J] [G] [N]
        [W] [H] [H] [S] [C] [N] [R] [W] [D]
        [N] [P] [P] [W] [H] [H] [B] [N] [G]
        [L] [C] [W] [C] [P] [T] [M] [Z] [W]
        1   2   3   4   5   6   7   8   9 
        """
        stacks = [
            deque(['L', 'N', 'W', 'T', 'D']), # 1
            deque(['C', 'P', 'H']), # 2
            deque(['W', 'P', 'H', 'N', 'D', 'G', 'M', 'J']), # 3
            deque(['C', 'W', 'S', 'N', 'T', 'Q', 'L']), # 4
            deque(['P', 'H', 'C', 'N']), # 5
            deque(['T', 'H', 'N', 'D', 'M', 'W', 'Q', 'B']), # 6
            deque(['M', 'B', 'R', 'J', 'G', 'S', 'L']), # 7
            deque(['Z', 'N', 'W', 'G', 'V', 'B', 'R', 'T']), # 8
            deque(['W', 'G', 'D', 'N', 'P', 'L']), # 9
        ]

        moves = [
            move.split() for move in problem_string.splitlines()
        ]
        moves = [
            [int(move[1]), int(move[3]), int(move[5])] for move in moves
        ]

        return stacks, moves

    def part1(self, problem_string) -> int:
        stacks, moves = self.reader_parser(problem_string)
        #stacks, moves = self.provide_example()
        for no_elements, origin, destination in moves:
            for _ in range(no_elements):
                orig_elem = stacks[origin - 1].pop()
                stacks[destination - 1].append(orig_elem)
        
        # return the top element of every stack
        return ''.join([stack[-1] for stack in stacks])

    def part2(self, problem_string) -> int:
        stacks, moves = self.reader_parser(problem_string)
        
        for no_elements, origin, destination in moves:
            orig_elems = []
            for _ in range(no_elements):
                orig_elems.append(stacks[origin - 1].pop())
            
            # reverse orig_elems and append to destination
            orig_elems.reverse()
            for elem in orig_elems:
                stacks[destination - 1].append(elem)
        
        # return the top element of every stack
        return ''.join([stack[-1] for stack in stacks])

    def original_length(self):
        pass