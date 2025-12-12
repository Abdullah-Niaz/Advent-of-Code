import sys

def loadInput(filename):
    result = []
    with open(filename, 'r') as file:
        for line in file:
            result.append(line.rstrip('\n'))
    return result


def partOne():
    lines = loadInput("./input.txt")
    beams = set()
    result = 0

    for line in lines:
        for i in range(len(line)):
            c = line[i]
            if c == 'S':
                beams.add(i)
            elif c == '^' and i in beams:
                result += 1
                beams.remove(i)
                beams.add(i - 1)
                beams.add(i + 1)

    print(result)
    # assert result == 1507


def trackBeam(lines, i, j, memo):
    if i == len(lines) - 1:
        return 1

    if lines[i][j] == '^':
        key = (i, j)
        if key in memo:
            return memo[key]

        traces = (
            trackBeam(lines, i + 1, j - 1, memo)
            + trackBeam(lines, i + 1, j + 1, memo)
        )
        memo[key] = traces
        return traces

    return trackBeam(lines, i + 1, j, memo)


def partTwo():
    lines = loadInput("./input.txt")
    memo = {}
    result = 0

    for j in range(len(lines[0])):
        c = lines[0][j]
        if c == 'S':
            result = trackBeam(lines, 0, j, memo)
            break

    print(result)
    # assert result == 1537373473728


def main():
    partOne()
    partTwo()


if __name__ == "__main__":
    main()
