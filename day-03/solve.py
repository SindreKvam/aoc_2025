"""Day 03 Puzzle Solution"""

import argparse

import numpy as np


def solution1(data):
    """Solution to part 1"""

    total_joltage = 0

    for line in data:
        line = line.strip()

        # Find the largest digit from the front
        first_digits_as_ints = [int(num) for num in line[:-1]]
        index_first_digit = np.argmax(first_digits_as_ints)

        # Find the largest digit after the first digit
        last_digits_as_ints = [int(num) for num in line[index_first_digit + 1 :]]
        index_last_digit = np.argmax(last_digits_as_ints) + index_first_digit + 1

        total_joltage += int(line[index_first_digit] + line[index_last_digit])

    return total_joltage


def solution2(data):
    """Solution to part 2"""

    return


if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", action="store_true")
    args = parser.parse_args()

    filename = "day-03/input.txt" if not args.debug else "day-03/example_input.txt"

    # Read the input file
    with open(filename, "r", encoding="utf-8") as f:
        DATA = f.readlines()

    answ1 = solution1(DATA)
    print(f"Solution 1: {answ1}")

    answ2 = solution2(DATA)
    print(f"Solution 2: {answ2}")
