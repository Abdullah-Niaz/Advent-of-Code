from typing import List, Tuple

def load_ranges(filename: str) -> List[Tuple[int, int]]:
    result = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                break
            start, end = map(int, line.split('-'))
            result.append((start, end))
    result.sort(key=lambda x: x[0])
    return result

def load_ids(filename: str) -> List[int]:
    result = []
    parse_ids = False
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                parse_ids = True
                continue
            if parse_ids:
                result.append(int(line))
    return result

def part_one():
    filename = "./input.txt"
    ids = load_ids(filename)
    ranges = load_ranges(filename)
    result = 0
    for id_ in ids:
        for start, end in ranges:
            if start <= id_ <= end:
                result += 1
                break
    print(result)

def merge_ranges(ranges: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    result = []
    start, end = ranges[0]
    for next_start, next_end in ranges[1:]:
        if next_start > end:
            result.append((start, end))
            start, end = next_start, next_end
        elif next_end > end:
            end = next_end
    result.append((start, end))
    return result

def part_two():
    filename = "./input.txt"
    ranges = load_ranges(filename)
    merged_ranges = merge_ranges(ranges)
    result = sum(end - start + 1 for start, end in merged_ranges)
    print(result)

if __name__ == "__main__":
    part_one()
    part_two()
