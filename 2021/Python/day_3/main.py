

def part_1():
    numbits = 12
    binary_store = [0]*numbits
    binary = [0]*numbits
    with open('input') as f:
        lines = f.readlines()
        for line in lines:
            line_binary = line.strip()
            arr = list(line_binary)
            for idx, val in enumerate(arr):
                if int(val) == 1:
                    binary_store[idx] += 1
                if int(val) == 0:
                    binary_store[idx] -= 1
        for idx, val in enumerate(binary_store):
            if val > 0:
                binary[idx] = 1
            if val < 0:
                binary[idx] = 0
    string_ints = [str(int) for int in binary]
    bin_string = ''.join(string_ints)
    gamma = int(bin_string, 2)
    epsilon = ~gamma & ((1 << numbits) - 1)
    print(f'Gamma: {gamma}')
    print(f'Epsilon: {epsilon}')
    print(f'Answer: {gamma*epsilon}')


def part_2():
    numbits = 12
    binary_store = [0]*numbits
    binary = [0]*numbits
    with open('input') as f:
        lines = f.readlines()
        check_idx = 0
        while len(lines) > 1:
            for line in lines:
                line_binary = line.strip()
                line_binary_striped = list(line_binary)
                for idx, val in enumerate(line_binary_striped):
                    if int(val) == 1:
                        binary_store[idx] += 1
                    if int(val) == 0:
                        binary_store[idx] -= 1
            for idx, val in enumerate(binary_store):
                if val > 0:
                    binary[idx] = 0 #<-- invert this
                if val < 0:
                    binary[idx] = 1 #<-- invert this
                if val == 0:
                    binary[idx] = 0 #<-- invert this
            good_array = []
            for idx2, val2 in enumerate(lines):
                line_binary = val2.strip()
                line_binary_striped = list(line_binary)
                if int(binary[check_idx]) == int(line_binary_striped[check_idx]):
                    good_array.append(lines[idx2])
            lines = good_array
            check_idx += 1
            binary_store = [0] * numbits
        else:
            print(f'Last: {int(lines[0], 2)}')
    # 789
    # 3586


if __name__ == '__main__':
    # print_hi('PyCharm')
    part_2()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
