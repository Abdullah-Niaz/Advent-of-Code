def safe_grid_get(grid, r, c):
    # Returns the value at (r, c) or '' if out of bounds
    if 0 <= r < len(grid) and 0 <= c < len(grid[r]):
        return grid[r][c]
    return ''


def format_input(input_data):
    # Convert the input string into a list of rows
    return input_data.strip().split('\n')


def solution1(input_data):
    search = format_input(input_data)
    count = 0

    for r in range(len(search)):
        for c in range(len(search[r])):
            if search[r][c] == 'X':
                # Check for 'XMAS' in different directions

                # Forward
                if search[r][c:c+4] == 'XMAS':
                    count += 1

                # Backward
                if search[r][c-3:c+1] == 'SAMX':
                    count += 1

                # Down
                if (safe_grid_get(search, r+1, c) == 'M' and
                    safe_grid_get(search, r+2, c) == 'A' and
                        safe_grid_get(search, r+3, c) == 'S'):
                    count += 1

                # Up
                if (safe_grid_get(search, r-1, c) == 'M' and
                    safe_grid_get(search, r-2, c) == 'A' and
                        safe_grid_get(search, r-3, c) == 'S'):
                    count += 1

                # Down-right
                if (safe_grid_get(search, r+1, c+1) == 'M' and
                    safe_grid_get(search, r+2, c+2) == 'A' and
                        safe_grid_get(search, r+3, c+3) == 'S'):
                    count += 1

                # Up-left
                if (safe_grid_get(search, r-1, c-1) == 'M' and
                    safe_grid_get(search, r-2, c-2) == 'A' and
                        safe_grid_get(search, r-3, c-3) == 'S'):
                    count += 1

                # Down-left
                if (safe_grid_get(search, r+1, c-1) == 'M' and
                    safe_grid_get(search, r+2, c-2) == 'A' and
                        safe_grid_get(search, r+3, c-3) == 'S'):
                    count += 1

                # Up-right
                if (safe_grid_get(search, r-1, c+1) == 'M' and
                    safe_grid_get(search, r-2, c+2) == 'A' and
                        safe_grid_get(search, r-3, c+3) == 'S'):
                    count += 1

    return count


def solution2(input_data):
    search = format_input(input_data)
    count = 0

    for r in range(len(search)):
        for c in range(len(search[r])):
            if search[r][c] == 'A':
                # Check for 'M' and 'S' in specific patterns

                # M . M
                # . A .
                # S . S
                if (safe_grid_get(search, r-1, c-1) == 'M' and
                    safe_grid_get(search, r-1, c+1) == 'M' and
                    safe_grid_get(search, r+1, c-1) == 'S' and
                        safe_grid_get(search, r+1, c+1) == 'S'):
                    count += 1

                # S . S
                # . A .
                # M . M
                if (safe_grid_get(search, r-1, c-1) == 'S' and
                    safe_grid_get(search, r-1, c+1) == 'S' and
                    safe_grid_get(search, r+1, c-1) == 'M' and
                        safe_grid_get(search, r+1, c+1) == 'M'):
                    count += 1

                # S . S
                # . A .
                # M . M
                if (safe_grid_get(search, r-1, c-1) == 'S' and
                    safe_grid_get(search, r-1, c+1) == 'S' and
                    safe_grid_get(search, r+1, c-1) == 'M' and
                        safe_grid_get(search, r+1, c+1) == 'M'):
                    count += 1

                # M . S
                # . A .
                # M . S
                if (safe_grid_get(search, r-1, c-1) == 'M' and
                    safe_grid_get(search, r-1, c+1) == 'S' and
                    safe_grid_get(search, r+1, c-1) == 'M' and
                        safe_grid_get(search, r+1, c+1) == 'S'):
                    count += 1

    return count


def read_input_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


if __name__ == "__main__":

    input_data = read_input_from_file('input.txt')

    print("Solution 1:", solution1(input_data))
    print("Solution 2:", solution2(input_data))
