"""
Class for storing monkey information
"""

from abc import ABC, abstractmethod
from math import floor

class Monkey(ABC):
    """
    Abstract class for Monkey shenanigans
    """
    items = []
    inspected_count = 0

    @abstractmethod
    def evaluate_items(self):
        """
        Check if there are any items to evaluate, return empty dict
        Otherwise, increment inspected_count then perform the method and
        return a dict for item to throw
        """

    def has_items(self):
        """
        Check to see if Monkey has any items to evaluate
        """
        return len(self.items)

    def add_items(self, new_items):
        """
        Add items to the Monkey to evaluate
        """
        for item in new_items:
            self.items.append(item)

    def remove_item(self, item):
        """
        Remove items from the Monkey's items
        """
        index = self.items.index(item)
        self.items.pop(index)


class Monkey0(Monkey):
    """
    Info for Monkey 0
    """
    def __init__(self) -> None:
        super().__init__()
        self.items = [50, 70, 54, 83, 52, 78]

    def evaluate_items(self):
        """
        Operation: new = old * 3
            Test: divisible by 11
            If true: throw to monkey 2
            If false: throw to monkey 7
        """
        if not self.has_items():
            return {}

        throw_to_two = []
        throw_to_seven = []
        items_copy = self.items[:]
        for item in items_copy:
            self.inspected_count += 1

            worry_level = floor((item * 3) / 3)
            if worry_level % 11 == 0:
                throw_to_two.append(worry_level)
            else:
                throw_to_seven.append(worry_level)

            self.remove_item(item)

        return {2: throw_to_two, 7: throw_to_seven}


class Monkey1(Monkey):
    """
    Info for Monkey 1
    """
    def __init__(self) -> None:
        super().__init__()
        self.items = [71, 52, 58, 60, 71]

    def evaluate_items(self):
        """
        Operation: new = old * old
            Test: divisible by 7
            If true: throw to monkey 0
            If false: throw to monkey 2
        """
        if not self.has_items():
            return {}

        throw_to_zero = []
        throw_to_two = []
        items_copy = self.items[:]
        for item in items_copy:
            self.inspected_count += 1

            worry_level = floor((pow(item, 2)) / 3)
            if worry_level % 7 == 0:
                throw_to_zero.append(worry_level)
            else:
                throw_to_two.append(worry_level)

            self.remove_item(item)

        return {0: throw_to_zero, 2: throw_to_two}


class Monkey2(Monkey):
    """
    Info for Monkey 2
    """
    def __init__(self) -> None:
        super().__init__()
        self.items = [66, 56, 56, 94, 60, 86, 73]

    def evaluate_items(self):
        """
        Operation: new = old + 1
            Test: divisible by 3
            If true: throw to monkey 7
            If false: throw to monkey 5
        """
        if not self.has_items():
            return {}

        throw_to_five = []
        throw_to_seven = []
        items_copy = self.items[:]
        for item in items_copy:
            self.inspected_count += 1

            worry_level = floor((item + 1) / 3)
            if worry_level % 3 == 0:
                throw_to_seven.append(worry_level)
            else:
                throw_to_five.append(worry_level)

            self.remove_item(item)

        return {5: throw_to_five, 7: throw_to_seven}

class Monkey3(Monkey):
    """
    Info for Monkey 3
    """
    def __init__(self) -> None:
        super().__init__()
        self.items = [83, 99]

    def evaluate_items(self):
        """
        Operation: new = old + 8
            Test: divisible by 5
            If true: throw to monkey 6
            If false: throw to monkey 4
        """
        if not self.has_items():
            return {}

        throw_to_four = []
        throw_to_six = []
        items_copy = self.items[:]
        for item in items_copy:
            self.inspected_count += 1

            worry_level = floor((item + 8) / 3)
            if worry_level % 5 == 0:
                throw_to_six.append(worry_level)
            else:
                throw_to_four.append(worry_level)

            self.remove_item(item)

        return {6: throw_to_six, 4: throw_to_four}


class Monkey4(Monkey):
    """
    Info for Monkey 4
    """
    def __init__(self) -> None:
        super().__init__()
        self.items = [98, 98, 79]

    def evaluate_items(self):
        """
        Operation: new = old + 3
            Test: divisible by 17
            If true: throw to monkey 1
            If false: throw to monkey 0
        """
        if not self.has_items():
            return {}

        throw_to_zero = []
        throw_to_one = []
        items_copy = self.items[:]
        for item in items_copy:
            self.inspected_count += 1

            worry_level = floor((item + 3) / 3)
            if worry_level % 17 == 0:
                throw_to_one.append(worry_level)
            else:
                throw_to_zero.append(worry_level)

            self.remove_item(item)

        return {0: throw_to_zero, 1: throw_to_one}


class Monkey5(Monkey):
    """
    Info for Monkey 5
    """
    def __init__(self) -> None:
        super().__init__()
        self.items = [76]

    def evaluate_items(self):
        """
        Operation: new = old + 4
            Test: divisible by 13
            If true: throw to monkey 6
            If false: throw to monkey 3
        """
        if not self.has_items():
            return {}

        throw_to_three = []
        throw_to_six = []
        items_copy = self.items[:]
        for item in items_copy:
            self.inspected_count += 1

            worry_level = floor((item + 4) / 3)
            if worry_level % 13 == 0:
                throw_to_six.append(worry_level)
            else:
                throw_to_three.append(worry_level)

            self.remove_item(item)

        return {3: throw_to_three, 6: throw_to_six}


class Monkey6(Monkey):
    """
    Info for Monkey 6
    """
    def __init__(self) -> None:
        super().__init__()
        self.items = [52, 51, 84, 54]

    def evaluate_items(self):
        """
        Operation: new = old * 17
            Test: divisible by 19
            If true: throw to monkey 4
            If false: throw to monkey 1
        """
        if not self.has_items():
            return {}

        throw_to_one = []
        throw_to_four = []
        items_copy = self.items[:]
        for item in items_copy:
            self.inspected_count += 1

            worry_level = floor((item * 17) / 3)
            if worry_level % 19 == 0:
                throw_to_four.append(worry_level)
            else:
                throw_to_one.append(worry_level)

            self.remove_item(item)

        return {1: throw_to_one, 4: throw_to_four}


class Monkey7(Monkey):
    """
    Info for Monkey 7
    """
    def __init__(self) -> None:
        super().__init__()
        self.items = [82, 86, 91, 79, 94, 92, 59, 94]

    def evaluate_items(self):
        """
        Operation: new = old + 7
            Test: divisible by 2
            If true: throw to monkey 5
            If false: throw to monkey 3
        """
        if not self.has_items():
            return {}

        throw_to_three = []
        throw_to_five = []
        items_copy = self.items[:]
        for item in items_copy:
            self.inspected_count += 1

            worry_level = floor((item + 7) / 3)
            if worry_level % 2 == 0:
                throw_to_five.append(worry_level)
            else:
                throw_to_three.append(worry_level)

            self.remove_item(item)

        return {3: throw_to_three, 5: throw_to_three}
