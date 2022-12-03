"""
https://adventofcode.com/2022/day/2

Given strategy guide input, calculate total score to Rock, Paper, Scissors

A and X == Rock
B and Y == Paper
C and Z == Scissors

Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.
If both players choose the same shape, the round instead ends in a draw.

IMPORTANT: The second column says how the round needs to end:
    - X means you need to lose
    - Y means you need to end the round in a draw
    - Z means you need to win

The score for a single round is the score for the shape you selected:
    - 1 for Rock
    - 2 for Paper
    - 3 for Scissors
Plus the score for the outcome of the round:
    - 0 if you lost
    - 3 if the round was a draw
    - 6 if you won
"""
ROCK_SCORE = 1
PAPER_SCORE = 2
SCISSORS_SCORE = 3
WIN_SCORE = 6
DRAW_SCORE = 3
LOSE_SCORE = 0

def calculate_score() -> int:
    """
    Method for reading in the strategy guide and calculating the final score
    """
    total_score = 0
    with open('day-2/strategy_guide.txt', 'r', encoding="utf-8") as strategy_guide:
        for line in strategy_guide:
            total_score += calculate_round(line)

    return total_score


def calculate_round(line_input: str) -> int:
    """
    Method that takes an match input and caluclates the score based off its result.

    Args:
      line_input (str): Individual line from the strategy guide

    Returns:
      Total score for the round based off what you played and the result
    """
    round_score = 0
    line_parts = line_input.split(" ")
    if line_parts[0].casefold() == "a" and line_parts[1].strip().casefold() == "x":
        round_score = SCISSORS_SCORE + LOSE_SCORE
    elif line_parts[0].casefold() == "a" and line_parts[1].strip().casefold() == "y":
        round_score = ROCK_SCORE + DRAW_SCORE
    elif line_parts[0].casefold() == "a" and line_parts[1].strip().casefold() == "z":
        round_score = PAPER_SCORE + WIN_SCORE
    elif line_parts[0].casefold() == "b" and line_parts[1].strip().casefold() == "x":
        round_score = ROCK_SCORE + LOSE_SCORE
    elif line_parts[0].casefold() == "b" and line_parts[1].strip().casefold() == "y":
        round_score = PAPER_SCORE + DRAW_SCORE
    elif line_parts[0].casefold() == "b" and line_parts[1].strip().casefold() == "z":
        round_score = SCISSORS_SCORE + WIN_SCORE
    elif line_parts[0].casefold() == "c" and line_parts[1].strip().casefold() == "x":
        round_score = PAPER_SCORE + LOSE_SCORE
    elif line_parts[0].casefold() == "c" and line_parts[1].strip().casefold() == "y":
        round_score = SCISSORS_SCORE + DRAW_SCORE
    elif line_parts[0].casefold() == "c" and line_parts[1].strip().casefold() == "z":
        round_score = ROCK_SCORE + WIN_SCORE
    else:
        print("This shouldn't happen")

    return round_score

if __name__ == "__main__":
    print(f"Final score: {calculate_score()}")
