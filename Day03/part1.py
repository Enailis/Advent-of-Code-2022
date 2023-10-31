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


# Self-explanatory
def cutWordInTwo(input):
    toRet = []
    for word in input:
        toRet.append([word[:len(word) // 2], word[len(word) // 2:]])
    return toRet


# return the common letters between two half of every word in the list
def getCommonLetters(input):
    commonLetters = []
    for word in input:
        commonLetters.append(''.join(sorted(set(word[0]).intersection(set(word[1])))))
    return commonLetters


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


if __name__ == '__main__':
    print("Part 1 : ", countValueLetters(getCommonLetters(cutWordInTwo(readInput()))))
