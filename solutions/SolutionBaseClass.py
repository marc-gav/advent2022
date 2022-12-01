import cProfile
import pstats

def profileit(func):
    def wrapper(*args, **kwargs):
        # only show filename and line number
        prof = cProfile.Profile()
        prof.runcall(func, *args, **kwargs)
        p = pstats.Stats(prof)
        p.strip_dirs()
        # print the stats, sort by cumulative time
        print(f'Profile for {func.__name__.split("_")[1]}:')
        p.sort_stats('cumulative').print_stats()

    return wrapper

class AdventSolution():
    def __init__(self, day):
        print(f'Reading problem input from: "problem_inputs/day{day}.txt"')
        with open(f'problem_inputs/day{day}.txt', 'r', encoding='utf-8') as f:
            self.problem_string = f.read()
        self.day = day
        self.cache = {}
    
    def part1(self):
        raise NotImplementedError("You must implement part 1")

    def part2(self):
        raise NotImplementedError("You must implement part 2")

    @profileit
    def profile_part1(self):
        self.part1()
    
    @profileit
    def profile_part2(self):
        self.part2()