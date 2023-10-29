##############
# Read input #
##############
def readInput():
    with open('input') as f:
        return f.readlines()


# I have no idea if this is clean or not but it works
def solve(input):
    monkeys = {}

    for line in input:
        parts = line.split()

        monkey = parts[0][:-1]
        pieces = []

        if len(parts) == 2:
            pieces.append(int(parts[1]))
        else:
            pieces += parts[1:]

        monkeys[monkey] = pieces

    while len(monkeys['root']) > 1:
        for k in monkeys.keys():
            mon_key = monkeys[k]

            if len(mon_key) == 1:
                continue

            if not isinstance(mon_key[0], int):
                if len(monkeys[mon_key[0]]) == 1:
                    mon_key[0] = monkeys[mon_key[0]][0]
            if not isinstance(mon_key[2], int):
                if len(monkeys[mon_key[2]]) == 1:
                    mon_key[2] = monkeys[mon_key[2]][0]

            operator = mon_key[1]

            if isinstance(mon_key[0], int) and isinstance(mon_key[2], int):
                a = mon_key[0]
                b = mon_key[2]
                val = 0

                if operator == '+':
                    val = a+b
                elif operator == '-':
                    val = a-b
                elif operator == '/':
                    val = a//b
                else:
                    val = a*b

                monkeys[k] = [val]

    return str(monkeys['root'][0])


if __name__ == '__main__':
    print("Part 1 : " + solve(readInput()))