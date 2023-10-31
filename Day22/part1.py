import re


##############
# Read input #
##############
def readInput():
    with open('input') as f:
        grid, directions = f.read().split("\n\n")
        grid = grid.splitlines()
        return grid, directions


def add(a, b):
    result = []
    for x, y in zip(a, b):
        result.append(x + y)
    return tuple(result)


def make_move(grid_dict, dir, i, j):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    i2, j2 = i, j

    while True:
        i2, j2 = add((i2, j2), directions[dir])
        i2 %= 200
        j2 %= 150
        if (i2, j2) in grid_dict:
            break

    if grid_dict[i2, j2] == "#":
        return i, j

    return i2, j2


def solve(grid, directions):
    grid_dict = {}
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell != " ":
                grid_dict[(i, j)] = cell
    
    directions = re.split(r"(?<=\d)(?=[LR])|(?<=[LR])(?=\d)", directions)
    
    dir = 0
    i = 0
    j = next(j for j in range(150) if (0,j) in grid_dict)

    for c in directions:
        match c:
            case "R":
                dir = (dir + 1)%4
            case "L":
                dir = (dir - 1)%4
            case _:
                for _ in range(int(c)):
                    i, j = make_move(grid_dict, dir, i, j)

    return str((i + 1) * 1000 + (j + 1) * 4 + dir)


if __name__ == "__main__":
    grid, directions = readInput()
    print("Part 1 : " + solve(grid, directions))