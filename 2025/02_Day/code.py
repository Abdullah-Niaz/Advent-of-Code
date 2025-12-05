import sys

def extract_range(range_str, result):
    from_val = int(range_str[:range_str.find('-')])
    to_val = int(range_str[range_str.find('-') + 1:])
    for i in range(from_val, to_val + 1):
        result.append(str(i))


def load_input(filename):
    result = []
    with open(filename, 'r') as file:
        line = file.readline().strip()

        while ',' in line:
            pos = line.find(',')
            range_str = line[:pos]
            extract_range(range_str, result)
            line = line[pos + 1:]

        extract_range(line, result)

    return result


def is_invalid_id(id_str, max_parts=2):
    length = len(id_str)
    for i in range(2, max_parts + 1):
        if length % i == 0:
            part = id_str[:length // i]
            if id_str == part * i:
                return True
    return False


def part_one():
    ids = load_input("./input.txt")
    result = 0
    for id_str in ids:
        if is_invalid_id(id_str):
            result += int(id_str)
    print(result)


def part_two():
    ids = load_input("./input.txt")
    result = 0
    for id_str in ids:
        if is_invalid_id(id_str, len(id_str)):
            result += int(id_str)
    print(result)



if __name__ == "__main__":
    part_one()
    part_two()
