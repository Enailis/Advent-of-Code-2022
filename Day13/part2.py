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


# Add new packets and order them
# return the index of packet A * index of packet B
def countOrder(lists):
    lists.append([[2]])
    lists.append([[6]])
    for i in range(len(lists)):
        for j in range(i + 1, len(lists)):
            if compare(lists[i], lists[j]) == 0:
                lists[i], lists[j] = lists[j], lists[i]

    return (lists.index([[2]]) + 1) * (lists.index([[6]]) + 1)


if __name__ == '__main__':
    print("Part 2 : ", countOrder(parseData(readInput())))
