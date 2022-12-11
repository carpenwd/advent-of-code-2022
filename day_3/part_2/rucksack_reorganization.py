"""
https://adventofcode.com/2022/day/3
"""

PRIORITIES = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "A": 27,
    "B": 28,
    "C": 29,
    "D": 30,
    "E": 31,
    "F": 32,
    "G": 33,
    "H": 34,
    "I": 35,
    "J": 36,
    "K": 37,
    "L": 38,
    "M": 39,
    "N": 40,
    "O": 41,
    "P": 42,
    "Q": 43,
    "R": 44,
    "S": 45,
    "T": 46,
    "U": 47,
    "V": 48,
    "W": 49,
    "X": 50,
    "Y": 51,
    "Z": 52
}

def calculate_total_sum() -> int:
    """
    Method for reading in the puzzle input and calculating the
    sum of the priorities within the rucksack contents
    """
    total_score = 0
    with open('day-3/contents.txt', 'r', encoding="utf-8") as rucksack_contents:
        file_lines = rucksack_contents.readlines()
        for index in range(0, len(file_lines) - 1, 3):
            total_score += calculate_sum(
                file_lines[index].strip(),
                file_lines[index + 1].strip(),
                file_lines[index + 2].strip()
            )

    return total_score


def calculate_sum(input_line_1: str, input_line_2: str, input_line_3: str) -> int:
    """
    Method for taking in an input line and calculating the resulting priority score
    """
    # Get the intersection of the two halfs
    intersection_set = contents_intersection(input_line_1, input_line_2, input_line_3)

    # Grab the priority value based off the resulting value
    return PRIORITIES[intersection_set.pop()]


def contents_intersection(list_1: list, list_2: list, list_3: list) -> set:
    """
    Method for calulating the intersection between three given lists
    """
    temp_set = set(list_1).intersection(list_2)
    return temp_set.intersection(list_3)


if __name__ == "__main__":
    print(f"Final sum of priorites: {calculate_total_sum()}")
