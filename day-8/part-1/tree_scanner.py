"""
https://adventofcode.com/2022/day/8
"""

def scan_trees(file_input: str) -> int:
    """
    Method that will take in the puzzle input and calculate
    the number of trees that are visibl from outside the grid
    """
    tree_matrix = []
    with open(file_input, 'r', encoding="utf-8") as tree_map:
        for line in tree_map:
            line = line.strip()
            tree_list = []
            for string in list(line):
                tree_list.append(int(string))
            tree_matrix.append(tree_list)

    # Cycle through the matrix and determine visibility and
    # store the results in a separete bool 2D matrix
        
    # Cycle through that matrix to count the results


if __name__ == "__main__":
    print(f"Number of tree's visible from outside the grid {scan_trees('day-8/tree_map.txt')}")
