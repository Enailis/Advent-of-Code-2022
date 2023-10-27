import re


##############
# Read input #
##############
def readInput():
    inputs = []
    for l in open("input").readlines():
        ps = list(map(int, re.findall(r"-?\d+", l)))
        inputs.append(((ps[0], ps[1]), (ps[2], ps[3])))
    return inputs


def get_distance(b, s):
    return abs(b[0] - s[0]) + abs(b[1] - s[1])


def part1(inputs):
    free = []
    target_y = 2000000

    for sensor, beacon in inputs:
        distance = get_distance(sensor, beacon)

        dy = abs(sensor[1] - target_y)
        if dy <= distance:
            dx = distance - dy
            free.append((sensor[0] - dx, sensor[0] + dx))

    free.sort()
    range = [free[0]]

    # Merge overlapping ranges
    for r in free[1:]:
        if r[0] > range[-1][1]:
            range.append(r)
        else:
            range[-1] = (range[-1][0], max([range[-1][1], r[1]]))

    confirmed = 0

    # Count the number of confirmed points
    for r in range:
        confirmed += (r[1] - r[0])

    return str(confirmed)


if __name__ == "__main__":
    print("Part 1 : " + part1(readInput()))
