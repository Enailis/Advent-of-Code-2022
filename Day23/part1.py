from collections import defaultdict


##############
# Read Input #
##############
def readInput():
    input = defaultdict(int)
    with open('input') as f:
        for i, line in enumerate(f):
            for j, k in enumerate(line):
                if k == "#":
                    input[(i, j)] = 1
    return input


def corners(input):
    min_x = float("inf")
    max_x = -float("inf")
    min_y = float("inf")
    max_y = -float("inf")

    for y, x in input:
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        if y < min_y:
            min_y = y
        if y > max_y:
            max_y = y

    return min_x, max_x, min_y, max_y


def solve(input):
    cardinals = ["N", "S", "W", "E"]

    for _ in range(10):
        locations = defaultdict(int)
        new_data = {}
        items = list(input.items())
        
        for pos, i in items:
            if i == 0:
                continue

            checks = [(pos[0] - 1, pos[1] - 1), (pos[0] - 1, pos[1]), (pos[0] - 1, pos[1] + 1), (pos[0] + 1, pos[1] - 1), (pos[0] + 1, pos[1]), (pos[0] + 1, pos[1] + 1), (pos[0], pos[1] - 1), (pos[0], pos[1] + 1)]
            if all([input[c] == 0 for c in checks]):
                continue

            for d in cardinals:
                match d:
                    case "N":
                        checks = [(pos[0] - 1, pos[1] - 1), (pos[0] - 1, pos[1]), (pos[0] - 1, pos[1] + 1)]
                        new_pos = (pos[0] - 1, pos[1])
                    case "S":
                        checks = [(pos[0] + 1, pos[1] - 1), (pos[0] + 1, pos[1]), (pos[0] + 1, pos[1] + 1)]
                        new_pos = (pos[0] + 1, pos[1])
                    case "W":
                        checks = [(pos[0] - 1, pos[1] - 1), (pos[0], pos[1] - 1), (pos[0] + 1, pos[1] - 1)]
                        new_pos = (pos[0], pos[1] - 1)
                    case "E":
                        checks = [(pos[0] - 1, pos[1] + 1), (pos[0], pos[1] + 1), (pos[0] + 1, pos[1] + 1)]
                        new_pos = (pos[0], pos[1] + 1)

                if all([input[c] == 0 for c in checks]):
                    new_data[pos] = new_pos
                    locations[new_pos] += 1
                    break

        repeated = [p for p, c in locations.items() if c > 1]

        for pos_org, pos_new in new_data.items():
            if pos_new not in repeated:
                input[pos_org] = 0
                input[pos_new] = 1

        cardinals = cardinals[1:] + [cardinals[0]]

    p = [pos for pos, v in input.items() if v == 1]
    min_x, max_x, min_y, max_y = corners(p)

    return str((max_x - min_x + 1) * (max_y - min_y + 1) - len(p))


if __name__ == "__main__":
    print("Part 1 : " + solve(readInput()))