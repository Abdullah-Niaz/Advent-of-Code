#include <cassert>
#include <fstream>
#include <iostream>
#include <vector>
using namespace std;

std::vector<std::pair<char, int>> loadInput(const std::string &filename)
{
    std::vector<std::pair<char, int>> instructions;
    std::ifstream file(filename);
    std::string line;
    while (std::getline(file, line))
    {
        char direction = line[0];
        int distance = std::stoi(line.substr(1));
        instructions.emplace_back(direction, distance);
    }
    return instructions;
}

int calculateZeros(const std::vector<std::pair<char, int>> &instructions, bool countPassZero = false)
{
    int dial = 50;
    int zeros = 0;

    for (auto i : instructions)
    {
        char direction = i.first;
        int count = i.second;

        if (countPassZero)
        {
            if (direction == 'L')
            {
                for (int step = 1; step <= count; step++)
                {
                    dial = (dial - 1 + 100) % 100;
                    if (dial == 0)
                        zeros++;
                }
            }
            else // direction == 'R'
            {
                for (int step = 1; step <= count; step++)
                {
                    dial = (dial + 1) % 100;
                    if (dial == 0)
                        zeros++;
                }
            }
        }
        else
        {
            // Move the dial directly
            if (direction == 'L')
            {
                dial = (dial - count + 100) % 100;
            }
            else
            {
                dial = (dial + count) % 100;
            }

            if (dial == 0)
                zeros++;
        }
    }

    return zeros;
}

void partOne()
{
    auto instructions = loadInput("C:/Users/Abdullah-Niaz/Desktop/Advent-of-Code/2025/01_Day/input.txt");
    auto result = calculateZeros(instructions);
    std::cout << result << std::endl;
    assert(result == 1064);
}

void partTwo()
{
    const auto instructions = loadInput("C:/Users/Abdullah-Niaz/Desktop/Advent-of-Code/2025/01_Day/input.txt");
    const auto result = calculateZeros(instructions, true);
    std::cout << result << std::endl;
    assert(result == 6122);
}

int main()
{
    partOne();
    partTwo();
    return 0;
}