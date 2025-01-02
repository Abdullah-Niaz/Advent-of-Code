class Solution:
    def part1(self, data):
        equations = []
        for line in data:
            test_value, numbers = line.split(":")
            equations.append(
                (int(test_value), [*map(int, numbers.strip().split())]))

        result = []

        for test_value, numbers in equations:
            possibles = [numbers.pop(0)]
            while numbers:
                curr = numbers.pop(0)
                temp = []
                for p in possibles:
                    temp.append(p + curr)
                    temp.append(p * curr)
                possibles = temp

            if test_value in possibles:
                result.append(test_value)

        return sum(result)

    def part2(self, data):
        equations = []
        for line in data:
            test_value, numbers = line.split(":")
            equations.append(
                (int(test_value), [*map(int, numbers.strip().split())]))

        result = []

        for test_value, numbers in equations:
            possibles = [numbers.pop(0)]
            while numbers:
                curr = numbers.pop(0)
                temp = []
                for p in possibles:
                    next_values = [  # +, * and ||
                        p + curr,
                        p * curr,
                        int(str(p) + str(curr)),
                    ]
                    temp.extend([v for v in next_values if v <= test_value])
                possibles = temp

            if test_value in possibles:
                result.append(test_value)

        return sum(result)



with open('input.txt', 'r') as file:
    data = file.readlines()


data = [line.strip() for line in data]

solution = Solution()
result_part1 = solution.part1(data)
result_part2 = solution.part2(data)

print(result_part1)
print(result_part2)
