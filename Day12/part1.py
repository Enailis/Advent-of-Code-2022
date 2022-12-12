# During this day I stumbled upon a lot of lib that could solve this easily
# As I am using this AoC to train in Python, I will try as much as I can to not use external lib

##############
# Read input #
##############
# Just like yesterday, I'm thinking about changing the readInput function every day
# to adapt it depending on the input of the day
def readInput():
    with open('input') as f:
        return f.read().strip().split('\n')


# create an int map depending on the letters
def mapScore(x, score):
    return score.get(x, ord(x)-96)


# create a graph for dijkstra
# I changed this part and adapted it for part2
# it now make the mapping in reverse
# it mean that I'm mapping distances from E to S
def makeGraph(hmap, input):
    adjacent = {}
    ni = len(hmap)
    nj = len(hmap[0])

    keyElements = {'start': None, 'end': None, 'lowest': []}

    for i in range(ni):
        for j in range(nj):
            adjs = [] 
            if i > 0:
                if hmap[i][j] - hmap[i-1][j] <= 1:
                    adjs.append((i-1,j))
            if j > 0:
                if hmap[i][j] - hmap[i][j-1] <= 1:
                    adjs.append((i,j-1))
            if i < ni-1:
                if hmap[i][j] - hmap[i+1][j] <= 1:
                    adjs.append((i+1,j))
            if j < nj-1:
                if hmap[i][j] - hmap[i][j+1] <= 1:
                    adjs.append((i,j+1))
            adjacent[(i,j)] = adjs

            if input[i][j] == 'S':
                keyElements['start'] = (i,j)
            if input[i][j] == 'E':
                keyElements['end'] = (i,j)
            if input[i][j] =='a':
                keyElements['lowest'].append((i,j))
    return adjacent, keyElements


# classic dijkstra
# this is a copy/paste from internet adapted to my code
def dijkstra(graph, start_node):

    unvisitedNodes = list(graph.keys())
    lastNode = {}
 
    shortestPath = {node: 9999999999 for node in unvisitedNodes}
    shortestPath[start_node] = 0
    
    while unvisitedNodes:
        currentMin = None
        for node in unvisitedNodes:
            if currentMin == None:
                currentMin = node
            elif shortestPath[node] < shortestPath[currentMin]:  
                currentMin = node

        neighbors = graph[currentMin]
        for neighbor in neighbors:
            value = shortestPath[currentMin] + 1 
            if value < shortestPath[neighbor]:
                shortestPath[neighbor] = value
                lastNode[neighbor] = currentMin
        unvisitedNodes.remove(currentMin)    
    return shortestPath


def getMinDistance(input):
    score = {'S':1, 'E':27}
    hmap = [[mapScore(x, score) for x in row] for row in input]
    adjacent, keyElements = makeGraph(hmap, input)
    minDistance = dijkstra(adjacent, keyElements['end'])
    return minDistance[keyElements['start']]


if __name__ == '__main__':
    print("Part 1 : ", getMinDistance(readInput()))
