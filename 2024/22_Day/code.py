from itertools import combinations
import networkx as nx
from collections import defaultdict


class Solution:
    def part1(self, data):
        G = nx.Graph()
        for line in data:
            parts = line.split("-")
            G.add_edge(parts[0], parts[1])

        cliques = [c for c in nx.find_cliques(G) if len(
            c) >= 3 and any(n[0] == "t" for n in c)]
        sets = set()
        for c in cliques:
            for nodes in combinations(c, 3):
                if any(n[0] == "t" for n in nodes):
                    sets.add(tuple(sorted(nodes)))
        count = len(sets)

        return count

    def part2(self, data):
        G = nx.Graph()
        for line in data:
            parts = line.split("-")
            G.add_edge(parts[0], parts[1])

        cliques = nx.find_cliques(G)
        LAN = sorted(sorted(cliques, key=len, reverse=True)[0])

        return ",".join(LAN)


class Solution:
    def part1(self, data):
        results = []
        for secret in map(int, data):
            for _ in range(2000):
                secret = ((secret * 64) ^ secret) % 16777216
                secret = ((secret // 32) ^ secret) % 16777216
                secret = ((secret * 2048) ^ secret) % 16777216
            results.append(secret)
        return sum(results)

    def part2(self, data):
        prices = []
        for secret in map(int, data):
            price = []
            for _ in range(2000):
                secret = ((secret * 64) ^ secret) % 16777216
                secret = ((secret // 32) ^ secret) % 16777216
                secret = ((secret * 2048) ^ secret) % 16777216
                price.append(secret % 10)
            prices.append(price)

        changes = [[b - a for a, b in zip(p, p[1:])] for p in prices]

        amounts = defaultdict(int)
        for buyer_idx, change in enumerate(changes):
            keys = set()
            for i in range(len(change) - 3):
                key = tuple(change[i: i + 4])
                if key in keys:
                    continue
                amounts[key] += prices[buyer_idx][i + 4]
                keys.add(key)
        max_amount = max(amounts.values())

        return max_amount


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
