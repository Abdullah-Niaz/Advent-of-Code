from collections import defaultdict


class Solution:
    def part1(self, data):
        _map = [list(line) for line in data]
        rows, cols = len(_map), len(_map[0])

        antennas = defaultdict(list)

        # Collect coordinates of each antenna
        for row in range(rows):
            for col in range(cols):
                if _map[row][col] != ".":
                    antennas[_map[row][col]].append((row, col))

        antinodes = set()

        # Calculate antinode positions based on antenna coordinates
        for antenna, coords in antennas.items():
            for i in range(len(coords)):
                for j in range(i + 1, len(coords)):
                    diff = tuple(a - b for a, b in zip(coords[j], coords[i]))

                    for _idx, _dir in [(i, -1), (j, 1)]:
                        pos = tuple(
                            [a + b * _dir for a, b in zip(coords[_idx], diff)])
                        if 0 <= pos[0] < rows and 0 <= pos[1] < cols:
                            antinodes.add(pos)

        return len(antinodes)

    def part2(self, data):
        _map = [list(line) for line in data]
        rows, cols = len(_map), len(_map[0])

        antennas = defaultdict(list)

        # Collect coordinates of each antenna
        for row in range(rows):
            for col in range(cols):
                if _map[row][col] != ".":
                    antennas[_map[row][col]].append((row, col))

        antinodes = set()

        # Calculate antinode positions based on antenna coordinates
        for antenna, coords in antennas.items():
            for i in range(len(coords)):
                for j in range(i + 1, len(coords)):
                    diff = tuple(a - b for a, b in zip(coords[j], coords[i]))

                    for _idx, _dir in [(i, -1), (j, 1)]:
                        pos = coords[_idx]
                        # Add all intermediate positions until out of bounds
                        while 0 <= pos[0] < rows and 0 <= pos[1] < cols:
                            antinodes.add(pos)
                            pos = tuple(
                                [a + b * _dir for a, b in zip(pos, diff)])

        return len(antinodes)


solution = Solution()

with open('input.txt', 'r') as file:
    data = file.readlines()

data = [line.strip() for line in data]

result_part1 = solution.part1(data)
result_part2 = solution.part2(data)

print(result_part1)
print(result_part2)
