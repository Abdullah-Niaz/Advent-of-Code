from typing import List

def load_input(filename: str) -> List[str]:
    result = []
    with open(filename, 'r') as file:
        for line in file:
            result.append(line.strip())
    return result

def can_access(grid: List[str], row: int, col: int) -> bool:
    rolls = 0
    neighbors_str = ''

    if row > 0:
        top_row = grid[row - 1]
        start = max(0, col - 1)
        end = start + (2 if col == 0 else 3)
        neighbors_str += top_row[start:end]

    current_row = grid[row]
    start = max(0, col - 1)
    end = start + (2 if col == 0 else 3)
    neighbors_str += current_row[start:end]

    if row < len(grid) - 1:
        bottom_row = grid[row + 1]
        start = max(0, col - 1)
        end = start + (2 if col == 0 else 3)
        neighbors_str += bottom_row[start:end]

    rolls = neighbors_str.count('@')
    return (rolls - 1) < 4  # subtract self

def process_grid(grid: List[str]) -> List[str]:
    result = []
    for row_idx, row in enumerate(grid):
        next_row = list(row)  # convert to list for mutability
        for col_idx, element in enumerate(row):
            if element == '@' and can_access(grid, row_idx, col_idx):
                next_row[col_idx] = '.'
        result.append(''.join(next_row))
    return result

def count_grid(grid: List[str]) -> int:
    return sum(row.count('@') for row in grid)

def part_one():
    grid = load_input("./input.txt")
    start_count = count_grid(grid)
    next_grid = process_grid(grid)
    next_count = count_grid(next_grid)
    result = start_count - next_count
    print(result)

def part_two():
    grid = load_input("./input.txt")
    start_count = count_grid(grid)
    next_grid = process_grid(grid)
    previous_count = start_count
    next_count = count_grid(next_grid)
    
    while next_count < previous_count:
        previous_count = next_count
        next_grid = process_grid(next_grid)
        next_count = count_grid(next_grid)
    
    result = start_count - next_count
    print(result)

if __name__ == "__main__":
    part_one()
    part_two()
