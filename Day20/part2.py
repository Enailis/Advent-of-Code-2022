##############
# Read input #
##############
def readInput():
    with open('input') as f:
        return f.readlines()


# There has to be a better way to do this
def solve(input):
    key = 811589153

    coords = []
    for idx, item in enumerate(input):
        coords.append((idx, int(item) * key))
    
    coords_len = len(coords)

    for _ in range(10):
        for i in range(coords_len):
            for p, coord in enumerate(coords):
                if coord[0] == i:
                    pos, coord = p, coord
                    break

            new = (pos + coord[1] + (coords_len - 1)) % (coords_len - 1)

            coords.pop(pos)
            coords.insert(new, coord)

    zero = []
    for p, item in enumerate(coords):
        if item[1] == 0:
            zero = p
            break

    grove = coords[(zero + 1000) % coords_len][1] + coords[(zero + 2000) % coords_len][1] + coords[(zero + 3000) % coords_len][1]
 
    return str(grove)


if __name__ == "__main__":
    print("Part 2 : " + str(solve(readInput())))