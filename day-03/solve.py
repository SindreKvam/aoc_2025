"""Day 03 Puzzle Solution"""

import argparse

import numpy as np


def solution1(data, number_of_digits: int = 2):
    """Solution to part 1"""

    total_joltage = 0

    for line in data:
        line = line.strip()

        current_index = 0
        digits = []

        for digit in range(number_of_digits):
            possible_digits = [
                int(num)
                for num in line[
                    current_index : len(line) - number_of_digits + digit + 1
                ]
            ]
            current_index += np.argmax(possible_digits) + 1
            digits.append(
                np.max(possible_digits) * 10 ** (number_of_digits - 1 - digit)
            )

        total_joltage += np.sum(digits)

    return total_joltage


def solution2(data):
    """Solution to part 2"""

    return solution1(data, number_of_digits=12)


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
