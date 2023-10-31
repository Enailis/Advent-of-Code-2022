##############
# Read Input #
##############
def readInput():
    snafu2decimal = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}

    value = 0

    with open('input') as f:
        for line in f:
            for i, digit in enumerate(line.strip()[::-1]):
                value += snafu2decimal[digit] * 5**i
    
    return value


def solve(value):
    snafu2decimal = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
    decimal2snafu = {v: k for k, v in snafu2decimal.items()}

    number = ""

    while value > 0:
        value, digit = divmod(value, 5)
        if digit > 2:
            digit -= 5
            value += 1
        number += decimal2snafu[digit]

    return number[::-1]


if __name__ == "__main__":
    print("Part 1 : " + solve(readInput()))