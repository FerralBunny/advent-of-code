

def part_1():
    horizontal = 0
    depth = 0
    with open('input') as f:
        lines = f.readlines()
        for line in lines:
            direction, amount = line.split()
            if direction == 'forward':
                horizontal += int(amount)
            if direction == 'down':
                depth += int(amount)
            if direction == 'up':
                depth -= int(amount)

        print(f'Answer: {horizontal*depth}')


def part_2():
    horizontal = 0
    depth = 0
    aim = 0
    with open('input') as f:
        lines = f.readlines()
        for line in lines:
            direction, amount = line.split()
            if direction == 'forward':
                horizontal += int(amount)
                depth += int(amount)*aim
            if direction == 'down':
                aim += int(amount)
            if direction == 'up':
                aim -= int(amount)

        print(f'Answer: {horizontal*depth}')


if __name__ == '__main__':
    # print_hi('PyCharm')
    part_2()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
