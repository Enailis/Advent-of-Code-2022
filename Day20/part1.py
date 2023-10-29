##############
# Read input #
##############
def readInput():
    with open('input') as f:
        return f.readlines()


def solve(input):
    coords = []
    for idx, item in enumerate(input):
        coords.append((idx, int(item)))
    
    coords_len = len(coords)

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
    print("Part 1 : " + solve(readInput()))