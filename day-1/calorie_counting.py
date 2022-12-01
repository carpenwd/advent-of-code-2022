"""
https://adventofcode.com/2022/day/1

Part 1: Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
Part 2: Find the top three Elves carrying the most Calories. 
        How many Calories are those Elves carrying in total?
"""
with open('day-1/calorie_input.txt', 'r', encoding="utf-8") as calorie_file:
    ELF_COUNT = 1
    CALORIE_COUNT = 0
    calorie_dict = {}
    for line in calorie_file:
        line = line.strip()
        if '' == line:
            calorie_dict[ELF_COUNT] = CALORIE_COUNT
            ELF_COUNT += 1
            CALORIE_COUNT = 0
        else:
            CALORIE_COUNT += int(line)

    sorted_calories = sorted(calorie_dict.items(), key=lambda x:x[1], reverse=True)
    converted_dict = dict(sorted_calories)

    # Part 1
    print(f"Elf: {list(converted_dict.keys())[0]}, Calories: {list(converted_dict.values())[0]}")

    # Part 2
    TOP_THREE_COUNT = 0
    for index in range(0, 3):
        TOP_THREE_COUNT += list(converted_dict.values())[index]

    print(f"Top 3 calorie count: {TOP_THREE_COUNT}")
