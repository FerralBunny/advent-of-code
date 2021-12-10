import math
import numpy as np


def part_1():
    lines = []

    with open('input') as f:
        lines = f.readlines()
        for line_idx, line in enumerate(lines):
            line = line.strip()
            input_list = list(line.split(","))
            positions = [int(str) for str in input_list]

    median_position = np.median(positions)

    total_fuel = 0
    for position in positions:
        total_fuel += abs(position - median_position)

    print(f'Answer: {total_fuel}')


def part_2():
    lines = []

    with open('input') as f:
        lines = f.readlines()
        for line_idx, line in enumerate(lines):
            line = line.strip()
            input_list = list(line.split(","))
            positions = [int(str) for str in input_list]

    mean_position = np.mean(positions)
    target = round(mean_position) - 1 # <--- not sure why -1
    print(f'target: {target}')

    total_fuel = 0
    for position in positions:
        print(f'Move from {position} to {target}')
        distance = abs(position - target)
        fuel = distance * (distance + 1) / 2
        print(f'{fuel} fuel')
        total_fuel += fuel

    print(f'Answer: {total_fuel}')
#     104823358
#     104822130 <--- answer
#     104823019

if __name__ == '__main__':
    # print_hi('PyCharm')
    part_2()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
