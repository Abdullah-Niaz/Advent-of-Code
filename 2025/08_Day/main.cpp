#include <cassert>
#include <fstream>
#include <iostream>
#include <set>
#include <sstream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>

struct Node
{
    int x, y, z;

    bool operator==(const Node &other) const
    {
        return x == other.x && y == other.y && z == other.z;
    }

    bool operator<(const Node &other) const
    {
        if (x != other.x)
            return x < other.x;
        if (y != other.y)
            return y < other.y;
        return z < other.z;
    }
};

struct Edge
{
    const Node *from;
    const Node *to;
    double length;
};

struct Graph
{
    std::vector<Node> nodes;
    std::vector<Edge> edges;
};

double distance(const Node &a, const Node &b)
{
    return std::sqrt(
        std::pow(a.x - b.x, 2) +
        std::pow(a.y - b.y, 2) +
        std::pow(a.z - b.z, 2));
}

Graph loadInput(const std::string &filename)
{
    Graph graph;
    std::ifstream file(filename);
    std::string line;

    while (std::getline(file, line))
    {
        std::stringstream ss(line);
        int x, y, z;
        char comma;
        ss >> x >> comma >> y >> comma >> z;
        graph.nodes.push_back(Node{x, y, z});
    }

    for (size_t i = 0; i < graph.nodes.size(); ++i)
    {
        for (size_t j = i + 1; j < graph.nodes.size(); ++j)
        {
            double d = distance(graph.nodes[i], graph.nodes[j]);
            graph.edges.push_back(Edge{&graph.nodes[i], &graph.nodes[j], d});
        }
    }

    std::sort(graph.edges.begin(), graph.edges.end(),
              [](const Edge &a, const Edge &b)
              {
                  return a.length < b.length;
              });

    return graph;
}

int walk(const std::vector<Edge> &edges, const Node &node, std::set<Node> &visited)
{
    if (visited.count(node))
    {
        return 0;
    }

    visited.insert(node);
    int count = 1;

    for (const auto &edge : edges)
    {
        if (*edge.from == node && !visited.count(*edge.to))
        {
            count += walk(edges, *edge.to, visited);
        }
        else if (*edge.to == node && !visited.count(*edge.from))
        {
            count += walk(edges, *edge.from, visited);
        }
    }

    return count;
}

void partOne()
{
    auto distanceGraph = loadInput("input.txt");

    constexpr int numberOfConnections = 1000;
    std::vector<Edge> edges(
        distanceGraph.edges.begin(),
        distanceGraph.edges.begin() + numberOfConnections);

    std::set<Node> visited;
    std::vector<int> circuits;

    for (const auto &node : distanceGraph.nodes)
    {
        int count = walk(edges, node, visited);
        if (count > 0)
        {
            circuits.push_back(count);
        }
    }

    std::sort(circuits.begin(), circuits.end(), std::greater<>());

    unsigned long result = 1;
    for (int i = 0; i < 3; ++i)
    {
        result *= circuits[i];
    }

    std::cout << result << std::endl;
    // assert(result == 83520);
}

void partTwo()
{
    auto distanceGraph = loadInput("input.txt");

    std::vector<Edge> edges;
    std::set<Node> visited;

    int fullIndex = -1;

    for (size_t i = 0; i < distanceGraph.edges.size(); ++i)
    {
        edges.push_back(distanceGraph.edges[i]);
        visited.clear();

        if (walk(edges, distanceGraph.nodes[0], visited) == 1000)
        {
            fullIndex = i;
            break;
        }
    }

    assert(fullIndex != -1);

    Edge edge = distanceGraph.edges[fullIndex];
    long result = edge.from->x * edge.to->x;

    std::cout << result << std::endl;
}

int main()
{
    partOne();
    partTwo();
    return 0;
}
