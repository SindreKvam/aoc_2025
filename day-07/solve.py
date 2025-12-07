"""Day 07 Puzzle Solution"""

import argparse
from collections import defaultdict


def findall(pattern: str, string: str):
    """Find all occurences of a substring inside a string"""
    idx = string.find(pattern)
    while idx != -1:
        yield idx
        idx = string.find(pattern, idx + 1)


def solution1(data):
    """Solution to part 1"""

    beam_indexes = []
    num_splits = 0
    for line in data:
        line = line.strip()

        # Beam starts from S indicator
        start_index = line.find("S")
        if start_index != -1:
            beam_indexes.append(start_index)

        # Position of beam splitters
        split_index = list(findall("^", line))

        # Check if we have a beam that is going to hit the splitter
        for splitter in split_index:
            if splitter in beam_indexes:
                beam_indexes.pop(beam_indexes.index(splitter))

                beam_indexes.append(splitter - 1)
                beam_indexes.append(splitter + 1)

                beam_indexes = list(set(beam_indexes))

                num_splits += 1

    return num_splits


def solution2(data):
    """Solution to part 2"""

    beams = defaultdict(int)

    for line in data:
        line = line.strip()

        # Beam starts from S indicator
        start_index = line.find("S")
        if start_index != -1:
            beams[f"{start_index}"] += 1

        split_index = list(findall("^", line))
        for splitter in split_index:
            beams[f"{splitter + 1}"] += beams[f"{splitter}"]
            beams[f"{splitter - 1}"] += beams[f"{splitter}"]
            beams[f"{splitter}"] = 0

    return sum(beams.values())


if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", action="store_true")
    args = parser.parse_args()

    filename = "day-07/input.txt" if not args.debug else "day-07/example_input.txt"

    # Read the input file
    with open(filename, "r", encoding="utf-8") as f:
        data = f.readlines()

    answ1 = solution1(data)
    print(f"Solution 1: {answ1}")

    answ2 = solution2(data)
    print(f"Solution 2: {answ2}")
