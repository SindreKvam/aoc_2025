"""Day 04 Puzzle Solution"""

import argparse

import numpy as np


def parse_data_to_np_array(data) -> np.ndarray:
    # Add a grid of zeros around the entire board, to not have to wory about edge cases
    arr = np.zeros((len(data) + 2, len(data[0]) + 2), dtype=int)

    for idx, _ in enumerate(data, start=1):
        for jdx, val in enumerate(data[idx - 1], start=1):
            arr[idx][jdx] = 1 if val == "@" else 0

    return arr


def solution1(data):
    """Solution to part 1"""

    kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])

    to_be_removed = []
    for idx, _ in enumerate(data[1:-1], start=1):
        for jdx, val in enumerate(data[idx][1:-1], start=1):
            # If value in array contains a roll
            if data[idx, jdx]:
                # Check all surrounding values
                result = data[idx - 1 : idx + 2, jdx - 1 : jdx + 2] * kernel
                # If less than 4 of the surrounding contains a roll, mark the roll
                if np.sum(result) < 4:
                    to_be_removed.append((idx, jdx))
            else:
                continue

    return len(to_be_removed), to_be_removed


def solution2(data):
    """Solution to part 2"""

    num_to_be_removed, to_be_removed = solution1(data)
    sum = 0
    while num_to_be_removed > 0:
        for coord in to_be_removed:
            data[coord[0]][coord[1]] = 0

        sum += num_to_be_removed
        num_to_be_removed, to_be_removed = solution1(data)

    return sum


if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", action="store_true")
    args = parser.parse_args()

    filename = "day-04/input.txt" if not args.debug else "day-04/example_input.txt"

    # Read the input file
    with open(filename, "r", encoding="utf-8") as f:
        data = f.readlines()

    data = [line.strip() for line in data]
    arr = parse_data_to_np_array(data)

    answ1, _ = solution1(arr)
    print(f"Solution 1: {answ1}")

    answ2 = solution2(arr)
    print(f"Solution 2: {answ2}")
