"""
https://adventofcode.com/2022/day/5
"""

class CargoStacks:
    """
    Class to hold the cargo stacks and support their manipulation
    """
    stack_one: list = ['N', 'R', 'G', 'P']
    stack_two: list = ['J', 'T', 'B', 'L', 'F', 'G', 'D', 'C']
    stack_three: list = ['M', 'S', 'V']
    stack_four: list = ['L', 'S', 'R', 'C', 'Z', 'P']
    stack_five: list = ['P', 'S', 'L', 'V', 'C', 'W', 'D', 'Q']
    stack_six: list = ['C', 'T', 'N', 'W', 'D', 'M', 'S']
    stack_seven: list = ['H', 'D', 'G', 'W', 'P']
    stack_eight: list = ['Z', 'L', 'P', 'H', 'S', 'C', 'M', 'V']
    stack_nine: list = ['R', 'P', 'F', 'L', 'W', 'G', 'Z']

    stack_dict = {
        1: stack_one,
        2: stack_two,
        3: stack_three,
        4: stack_four,
        5: stack_five,
        6: stack_six,
        7: stack_seven,
        8: stack_eight,
        9: stack_nine
    }

    def handle_procedure_line(self, input_line: str) -> None:
        """
        Method for taking in a puzzle input line and moving the necessary crates around
        E.x. 'move 2 from 4 to 6' will move 2 entries from 'stack_four' into 'stack_six'
        """
        input_parts = input_line.split(' ')
        crate_amount = int(input_parts[1])
        source = int(input_parts[3])
        destination = int(input_parts[5])

        for _ in range (0, crate_amount):
            temp_crate = self.stack_dict[source].pop()
            self.stack_dict[destination].append(temp_crate)


    def get_top_of_stacks(self) -> str:
        """
        Method for retrieving the top value from each stack and outputing them in a string
        """
        resulting_str = self.stack_one.pop()
        resulting_str += self.stack_two.pop()
        resulting_str += self.stack_three.pop()
        resulting_str += self.stack_four.pop()
        resulting_str += self.stack_five.pop()
        resulting_str += self.stack_six.pop()
        resulting_str += self.stack_seven.pop()
        resulting_str += self.stack_eight.pop()
        resulting_str += self.stack_nine.pop()
        return resulting_str


if __name__ == "__main__":
    cargo_stacks = CargoStacks()
    with open('day-5/rearrangement_procedure.txt', 'r', encoding="utf-8") as procedure:
        for line in procedure:
            cargo_stacks.handle_procedure_line(line)

    print(f"Crates that are at the top of the stack: {cargo_stacks.get_top_of_stacks()}")
