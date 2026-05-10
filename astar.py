
import heapq

# Heuristic Function
def h(s, goal):

    c = 0

    for i in range(9):

        if s[i] != -1 and s[i] != goal[i]:

            c += 1

    return c


# Generate Possible Moves
def moves(s):

    p = s.index(-1)

    row = p // 3
    col = p % 3

    next_states = []

    d = [(-1,0), (1,0), (0,-1), (0,1)]

    for dr, dc in d:

        nr = row + dr
        nc = col + dc

        if 0 <= nr < 3 and 0 <= nc < 3:

            np = nr * 3 + nc

            t = s[:]

            t[p], t[np] = t[np], t[p]

            next_states.append(t)

    return next_states


# A* Algorithm
def astar(start, goal):

    open = []

    heapq.heappush(open, (h(start, goal), 0, start))

    visited = []

    while open:

        f, g, cur = heapq.heappop(open)

        print(cur)

        if cur == goal:

            print("Solved")

            return

        visited.append(cur)

        for nxt in moves(cur):

            if nxt not in visited:

                g1 = g + 1

                f1 = g1 + h(nxt, goal)

                heapq.heappush(open, (f1, g1, nxt))


# Driver Code

print("Enter Start State (use -1 for empty space):")

start = list(map(int, input().split()))

print("Enter Goal State:")

goal = list(map(int, input().split()))

astar(start, goal)
