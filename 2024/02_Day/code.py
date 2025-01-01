# index.py

def format_input(input_data):
    return [
        list(map(int, line.split()))
        for line in input_data.strip().split('\n')
    ]


def is_decreasing_correctly(arr):
    for i in range(len(arr) - 1):
        diff = arr[i] - arr[i + 1]
        if diff <= 0 or diff >= 4:
            return False
    return True


def is_increasing_correctly(arr):
    return is_decreasing_correctly(arr[::-1])


def is_row_safe(arr):
    return is_decreasing_correctly(arr) or is_increasing_correctly(arr)


def solution1(input_data):
    rows = format_input(input_data)
    return sum(1 for row in rows if is_row_safe(row))


def get_row_permutations(arr):
    return [arr[:i] + arr[i+1:] for i in range(len(arr))]


def solution2(input_data):
    rows = format_input(input_data)
    return sum(
        1 for row in rows
        if is_row_safe(row) or any(is_row_safe(perm) for perm in get_row_permutations(row))
    )


# Read input from input.txt
with open('input.txt', 'r') as file:
    data = file.read()

    # Test cases
    print(f"solution1: {solution1(data)}")  # Expected output: 2
    print(f"solution2: {solution2(data)}")  # Expected output: 4

    # Test function for is_row_safe
    print(is_row_safe([1, 2, 3, 4, 5]))  # Expected: True
    print(is_row_safe([5, 4, 3, 2, 1]))  # Expected: True
    print(is_row_safe([1, 2, 3, 2, 1]))  # Expected: False

    # Test function for is_decreasing_correctly
    print(is_decreasing_correctly([3, 2, 1]))  # Expected: True
    print(is_decreasing_correctly([1, 1, 1]))  # Expected: False

    # Test function for is_increasing_correctly
    print(is_increasing_correctly([1, 2, 3]))  # Expected: True
    print(is_increasing_correctly([1, 5, 9]))  # Expected: False

    # Test function for get_row_permutations
    # Expected: List of permutations
    print(get_row_permutations([1, 2, 3, 4, 5]))
