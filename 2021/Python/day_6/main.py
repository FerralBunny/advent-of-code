from copy import deepcopy


def part_1():
    lines = []
    fish_timers = []
    new_fish_timers = []
    day = 0
    end_day = 256
    with open('input') as f:
        lines = f.readlines()
        for line_idx, line in enumerate(lines):
            line = line.strip()
            input_list = list(line.split(","))
            fish_timers = [int(str) for str in input_list]

    while day < end_day:
        # print(f'After {day} days: {fish_timers}')
        new_fish_timers = fish_timers
        for fish_timer_idx, fish_timer in enumerate(fish_timers):
            new_timer = fish_timer - 1
            if new_timer < 0:
                new_timer = 6
                new_fish_timers.append(9)
            new_fish_timers[fish_timer_idx] = new_timer
        day += 1
        fish_timers = new_fish_timers

    # print(f'After {day} days: {fish_timers}')
    print(f'Answer: {len(fish_timers)}')


def part_2():
    lines = []
    fish_timers = []
                      #0  1  2  3  4  5  6  7  8 days
    num_fish_timers = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    day = 0
    end_day = 256
    with open('input') as f:
        lines = f.readlines()
        for line_idx, line in enumerate(lines):
            line = line.strip()
            input_list = list(line.split(","))
            fish_timers = [int(str) for str in input_list]

    for fish_timer in fish_timers:
        num_fish_timers[fish_timer] += 1

    while day < end_day:
        # print(f'After {day} days: {fish_timers}')
        new_num_fish_timers = list(num_fish_timers)

        new_num_fish_timers[0] = num_fish_timers[1]
        new_num_fish_timers[1] = num_fish_timers[2]
        new_num_fish_timers[2] = num_fish_timers[3]
        new_num_fish_timers[3] = num_fish_timers[4]
        new_num_fish_timers[4] = num_fish_timers[5]
        new_num_fish_timers[5] = num_fish_timers[6]
        new_num_fish_timers[6] = num_fish_timers[7] + num_fish_timers[0]
        new_num_fish_timers[7] = num_fish_timers[8]
        new_num_fish_timers[8] = num_fish_timers[0]

        num_fish_timers = list(new_num_fish_timers)
        day += 1

    print(f'Answer: {sum(num_fish_timers)}')

if __name__ == '__main__':
    # print_hi('PyCharm')
    part_2()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
