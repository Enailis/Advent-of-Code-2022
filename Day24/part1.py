##############
# Read Input #
##############
def readInput():
    directions = {
        ">": (0, 1),
        "<": (0, -1),
        "^": (-1, 0),
        "v": (1, 0),
    }

    with open('input') as f:
        f = [line.strip() for line in f]
        height = len(f)
        width = len(f[0])
        blizzards = []
        for y, line in enumerate(f[1:-1], 1):
            for i, c in enumerate(line[1:-1], 1):
                if c in "><^v":
                    blizzards.append(((y, i), directions[c]))

    return height, width, blizzards


def solve(height, width, blizzards):
    start = (0, 1)
    target = (height - 1, width - 2)

    areas = set()
    
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            areas.add((y, x))
    
    areas.add(start)
    areas.add(target)

    queue = {(start, 0)}
    seen = set()

    while queue:
        temp = []
        
        for bliz_pos, bliz_dir in blizzards:
            if bliz_dir[0] == 0:
                new_pos = (bliz_pos[0], (bliz_pos[1] + bliz_dir[1] + width - 3) % (width - 2) + 1)
            else:
                new_pos = ((bliz_pos[0] + bliz_dir[0] + height - 3) % (height - 2) + 1, bliz_pos[1])
            temp.append((new_pos, bliz_dir))
        
        blizzards = temp    
        avaliable_areas = areas - set([i[0] for i in blizzards])
        new_queue = set()
        
        for pos, history in queue:
            if pos == target:
                return str(history)

            state = (pos, history)
        
            if state in seen:
                continue
            seen.add(state)

            for d in [(0, 1), (1, 0), (0, -1), (-1, 0), (0, 0)]:
                new_pos = (pos[0] + d[0], pos[1] + d[1])
        
                if new_pos in avaliable_areas:
                    new_queue.add((new_pos, history + 1))
        
        queue = new_queue


if __name__ == '__main__':
    height, width, blizzards = readInput()
    print("Part 1 : " + solve(height, width, blizzards))