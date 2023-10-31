from pprint import pprint


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


# Parse the input stacks into arrays
def parseStacks(input):
    toRet = [[], [], [], [], [], [], [], [], []]
    for line in reversed(input):
        for i in range(1, len(line), 4):
            if line[i] != ' ':
                toRet[i//4].append(line[i])
    return toRet


# Parse sentences "move x from y to z"
# to [x, y, z]
def parseMoves(input):
    toRet = []
    for line in input:
        splitted = line.split(' ')
        temp = []
        for value in range(1, len(splitted), 2):
            temp.append(int(splitted[value]))
        toRet.append(temp)
    return toRet


# Move crates one by one
def doActions(stacks, moves):
    for move in moves:
        for i in range(move[0]):
            stacks[move[2]-1].append(stacks[move[1]-1].pop())
    return stacks


if __name__ == '__main__':
    input = readInput()
    print("Part 1 : ")
    pprint(doActions(parseStacks(input[:8]), parseMoves(input[10:])))
