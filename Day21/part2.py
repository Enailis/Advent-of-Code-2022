##############
# Read input #
##############
def readInput():
    with open('input') as f:
        return f.readlines()


# I have no idea if this is clean or not but it works
def solve(lines):
    monkeys = {}

    for line in lines:
        parts = line.split()

        monkey = parts[0][:-1]
        pieces = []

        if len(parts) == 2:
            pieces.append(int(parts[1]))
        else:
            pieces += parts[1:]

        monkeys[monkey] = pieces

    changed = True
    while changed:
        changed = False

        for k in monkeys.keys():
            if k == 'humn':
                continue

            mon_key = monkeys[k]

            if len(mon_key) == 1:
                continue

            if not isinstance(mon_key[0], int) and mon_key[0] != 'humn':
                if len(monkeys[mon_key[0]]) == 1:
                    changed = True
                    mon_key[0] = monkeys[mon_key[0]][0]
            if not isinstance(mon_key[2], int) and mon_key[2] != 'humn':
                if len(monkeys[mon_key[2]]) == 1:
                    changed = True
                    mon_key[2] = monkeys[mon_key[2]][0]

            op = mon_key[1]

            if isinstance(mon_key[0], int) and isinstance(mon_key[2], int):
                a = mon_key[0]
                b = mon_key[2]
                val = 0

                if op == '+':
                    val = a+b
                elif op == '-':
                    val = a-b
                elif op == '/':
                    val = a//b
                else:
                    val = a*b

                monkeys[k] = [val]

    res = [i for i in monkeys['root'] if isinstance(i, int)][0]
    symbol = [i for i in monkeys['root'][0:3:2] if isinstance(i, str)][0]

    while symbol != 'humn':
        monkey = monkeys[symbol]
        val = [i for i in monkey if isinstance(i, int)][0]
        symbol = [i for i in monkey[0:3:2] if isinstance(i, str) and i != '+'][0]
        op = monkey[1]

        leftval = monkey[0] == val

        if op == '+':
            res -= val
        elif op == '-':
            if leftval:
                res = val - res
            else:
                res += val
        elif op == '/':
            if leftval:
                res = val // res
            else:
                res *= val
        else:
            res //= val

    return res


if __name__ == '__main__':
    print("Part 2 : " + str(solve(readInput())))