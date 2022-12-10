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
                line = line.strip()
                line = line.split(' ')
                if len(line) == 1:
                    toRet.append([line[0], 0])
                else:
                    toRet.append(['noop', 0])
                    toRet.append([line[0], int(line[1])])
    return toRet

# will go through the cycles and add a █ where needed
# return a readable string to print
def CRT(input):
    temp = [[' ']*40 for _ in range(6)]
    x_register = 1
    for cycle, (instruction, value) in enumerate(input, 1):
        x1, x2 = divmod(cycle-1, 40)
        if x_register - 1 <= x2 <= x_register + 1:
            temp[x1][x2] = '█'
        x_register += value

    toRet = "\n"
    for row in temp:
        for ele in row:
            toRet += ele + " "
        toRet += "\n"
    return toRet


if __name__ == '__main__':
    print("Part 2 : ", CRT(readInput()))