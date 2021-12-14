
def part_1():
    energy_levels = []
    num_steps = 300
    num_flashes = 0

    with open('input') as f:
        lines = f.readlines()
        for line_idx, line in enumerate(lines):
            line = list(line.strip())
            line_ints = [int(str) for str in line]
            energy_levels.append(line_ints)

        for step_num in range(1, num_steps + 1):
            print(f'After step {step_num}:')
            flash_octopus_coords = []
            for line_idx, energy_line in enumerate(energy_levels):
                for octopus_idx, octopus in enumerate(energy_line):
                    if octopus == 9:
                        flash_octopus_coords.append([line_idx, octopus_idx])
                        num_flashes += 1
                        energy_levels[line_idx][octopus_idx] = 0
                    else:
                        energy_levels[line_idx][octopus_idx] += 1

            for flash_octopus_coord in flash_octopus_coords:
                start_i_idx = (flash_octopus_coord[0] - 1) if (flash_octopus_coord[0] - 1) >= 0 else 0
                end_i_idx = (flash_octopus_coord[0] + 1) if (flash_octopus_coord[0] + 1) <= (
                            len(energy_line) - 1) else (len(energy_line) - 1)
                start_j_idx = (flash_octopus_coord[1] - 1) if (flash_octopus_coord[1] - 1) >= 0 else 0
                end_j_idx = (flash_octopus_coord[1] + 1) if (flash_octopus_coord[1] + 1) <= (
                            len(energy_line) - 1) else (len(energy_line) - 1)
                for i in range(start_i_idx, end_i_idx + 1):
                    for j in range(start_j_idx, end_j_idx + 1):
                        octopus = energy_levels[i][j]
                        if octopus == 9:
                            flash_octopus_coords.append([i, j])
                            num_flashes += 1
                            energy_levels[i][j] = 0
                        elif octopus != 0:
                            energy_levels[i][j] += 1

            print(f'energy_levels: {energy_levels}')
            flat_energy_levels = [int(item) for sublist in energy_levels for item in sublist]
            if all(energy == 0 for energy in flat_energy_levels):
                print(f'All Octopuses flash on step: {step_num}')
                break

        print(f'Answer: {num_flashes}')


if __name__ == '__main__':
    # Part 1 and 2 can both use part_1()
    part_1()
