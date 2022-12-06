##############
# Read input #
##############
def readInput():
    toRet = ""
    with open('input') as f:
        while True:
            line = f.readline()
            if not line:
                break
            else:
                toRet = line
    return toRet

# get the start-of-packet marker
# return the number of character processed to find it
def getFirstStartOfPacket(input):
    startOfPacket = ""
    counter = 1
    for n_letter in range(len(input)):
        if len(startOfPacket) < 14:
            startOfPacket = startOfPacket + input[n_letter]
        else:
            # if no matching char return true
            # else return false
            if len(set(startOfPacket)) == len(startOfPacket):
                break
            else:
                startOfPacket = startOfPacket[1:] + input[n_letter+1]
        counter = counter + 1
    return startOfPacket, counter



if __name__ == '__main__':
    print("Part 2 : ", getFirstStartOfPacket(readInput()))