import math
import numpy as np


def part_1():
    lines = []
    opening_brackets = ['(', '[', '{', '<']
    closing_brackets = [')', ']', '}', '>']

    opening_bracket_store = []

    illegal_brackets = []
    error_score_dictionary = {')': 3, ']': 57, '}': 1197, '>': 25137}
    syntax_error_score = 0

    with open('input') as f:
        lines = f.readlines()
        for line_idx, line in enumerate(lines):
            line = list(line.strip())
            for bracket in line:
                if bracket in opening_brackets:
                    opening_bracket_store.append(bracket)
                else:
                    last_opening_bracket_index = opening_brackets.index(opening_bracket_store[-1])
                    if closing_brackets[last_opening_bracket_index] == bracket:
                        opening_bracket_store.pop()
                    else:
                        illegal_brackets.append(bracket)
                        syntax_error_score += error_score_dictionary.get(bracket)
                        print(f'Expected {closing_brackets[last_opening_bracket_index]}, but found {bracket} instead.')
                        break




        print(f'Answer: {syntax_error_score}')


def part_2():
    opening_brackets = ['(', '[', '{', '<']
    closing_brackets = [')', ']', '}', '>']

    illegal_brackets = []
    score_dictionary = {')': 1, ']': 2, '}': 3, '>': 4}
    total_line_scores = []

    with open('input') as f:
        lines = f.readlines()
        for line_idx, line in enumerate(lines):
            line = list(line.strip())
            opening_bracket_store = []
            for bracket_idx, bracket in enumerate(line):
                if bracket in opening_brackets:
                    opening_bracket_store.append(bracket)
                else:
                    last_opening_bracket_index = opening_brackets.index(opening_bracket_store[-1])
                    if closing_brackets[last_opening_bracket_index] == bracket:
                        opening_bracket_store.pop()
                    else:
                        illegal_brackets.append(bracket)
                        print(f'Expected {closing_brackets[last_opening_bracket_index]}, but found {bracket} instead.')
                        break

                if bracket_idx == len(line) - 1:
                    if len(opening_bracket_store):
                        print(f'Remaining: {opening_bracket_store}')
                        opening_bracket_store.reverse()
                        total_line_score = 0
                        for remaining_open_bracket in opening_bracket_store:
                            opening_bracket_index = opening_brackets.index(remaining_open_bracket)
                            bracket_score = score_dictionary.get(closing_brackets[opening_bracket_index])
                            total_line_score = (total_line_score * 5) + bracket_score
                        total_line_scores.append(total_line_score)

        sorted_middle_total_line_score = sorted(total_line_scores)[len(total_line_scores)//2]
        print(f'Answer: {sorted_middle_total_line_score}')




if __name__ == '__main__':
    # print_hi('PyCharm')
    part_2()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
