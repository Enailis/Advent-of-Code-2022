import re

##############
# Read input #
##############
# I admit, this readInput is useless,
# but I want to keep the same structure every day (I might change my mind later)
def readInput():
    return open('input').read().strip().split('\n\n')


# This line : "op = f'({op}) // 3'"
# was removed from the parseInput of part1
def parseInput(input):
    temp = []
    for i, monkey in enumerate(input):
        _, items, op, test, if_true, if_false = monkey.splitlines()
        items = list(map(int,list(re.findall('\d+', items))))
        _, op = op.split('=')
        temp.append(int(re.findall('\d+', test)[0]))
        if_true = int(if_true[-1])
        if_false = int(if_false[-1])
        input[i] = [items, op, test, if_true, if_false, 0]
    return temp, input


# This was the part I was talking about in part1
# I couldn't find this on my own so thank you random guy on r/adventofcode
def reduceWorry(op, idx, obj, temp):
    res = op.replace('old', str(obj))
    res = eval(res) % temp[idx]
    return res


# As said in part1 and just above, this code is inspired by a code I found on r/adventofcode
# It's slow, but it works
def monkeyBusiness(temp, monkeys):
    for i, monkey in enumerate(monkeys):
        items = monkey[0]
        new_items = []
        for item in items:
            new_items.append([item % temp[i] for i in range(len(monkeys))])
        monkeys[i][0] = new_items

    for _ in range(10000):
        for i, monkey in enumerate(monkeys):
            items = monkey.pop(0)
            op, test, if_true, if_false, count = monkey
            while items:
                item = items.pop(0)
                new_item = []
                for j, it in enumerate(item):
                    new_item.append(reduceWorry(op, j, it, temp))
                if new_item[i] % temp[i] == 0:
                    monkeys[if_true][0].append(new_item)
                else:
                    monkeys[if_false][0].append(new_item)
                count += 1
            monkeys[i] = [[], op, test, if_true, if_false, count]

    activity = [monkey[-1] for monkey in monkeys]
    activity.sort()
    return activity[-1] * activity[-2]


if __name__ == "__main__":
    temp, monkeys = parseInput(readInput())
    print("Part 1 : ", monkeyBusiness(temp, monkeys))
