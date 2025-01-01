def read_input_file(file_path):
    array_b = []
    array_c = []

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 2:
                array_b.append(int(parts[0]))
                array_c.append(int(parts[1]))

    return array_b, array_c


def calculate_distance(array_b, array_c):
    array_b.sort()
    array_c.sort()

    total_distance = sum(abs(left - right)
                         for left, right in zip(array_b, array_c))
    return total_distance


input_file_path = "input.txt"
array_b, array_c = read_input_file(input_file_path)

total_distance = calculate_distance(array_b, array_c)
print("Total Distance:", total_distance)
