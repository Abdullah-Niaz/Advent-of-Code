import json

# Assuming SolutionBase is defined elsewhere, otherwise this will throw an error


class SolutionBase:
    pass


class Solution(SolutionBase):
    def get_guard_pos(self, _map):
        rows, cols = len(_map), len(_map[0])
        for i in range(rows):
            for j in range(cols):
                if _map[i][j] == "^":
                    return (i, j)

    def patrol(self, _map, pos=None, idx=None):
        if not pos:
            pos = self.get_guard_pos(_map)

        if not idx:
            idx = 0

        directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
        rows, cols = len(_map), len(_map[0])

        visited = set()
        visited.add((pos[0], pos[1]))

        visited_entry = {}  # for part 2, mark the entry point of the visited node

        while True:
            d = directions[idx]
            n = (pos[0] + d[0], pos[1] + d[1])

            if n[0] < 0 or n[0] >= rows or n[1] < 0 or n[1] >= cols:
                return True, visited, visited_entry  # leaving the map

            if _map[n[0]][n[1]] == "#":
                idx = (idx + 1) % 4
                continue
            else:
                visited.add((n[0], n[1]))
                if n not in visited_entry:
                    visited_entry[n] = (pos, idx)
                elif visited_entry[n] == (pos, idx):
                    return False, None, None  # loop detected
                pos = n

    def part1(self, data):
        _map = [list(line) for line in data]
        is_leaving, visited, visited_entry = self.patrol(_map)

        return len(visited)

    def part2(self, data):
        _map = [list(line) for line in data]
        is_leaving, visited, visited_entry = self.patrol(_map)

        # avoid the guard position, you cannot put obstruction there
        visited.remove(self.get_guard_pos(_map))
        loop_count = 0

        _map_dump = json.dumps(_map)  # json dumps/loads faster than deepcopy

        # Don't have to test every empty space, just the visited ones
        # because the obstruction must be on the visited path
        for vi, vj in visited:
            _map_copy = json.loads(_map_dump)
            _map_copy[vi][vj] = "#"

            pos = visited_entry[(vi, vj)][0]
            idx = visited_entry[(vi, vj)][1]

            is_leaving_copy, visited_copy, visited_entry_copy = self.patrol(
                _map_copy, pos, idx)
            if not is_leaving_copy:  # not leaving, because of the loop
                loop_count += 1

        return loop_count

# Function to read data from input file


def read_input(file_path="input.txt"):
    with open(file_path, "r") as file:
        return file.readlines()


def main():
    # Read the map data from the input file
    data = read_input()

    # Create an instance of the Solution class
    solution = Solution()

    # Part 1: Get the number of distinct positions visited by the guard
    part1_result = solution.part1(data)
    print(f"Part 1: Guard visits {part1_result} distinct positions.")

    # Part 2: Get the number of possible positions where we can place an obstruction
    part2_result = solution.part2(data)
    print(f"Part 2: There are {part2_result} possible obstruction positions.")


if __name__ == "__main__":
    main()
