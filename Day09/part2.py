import math

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


# Handle the movement of the tail towards the head
def moveTail(Hx, Hy, Tx, Ty):
    # check if head and tail are touching
    touching = math.dist((Hx,Hy),(Tx,Ty)) < 2
    # if not, move the tail towards the head
    if not touching:
        Ty += [-1, 1][Ty < Hy] if Ty != Hy else 0
        Tx += [-1, 1][Tx < Hx] if Tx != Hx else 0
    return Tx, Ty


# go through all been inputs
# the tail is now an array of 10 tuples
def doInput(input):
    Hx, Hy = 0, 0

    tail = [(0, 0)]*9
    seen = set()

    directions = {
        'U': (0, -1),
        'D': (0, 1),
        'L': (-1, 0),
        'R': (1, 0),
    }

    for line in input:
        split = line.split(' ')
        dx, dy = directions[split[0]]
        for i in range(int(split[1])):
            Hx = Hx + dx
            Hy = Hy + dy

            previous = (Hx, Hy)
            tail = [previous := moveTail(*previous, *value) for value in tail]
            seen.add(tail[-1])
    return len(seen)


if __name__ == '__main__':
    print("Part 2 : ", doInput(readInput()))