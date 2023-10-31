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


# count the number of time a range is contained in other range
def countContainOverlap(input):
    counter = 0
    for ranges in input:
        # I didn't find a better way to do this, it looks bad, but it works
        if (ranges[0].start <= ranges[1].start and ranges[0].stop >= ranges[1].stop)\
                or (ranges[1].start <= ranges[0].start and ranges[1].stop >= ranges[0].stop):
            counter = counter + 1
    return counter


if __name__ == '__main__':
    print("Part 1 : ", countContainOverlap(getRanges(readInput())))
