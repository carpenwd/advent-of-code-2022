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
            # We know everything on the edges is visible, so the first and last row are
            # Same with the first and last column
            if row_idx == 0 or row_idx == len(tree_matrix) - 1 or \
                col_idx == 0 or col_idx == len(tree_matrix[row_idx]) - 1:
                visibility_matrix[row_idx][col_idx] = 1
            else:
                # Now need to check the north, south, east, and west directions
                north_val = check_north(tree_matrix, row_idx, col_idx)
                south_val = check_south(tree_matrix, row_idx, col_idx)
                west_val = check_west(tree_matrix, row_idx, col_idx)
                east_val = check_east(tree_matrix, row_idx, col_idx)
                visibility_value = north_val or south_val or west_val or east_val
                visibility_matrix[row_idx][col_idx] = visibility_value

    # Cycle through that matrix to count the results
    visibility_count = 0
    for row_idx, _ in enumerate(tree_matrix):
        for col_idx, _ in enumerate(_):
            visibility_count += visibility_matrix[row_idx][col_idx]
    return visibility_count


def check_north(tree_matrix, row_index, col_index):
    """
    Cycle through the columns in a northward direction to determine
    if the tree is visible
    """
    # Column value stays the same, row counts backwards starting at the current row_index
    north_list = []
    for nidx in range(row_index, -1, -1):
        north_list.append(tree_matrix[nidx][col_index])

    north_list.sort()
    if tree_matrix[row_index][col_index] == north_list[len(north_list) - 1]:
        # This means its the highest value, just need to determine if there's any duplicates
        if north_list.count(tree_matrix[row_index][col_index]) == 1:
            return 1
    return 0


def check_south(tree_matrix, row_index, col_index):
    """
    Cycle through the columns in a southward direction to determine
    if the tree is visible
    """
    # Column value stays the same, row counts forwards starting at the current row_index
    south_list = []
    for sidx in range(row_index, len(tree_matrix)):
        south_list.append(tree_matrix[sidx][col_index])

    south_list.sort()
    if tree_matrix[row_index][col_index] == south_list[len(south_list) - 1]:
        # This means its the highest value, just need to determine if there's any duplicates
        if south_list.count(tree_matrix[row_index][col_index]) == 1:
            return 1
    return 0


def check_west(tree_matrix, row_index, col_index):
    """
    Cycle through the rows in a westward direction to determine
    if the tree is visible
    """
    # Row value stays the same, col counts backwards starting at the current col_index
    west_list = []
    for widx in range(col_index, -1, -1):
        west_list.append(tree_matrix[row_index][widx])

    west_list.sort()
    if tree_matrix[row_index][col_index] == west_list[len(west_list) - 1]:
        # This means its the highest value, just need to determine if there's any duplicates
        if west_list.count(tree_matrix[row_index][col_index]) == 1:
            return 1
    return 0


def check_east(tree_matrix, row_index, col_index):
    """
    Cycle through the columns in a eastward direction to determine
    if the tree is visible
    """
    # Row value stays the same, col counts backwards starting at the current col_index
    east_list = []
    for eidx in range(col_index, len(tree_matrix)):
        east_list.append(tree_matrix[row_index][eidx])

    east_list.sort()
    if tree_matrix[row_index][col_index] == east_list[len(east_list) - 1]:
        # This means its the highest value, just need to determine if there's any duplicates
        if east_list.count(tree_matrix[row_index][col_index]) == 1:
            return 1
    return 0

if __name__ == "__main__":
    print(f"Number of tree's visible from outside the grid {scan_trees('day-8/tree_map.txt')}")
