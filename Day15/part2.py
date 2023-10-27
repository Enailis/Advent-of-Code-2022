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


def part2(inputs):
    # Do the same thing as part 1, but for indicated range
    for y in range(0, 4000000):
        free = []
        for sensor, beacon in inputs:

            distance = get_distance(sensor, beacon)
            dy = abs(sensor[1] - y)
            if dy <= distance:
                dx = distance - dy
                free.append((max([sensor[0] - dx, 0]), min([sensor[0] + dx, 4000000])))

        free.sort()
        ranges = [free[0]]

        # Merge overlapping ranges
        for r in free[1:]:
            to_check = ranges[-1]
            if r[0] > to_check[1]:
                ranges.append(r)
            else:
                ranges[-1] = (to_check[0], max([to_check[1], r[1]]))

        if len(ranges) > 1 or (ranges[0][0] > 0 and ranges[0][1] > 4000000):
            # there's a gap in this range
            if len(ranges) == 1:
                # the gap is an extremity 
                x = 0 if ranges[0][0] > 0 else 4000000
                # assert that there's only one slot
                assert(ranges[0][0] == 0 != ranges[0][1] == 4000000)
            else:
                # the gap is not an extremity
                x = ranges[0][1] + 1
                # assert that there's only one slot
                assert(x == ranges[1][0] - 1)

            return str(x*4000000+y)


if __name__ == "__main__":
    print("Part 2 : " + part2(readInput()))
