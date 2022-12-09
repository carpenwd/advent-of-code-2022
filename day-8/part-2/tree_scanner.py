"""
https://adventofcode.com/2022/day/8
"""

def scan_trees(file_input: str) -> int:
    """
    Method that will take in the puzzle input and calculate
    the number of trees that are visibl from outside the grid
    """
    tree_matrix = []
    visibility_matrix = []
    with open(file_input, 'r', encoding="utf-8") as tree_map:
        for line in tree_map:
            line = line.strip()
            tree_list = []
            visibility_row = []
            for string in list(line):
                tree_list.append(int(string))
                visibility_row.append(0)
            tree_matrix.append(tree_list)
            visibility_matrix.append(visibility_row)

    # Cycle through the matrix and determine visibility and
    # store the results in a separete bool 2D matrix
    for row_idx, _ in enumerate(tree_matrix):
        for col_idx, _ in enumerate(_):
            # If a tree is right on the edge, at least one of its viewing distances will be zero
            if row_idx == 0 or row_idx == len(tree_matrix) - 1 or \
                col_idx == 0 or col_idx == len(tree_matrix[row_idx]) - 1:
                visibility_matrix[row_idx][col_idx] = 0
            else:
                # Now need to check the north, south, east, and west directions
                north_val = check_north(tree_matrix, row_idx, col_idx)
                south_val = check_south(tree_matrix, row_idx, col_idx)
                west_val = check_west(tree_matrix, row_idx, col_idx)
                east_val = check_east(tree_matrix, row_idx, col_idx)
                visibility_value = north_val * south_val * west_val * east_val
                visibility_matrix[row_idx][col_idx] = visibility_value

    print(visibility_matrix)

    # Cycle through that matrix to get the highest scenic score
    scenic_score = 0
    for row_idx, _ in enumerate(tree_matrix):
        for col_idx, _ in enumerate(_):
            scenic_score = max(scenic_score, visibility_matrix[row_idx][col_idx])
    return scenic_score


def check_north(tree_matrix, row_index, col_index):
    """
    Cycle through the columns in a northward direction to determine the scenic_score
    """
    # Column value stays the same, row counts backwards starting at the current row_index
    scenic_score = 0
    compare_value = tree_matrix[row_index][col_index]
    for nidx in range(row_index, -1, -1):
        if nidx == 0:
            return scenic_score
        if compare_value <= tree_matrix[nidx - 1][col_index]:
            scenic_score += 1
            return scenic_score
        scenic_score += 1


def check_south(tree_matrix, row_index, col_index):
    """
    Cycle through the columns in a southward directionto determine the scenic_score
    """
    # Column value stays the same, row counts forwards starting at the current row_index
    scenic_score = 0
    compare_value = tree_matrix[row_index][col_index]
    for sidx in range(row_index, len(tree_matrix)):
        if sidx == len(tree_matrix) - 1:
            return scenic_score
        if compare_value <= tree_matrix[sidx + 1][col_index]:
            scenic_score += 1
            return scenic_score
        scenic_score += 1


def check_west(tree_matrix, row_index, col_index):
    """
    Cycle through the rows in a westward direction to determine the scenic_score
    """
    # Row value stays the same, col counts backwards starting at the current col_index
    scenic_score = 0
    compare_value = tree_matrix[row_index][col_index]
    for widx in range(col_index, -1, -1):
        if widx == 0:
            return scenic_score
        if compare_value <= tree_matrix[row_index][widx - 1]:
            scenic_score += 1
            return scenic_score
        scenic_score += 1


def check_east(tree_matrix, row_index, col_index):
    """
    Cycle through the columns in a eastward direction to determine
    if the tree is visible
    """
    # Row value stays the same, col counts backwards starting at the current col_index
    scenic_score = 0
    compare_value = tree_matrix[row_index][col_index]
    for eidx in range(col_index, len(tree_matrix)):
        if eidx == len(tree_matrix) - 1:
            return scenic_score
        if compare_value <= tree_matrix[row_index][eidx + 1]:
            scenic_score += 1
            return scenic_score
        scenic_score += 1


if __name__ == "__main__":
    print(f"Highest scenic score: {scan_trees('day-8/tree_map.txt')}")
