from collections import Counter


def part_1():
    pair_insertion_rules = {}
    polymer_template = []
    num_steps = 10

    with open('input_example') as f:
        lines = f.readlines()
        for line_idx, line in enumerate(lines):
            line = line.strip()

            if line_idx == 0:
                line_list = list(line)
                polymer_template = line_list
            elif len(line):
                line_list = line.split(" -> ")
                pair_insertion_rules[line_list[0]] = line_list[1]

        print(f'Template: {polymer_template}')

        for step_num in range(1, num_steps + 1):
            polymer_template_tmp = []
            for i in range(len(polymer_template) - 1):
                first = polymer_template[i]
                last = polymer_template[i + 1]
                pair_key = first + last
                insertion_element = pair_insertion_rules[pair_key]
                new_section = [first, insertion_element, last] if i == 0 else [insertion_element, last]
                polymer_template_tmp += new_section
            polymer_template = list(polymer_template_tmp)
            print(f'After step {step_num}: {polymer_template}')

        polymer_template_occurrences = Counter(polymer_template)
        most_common_element = polymer_template_occurrences.most_common(1)[0]
        most_common_element_count = most_common_element[1]
        least_common_element = polymer_template_occurrences.most_common()[-1]
        least_common_element_count = least_common_element[1]

        print(f'Answer: {most_common_element_count - least_common_element_count}')


def part_2():
    pair_insertion_rules = {}
    pair_count = {}
    polymer_template = []
    num_steps = 40

    with open('input') as f:
        lines = f.readlines()
        for line_idx, line in enumerate(lines):
            line = line.strip()

            if line_idx == 0:
                line_list = list(line)
                polymer_template = line_list
            elif len(line):
                line_list = line.split(" -> ")
                pair_insertion_rules[line_list[0]] = line_list[1]
                pair_count[line_list[0]] = 0

        zero_pair_count = pair_count.copy()
        print(f'Template: {polymer_template}')
        for i in range(len(polymer_template) - 1):
            first = polymer_template[i]
            last = polymer_template[i + 1]

            pair_count[first + last] += 1

        print(f'Template count: {pair_count}')
        for step_num in range(1, num_steps + 1):
            pair_count_tmp = zero_pair_count.copy()
            for pair, count in pair_count.items():
                first = pair[:1]
                last = pair[-1:]
                insertion_element = pair_insertion_rules[pair]
                pair_count_tmp[first + insertion_element] += count
                pair_count_tmp[insertion_element + last] += count
            pair_count = pair_count_tmp.copy()
            print(f'After step {step_num}: {pair_count}')

        element_count = {}
        for pair, count in pair_count.items():
            # Only use the last letter in a pair to avoid duplicates and to ensure last letter is included
            last = pair[-1:]

            if last in element_count.keys():
                element_count[last] += count
            else:
                element_count[last] = count

        # Ensure first letter is included
        element_count[polymer_template[0]] += 1

        print(f'Element Count: {element_count}')
        counts = list(element_count.values())
        counts.sort()
        most_common_element_count = counts[-1]
        least_common_element_count = counts[0]

        print(f'Answer: {most_common_element_count - least_common_element_count}')


if __name__ == '__main__':
    part_2()
