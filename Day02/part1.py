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


# Count every Rock Paper Scissors wins (pt1)
def countWins(input):
    count = 0
    # Value in which we win or draw
    valuesOpponent = ['A', 'B', 'C']
    values = ['Y', 'Z', 'X']
    draw = ['X', 'Y', 'Z']

    for i in range(len(input)):
        # win condition
        if valuesOpponent.index(input[i][0]) == values.index(input[i][1]):
            count = count + 6
        else:
            # draw condition
            if valuesOpponent.index(input[i][0]) == draw.index(input[i][1]):
                count = count + 3
        count = count + draw.index(input[i][1]) + 1
    return count


if __name__ == '__main__':
    print(countWins(readInput()))
