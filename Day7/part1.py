##############
# Read input #
##############
def readInput():
    with open('input') as f:
        return f.read().strip()


def getFoldersAndFiles(input):
    files = {}
    folders = set()
    temp = []
    for line in input.split("\n"):
        if line.startswith("$"):
            if line.startswith("$ cd"):
                if line[5:] == "..":
                    if len(temp) > 0:
                        temp.pop(-1)
                elif line[5:] == "/":
                    temp = []
                else:
                    temp.extend(line[5:].split("/"))
        else:
            size, name = line.split(" ")
            if size == "dir":
                continue
            size = int(size)
            files["/".join(temp + [name])] = size
        folders.add("/".join(temp))
    return folders, files


def getSizes(folders, files):
    totalSize = 0
    for folder in folders:
        fileSize = 0
        for file in files:
            if file.startswith(folder):
                fileSize += files[file]
        if fileSize <= 100000:
            totalSize += fileSize
    return totalSize


if __name__ == '__main__':
    folders, files = getFoldersAndFiles(readInput())
    print("Part 1 : ", getSizes(folders, files))
