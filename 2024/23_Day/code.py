from itertools import combinations
import networkx as nx


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
