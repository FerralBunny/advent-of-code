from copy import deepcopy


def part_1():
    lines = []
    bingo_numbers = []
    bingo_boards = []
    bingo_board_store = []
    with open('input') as f:
        lines = f.readlines()
        for line_idx, line in enumerate(lines):
            line = line.strip()

            if line_idx == 0:
                bingo_numbers = list(line.split(","))
            if len(line) != 0 and line_idx != 0:
                bingo_board_store.append(list(line.split()))
            if (len(line) == 0 or line_idx == len(lines) - 1) and len(bingo_board_store) != 0:
                bingo_boards.append(bingo_board_store)
                print(f'bingo_board: {bingo_board_store}')
                bingo_board_store = []

    # bingo_boards_checker = deepcopy(bingo_boards)
    checking_bingo_number = 0
    winning_board = []
    winning_bingo_number = -1
    for bingo_number in bingo_numbers:
        checking_bingo_number = bingo_number
        for bb_idx, bingo_board in enumerate(bingo_boards):

            if len(winning_board):
                break
            for bbl_idx, bingo_board_line in enumerate(bingo_board):
                for bbln_idx, bingo_board_line_no in enumerate(bingo_board_line):
                    if bingo_board_line_no == bingo_number:
                        bingo_boards[bb_idx][bbl_idx][bbln_idx] = -1
                bingo_board_line_ints = [int(str) for str in bingo_board_line]
                if sum(bingo_board_line_ints) == -5:
                    winning_bingo_number = checking_bingo_number
                    winning_board = bingo_boards[bb_idx]
                    print(f'Winning Number1: {checking_bingo_number}')
                    print(f'Winning Board1: {bingo_boards[bb_idx]}')
                    break


                for i in range(5):
                    vertical_count = 0
                    for j in range(5):
                        if bingo_boards[bb_idx][j][i] == -1:
                            print(f'wut: {bingo_boards[bb_idx][i]}')
                            vertical_count += 1
                            if vertical_count == 5:
                                winning_bingo_number = checking_bingo_number
                                winning_board = bingo_boards[bb_idx]
                                print(f'Winning Number2: {checking_bingo_number}')
                                print(f'Winning Board2: {bingo_boards[bb_idx]}')
                                break


    winning_board_unmarked_sum = 0
    for winning_board_line in winning_board:
        for winning_board_line_no in winning_board_line:
            if int(winning_board_line_no) > -1:
                winning_board_unmarked_sum += int(winning_board_line_no)
    print(f'Sum: {winning_board_unmarked_sum}')
    print(f'Number: {winning_bingo_number}')
    print(f'Answer: {int(winning_board_unmarked_sum) * int(winning_bingo_number)}')



def part_2():
    lines = []
    bingo_numbers = []
    bingo_boards = []
    bingo_board_store = []
    with open('input') as f:
        lines = f.readlines()
        for line_idx, line in enumerate(lines):
            line = line.strip()

            if line_idx == 0:
                bingo_numbers = list(line.split(","))
            if len(line) != 0 and line_idx != 0:
                bingo_board_store.append(list(line.split()))
            if (len(line) == 0 or line_idx == len(lines) - 1) and len(bingo_board_store) != 0:
                bingo_boards.append(bingo_board_store)
                # print(f'bingo_board: {bingo_board_store}')
                bingo_board_store = []

    # bingo_boards_checker = deepcopy(bingo_boards)
    # print(f'bingo_boards_checker: {bingo_boards_checker}')
    checking_bingo_number = 0
    winning_boards = []
    winning_bingo_number = -1
    winning_board_idxs = []
    for bingo_number in bingo_numbers:

        if len(bingo_boards) == 0:
            break

        checking_bingo_number = bingo_number
        # print(f'bingo_boards: {len(bingo_boards)}')
        for bb_idx, bingo_board in enumerate(bingo_boards):

            # if len(winning_board):
            #     break

            for bbl_idx, bingo_board_line in enumerate(bingo_board):
                # print(f'bbl_idx: {bbl_idx}')
                for bbln_idx, bingo_board_line_no in enumerate(bingo_board_line):

                    if bingo_board_line_no == bingo_number:
                        bingo_boards[bb_idx][bbl_idx][bbln_idx] = -1
                        # bingo_boards_checker = deepcopy(bingo_boards)

                # if len(winning_board_idxs):
                #     break

                bingo_board_line_ints = [int(str) for str in bingo_board_line]
                # print(f'sum(bingo_board_line_ints): {sum(bingo_board_line_ints)}')
                if sum(bingo_board_line_ints) == -5:
                    winning_bingo_number = checking_bingo_number
                    winning_boards.append(bingo_boards[bb_idx])
                    winning_board_idxs.append(bb_idx)
                    break

                    # winning_board_idxs.append(bb_idx)
                    # bingo_boards_checker.pop(bb_idx)

                for i in range(5):
                    vertical_count = 0
                    for j in range(5):
                        if bingo_boards[bb_idx][j][i] == -1:
                            vertical_count += 1
                            if vertical_count == 5:
                                winning_bingo_number = checking_bingo_number
                                winning_boards.append(bingo_boards[bb_idx])
                                winning_board_idxs.append(bb_idx)
                                break

                            # winning_board_idxs.append(bb_idx)
                            # bingo_boards_checker.pop(bb_idx)
        if len(winning_board_idxs):


            winning_board_set = set(winning_board_idxs)
            winning_boardz = list(winning_board_set)
            winning_boardz.sort()
            winning_boardz.reverse()
            print(f'bingo_boards: {len(bingo_boards)}')
            print(f'winning_boardz: {winning_boardz}')
            winning_board = winning_boards[0]
            for idx in winning_boardz:
                bingo_boards.pop(idx)
            winning_board_idxs = []
            winning_boards = []

        # bingo_boards = deepcopy(bingo_boards_checker)
        #
        # print(f'bingo_boards: {len(bingo_boards_checker)}')


    # print(f'winning_board_idxs: {winning_board_idxs}')
    # print(f'bingo_boards: {len(bingo_boards)}')

    winning_board_unmarked_sum = 0
    for winning_board_line in winning_board:
        for winning_board_line_no in winning_board_line:
            if int(winning_board_line_no) > -1:
                winning_board_unmarked_sum += int(winning_board_line_no)
    print(f'winning_board: {winning_board}')
    print(f'Sum: {winning_board_unmarked_sum}')
    print(f'Number: {winning_bingo_number}')
    print(f'Answer: {int(winning_board_unmarked_sum) * int(winning_bingo_number)}')
    # 3586


if __name__ == '__main__':
    # print_hi('PyCharm')
    part_2()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
