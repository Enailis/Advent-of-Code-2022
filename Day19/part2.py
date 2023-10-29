# This file has been reworked since I first made it
# It's *almost* the same code for both parts

import re

# No readInput() this time
# I find it easier to go throught the input this way

def get_quality(blueprint, maxspend, cache, time, bots, amount):
    if time == 0:
        return amount[3]
    
    tba = tuple([time, *bots, *amount])
    
    if tba in cache:
        return cache[tba]
    
    maxval = amount[3] + bots[3] * time
    
    for type, recipe in enumerate(blueprint):
        if type != 3 and bots[type] >= maxspend[type]:
            continue
    
        wait = 0
        
        for ramount, rtype in recipe:
            if bots[rtype] == 0:
                break
            wait = max(wait, -(-(ramount - amount[rtype]) // bots[rtype]))
        else:
            remtime = time - wait - 1
            
            if remtime <= 0:
                continue
            
            bots_ = bots[:]
            amount_ = [x + y * (wait + 1) for x, y in zip(amount, bots)]
            
            for ramount, rtype in recipe:
                amount_[rtype] -= ramount
            
            bots_[type] += 1
            
            for i in range(3):
                amount_[i] = min(amount_[i], maxspend[i] * remtime)
            maxval = max(maxval, get_quality(blueprint, maxspend, cache, remtime, bots_, amount_))
    
    cache[tba] = maxval
    return maxval


def solve():
    total = 1

    with open('input') as f:
        i = 0
    
        for line in list(f)[:3]:
            blueprint = []
            maxspend = [0, 0, 0]

            for section in line.split(": ")[1].split(". "):
                recipe = []
            
                for x, y in re.findall(r"(\d+) (\w+)", section):
                    x = int(x)
                    y = ["ore", "clay", "obsidian"].index(y)
                    recipe.append((x, y))
                    maxspend[y] = max(maxspend[y], x)
            
                blueprint.append(recipe)
            
            v = get_quality(blueprint, maxspend, {}, 32, [1, 0, 0, 0], [0, 0, 0, 0])
            total *= v
            i += 1

    return str(total)


if __name__ == "__main__":
    print("Part 2 : " + solve())