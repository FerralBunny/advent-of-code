from copy import deepcopy
from collections import Counter

def part_1():
    dictionary = {}
    routes = []
    complete_routes = []

    with open('input') as f:
        lines = f.readlines()
        for line_idx, line in enumerate(lines):
            line = line.strip()
            line_list = line.split("-")
            first = line_list[0]
            second = line_list[1]

            if second != 'start':
                if first in dictionary.keys():
                    dictionary[first].append(second)
                elif first != 'end':
                    dictionary[first] = [second]

            if first != 'start':
                if second in dictionary.keys():
                    dictionary[second].append(first)
                elif second != 'end':
                    dictionary[second] = [first]

        current_position = 'start'
        next_positions = dictionary[current_position]

        for position in next_positions:
            routes.append([current_position, position])

        while len(routes):
            new_routes = []
            for route_idx, route in enumerate(routes):
                current_position = route[-1]
                next_positions = dictionary[current_position]

                for position_idx, position in enumerate(next_positions):

                    route_copy = list(route)
                    route_copy.append(position)
                    new_routes.append(route_copy)

                    if (position in route) and position.islower():
                        # bad route
                        del new_routes[-1]
                    elif position == 'end':
                        complete_routes.append(route_copy)
                        del new_routes[-1]
            routes = deepcopy(new_routes)

        print(f'dictionary: {dictionary}')
        print(f'Routes: {complete_routes}')
        print(f'Answer: {len(complete_routes)}')


def part_2():
    dictionary = {}
    routes = []
    complete_routes = []

    with open('input') as f:
        lines = f.readlines()
        for line_idx, line in enumerate(lines):
            line = line.strip()
            line_list = line.split("-")
            first = line_list[0]
            second = line_list[1]

            if second != 'start':
                if first in dictionary.keys():
                    dictionary[first].append(second)
                elif first != 'end':
                    dictionary[first] = [second]

            if first != 'start':
                if second in dictionary.keys():
                    dictionary[second].append(first)
                elif second != 'end':
                    dictionary[second] = [first]

        current_position = 'start'
        next_positions = dictionary[current_position]

        for position in next_positions:
            routes.append([current_position, position])

        while len(routes):
            new_routes = []
            for route_idx, route in enumerate(routes):
                current_position = route[-1]
                next_positions = dictionary[current_position]

                for position_idx, position in enumerate(next_positions):

                    route_copy = list(route)
                    route_copy.append(position)
                    new_routes.append(route_copy)

                    if (position in route) and position.islower():
                        lower_positions = [x for i, x in enumerate(route) if x.islower() and x != 'start']
                        num_each_lower_positions = Counter(lower_positions)
                        if 2 in num_each_lower_positions.values():
                            # bad route as we already have 2 occurrences of a lower-case position
                            del new_routes[-1]
                    elif position == 'end':
                        complete_routes.append(route_copy)
                        del new_routes[-1]
            routes = deepcopy(new_routes)

        print(f'dictionary: {dictionary}')
        print(f'Routes: {complete_routes}')
        print(f'Answer: {len(complete_routes)}')


if __name__ == '__main__':
    part_2()
