"""Day 09 Puzzle Solution"""

import argparse

import numpy as np


def parse_data_to_vectors(data) -> np.ndarray:
    num_red_tiles = len(data)
    coordinates = np.ndarray((num_red_tiles, 2), dtype=int)
    for idx, line in enumerate(data):
        coordinates[idx] = np.array(line.split(","))

    return coordinates


def solution1(data):
    """Solution to part 1"""

    coordinates = parse_data_to_vectors(data)

    # Find all possible 2d distances between all coordinates
    distances = abs(coordinates[:, None, :] - coordinates)
    side_lengths = distances + 1
    rectangle_areas = np.prod(side_lengths, axis=2)

    return np.max(rectangle_areas)


def solution2(data):
    """Solution to part 2"""

    coordinates = parse_data_to_vectors(data)

    distances = coordinates[:, None, :] - coordinates

    # Find lines that make up the grid
    vertical_lines = []
    horizontal_lines = []
    for idx in range(len(coordinates) - 1):
        if coordinates[idx][0] == coordinates[idx + 1][0]:
            # Horizontal coordinates are identical
            vertical_lines.append(
                [coordinates[idx, 0], coordinates[idx, 1], coordinates[idx + 1, 1]]
            )

        elif coordinates[idx][1] == coordinates[idx + 1][1]:
            horizontal_lines.append(
                [coordinates[idx, 1], coordinates[idx, 0], coordinates[idx + 1, 0]]
            )

    # Extra step to wrap around
    if coordinates[-1][0] == coordinates[0][0]:
        vertical_lines.append(
            [coordinates[-1, 0], coordinates[-1, 1], coordinates[0, 1]]
        )
    if coordinates[-1][1] == coordinates[0][1]:
        horizontal_lines.append(
            [coordinates[-1, 1], coordinates[-1, 0], coordinates[0, 0]]
        )

    # Horizontal and vertical lines are now (N,3) matrices, where the first value
    # Contains the coordinate in the axis along its own axis, and the second
    # and third arguments are the start and end positions
    horizontal_lines = np.array(horizontal_lines)
    vertical_lines = np.array(vertical_lines)

    print(horizontal_lines)
    print(vertical_lines)

    print(coordinates[:,None,:] + distances)
    # If some of the lines intercept the walls of the rectangles, then it is not a valid square
    # for x, start, end in horizontal_lines:
    #     print(x, start, end)
    #
    # for dist in distances:
    #     print(dist + coordinates)


    distances = abs(distances)
    side_lengths = distances + 1

    rectangle_areas = np.prod(side_lengths, axis=2)

    return


if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", action="store_true")
    args = parser.parse_args()

    filename = "day-09/input.txt" if not args.debug else "day-09/example_input.txt"

    # Read the input file
    with open(filename, "r", encoding="utf-8") as f:
        data = f.readlines()

    answ1 = solution1(data)
    print(f"Solution 1: {answ1}")

    answ2 = solution2(data)
    print(f"Solution 2: {answ2}")
