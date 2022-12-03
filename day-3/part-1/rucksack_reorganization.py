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
        for line in rucksack_contents:
            total_score += calculate_sum(line)

    return total_score


def calculate_sum(input_line: str) -> int:
    """
    Method for taking in an input line and calculating the resulting priority score
    """
    # Divide the input line in half
    input_list = list(input_line)
    first_half = input_list[:len(input_list) // 2]
    second_half = input_list[len(input_list) // 2:]

    # Uncomment to see where the input line is being split
    # print(f"First half: {first_half} - Second half {second_half}")

    # Get the intersection of the two halfs
    intersection_set = contents_intersection(first_half, second_half)

    # Grab the priority value based off the resulting value
    return PRIORITIES[intersection_set.pop()]


def contents_intersection(list_1: list, list_2: list) -> set:
    """
    Method for calulating the intersection between two given lists
    """
    return set(list_1).intersection(list_2)


if __name__ == "__main__":
    print(f"Final sum of priorites: {calculate_total_sum()}")
