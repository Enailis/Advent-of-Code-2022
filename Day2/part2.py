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
                temp = line.split(" ")
                temp[1] = temp[1].strip()
                toRet.append(temp)
    return toRet


# Count every Rock Paper Scissors wins (pt2)
def countWins(input):
    count = 0
    # Value in which we win or draw
    valuesOpponent = ['A', 'B', 'C']
    values = ['Y', 'Z', 'X']
    draw = ['X', 'Y', 'Z']

    # number of points if we
    # lose, draw, win
    points = [0, 3, 6]

    for i in range(len(input)):
        # draw condition
        if input[i][1] == 'Y':
            count = count + valuesOpponent.index(input[i][0]) + 1
        else:
            # win condition
            if input[i][1] == 'Z':
                count = count + draw.index(values[valuesOpponent.index(input[i][0])]) + 1
            else:
                count = count + draw.index(draw[((valuesOpponent.index(input[i][0]) + 2) % 3)]) + 1
        count = count + points[draw.index(input[i][1])]
    return count


if __name__ == '__main__':
    print(countWins(readInput()))
