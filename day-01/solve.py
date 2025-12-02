"""Day 01 Puzzle Solution"""

import argparse

import numpy as np


class RotationWheel:
    """Implementation of a number dial that keeps track of how many times
    it has landed on, or passed the digit zero
    """

    num_zeros: int = None
    num_passed_zeros: int = None

    current_position: int = None
    num_positions: int = None
    rotation_wheel: np.ndarray = None

    def __init__(self, start_position: int = 50, num_positions: int = 100):
        """Initialize a wheel that wraps around"""

        self.current_position = start_position
        self.num_positions = num_positions

        self.num_zeros = 0
        self.num_passed_zeros = 0

        self.rotation_wheel = np.linspace(
            0, num_positions - 1, num_positions, dtype=int
        )

    def _count_full_rotations(self, distance: int) -> int:
        """Count how many full rotations are performed"""

        return distance // self.num_positions

    def _check_if_pass_zero(self, distance: int, position:int) -> bool:
        """Check if we pass zero during the rotation"""

        if position != 0:
            return not (0 <= (position + distance) <= self.num_positions)

        else:
            return False

    def turn_dial(self, distance: int) -> int:
        """Turn dial, supports both positive and negative distances"""

        # Check how many times we will pass zero
        self.num_passed_zeros += int(self._check_if_pass_zero(distance, self.current_position))
        self.num_passed_zeros += self._count_full_rotations(np.abs(distance))

        # Edgecase: if we stand on zero and perform only full rotations
        # Do not count the final rotation, as it will be counted as landed on zero
        # Not that we pass it.
        if self._count_full_rotations(np.abs(distance)) > 0 and (distance % self.num_positions) == 0:
            self.num_passed_zeros -= 1

        # Find the new position that we will get
        new_position = self.rotation_wheel[
            (self.current_position + distance) % self.num_positions
        ]

        # Check if we landed on a zero
        if new_position == 0:
            self.num_zeros += 1

        return new_position

    def turn_right(self, distance: int):
        """Turn the dial to the right"""

        # Move the pointer to new position
        self.current_position = self.turn_dial(distance)

    def turn_left(self, distance: int):
        """Turn the dial to the left"""

        # Move the pointer to new position
        self.current_position = self.turn_dial(-distance)

    def __repr__(self):
        data = f"Number of zeros landed on: {self.num_zeros}\n"
        data += f"Number of zeros passed: {self.num_passed_zeros}\n"
        data += f"Total: {self.num_zeros + self.num_passed_zeros}"
        return data


def solution1(
    data,
    start_position: int = 50,
    num_positions: int = 100,
):
    """Solution to part 1"""

    wheel = RotationWheel(start_position, num_positions)

    for line in data:
        direction, distance = line[0], int(line[1:])

        match direction.lower():
            case "l":
                wheel.turn_left(distance)
            case "r":
                wheel.turn_right(distance)
            case _:
                raise ValueError("Invalid direction")

    return wheel


def solution2(data, start_position: int = 50, num_positions: int = 100):
    """Solution to part 2"""

    # Tried to get it working as a part of solution 1, but there is some edgecase
    # I am not catching. So here is a brute force implementation instead
    position = start_position
    sum = 0

    for line in data:
        direction, distance = line[0], int(line[1:])

        match direction.lower():
            case "l":
                step = -1
            case "r":
                step = 1
            case _:
                raise ValueError("Invalid direction")

        for idx in range(distance):
            position = (position + step) % num_positions

            if position == 0:
                sum += 1

    return sum

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", action="store_true")
    args = parser.parse_args()

    filename = "day-01/input.txt" if not args.debug else "day-01/example_input.txt"

    # Read the input file
    with open(filename, "r", encoding="utf-8") as f:
        DATA = f.readlines()

    answ1 = solution1(DATA)
    print(f"Solution 1: \n{answ1}")

    answ2 = solution2(DATA)
    print(f"Solution 2: {answ2}")
