# To solve the 8-puzzle problem using A* search and the Manhattan-distance heuristic. The puzzle consists of eight numbered tiles and one blank space.


import heapq

goal = ('1','2','3','4','5','6','7','8','_')

def heuristic(s):
    d = 0
    for i, x in enumerate(s):
        if x != '_':
            g = int(x) - 1
            d += abs(i//3 - g//3) + abs(i%3 - g%3)
    return d

def show(s):
    for i in range(0, 9, 3):
        print(' '.join(s[i:i+3]))
    print()

def astar(start):
    pq = [(heuristic(start), 0, start)]
    cost = {start: 0}
    parent = {start: (None, None)}

    while pq:
        f, g, s = heapq.heappop(pq)

        if g != cost[s]:
            continue

        if s == goal:
            path = []
            while parent[s][0] is not None:
                prev, move = parent[s]
                path.append((move, s))
                s = prev
            path.reverse()
            return path

        z = s.index('_')
        r, c = z//3, z%3

        moves = [('UP', -1, 0), ('DOWN', 1, 0),
                 ('LEFT', 0, -1), ('RIGHT', 0, 1)]

        for name, dr, dc in moves:
            nr, nc = r+dr, c+dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                nz = nr*3 + nc
                t = list(s)
                t[z], t[nz] = t[nz], t[z]
                t = tuple(t)
                ng = g + 1

                if ng < cost.get(t, float('inf')):
                    cost[t] = ng
                    parent[t] = (s, name)
                    heapq.heappush(pq, (ng + heuristic(t), ng, t))

    return None

print("Enter the initial state (_ for blank):")
start = tuple(input().split() + input().split() + input().split())

if len(start) != 9 or set(start) != set(goal):
    print("Invalid puzzle!")
else:
    print("\nInitial State:")
    show(start)
    path = astar(start)

    if path is None:
        print("No solution exists")
    else:
        for i, (move, state) in enumerate(path, 1):
            print("Move", i, ":", move)
            show(state)
        print("Goal State Reached")
        print("Solution Cost =", len(path))
