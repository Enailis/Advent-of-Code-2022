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


def options(graph, flows, location, path, opened):
    options = []
    
    for neigh in graph[location]:
        options.append((path + [neigh], opened.copy()))
    
    if flows[location] > 0 and location not in opened:
        options.append((path, opened | {location}))
    
    return options


def frontier(graph, flows, start):
    res = [(0, ([start], [start]), set())]
    
    for i in range(1, 27):
        if i > 5:
            res.sort(reverse=True)
            res = res[:9000]
        new = []
    
        for pressure, paths, opened in res:
            me = paths[0][-1]
            elephant = paths[1][-1]

            p = sum(flows[o] for o in opened)
            pressure += p

            for my_paths, op in options(graph, flows, me, paths[0], opened):
                options = options(graph, flows, elephant, paths[1], op)
                for elephant_paths, elephant_options in options:
                    new.append((pressure, [my_paths, elephant_paths], elephant_options))
        res = new

    return max(res)


def solve(graph, flows):
    res, _, _ = frontier(graph, flows, "AA")
    return str(res)


if __name__ == "__main__":
    print("Part 2 : " + solve())