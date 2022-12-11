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

    def has_children(self) -> bool:
        """
        Method for determing if this directory has any children
        """
        if len(self.children) > 0:
            return True
        return False

    def add_file(self, name: str, size: int) -> None:
        """
        Method for adding a file to the directory list
        """
        self.files.append({"file_name": name, "file_size": size})

    def find_child_dir(self, name: str):
        """
        Method that will attempt to find a directory within this instances children
        """
        search_directory = None
        if self.has_children():
            for child in self.children:
                if child.name == name:
                    return child
        return search_directory

    def handle_cmd(self, cmd: str, parent: str) -> None:
        """
        Method that will parse the cli input and either
        create subdirectories or add files to the current directory
        """
        cmd_segments = cmd.split(" ")
        if cmd_segments[0] == "dir":
            self.add_child_dir(Directory(name=cmd_segments[1], parent=parent))
        else:
            self.add_file(cmd_segments[1], cmd_segments[0])


def process_commands(file_input: str) -> dict:
    """
    Method that will taken in the provided command input and formulate a dictionary
    that represents the directory structure based off those commands
    """
    dir_listing = Directory()
    with open(file_input, 'r', encoding="utf-8") as command_input:
        current_directory = None
        for line in command_input:
            line = line.strip()
            if line == "$ cd /":
                current_directory = dir_listing
                continue

            line_segments = line.split(" ")
            if line.startswith("$ cd"):
                # Inside a change directory command
                if line_segments[2] == "..":
                    # TODO Instead of attempting to recursively search through this, just keep track of the hierarchy in a list
                    # Should enable some quick navigation that way
"""                     current_directory = find_directory(
                        dir_listing,
                        current_directory.parent,
                        current_directory.name
                    ) """
                else:
                    search_directory = current_directory.find_child_dir(line_segments[2])
                    if search_directory:
                        current_directory = search_directory
                    else:
                        new_dir = Directory(name=line_segments[2], parent=current_directory.name)
                        current_directory.add_child_dir(new_dir)
                        current_directory = new_dir
            elif line.startswith("$ ls"):
                # Start of a list command, nothing really to do
                continue
            else:
                current_directory.handle_cmd(line, current_directory.name)

    return dir_listing

if __name__ == "__main__":
    print(f"Directory contents {process_commands('day-7/commands.txt')}")
