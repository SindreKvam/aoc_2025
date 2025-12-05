"""Day 05 Puzzle Solution"""

import argparse


def solution1(data):
    """Solution to part 1"""

    ranges = []
    file_index = 0
    for line in data:
        file_index += 1
        # The break between ranges and test-data is an empty line
        if line == "":
            break

        rang = line.split("-")
        min, max = [int(val) for val in rang]

        ranges.append((min, max))

    fresh_ingredients = 0
    for line in data[file_index:]:
        ingredient = int(line)

        for min, max in ranges:
            if min <= ingredient <= max:
                fresh_ingredients += 1
                break

    return fresh_ingredients


def solution2(data):
    """Solution to part 2"""

    ranges = []
    for line in data:
        # We are only interested in ranges in this problem
        if line == "":
            break

        rang = line.split("-")
        min1, max1 = [int(val) for val in rang]

        ranges.append((min1, max1))

    # Sort ranges based on the start value
    ranges = sorted(ranges, key=(lambda x: x[0]))

    # Merge overlapping ranges
    updated_ranges = [ranges[0]]
    for min1, max1 in ranges[1:]:
        last_min, last_max = updated_ranges[-1]

        if min1 <= last_max:
            updated_ranges[-1] = (last_min, max(last_max, max1))
        else:
            updated_ranges.append((min1, max1))

    # Count how many total values are within the ranges
    total_valid_ids = 0
    for min1, max1 in updated_ranges:
        total_valid_ids += max1 - min1 + 1

    return total_valid_ids


if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", action="store_true")
    args = parser.parse_args()

    filename = "day-05/input.txt" if not args.debug else "day-05/example_input.txt"

    # Read the input file
    with open(filename, "r", encoding="utf-8") as f:
        data = f.readlines()

    data = [line.strip() for line in data]

    answ1 = solution1(data)
    print(f"Solution 1: {answ1}")

    answ2 = solution2(data)
    print(f"Solution 2: {answ2}")
