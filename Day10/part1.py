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


# Go through inputs and calculate signal strength for
# 20th, 60th, 100th, 140th, 180th, and 220th cycles
def getSignalStrength(input):
    result = 0
    x_register = 1
    for cycle, (instruction, value) in enumerate(input, 1):
        if (cycle + 20) % 40 == 0:
            result += x_register*cycle
        x_register += value
    return result


if __name__ == '__main__':
    print("Part 1 : ", getSignalStrength(readInput()))
