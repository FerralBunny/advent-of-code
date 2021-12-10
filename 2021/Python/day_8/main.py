import math
import numpy as np


def part_1():
    lines = []
    #1, 4, 7, and 8
    unique_lengths = [2, 4, 3, 7]
    count = 0

    with open('input') as f:
        lines = f.readlines()
        for line_idx, line in enumerate(lines):
            line = line.strip()
            input_list = line.split(" | ")
            pattern_output = [str.split() for str in input_list]

            # print(f'pattern_output: {pattern_output}')
            for output in pattern_output[1]:
                # print(f'output: {output}')
                # print(f'len(output): {len(output)}')
                if len(output) in unique_lengths:
                    # print(f'counting')
                    count += 1


    print(f'Answer: {count}')


# 0 (6) - len 6 and all in 7 and not all in 4
# 1 (2) - known
# 2 (5) - 2 in 4 (?)
# 3 (5) - len 5 and all in 7
# 4 (4) - known
# 5 (5) - 3 in 4 (?)
# 6 (6) - len 6 and not all in 7 and not all in 4
# 7 (3) - known
# 8 (7) - known
# 9 (6) - len 6 and all in 4 and 7

def part_2():
    lines = []

    with open('input') as f:
        lines = f.readlines()
        output_value_total = 0
        for line_idx, line in enumerate(lines):
            line = line.strip()
            input_list = line.split(" | ")
            pattern_output = [str.split() for str in input_list]

            solved = ['']*10
            num_solved = 0

            while num_solved < 10:
                for pattern in pattern_output[0]:
                    sorted_pattern = "".join(sorted(pattern))
                    if len(sorted_pattern) == 2:
                        solved[1] = sorted_pattern
                        num_solved += 1
                    if len(sorted_pattern) == 4:
                        solved[4] = sorted_pattern
                        num_solved += 1
                    if len(sorted_pattern) == 3:
                        solved[7] = sorted_pattern
                        num_solved += 1
                    if len(sorted_pattern) == 7:
                        solved[8] = sorted_pattern
                        num_solved += 1

                    if len(sorted_pattern) == 6:
                        sorted_pattern_list = list(sorted_pattern)
                        if len(solved[4]) and len(solved[7]):
                            all_in_4 = all(b in sorted_pattern_list for b in list(solved[4]))
                            all_in_7 = all(b in sorted_pattern_list for b in list(solved[7]))
                            if all_in_7 and not all_in_4:
                                solved[0] = sorted_pattern
                                num_solved += 1
                            elif not all_in_7 and not all_in_4:
                                solved[6] = sorted_pattern
                                num_solved += 1
                            elif all_in_7 and all_in_4:
                                solved[9] = sorted_pattern
                                num_solved += 1

                    if len(sorted_pattern) == 5:
                        sorted_pattern_list = list(sorted_pattern)
                        if len(solved[4]) and len(solved[7]):
                            all_in_7 = all(b in sorted_pattern_list for b in list(solved[7]))
                            checking_list = list(set(solved[4]) - set(solved[7]))
                            all_in_checking_list = all(b in sorted_pattern_list for b in checking_list)
                            if all_in_7:
                                solved[3] = sorted_pattern
                                num_solved += 1
                            elif not all_in_checking_list:
                                solved[2] = sorted_pattern
                                num_solved += 1
                            elif all_in_checking_list:
                                solved[5] = sorted_pattern
                                num_solved += 1

            print(f'{solved}')
            output_value = ''
            for output in pattern_output[1]:
                sorted_output = "".join(sorted(output))
                for idx, val in enumerate(solved):
                    if sorted_output == val:
                        output_value += str(idx)
            print(f'{output_value}')
            output_value_total += int(output_value)

        print(f'Answer: {output_value_total}')





if __name__ == '__main__':
    # print_hi('PyCharm')
    part_2()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
