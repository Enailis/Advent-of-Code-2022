import re


##############
# Read input #
##############
def readInput():
    with open('input') as f:
        input = re.findall(r"Valve (\w\w).*?rate=(\d+).*?valves? (.*)", f.read())
        flows = dict((start, int(rate)) for start, rate, _ in input)
        graph = dict((start, line.replace(" ", "").split(",")) for start, _, line in input)

        return graph, flows


def frontier(graph, flows, start):
    res = [(0, [start], set())]
    
    for i in range(1, 31):
        if i > 5:
            res.sort(reverse=True)
            res = res[:3000]
        new = []
    
        for pressure, path, opened in res:
            location = path[-1]

            p = sum(flows[o] for o in opened)
            pressure += p

            for neigh in graph[location]:
                new.append((pressure, path + [neigh], opened.copy()))

            if flows[location] > 0 and location not in opened:
                new.append((pressure, path, opened | {location}))
    
        res = new
    return max(res)


def solve():
    graph, flows = readInput()
    res, _, _ = frontier(graph, flows, "AA")
    return str(res)


if __name__ == "__main__":
    print("Part 1 : " + solve())