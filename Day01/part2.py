# As it's the first day of this year's AoC
# I forgot to split my two parts function
# so here is my final file for pt2 of day1

##############
# Read input #
##############
def readInput():
    toRet = []
    val = []
    with open('values.txt') as f:
        while True:
            line = f.readline()
            if not line:
                break
            else:
                if line == "\n":
                    toRet.append(val)
                    val = []
                else:
                    val.append(int(line))

    return toRet


# get the highest value of all arrays
# return that value with its index
def getHightAndCount(values):
    higher = 0
    count = 0
    toRet = 0
    for v in values:
        sumValues = sum(v)
        if sumValues > higher:
            higher = sumValues
            toRet = count
        count = count+1

    return higher, toRet


if __name__ == '__main__':
    values = readInput()

    top3 = 0
    res = getHightAndCount(values)
    top3 = top3 + res[0]
    values.pop(res[1])
    res = getHightAndCount(values)
    top3 = top3 + res[0]
    values.pop(res[1])
    res = getHightAndCount(values)
    top3 = top3 + res[0]
    print(top3)



