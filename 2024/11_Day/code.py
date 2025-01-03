from math import log, floor


class Solution:
    tracking = {}

    def blink(self, stone, times):
        if times == 0:
            return 1

        if (stone, times) in self.tracking:
            return self.tracking[(stone, times)]

        if stone == 0:
            size = self.blink(1, times - 1)
        elif (digits := (floor(log(stone, 10)) + 1)) % 2 < 1:
            left = stone // 10 ** (digits // 2)
            right = stone % 10 ** (digits // 2)
            size = self.blink(left, times - 1) + self.blink(right, times - 1)
        else:
            size = self.blink(stone * 2024, times - 1)

        self.tracking[(stone, times)] = size
        return size

    def part1(self, data):
        stones = map(int, data[0].split())
        count = sum(self.blink(stone, 25) for stone in stones)
        return count

    def part2(self, data):
        stones = map(int, data[0].split())
        count = sum(self.blink(stone, 75) for stone in stones)
        return count


with open('input.txt', 'r') as file:
    data = file.read().strip().splitlines()

    # Create an instance of the Solution class
solution = Solution()

# Execute part1 and part2 with the input data
part1_result = solution.part1(data)
part2_result = solution.part2(data)

# Print the results
print(f"Part 1 Result: {part1_result}")
print(f"Part 2 Result: {part2_result}")
