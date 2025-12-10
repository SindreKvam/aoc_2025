"""Day 10 Puzzle Solution"""

import argparse
import re

from itertools import combinations


def parse_data(data):
    """Parse input data into 3 parts;
    indicator light diagrams, buttons and joltage requirements
    """

    indicator_lights = []
    buttons = []
    joltage = []

    for line in data:
        line = line.strip()

        indicator_lights_pattern = r"\[([\.\#]+)\]"
        indicator_lights += re.findall(indicator_lights_pattern, line)

        buttons_pattern = r"\(([\d\,]+)\)"
        buttons += [re.findall(buttons_pattern, line)]

        joltage_pattern = r"\{(.*)\}"
        joltage += re.findall(joltage_pattern, line)

    for idx, lights in enumerate(indicator_lights):
        indicator_lights[idx] = [True if s == "#" else False for s in lights]

    for idx, button in enumerate(buttons):
        for jdx, b in enumerate(button):
            buttons[idx][jdx] = [int(val) for val in b.split(",")]

    for idx, jolt in enumerate(joltage):
        joltage[idx] = [int(a) for a in jolt.split(",")]

    return indicator_lights, buttons, joltage


def push_button(lights: list[bool], button_label:list[int]):
    """button_label should contain the indexes of the lights we want to toggle,
    returns the updated lights"""

    new_lights = lights[:]
    for index in button_label:
        new_lights[index] = not new_lights[index]

    return new_lights


def solution1(data):
    """Solution to part 1"""
    light_diagram, button_wirings, _ = parse_data(data)

    for wanted_lights, buttons in zip(light_diagram, button_wirings):
        lights = [False] * len(wanted_lights)
        print(wanted_lights, buttons)

        print(lights)
        lights = push_button(lights, buttons[0])
        lights = push_button(lights, buttons[1])
        lights = push_button(lights, buttons[2])
        print(lights)

        if lights == wanted_lights:
            print("Solved")

        print("-"*20)



    return


def solution2(data):
    """Solution to part 2"""

    return


if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", action="store_true")
    args = parser.parse_args()

    filename = "day-10/input.txt" if not args.debug else "day-10/example_input.txt"

    # Read the input file
    with open(filename, "r", encoding="utf-8") as f:
        data = f.readlines()

    answ1 = solution1(data)
    print(f"Solution 1: {answ1}")

    answ2 = solution2(data)
    print(f"Solution 2: {answ2}")
