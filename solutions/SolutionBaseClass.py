import cProfile
import pstats
import time
import numpy as np
from matplotlib import pyplot as plt
from tqdm import tqdm


def profileit(func):
    def wrapper(*args, **kwargs):
        print(f"🐌 Profiling {func.__name__} 🐇")
        start_time = time.perf_counter_ns()
        func(*args, **kwargs)
        end_time = time.perf_counter_ns()
        # covert to ms
        print(f"Time taken: {(end_time - start_time) / 1000000} ms 🐇🐇🐇\n")

    return wrapper


class AdventSolution:
    def __init__(self, day):
        print(f'Reading problem input from: "problem_inputs/day{day}.txt"')
        self.day = day
        self.cache = {}
        with open(f"problem_inputs/day{day}.txt", "r", encoding="utf-8") as f:
            self.problem_string = f.read()

    def reader_parser(self):
        raise NotImplementedError("You must further implement a parser")

    def part1(self, input_string):
        raise NotImplementedError("You must implement part 1")

    def part2(self, input_string):
        raise NotImplementedError("You must implement part 2")

    @profileit
    def profile_solution(self, part):
        if part == 1:
            self.part1(self.problem_string)
        elif part == 2:
            self.part2(self.problem_string)

    def original_length(self):
        raise NotImplementedError(
            "You must implement a function to return the original length of the problem string"
        )

    def solution_time_complexity(self):

        times_part1 = []
        times_part2 = []
        original_length = self.original_length()
        for i in tqdm(range(1, original_length + 10000, 10)):
            problem_string = self.create_input(i)

            start_time = time.perf_counter_ns()
            self.part1(problem_string)
            end_time = time.perf_counter_ns()
            time_difference_ms = (end_time - start_time) / 1000000
            times_part1.append((i, time_difference_ms))

            start_time = time.perf_counter_ns()
            self.part2(problem_string)
            end_time = time.perf_counter_ns()
            time_difference_ms = (end_time - start_time) / 1000000
            times_part2.append((i, time_difference_ms))

        # two plots
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
        fig.suptitle(f"Time complexity of day {self.day}")
        ax1.set_title("Part 1")
        ax2.set_title("Part 2")
        ax1.set_xlabel("Input size")
        ax2.set_xlabel("Input size")
        ax1.set_ylabel("Time (ms)")
        ax2.set_ylabel("Time (ms)")
        ax1.scatter(*zip(*times_part1))
        ax2.scatter(*zip(*times_part2))

        # show vertical line at original length
        ax1.axvline(x=original_length, color="r", linestyle="--")
        ax2.axvline(x=original_length, color="r", linestyle="--")

        # add a legend showing the original length
        ax1.legend([f"Original length: {original_length}"])
        ax2.legend([f"Original length: {original_length}"])
        plt.show()

    def create_input(self, number_cases: int):
        raise NotImplementedError(
            "You must implement a function to create a random input"
        )
