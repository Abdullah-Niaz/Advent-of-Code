import math
from dataclasses import dataclass
from typing import List, Set


# =========================
# Data Structures
# =========================

@dataclass(frozen=True)
class Node:
    id: int
    x: int
    y: int
    z: int


@dataclass
class Edge:
    from_id: int
    to_id: int
    length: float


@dataclass
class Graph:
    nodes: List[Node]
    edges: List[Edge]


# =========================
# Utility Functions
# =========================

def distance(a: Node, b: Node) -> float:
    return math.sqrt(
        (a.x - b.x) ** 2 +
        (a.y - b.y) ** 2 +
        (a.z - b.z) ** 2
    )


# =========================
# Input Loader
# =========================

def loadInput(filename: str) -> Graph:
    nodes: List[Node] = []

    with open(filename, "r") as file:
        for idx, line in enumerate(file):
            x, y, z = map(int, line.strip().split(","))
            nodes.append(Node(idx, x, y, z))

    edges: List[Edge] = []
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            d = distance(nodes[i], nodes[j])
            edges.append(Edge(i, j, d))

    edges.sort(key=lambda e: e.length)
    return Graph(nodes, edges)


# =========================
# Graph Traversal
# =========================

def walk(edges: List[Edge], node_id: int, visited: Set[int]) -> int:
    if node_id in visited:
        return 0

    visited.add(node_id)
    count = 1

    for edge in edges:
        if edge.from_id == node_id and edge.to_id not in visited:
            count += walk(edges, edge.to_id, visited)
        elif edge.to_id == node_id and edge.from_id not in visited:
            count += walk(edges, edge.from_id, visited)

    return count


# =========================
# Part One
# =========================

def partOne():
    distanceGraph = loadInput("input.txt")
    NUMBER_OF_CONNECTIONS = 1000

    edges = distanceGraph.edges[:NUMBER_OF_CONNECTIONS]

    visited: Set[int] = set()
    circuits: List[int] = []

    for node in distanceGraph.nodes:
        count = walk(edges, node.id, visited)
        if count > 0:
            circuits.append(count)

    circuits.sort(reverse=True)

    result = 1
    for i in range(3):
        result *= circuits[i]

    print(result)
    # assert result == 83520


# =========================
# Part Two
# =========================

def partTwo():
    distanceGraph = loadInput("input.txt")

    edges = distanceGraph.edges[:5601]

    visited: Set[int] = set()
    assert walk(edges, distanceGraph.nodes[0].id, visited) == 1000

    edge = edges[-1]
    result = distanceGraph.nodes[edge.from_id].x * distanceGraph.nodes[edge.to_id].x

    print(result)
    # assert result == 1131823407


# =========================
# Main
# =========================

def main():
    partOne()
    partTwo()


if __name__ == "__main__":
    main()
