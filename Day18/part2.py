##############
# Read input #
##############
def readInput():
    lines = []
    with open('input') as f:
        for line in f.readlines():
            lines.append([int(i) for i in line.strip().split(",")])
    return lines


# Check if current cube is in boundaries
def boundaries(x, y, z, min_x, max_x, min_y, max_y, min_z, max_z):
    return min_x <= x <= max_x and min_y <= y <= max_y and min_z <= z <= max_z

def solve(input):
    area = 0
    cubes = set()
    
    for cube in input:
        cubes.add(tuple(cube))

    # Define min and max boundaries
    min_x = min([x for x, _, _ in cubes]) - 1
    max_x = max([x for x, _, _ in cubes]) + 1
    min_y = min([y for _, y, _ in cubes]) - 1
    max_y = max([y for _, y, _ in cubes]) + 1
    min_z = min([z for _, _, z in cubes]) - 1
    max_z = max([z for _, _, z in cubes]) + 1

    seen = {(min_x, min_y, min_z)}
    cube = [(min_x, min_y, min_z)]

    for x, y, z in cube:
        for delta in (-1, 1):
            for coord in range(3):
                neighbour = [x, y, z]
                neighbour[coord] += delta
                neighbour = tuple(neighbour)
                
                if neighbour in cubes:
                    area += 1
                elif boundaries(*neighbour, min_x, max_x, min_y, max_y, min_z, max_z) and neighbour not in seen:
                    seen.add(neighbour)
                    cube.append(neighbour)
    
    return str(area)


if __name__ == "__main__":
    print("Part 1 : " + solve(readInput()))