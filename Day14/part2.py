##############
# Read input #
##############
def readInput():
    with open('input') as f:
        return f.readlines()

# parse input to get a set of rocks
def parse_input(input):
    rocks = set()

    for line in input:
        points = [
            tuple(map(int, coords.split(","))) for coords in line.strip().split(" -> ")
        ]
        
        for ind, point in enumerate(points[:-1:]):
            rocks.add(point)
            dx, dy = points[ind + 1][0] - point[0], points[ind + 1][1] - point[1]
        
            if dx:
                count = 0
                step = dx // abs(dx)
                while dx != count:
                    rocks.add((point[0] + count, point[1]))
                    count += step
        
            if dy:
                count = 0
                step = dy // abs(dy)
                while dy != count:
                    rocks.add((point[0], point[1] + count))
                    count += step
            rocks.add(points[ind + 1])
    
    return rocks

def part2(input):
    rocks = parse_input(input)
    y_max = max([y for _, y in rocks])
    sand = {(500, 0)}
    queue = {(500, 0)}
    
    while queue:
        current = queue.pop()
    
        if current[1] >= y_max + 1:
            continue
    
        for dx, dy in [(0, 1), (-1, 1), (1, 1)]:
            next = (current[0] + dx, current[1] + dy)
            if next not in rocks:
                sand.add(next)
                queue.add(next)
    
    return str(len(sand))

if __name__ == "__main__":
    print("Part 2 : " + part2(readInput()))