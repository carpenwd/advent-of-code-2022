"""
https://adventofcode.com/2022/day/2

Given strategy guide input, calculate total score to Rock, Paper, Scissors

A and X == Rock
B and Y == Paper
C and Z == Scissors

Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.
If both players choose the same shape, the round instead ends in a draw.
"""
def calculate_score() -> None:
    """
    Method for reading in the strategy guide and calculating the final score
    """
    total_score = 0
    with open('day-2/strategy_guide.txt', 'r', encoding="utf-8") as strategy_guide:
        for line in strategy_guide:
            total_score += calculate_round(line)

    return total_score


def calculate_round(line_input: str) -> None:
    """
    Method that takes an match input and caluclates the score based off its result.
    The score for a single round is the score for the shape you selected:
      - 1 for Rock
      - 2 for Paper
      - 3 for Scissors
    Plus the score for the outcome of the round:
      - 0 if you lost
      - 3 if the round was a draw
      - 6 if you won

    Args:
      line_input (str):

    Returns:

    """
    line_parts = line_input.split(" ")
    print(line_parts)
    return 0

if __name__ == "__main__":
    print(f"Final score: {calculate_score()}")
