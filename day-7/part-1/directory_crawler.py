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

    def find_directory(self, name: str):
        """
        Method that will recursively search through the child directories
        to find the matching directory instance
        """
        for child in self.children:
            directory = None
            if child.name == name:
                directory = child
            else:
                if child.has_children():
                    child.find_directory(name)
            return directory

    def handle_cmd(self, cmd: str) -> None:
        """
        Method that will parse the cli input and either
        create subdirectories or add files to the current directory
        """
        cmd_segments = cmd.split(" ")
        if cmd_segments[0] == "dir":
            self.add_child_dir(Directory(name=cmd_segments[1], parent=self.parent))
        else:
            self.add_file(cmd_segments[1], cmd_segments[0])


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
            line = line.strip()
            line_segments = line.split(" ")
            if line.startswith("$ cd"):
                # Inside a change directory command
                if line_segments[2] == "..":
                    current_directory = dir_listing.find_directory(parent)
                else:
                    current_directory = dir_listing.find_directory(line_segments[2])
                    if current_directory == None:
                        current_directory = Directory(name=line_segments[2], parent=parent)
                        dir_listing.add_child_dir(current_directory)
            elif line.startswith("$ ls"):
                # Start of a list command
                parent = line_segments[2]
            else:
                current_directory.handle_cmd(line)
   
    return dir_listing

if __name__ == "__main__":
    print(f"Directory contents {process_commands('day-7/example_commands.txt')}")
