import re
from functools import reduce
from operator import mul

# Load input lines
def loadInput(filename):
    result = []
    with open(filename, 'r') as f:
        for line in f:
            result.append(line.rstrip('\n'))
    return result

# Load numbers row-wise (Part One)
def loadNumbersPartOne(lines):
    result = []
    for i in range(len(lines) - 1):
        row = []
        del_regex = re.compile(r'\s+')
        tokens = del_regex.split(lines[i])
        for value in tokens:
            if value != '':
                row.append(int(value))
        result.append(row)
    return result

# Load numbers column-wise (Part Two)
def loadNumbersPartTwo(lines):
    result = []
    v = []
    for j in range(len(lines[0]) + 3):
        ss = ''
        for k in range(len(lines) - 1):
            if j < len(lines[k]):
                c = lines[k][j]
                if c != ' ':
                    ss += c
        col = ss
        if col == '':
            if v:
                result.append(v)
                v = []
        else:
            v.append(int(col))
    return result

# Load operators
def loadOperators(line):
    result = []
    for c in line:
        if c == '+' or c == '*':
            result.append(c)
    return result

# Part One: row-wise operations
def partOne():
    input_lines = loadInput("./input.txt")
    numbers = loadNumbersPartOne(input_lines)
    operators = loadOperators(input_lines[-1])
    totals = [0] * len(numbers[0])
    for row in numbers:
        for j in range(len(row)):
            if totals[j] == 0:
                totals[j] = row[j]
            elif operators[j] == '+':
                totals[j] = totals[j] + row[j]
            elif operators[j] == '*':
                totals[j] = totals[j] * row[j]
    result = sum(totals)
    print(result)
    # assert result == 7229350537438

# Part Two: column-wise operations
def partTwo():
    input_lines = loadInput("./input.txt")
    columns = loadNumbersPartTwo(input_lines)
    operators = loadOperators(input_lines[-1])
    totals = [0] * len(columns)
    for j in range(len(columns)):
        if operators[j] == '+':
            totals[j] = sum(columns[j])
        elif operators[j] == '*':
            totals[j] = reduce(mul, columns[j], 1)
    result = sum(totals)
    print(result)
    # assert result == 11479269003550

if __name__ == "__main__":
    partOne()
    partTwo()
