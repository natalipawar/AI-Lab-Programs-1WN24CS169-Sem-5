# Iterative Deepening Search (IDS)

def dls(graph, node, goal, limit, path):
    if node == goal:
        return path + [node]
    if limit == 0:
        return None

    for child in graph.get(node, []):
        if child not in path:
            result = dls(graph, child, goal, limit - 1, path + [node])
            if result:
                return result
    return None

def ids(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        print("Depth limit:", depth)
        result = dls(graph, start, goal, depth, [])
        if result:
            return result
    return None

graph = {}
n = int(input("Enter number of nodes: "))

for _ in range(n):
    node, *children = input("Enter node and children: ").split()
    graph[node] = [] if children == ['-'] else children

start = input("Enter initial state: ")
goal = input("Enter goal state: ")
max_depth = int(input("Enter maximum depth: "))

result = ids(graph, start, goal, max_depth)

if result:
    print("Goal found!")
    print("Solution path:", " -> ".join(result))
    print("Solution depth:", len(result) - 1)
else:
    print("Goal not found within maximum depth.")
