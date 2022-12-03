from solutions.SolutionBaseClass import AdventSolution
from pprint import pprint as pp


class Solution(AdventSolution):
    def __init__(self):
        super().__init__(day=2)
        self.score_system = {
            "A": 1,  # rock
            "B": 2,  # paper
            "C": 3,  # scissors
        }

        self.desencrpytion_part1 = {
            "X": "A",
            "Y": "B",
            "Z": "C",
        }

        self.desencrpytion_part2 = {
            "X": 0,
            "Y": 3,
            "Z": 6,
        }

        self.defeated_by = {
            "A": "B",  # rock is defeated by paper
            "B": "C",  # paper is defeated by scissors
            "C": "A",  # scissors is defeated by rock
        }

    def part1(self) -> int:
        game = [round.split() for round in self.problem_string.split("\n")]
        self.cache["game"] = game
        # let's assume that the letter with the highest count is the winner
        return sum(
            [
                self.determine_outcome_part1(round[0], self.desencrpytion_part1[round[1]])
                for round in game
            ]
        )

    def part2(self) -> int:
        game = self.cache["game"]
        return sum(
            [
                self.determine_outcome_part2(round[0], self.desencrpytion_part2[round[1]])
                for round in game
            ]
        )    

    def determine_outcome_part1(self, foe: str, player: str) -> int:
        move_score = self.score_system[player]
        if foe == player:
            game_score = 3  # draw
        elif self.defeated_by[foe] == player:
            game_score = 6  # win
        else:
            game_score = 0  # loss

        return game_score + move_score
    
    def determine_outcome_part2(self, foe: str, result: int) -> int:
        if result == 6:
            move = self.defeated_by[foe]
        elif result == 3:
            move = foe
        else:
            move = self.defeated_by[self.defeated_by[foe]]

        move_score = self.score_system[move]
        return move_score + result

