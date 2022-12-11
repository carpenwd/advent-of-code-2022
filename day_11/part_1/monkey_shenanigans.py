"""
https://adventofcode.com/2022/day/11
"""

from monkey import Monkey0, Monkey1, Monkey2, Monkey3, Monkey4, Monkey5, Monkey6, Monkey7

MONKEY_DICT = {
    0: Monkey0(),
    1: Monkey1(),
    2: Monkey2(),
    3: Monkey3(),
    4: Monkey4(),
    5: Monkey5(),
    6: Monkey6(),
    7: Monkey7()
}

if __name__ == "__main__":
    monkey_dict = {}
    for index in range(1, 21):
        for key, value in MONKEY_DICT.items():
            result = value.evaluate_items()

            for k, v in result.items():
                MONKEY_DICT[k].add_items(v)

        print(f"After round {index}, the monkeys are holding items with these worry levels:")
        for key, value in MONKEY_DICT.items():
            print(f"Monkey {key}: {value.items}")

    for key, value in MONKEY_DICT.items():
        print(f"Monkey {key} insepcted items {value.inspected_count} times")
