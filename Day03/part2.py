import string

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
                toRet.append(line.split("\n")[0])
    return toRet


# For all letters :
# check if the letter is uppercase
# if uppercase then get index of letter in alphabet and add 27
# else get index of letter in alphabet and add 1
def countValueLetters(letters):
    value = 0
    for letter in letters:
        if letter.isupper():
            value = value + string.ascii_uppercase.index(letter) + 27
        else:
            value = value + string.ascii_lowercase.index(letter) + 1
    return value


# Group word by n
def groupBy(input, n):
    toRet = []
    for i in range(0, len(input), n):
        toRet.append([input[i], input[i + 1], input[i + 2]])
    return toRet


# get common letter between 3 words
def getCommonLetters(input):
    commonLetters = []
    for word in input:
        commonLetters.append(''.join(sorted(set(word[0]).intersection(set(word[1])).intersection((set(word[2]))))))
    return commonLetters


if __name__ == '__main__':
    print("Part 2 : ", countValueLetters(getCommonLetters(groupBy(readInput(), 3))))
