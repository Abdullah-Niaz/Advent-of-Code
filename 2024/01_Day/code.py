import os

# Function to sum an array of numbers


def sum_array(array):
    return sum(array)

# Function to read input from `input.txt`


def get_input(dirname):
    file_path = os.path.join(dirname, 'input.txt')
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading input file: {e}")
        exit(1)


data = get_input(os.getcwd())


def format_input(input_data):
    tuples = [
        list(map(int, line.split()))
        for line in input_data.strip().split('\n')
    ]

    left = []
    right = []

    for a, b in tuples:
        left.append(a)
        right.append(b)

    return [left, right]


def solution1(input_data):
    left, right = format_input(input_data)

    sorted_left = sorted(left)
    sorted_right = sorted(right)

    distances = [abs(sorted_left[i] - sorted_right[i])
                 for i in range(len(sorted_left))]

    return sum_array(distances)


def solution2(input_data):
    left, right = format_input(input_data)

    right_counts = {}

    for num in right:
        right_counts[num] = right_counts.get(num, 0) + 1

    total = 0
    for num in left:
        count = right_counts.get(num, 0)
        total += num * count

    return total


# Test cases
test_input = """
3   4
4   3
2   5
1   3
3   9
3   3
"""


def test(description, callback):
    try:
        callback()
        print(f"✔ {description}")
    except Exception as e:
        print(f"✘ {description}")
        print(e)


test('solution1', lambda: solution1(test_input) == 11)
test('solution2', lambda: solution2(test_input) == 31)

# Run solutions using the `input.txt` data
print('Solution 1 Output:', solution1(data))  # Replace with actual output
print('Solution 2 Output:', solution2(data))  # Replace with actual output
