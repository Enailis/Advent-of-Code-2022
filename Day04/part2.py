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


# parse input like :
# [range1(start, end), range2(start, end)]
def getRanges(input):
    toRet = []
    for line in input:
        temp = line.replace('-', ',').split(',')
        toRet.append([range(int(temp[0]), int(temp[1])), range(int(temp[2]), int(temp[3]))])
    return toRet


# Count everytime there's an overlap
def countOverlap(input):
    counter = 0
    for ranges in input:
        if max(ranges[0].start, ranges[1].start) <= min(ranges[0].stop, ranges[1].stop):
            counter = counter + 1
    return counter


if __name__ == '__main__':
    print("Part 2 : ", countOverlap(getRanges(readInput())))
