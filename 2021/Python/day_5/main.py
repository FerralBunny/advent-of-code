

def part_1():
    lines = []
    hor_ver_line_coords = []
    dictionary = {}
    with open('input') as f:
        lines = f.readlines()
        for line_idx, line in enumerate(lines):
            line = line.strip()
            input_list = line.split(" -> ")
            positions = [str.split(",") for str in input_list]
            flat_positions = [int(item) for sublist in positions for item in sublist]

            if flat_positions[0] == flat_positions[2] or flat_positions[1] == flat_positions[3]:
                hor_ver_line_coords.append(flat_positions)

        for hor_ver_line_coord in hor_ver_line_coords:
            if hor_ver_line_coord[0] == hor_ver_line_coord[2]:
                step = 0
                if hor_ver_line_coord[1] < hor_ver_line_coord[3]:
                    step = 1
                else:
                    step = -1
                for i in range(hor_ver_line_coord[1], hor_ver_line_coord[3] + step, step):
                    key = str(hor_ver_line_coord[0]) + '-' + str(i)
                    if key in dictionary.keys():
                        dictionary[key] += 1
                    else:
                        dictionary[key] = 1

            if hor_ver_line_coord[1] == hor_ver_line_coord[3]:
                step = 0
                if hor_ver_line_coord[0] < hor_ver_line_coord[2]:
                    step = 1
                else:
                    step = -1
                for i in range(hor_ver_line_coord[0], hor_ver_line_coord[2] + step, step):
                    key = str(i) + '-' + str(hor_ver_line_coord[1])
                    if key in dictionary.keys():
                        dictionary[key] += 1
                    else:
                        dictionary[key] = 1

        total = 0
        for value in dictionary.values():
            if value >= 2:
                total += 1

    print(f'dictionary: {dictionary}')
    print(f'Answer: {total}')


def part_2():
    lines = []
    line_coords = []
    dictionary = {}
    with open('input') as f:
        lines = f.readlines()
        for line_idx, line in enumerate(lines):
            line = line.strip()
            input_list = line.split(" -> ")
            positions = [str.split(",") for str in input_list]
            flat_positions = [int(item) for sublist in positions for item in sublist]

            line_coords.append(flat_positions)

        for hor_ver_line_coord in line_coords:
            if hor_ver_line_coord[0] == hor_ver_line_coord[2]:
                step = 0
                if hor_ver_line_coord[1] < hor_ver_line_coord[3]:
                    step = 1
                else:
                    step = -1
                for i in range(hor_ver_line_coord[1], hor_ver_line_coord[3] + step, step):
                    key = str(hor_ver_line_coord[0]) + '-' + str(i)
                    if key in dictionary.keys():
                        dictionary[key] += 1
                    else:
                        dictionary[key] = 1

            elif hor_ver_line_coord[1] == hor_ver_line_coord[3]:
                step = 0
                if hor_ver_line_coord[0] < hor_ver_line_coord[2]:
                    step = 1
                else:
                    step = -1
                for i in range(hor_ver_line_coord[0], hor_ver_line_coord[2] + step, step):
                    key = str(i) + '-' + str(hor_ver_line_coord[1])
                    if key in dictionary.keys():
                        dictionary[key] += 1
                    else:
                        dictionary[key] = 1

            else:
                x_step = 0
                y_step = 0
                if hor_ver_line_coord[0] < hor_ver_line_coord[2]:
                    x_step = 1
                else:
                    x_step = -1
                if hor_ver_line_coord[1] < hor_ver_line_coord[3]:
                    y_step = 1
                else:
                    y_step = -1
                step = abs(hor_ver_line_coord[0] - hor_ver_line_coord[2])
                for i in range(0, step + 1):
                    key = str(hor_ver_line_coord[0] + i*x_step) + '-' + str(hor_ver_line_coord[1] + i*y_step)
                    if key in dictionary.keys():
                        dictionary[key] += 1
                    else:
                        dictionary[key] = 1

        total = 0
        for value in dictionary.values():
            if value >= 2:
                total += 1

    print(f'dictionary: {dictionary}')
    print(f'Answer: {total}')


if __name__ == '__main__':
    # print_hi('PyCharm')
    part_2()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
