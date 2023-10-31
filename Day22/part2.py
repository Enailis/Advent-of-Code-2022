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


# This is not clean, but it works
# I have no idea how to make something cleaner than that tbh
def make_move(grid, dir, i, j):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    dir2, i2, j2 = dir, *add((i, j), directions[dir])

    match dir2, i2, j2:
        case 0, _, 150 if i2 in range(50):
            dir2, i2, j2 = 2, 149 - i2, 99
        case 0, _, 100 if i2 in range(50, 100):
            dir2, i2, j2 = 3, 49, 50 + i2
        case 0, _, 100 if i2 in range(100, 150):
            dir2, i2, j2 = 2, 149 - i2, 149
        case 0, _, 50 if i2 in range(150, 200):
            dir2, i2, j2 = 3, 149, i2 - 100

        case 1, 200, _ if j2 in range(50):
            dir2, i2, j2 = 1, 0, j2 + 100
        case 1, 150, _ if j2 in range(50, 100):
            dir2, i2, j2 = 2, j2 + 100, 49
        case 1, 50, _ if j2 in range(100, 150):
            dir2, i2, j2 = 2, j2 - 50, 99

        case 2, _, 49 if i2 in range(0, 50):
            dir2, i2, j2 = 0, 149 - i2, 0
        case 2, _, 49 if i2 in range(50, 100):
            dir2, i2, j2 = 1, 100, i2 - 50
        case 2, _, -1 if i2 in range(100, 150):
            dir2, i2, j2 = 0, 149 - i2, 50
        case 2, _, -1 if i2 in range(150, 200):
            dir2, i2, j2 = 1, 0, i2 - 100

        case 3, 99, _ if j2 in range(50):
            dir2, i2, j2 = 0, 50 + j2, 50
        case 3, -1, _ if j2 in range(50, 100):
            dir2, i2, j2 = 0, j2 + 100, 0
        case 3, -1, _ if j2 in range(100, 150):
            dir2, i2, j2 = 3, 199, j2 - 100

    if grid[i2, j2] == ".":
        return dir2, i2, j2
    elif grid[i2, j2] == "#":
        return dir, i, j


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
                    dir, i, j = make_move(grid_dict, dir, i, j)

    return str((i + 1) * 1000 + (j + 1) * 4 + dir)


if __name__ == "__main__":
    grid, directions = readInput()
    print("Part 2 : " + solve(grid, directions))