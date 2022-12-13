##############
# Read input #
##############
# after many tests; I found it easier to go through the datas this way
def readInput():
    with open('input') as f:
        return list(map(lambda i: i.strip(), f.readlines()))


def parseData(input):
    lists = []
    for l in input:
        if not l:
            continue
        lists.append(eval(l))
    return lists


# This is not clean at all but I have no idea how to do it cleaner
# Basically it just compares the left and right value
# if left > right return 0
# else return 1
def compare(l, r):
    i = 0
    while True:
        if len(l) <= i < len(r):
            return 1
        elif len(r) <= i < len(l):
            return 0
        elif i >= len(l) and i >= len(r):
            return None
        if isinstance(l[i], int) and isinstance(r[i], int):
            if l[i] < r[i]:
                return 1
            elif r[i] < l[i]:
                return 0

        if isinstance(l[i], list) and isinstance(r[i], list):
            result = compare(l[i], r[i])
            if result is not None:
                return result

        if isinstance(l[i], list) and isinstance(r[i], int):
            result = compare(l[i], [r[i]])
            if result is not None:
                return result

        if isinstance(l[i], int) and isinstance(r[i], list):
            result = compare([l[i]], r[i])
            if result is not None:
                return result
        i += 1


# Compare every value and count which values are in order
def countOrder(lists):
    counter = 0
    i = 0
    for i in range(0, len(lists) - 1, 2):
        res = compare(lists[i], lists[i + 1])
        if res == 1:
            counter += i // 2 + 1
    return counter


if __name__ == '__main__':
    print("Part 1 : ", countOrder(parseData(readInput())))
