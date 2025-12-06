"""Day 06 Puzzle Solution"""

import argparse

import numpy as np


def solution1(data):
    """Solution to part 1"""

    array = []
    operators = None
    for line in data:
        arr = list(filter(lambda x: x not in ["", "\n"], line.split(" ")))
        if "+" in arr or "*" in arr:
            operators = arr[:]
            continue
        array.append(np.array([int(val) for val in arr]))

    array = np.array(array).T

    sum = 0
    for idx, operator in enumerate(operators):
        if operator == "+":
            sum += np.sum(array[idx])
        if operator == "*":
            sum += np.prod(array[idx])

    return sum


def solution2(data):
    """Solution to part 2"""

    array = []
    operators = None
    for line in data:
        data = line.replace("\n", "")
        if "+" in data or "*" in data:
            operators = data[:]
            continue
        array.append(list(data))

    array = np.array(array).T

    sum = 0
    tmp = []
    for idx, line in enumerate(array[::-1], start=1):
        try:
            val = int("".join(line))
        except ValueError:
            # Skip spaces between numbers
            continue

        tmp.append(val)

        match operators[len(operators) - idx]:
            case "*":
                sum += np.prod(tmp)
                tmp = []
            case "+":
                sum += np.sum(tmp)
                tmp = []
            case _:
                continue

    return sum


if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", action="store_true")
    args = parser.parse_args()

    filename = "day-06/input.txt" if not args.debug else "day-06/example_input.txt"

    # Read the input file
    with open(filename, "r", encoding="utf-8") as f:
        data = f.readlines()

    answ1 = solution1(data)
    print(f"Solution 1: {answ1}")

    answ2 = solution2(data)
    print(f"Solution 2: {answ2}")
