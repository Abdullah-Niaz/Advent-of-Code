import os
import re


def add(a, b):
    return a + b


input_file_path = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(input_file_path, 'r', encoding='utf-8') as file:
    data = file.read()


def format_input(input_str):
    return input_str.strip().split('\n')


# Regular expression to match "mul(x, y)"
MUL_PATTERN = re.compile(r'mul\(\d{1,3},\d{1,3}\)')

# Function to calculate the sum of multiplication matches


def sum_muls(muls):
    total = 0
    for match in muls:
        x, y = match.replace('mul(', '').replace(')', '').split(',')
        total += int(x) * int(y)
    return total


def solution1(input_str):
    lines = format_input(input_str)
    matches = [match.group()
               for line in lines for match in re.finditer(MUL_PATTERN, line)]
    return sum_muls(matches)


# Regular expression to match "mul(x, y)", "do()", and "don't()"
MUL_DO_DONT_PATTERN = re.compile(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)')


def solution2(input_str):
    lines = format_input(input_str)
    matches = [match.group() for line in lines for match in re.finditer(
        MUL_DO_DONT_PATTERN, line)]

    kept = []
    keeping = True
    for match in matches:
        if match == 'do()':
            keeping = True
            continue
        elif match == "don't()":
            keeping = False
            continue

        if keeping:
            kept.append(match)

    return sum_muls(kept)


print('Solution 1 Result:', solution1(data))
print('Solution 2 Result:', solution2(data))
