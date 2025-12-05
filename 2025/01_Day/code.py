def load_input(filename):
    instructions = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            direction = line[0]
            distance = int(line[1:])
            instructions.append((direction, distance))
    return instructions


def calculate_zeros(instructions, count_pass_zero=False):
    dial = 50
    zeros = 0

    for direction, count in instructions:
        if count_pass_zero:
            if direction == 'L':
                for _ in range(count):
                    dial = (dial - 1 + 100) % 100
                    if dial == 0:
                        zeros += 1
            else:
                for _ in range(count):
                    dial = (dial + 1) % 100
                    if dial == 0:
                        zeros += 1
        else:
            if direction == 'L':
                dial = (dial - count + 100) % 100
            else:
                dial = (dial + count) % 100

            if dial == 0:
                zeros += 1

    return zeros


def part_one():
    instructions = load_input(
        "./input.txt"
    )
    result = calculate_zeros(instructions)
    print(result)


def part_two():
    instructions = load_input(
        "./input.txt"
    )
    result = calculate_zeros(instructions, True)
    print(result)


if __name__ == "__main__":
    part_one()
    part_two()
