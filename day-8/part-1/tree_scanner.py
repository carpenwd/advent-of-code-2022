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
    for row in range(0, len(tree_matrix)):
        for col in range(0, len(tree_matrix[row])):
            # We know everything on the edges is visible, so the first and last row are
            # Same with the first and last column
            if row == 0 or row == len(tree_matrix) - 1 or col == 0 or col == len(tree_matrix[row]) - 1:
                visibility_matrix[row][col] = 1
            else:
                # Now need to check the north, south, east, and west directions
                check_north(tree_matrix, 4, 3)
                continue

    # Cycle through that matrix to count the results
    visibility_count = 0
    for row in range(0, len(tree_matrix)):
        for col in range(0, len(tree_matrix[row])):
            visibility_count += visibility_matrix[row][col]
    return visibility_count


def check_north(tree_matrix, row_index, col_index):
    """
    Cycle through the columns in a northward direction to determine
    if the tree is visible
    """
    # Column value stays the same, row counts backwards starting at the current row_index
    north_list = []
    for nidx in range(row_index, 0, -1):
        print(tree_matrix[nidx][col_index])



if __name__ == "__main__":
    print(f"Number of tree's visible from outside the grid {scan_trees('day-8/example_tree_map.txt')}")
