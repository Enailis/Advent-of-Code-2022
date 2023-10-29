##############
# Read input #
##############
def readInput():
    lines = []
    with open('input') as f:
        for line in f.readlines():
            lines.append([int(i) for i in line.strip().split(",")])
    return lines


def solve(input):
    area = 0
    cubes = set()

    for cube in input:
        cubes.add(tuple(cube))

    for cube in cubes:
        collisions = 0
        x, y, z = cube
        for x2, y2, z2 in cubes:
            if x == x2 and y == y2 and z == z2:
                    continue
            # check if sides are connected
            if abs(x - x2) + abs(y - y2) + abs(z - z2) <= 1:
                collisions += 1
        area += 6 - collisions

    return str(area)


if __name__ == "__main__":
    print("Part 1 : " + solve(readInput()))