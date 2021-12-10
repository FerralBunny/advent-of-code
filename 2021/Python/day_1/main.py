# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def part_1():
    larger = 0
    with open('input') as f:
        lines = f.readlines()

        prev = None
        for line in lines:
            if prev:
                if int(prev) > int(line):
                    print(f'{line}: (decreased)')
                else:
                    print(f'{line}: (increased)')
                    larger += 1
            prev = line
        print(f'Answer: {larger}')


def part_2():
    larger = 0
    with open('input') as f:
        lines = f.readlines()

        curr = []
        prev_total = None
        for line in lines:
            curr.append(line)
            if len(curr) == 3:
                total = 0
                for n in curr:
                    total += int(n)
                if prev_total:
                    if int(total) < int(prev_total):
                        print(f'{curr} ({total}): (decreased)')
                    if int(total) > int(prev_total):
                        print(f'{curr} ({total}): (increased)')
                        larger += 1
                    if int(total) == int(prev_total):
                        print(f'{curr} ({total}): (no change)')
                else:
                    print(f'{curr} ({total}): (no comparison)')
                prev_total = total
                curr.pop(0)

        print(f'Answer: {larger}')


if __name__ == '__main__':
    # print_hi('PyCharm')
    part_2()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
