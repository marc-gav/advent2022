from solutions.SolutionBaseClass import AdventSolution
import numpy as np

class Solution(AdventSolution):
    def __init__(self):
        super().__init__(day=8)

    def create_input(self, number_cases: int):
        pass

    def provide_example(self):
        with open("problem_inputs/day8.example.txt") as f:
            return f.read()

    def reader_parser(self, problem_string):
        lines = [line.strip() for line in problem_string.split("\n")]
        lines = [[int(c) for c in line] for line in lines]
        # conver to 2D numpy array
        lines = np.array(lines)
        return lines


    def part1(self, problem_string):
        problem = self.reader_parser(problem_string)
        # do it for the 4 sides
        visited_trees = np.zeros(problem.shape, dtype=bool)
        
        # from left
        count_visible_trees(problem, visited_trees)

        problem = np.fliplr(problem)
        visited_trees = np.fliplr(visited_trees)

        # from right
        count_visible_trees(problem, visited_trees)
        problem = np.fliplr(problem)
        visited_trees = np.fliplr(visited_trees)

        # from top
        problem = np.transpose(problem)
        visited_trees = np.transpose(visited_trees)
        count_visible_trees(problem, visited_trees)

        problem = np.fliplr(problem)
        visited_trees = np.fliplr(visited_trees)

        # from bottom
        count_visible_trees(problem, visited_trees)

        return np.sum(visited_trees)

    def part2(self, problem_string) -> int:
        problem = self.reader_parser(problem_string)
        visible_from_left = count_visible_trees_at_pos(problem)
        visible_from_right = np.fliplr(count_visible_trees_at_pos(np.fliplr(problem)))
        visible_from_top = np.transpose(count_visible_trees_at_pos(np.transpose(problem)))
        visible_from_bottom = np.transpose(np.fliplr(count_visible_trees_at_pos(np.fliplr(np.transpose(problem)))))

        visible_at_pos = np.multiply(visible_from_left, visible_from_right)
        visible_at_pos = np.multiply(visible_at_pos, visible_from_top)
        visible_at_pos = np.multiply(visible_at_pos, visible_from_bottom)

        return np.max(visible_at_pos)

    def original_length(self):
        pass

def count_visible_trees(array: np.ndarray, visited_trees: np.ndarray):
    for row_id, row in enumerate(array):
        start = -1
        for val_id, val in enumerate(row):
            if val > start:
                start = val
                visited_trees[row_id, val_id] = True
    return array, visited_trees

def line_of_sight(array: np.ndarray, start_vals: np.ndarray):
    los_trees = np.zeros(array.shape[0], dtype=int)
    for row_id, row in enumerate(array):
        start = start_vals[row_id]
        trees = 0
        for _, val in enumerate(row):
            trees += 1
            if val >= start:
                break

        los_trees[row_id] = trees
    return los_trees

def count_visible_trees_at_pos(array: np.ndarray):
    # This time we want to count the number of visible trees from all the elements of the row
    visible_at_pos = np.zeros(array.shape, dtype=int)
    for index in range(array.shape[1]):
        start_vals = array[:, index]
        visible_from_index = line_of_sight(array[:, index+1:], start_vals)
        visible_at_pos[:, index] = visible_from_index
        
    return visible_at_pos
