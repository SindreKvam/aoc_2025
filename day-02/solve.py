"""Day 02 Puzzle Solution"""

import argparse
import re


def parse_data(data):
    """Parse input data into a nice format"""

    # All data is in one single line
    split_data = data[0].strip().split(",")
    updated_data = []

    for ranges in split_data:
        range_from, range_to = ranges.split("-")

        updated_data.append((int(range_from), int(range_to) + 1))

    return updated_data


def solution1(data):
    """Solution to part 1

    Invalid IDs are values within a range that has a repeating pattern"""

    sum_invalid_ids = 0
    for slice in parse_data(data):
        for val in range(*slice):
            # If there is an odd number of characters in the number, the value cannot have a
            # repeating pattern by 2
            num_characters = len(str(val))
            if num_characters % 2 == 1:
                continue

            # Check if there is a repeating pattern by 2 in the value
            pattern = r"(\d{" + f"{num_characters // 2}" + r"})\1$"
            match = re.match(pattern, str(val))

            if match:
                sum_invalid_ids += int(match.group())
            else:
                continue

    return sum_invalid_ids


def solution2(data):
    """Solution to part 2"""

    sum_invalid_ids = 0
    for slice in parse_data(data):
        for val in range(*slice):
            num_characters = len(str(val))
            # Check if there is a repeating pattern by 2 in the value
            pattern = (
                r"(\d{1,"
                + f"{num_characters}"
                + r"})\1{1,"
                + f"{num_characters}"
                + r"}$"
            )
            match = re.match(pattern, str(val))

            if match:
                sum_invalid_ids += int(match.group())
            else:
                continue

    return sum_invalid_ids


if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", action="store_true")
    args = parser.parse_args()

    filename = "day-02/input.txt" if not args.debug else "day-02/example_input.txt"

    # Read the input file
    with open(filename, "r", encoding="utf-8") as f:
        DATA = f.readlines()

    answ1 = solution1(DATA)
    print(f"Solution 1: {answ1}")

    answ2 = solution2(DATA)
    print(f"Solution 2: {answ2}")
