"""
https://adventofcode.com/2022/day/4
"""

def calculate_assignments() -> int:
    """
    Method that will read in the puzzle input and calculate how many
    assignment pairs where one range fully contains the other
    """
    total_score = 0
    with open('day-4/section_assignments.txt', 'r', encoding="utf-8") as section_assignments:
        for line in section_assignments:
            total_score += calculate_assignment(line)

    return total_score

def calculate_assignment(input_line: str) -> int:
    """
    Method that will take an input line, separate it into two ranges,
    populate lists based off these ranges and then determine if one range
    overlaps with the other.
    """
    range_inputs = input_line.split(",")

    # Make lists out out of the input ranges
    first_list = []
    first_range = range_inputs[0].split("-")
    for index in range(int(first_range[0]), int(first_range[1]) + 1):
        first_list.append(index)

    second_list = []
    second_range = range_inputs[1].split("-")
    for index in range(int(second_range[0]), int(second_range[1]) + 1):
        second_list.append(index)

    # Now calculate the intersection between the two lists
    # If the length of the resulting intersection is greater than 1,
    # then return 1 for this method, otherwise return 0
    final_list = list(set(first_list).intersection(second_list))
    final_length = len(final_list)
    if final_length >= 1:
        return 1
    return 0


if __name__ == "__main__":
    print(f"Assignment pairs where one range fully contains the other: {calculate_assignments()}")
