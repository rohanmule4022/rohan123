# Graph Coloring using Backtracking and Branch & Bound

n = int(input("Enter number of vertices: "))

graph = []

print("Enter adjacency matrix:")

for i in range(n):

    row = list(map(int, input().split()))
    graph.append(row)

m = int(input("Enter number of colors: "))

colors = [0] * n

def isSafe(node, color):

    for k in range(n):

        if graph[node][k] == 1 and colors[k] == color:
            return False

    return True

def solve(node):

    if node == n:
        return True

    for color in range(1, m + 1):

        if isSafe(node, color):

            colors[node] = color

            if solve(node + 1):
                return True

            colors[node] = 0

    return False

if solve(0):

    print("\nSolution Found:\n")

    for i in range(n):

        print("Vertex", i, "--> Color", colors[i])

else:

    print("No solution exists")
