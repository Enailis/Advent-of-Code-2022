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

def part1(input):
    rocks = parse_input(input)
    y_max = max([y for _, y in rocks])
    sand = set()
    dead = False
    count_sand = 0
    
    while not dead:
        new_sand = (500, 0)
        current = new_sand
        rest = False
        
        while not rest:
            if current[1] > y_max:
                dead = True
                break
            
            for dx, dy in [(0, 1), (-1, 1), (1, 1)]:
                next = (current[0] + dx, current[1] + dy)
                if next not in rocks | sand:
                    current = next
                    break
            else:
                rest = True
                count_sand += 1
                sand.add(current)

    return str(count_sand)

if __name__ == "__main__":
    print("Part 1 : " + part1(readInput()))