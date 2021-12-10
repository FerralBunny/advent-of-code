import math
import numpy as np


def part_1():
    locations = []
    total_risk_level = 0

    with open('input') as f:
        lines = f.readlines()
        for line_idx, line in enumerate(lines):
            line = line.strip()
            input_list = list(line)
            location_line = [int(str) for str in input_list]
            locations.append(location_line)

        for row_idx, row in enumerate(locations):
            for col_idx, col in enumerate(row):
                location_height = locations[row_idx][col_idx]
                north_location_height = 9
                if row_idx > 0:
                    north_location_height = locations[row_idx - 1][col_idx]
                south_location_height = 9
                if row_idx < len(locations) - 1:
                    south_location_height = locations[row_idx + 1][col_idx]
                east_location_height = 9
                if col_idx < len(row) - 1:
                    east_location_height = locations[row_idx][col_idx + 1]
                west_location_height = 9
                if col_idx > 0:
                    west_location_height = locations[row_idx][col_idx - 1]

                if location_height < north_location_height and location_height < south_location_height and location_height < west_location_height and location_height < east_location_height:
                    total_risk_level += (location_height + 1)

        print(f'Answer: {total_risk_level}')


def part_2():
    locations = []
    total_risk_level = 0
    basin_sizes = []

    with open('input') as f:
        lines = f.readlines()
        for line_idx, line in enumerate(lines):
            line = line.strip()
            input_list = list(line)
            location_line = [int(str) for str in input_list]
            locations.append(location_line)

        for row_idx, row in enumerate(locations):
            for col_idx, col in enumerate(row):
                location_height = locations[row_idx][col_idx]
                north_location_height = 9
                if row_idx > 0:
                    north_location_height = locations[row_idx - 1][col_idx]
                south_location_height = 9
                if row_idx < len(locations) - 1:
                    south_location_height = locations[row_idx + 1][col_idx]
                east_location_height = 9
                if col_idx < len(row) - 1:
                    east_location_height = locations[row_idx][col_idx + 1]
                west_location_height = 9
                if col_idx > 0:
                    west_location_height = locations[row_idx][col_idx - 1]

                if location_height < north_location_height and location_height < south_location_height and location_height < west_location_height and location_height < east_location_height:
                    total_risk_level += (location_height + 1)
                    basin_heights = []
                    basin_locations = {}
                    print(f'minima: height: {location_height} coords: {[row_idx, col_idx]}')
                    basin_heights.append(locations[row_idx][col_idx])
                    basin_locations[str(row_idx) + '-' + str(col_idx)] = [row_idx, col_idx]
                    to_check_positions = {str(row_idx) + '-' + str(col_idx): [row_idx, col_idx]}
                    checked_locations = []

                    while len(to_check_positions):
                        check = to_check_positions.popitem()
                        if check[0] not in checked_locations:
                            basin_locations_check = check_directions(check[1][0], check[1][1], row, locations)
                            to_check_positions = to_check_positions | basin_locations_check
                            checked_locations.append(check[0])
                            # merge dictionaries
                            basin_locations = basin_locations | basin_locations_check

                    basin_size = len(basin_locations)
                    basin_sizes.append(basin_size)
                    print(f'basin_locations: {basin_locations}')

        basin_sizes.sort()
        basin_sizes.reverse()
        print(f'Answer: {basin_sizes[0] * basin_sizes[1] * basin_sizes[2]}')


def check_directions(row_idx, col_idx, row, locations):
    basin_locations = {}
    # check south
    row_check = row_idx if row_idx == (len(locations) - 1) else row_idx + 1
    if (row_idx + 1) <= len(locations):
        for y in range(row_check, len(locations), 1):
            if locations[y][col_idx] != 9:
                basin_locations[str(y) + '-' + str(col_idx)] = [y, col_idx]
            else:
                break
    # check north
    row_check = row_idx if row_idx == 0 else row_idx - 1
    if (row_idx - 1) >= 0:
        for y in range(row_check, -1, -1):
            if locations[y][col_idx] != 9:
                basin_locations[str(y) + '-' + str(col_idx)] = [y, col_idx]
            else:
                break
    # check east
    col_check = col_idx if col_idx == (len(row) + 1) else col_idx + 1
    if (col_idx + 1) <= len(row):
        for x in range(col_check, len(row), 1):
            if locations[row_idx][x] != 9:
                basin_locations[str(row_idx) + '-' + str(x)] = [row_idx, x]
            else:
                break
    # check west
    col_check = col_idx if col_idx == 0 else col_idx - 1
    if (col_idx - 1) >= 0:
        for x in range(col_check, -1, -1):
            if locations[row_idx][x] != 9:
                basin_locations[str(row_idx) + '-' + str(x)] = [row_idx, x]
            else:
                break
    return basin_locations


if __name__ == '__main__':
    # print_hi('PyCharm')
    part_2()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
