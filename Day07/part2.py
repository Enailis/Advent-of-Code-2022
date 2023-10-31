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

# return 2 values
# folders :
#   this value contains string of the path to different folders
#   they are formatted like : dir1/dir2/dir3
# files :
#   this value is a dictionary containing path/fileName as key and size as value
#   they are formatted like : dir1/dir2/fileName
def getFoldersAndFiles(input):
    files = {}
    folders = set()
    temp = []
    for line in input:
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

# go through folders and find files that have the name of the folder in their key
# return a dictionary of every folder with the name as key and the size as value
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
    print(fileSizes)
    print("Part 2 : ", min(i for i in fileSizes.values() if 70000000 - fileSizes[""] + i >= 30000000))
