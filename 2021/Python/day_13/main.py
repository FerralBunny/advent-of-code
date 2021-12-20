from copy import deepcopy


def part_1():
    coordinates = []
    folds = []

    with open('input') as f:
        lines = f.readlines()
        for line_idx, line in enumerate(lines):
            line = line.strip()
            if len(line):
                if line.startswith('fold along'):
                    fold = line[11:].split('=')
                    folds.append([fold[0], int(fold[1])])
                else:
                    line_list = line.split(",")
                    line_ints = [int(str) for str in line_list]
                    coordinates.append(line_ints)

        fold = folds[0]

        folding_idx = 0 if fold[0] == 'x' else 1
        fold_num = fold[1]

        new_coordinates = []
        for coordinate in coordinates:
            if coordinate[folding_idx] < fold_num:
                new_coordinates.append(coordinate)
            else:
                mirror_coordinate = list(coordinate)
                diff = mirror_coordinate[folding_idx] - fold_num
                mirror_coordinate[folding_idx] -= diff*2
                new_coordinates.append(mirror_coordinate)

        coordinates = deepcopy(new_coordinates)

        print(f'coordinates: {coordinates}')
        print(f'folds: {folds}')
        coordinates_strings = [str(int) for int in coordinates]
        print(f'Answer: {len(set(coordinates_strings))}')


def part_2():
    coordinates = []
    folds = []

    with open('input') as f:
        lines = f.readlines()
        for line_idx, line in enumerate(lines):
            line = line.strip()
            if len(line):
                if line.startswith('fold along'):
                    fold = line[11:].split('=')
                    folds.append([fold[0], int(fold[1])])
                else:
                    line_list = line.split(",")
                    line_ints = [int(str) for str in line_list]
                    coordinates.append(line_ints)

        for fold in folds:
            folding_idx = 0 if fold[0] == 'x' else 1
            fold_num = fold[1]

            new_coordinates = []
            for coordinate in coordinates:
                if coordinate[folding_idx] < fold_num:
                    new_coordinates.append(coordinate)
                else:
                    mirror_coordinate = list(coordinate)
                    diff = mirror_coordinate[folding_idx] - fold_num
                    mirror_coordinate[folding_idx] -= diff*2
                    new_coordinates.append(mirror_coordinate)

            coordinates = deepcopy(new_coordinates)

        maxX = max(coordinates, key=lambda item: item[0])[0] + 1
        maxY = max(coordinates, key=lambda item: item[1])[1] + 1
        mapBase = [["."] * maxX for _ in range(maxY)]

        for coordinate in coordinates:
            x_idx = coordinate[1]
            y_idx = coordinate[0]
            mapBase[x_idx][y_idx] = "#"

        s = [[str(e) for e in row] for row in mapBase]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        print('Answer:')
        print('\n'.join(table))


if __name__ == '__main__':
    part_2()
