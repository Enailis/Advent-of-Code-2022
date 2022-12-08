##############
# Read input #
##############
def readInput():
    toRet = []
    with open('input') as f:
        while True:
            line = f.readline()
            if not line:
                break
            else:
                toRet.append(line.split("\n")[0])
    return toRet


# this function uses the all() function to check the lines and columns
def countVisibleTrees(input):
    # count the number of trees on the edge
    count = 2 * len(input) + 2 * (len(input) - 2)

    for i in range(1, len(input) - 1):
        for j in range(1, len(input[0]) - 1):
            # North
            if all(input[k][j] < input[i][j] for k in range(0, i)):
                count += 1
                continue
            # South
            if all(input[k][j] < input[i][j] for k in range(i + 1, len(input))):
                count += 1
                continue
            # West
            if all(input[i][k] < input[i][j] for k in range(0, j)):
                count += 1
                continue
            # East
            if all(input[i][k] < input[i][j] for k in range(j + 1, len(input[i]))):
                count += 1
                continue
    return count


if __name__ == '__main__':
    print("Part 1 : ", countVisibleTrees(readInput()))