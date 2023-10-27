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
    states = {}
    total_rocks = 0
    r = 0
    cycle = False
    
    while total_rocks < 1000000000000:
        # Create copy of current array
        rock = copy.deepcopy(rocks[r])
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
    
        total_rocks += 1
    
        if not cycle:
            state = []
    
            for i in range(7):
                state.append(max([x[1] for x in chamber if x[0] == i]))
    
            lowest = min(state)
            state = [x - lowest for x in state]
            state += [r, jet]
            state = tuple(state)
    
            if state in states:
                height_gain_in_cycle = res - states[state][0]
                rocks_in_cycle = total_rocks - states[state][1]
                skipped_cycles = (1000000000000 - total_rocks) // rocks_in_cycle
                total_rocks += skipped_cycles * rocks_in_cycle
                cycle = True
            else:
                states[state] = [res, total_rocks]
    
        r = (r + 1) % 5
    
    return str(res + (skipped_cycles * height_gain_in_cycle))

if __name__ == "__main__":
    print("Part 2 : " + solve(readInput()))