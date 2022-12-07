"""
https://adventofcode.com/2022/day/7
"""

class Directory():
    """
    Essentially a generic tree structure
    """
    def __init__(self, name='/', parent=None, children=None):
        self.name = name
        self.parent = parent
        self.total_size = 0
        self.files = []
        self.children = []
        if children is not None:
            for child in children:
                self.add_child_dir(child)

    def __repr__(self):
        return self.name

    def add_child_dir(self, node) -> None:
        """
        Method for adding a child to the directory
        """
        assert isinstance(node, Directory)
        self.children.append(node)

    def add_file(self, name, size) -> None:
        """
        Method for adding a file to the directory list
        """
        self.files.append({"file_name": name, "file_size": size})

    # TODO Add method for finding directory instance and returning that instance
    #      This can also be used for checking the existance of a directory

def process_commands(file_input: str) -> dict:
    """
    Method that will taken in the provided command input and formulate a dictionary
    that represents the directory structure based off those commands
    """
    dir_listing = Directory()
    with open(file_input, 'r', encoding="utf-8") as command_input:
        parent = None
        current_directory = None
        for line in command_input:
            line_segments = line.split(" ")
            if line.startswith("$ cd"):
                # Inside a change directory command
                if parent == "..":
                    # get_parent_directory(parent)
                    continue

            elif line.startswith("$ ls"):
                # Start of a list command
                parent = line_segments[2]
                continue
            else:
                #handle_list_cmd()
                continue


        # Notes:
        # Might help to create my own class for this one that will calculate the total file sizes as they are added
        # (i.e. make a 'get_dir_size' command that will recursively search through the child to get the total)

    
    return dir_listing

if __name__ == "__main__":
    print(f"Directory contents {process_commands('day-7/example_commands.txt')}")
