from solutions.SolutionBaseClass import AdventSolution

class Day1(AdventSolution):
    def __init__(self):
        super().__init__(day=1)

    def part1(self) -> int:
        elfs_snacks = [list(map(int, elf.split('\n'))) for elf in self.problem_string.split('\n\n')]
        self.cache['elfs_snacks'] = elfs_snacks
        snack_count = [sum(snack) for snack in elfs_snacks]
        return max(snack_count)

    def part2(self) -> int:
        elfs_snacks = self.cache['elfs_snacks']
        snack_count = [len(set(snack)) for snack in elfs_snacks]
        return max(snack_count)