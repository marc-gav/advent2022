f = open("problem1.txt", "r")

elfs_snacks = [list(map(int, elf.split('\n'))) for elf in f.read().split('\n\n')]
snack_count = [sum(snack) for snack in elfs_snacks]
print(f"Solution 1: {max(snack_count)}")
print(f"Solution 2: {sum(sorted(snack_count, reverse=True)[:3])}")