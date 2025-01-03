

class Solution():
    def get_score(self, _map, i, j):
        rows, cols = len(_map), len(_map[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        endpoints = []
        queue = [(i, j)]

        while queue:
            y, x = queue.pop(0)
            curr = _map[y][x]
            _next = curr + 1
            for dy, dx in dirs:
                ny, nx = y + dy, x + dx
                if 0 <= ny < rows and 0 <= nx < cols and _map[ny][nx] == _next:
                    if _next == 9:
                        endpoints.append((ny, nx))
                    else:
                        queue.append((ny, nx))

        return endpoints

    def part1(self, data):
        _map = [list(map(int, line)) for line in data]
        rows, cols = len(_map), len(_map[0])

        score = 0

        for i in range(rows):
            for j in range(cols):
                if _map[i][j] == 0:
                    endpoints = self.get_score(_map, i, j)
                    score += len(set(endpoints))
        return score

    def part2(self, data):
        _map = [list(map(int, line)) for line in data]
        rows, cols = len(_map), len(_map[0])

        score = 0

        for i in range(rows):
            for j in range(cols):
                if _map[i][j] == 0:
                    endpoints = self.get_score(_map, i, j)
                    score += len(endpoints)
        return score


def main():

    with open('input.txt', 'r') as file:
        data = file.read().strip().splitlines()

    solution = Solution()

    part1_result = solution.part1(data)
    part2_result = solution.part2(data)

    print(f"Part 1 Result: {part1_result}")
    print(f"Part 2 Result: {part2_result}")


if __name__ == "__main__":
    main()
