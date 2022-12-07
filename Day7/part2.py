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
    folderSizes = {}
    for folder in folders:
        fileSize = 0
        for file in files:
            if file.startswith(folder):
                fileSize += files[file]
        folderSizes[folder] = fileSize
    return folderSizes


if __name__ == '__main__':
    folders, files = getFoldersAndFiles(readInput())
    fileSizes = getSizes(folders, files)
    print("Part 2 : ", min(i for i in fileSizes.values() if 70000000 - fileSizes[""] + i >= 30000000))
