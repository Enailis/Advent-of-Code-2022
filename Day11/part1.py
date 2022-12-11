import re

##############
# Read input #
##############
# I admit, this readInput is useless,
# but I want to keep the same structure every day (I might change my mind later)
def readInput():
    return open('input').read().strip().split('\n\n')


# I really don't like parsing input like that, but I feel like I didn't have a choice
def parseInput(input):
    temp = []
    for i, monkey in enumerate(input):
        _, items, op, test, if_true, if_false = monkey.splitlines()
        items = list(map(int, list(re.findall('\d+', items))))
        _, op = op.split('=')
        op = f'({op}) // 3'
        temp.append(int(re.findall('\d+', test)[0]))
        if_true = int(if_true[-1])
        if_false = int(if_false[-1])
        input[i] = [items, op, test, if_true, if_false, 0]
    return temp, input


# That was not my first function at all
# I decided to change it after doing the part 2 since it was a cleaner solution than I had
# I didn't find it on own, I had to search on r/adventofcode to find it
def monkeyBusiness(temp, monkeys):
    for _ in range(20):
        for i, monkey in enumerate(monkeys):
            items = monkey.pop(0)
            op, test, if_true, if_false, count = monkey
            while items:
                item = items.pop(0)
                compute = op.replace('old', str(item))
                item = eval(compute)
                if item % temp[i] == 0:
                    monkeys[if_true][0].append(item)
                else:
                    monkeys[if_false][0].append(item)
                count += 1
            monkeys[i] = [[], op, test, if_true, if_false, count]
    activity = [monkey[-1] for monkey in monkeys]
    activity.sort()
    return activity[-1] * activity[-2]


if __name__ == "__main__":
    temp, monkeys = parseInput(readInput())
    print("Part 1 : ", monkeyBusiness(temp, monkeys))
