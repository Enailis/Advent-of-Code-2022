##############
# Read input #
##############
def readInput():
    toRet = []
    with open('inputTristan') as f:
        while True:
            line = f.readline()
            if not line:
                break
            else:
                toRet.append(line.split("\n")[0])
    return toRet

# self-explanatory
def countVisibleTrees(input, i, j):
    north = 0
    for k in range(i - 1, -1, -1):
        north += 1
        if input[k][j] >= input[i][j]:
            break

    south = 0
    for k in range(i + 1, len(input)):
        south += 1
        if input[k][j] >= input[i][j]:
            break

    west = 0
    for k in range(j - 1, -1, -1):
        west += 1
        if input[i][k] >= input[i][j]:
            break

    east = 0
    for k in range(j + 1, len(input[i])):
        east += 1
        if input[i][k] >= input[i][j]:
            break

    return north * south * west * east


if __name__ == '__main__':
    input = readInput()
    print("Part 2 : ", max(countVisibleTrees(input, i, j) for i in range(len(input)) for j in range(len(input[0]))))