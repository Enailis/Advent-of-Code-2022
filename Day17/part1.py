import copy


##############
# Read input #
##############
def readInput():
    with open('input') as f:
        return f.readline().strip()


def solve(input):
    # Define rocks
    rocks = [[[2, 0], [3, 0], [4, 0], [5, 0]], [[2, 1], [3, 1], [3, 2], [3, 0], [4, 1]],
            [[2, 0], [3, 0], [4, 0], [4, 1], [4, 2]], [[2, 0], [2, 1], [2, 2], [2, 3]], [[2, 0], [3, 0], [2, 1], [3, 1]]]
    
    # Define chamber size
    chamber = {(x, 0) for x in range(7)}
    res = 0
    jet = 0
    
    for i in range(2022):
        # Create copy of current array
        rock = copy.deepcopy(rocks[i % 5])
        adjustment = res + 4
    
        for n in rock:
            n[1] += adjustment
    
        rest = False
    
        while not rest:
            new_rock = []
    
            if input[jet] == '<':
                if rock[0][0] > 0:
                    for n in rock:
                        if (n[0] - 1, n[1]) in chamber:
                            break
                        new_rock.append([n[0] - 1, n[1]])
                    else:
                        rock = new_rock
            else:
                if rock[-1][0] < 6:
                    for n in rock:
                        if (n[0] + 1, n[1]) in chamber:
                            break
                        new_rock.append([n[0] + 1, n[1]])
                    else:
                        rock = new_rock
    
            jet = (jet + 1) % len(input)
            new_rock = []
    
            for n in rock:
                if (n[0], n[1] - 1) in chamber:
                    for m in rock:
                        chamber.add((m[0], m[1]))
                    rest = True
                    res = max([o[1] for o in rock] + [res])
                    break
                else:
                    new_rock.append([n[0], n[1] - 1])
            else:
                rock = new_rock
    
    return str(res)


if __name__ == '__main__':
    print("Part 1 : " + solve(readInput()))