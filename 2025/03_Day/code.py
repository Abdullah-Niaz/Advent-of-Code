import math

def load_input(filename):
    result = []
    with open(filename, "r") as f:
        for line in f:
            result.append(line.strip())
    return result


def largest_joltage(bank, length, lookup_map):
    key = (bank, length)
    if key in lookup_map:
        return lookup_map[key]

    result = 0

    for i in range(len(bank)):
        # prefix digit * 10^(length-1)
        prefix = (ord(bank[i]) - ord('0')) * (10 ** (length - 1))
        candidate = prefix

        # if remaining characters are fewer than length, skip
        if len(bank) - i < length:
            continue

        # if length > 1, compute suffix recursively
        if length > 1:
            suffix = largest_joltage(bank[i + 1:], length - 1, lookup_map)
            candidate += suffix

        if candidate > result:
            result = candidate

    lookup_map[key] = result
    return result


def part_one():
    banks = load_input("./input.txt")
    total = 0
    for bank in banks:
        lookup_map = {}
        total += largest_joltage(bank, 2, lookup_map)
    print(total)

def part_two():
    banks = load_input("./input.txt")
    total = 0
    for bank in banks:
        lookup_map = {}
        total += largest_joltage(bank, 12, lookup_map)
    print(total)

def main():
    part_one()
    part_two()

if __name__ == "__main__":
    main()