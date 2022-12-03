"""
https://adventofcode.com/2022/day/3
"""

PRIORITES = {
    "a": 1,
    "A": 27
}

def calculate_sum() -> int:
    """
    Method for reading in the puzzle input and calculating the
    sum of the priorities within the rucksack contents
    """
    # TODO
    # 1) Check to see if everything can be split evenly (i.e. no odds)
    # 2) Set up the rest of the priorities dictionary
    # 3) Set up a method that will take a line input, split it and then find the same letter
    # 4) Double check to see if there can be more than one duplicate letter
    # 5) Have method return the score from the priorites dictionary
    # 6) Get the total score via cycling through every line and return that value
    return 0


if __name__ == "__main__":
    print(f"Final sum of priorites: {calculate_sum()}")
