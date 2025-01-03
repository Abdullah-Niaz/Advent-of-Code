class Solution:
    def part1(self, data):
        data = "\n".join(data).split("\n\n")
        locks = []
        keys = []

        for item in data:
            item = item.split("\n")
            cols = [[row[c] for row in item] for c in range(len(item[0]))]
            heights = [col.count("#") - 1 for col in cols]

            if item[0].count("#") == 5:
                locks.append(heights)
            else:
                keys.append(heights)

        count = sum(all(c <= 5 for c in [
                    a + b for a, b in zip(lock, key)]) for lock in locks for key in keys)
        return count

    def part2(self, data):
        return "Ho Ho Ho"


def main():

    with open("input.txt", "r") as file:
        input_data = file.read().strip().split("\n")

    solution = Solution()
    result_part1 = solution.part1(input_data)
    result_part2 = solution.part2(input_data)
    print("Part 1:", result_part1)
    print("Part 2:", result_part2)


if __name__ == "__main__":
    main()
