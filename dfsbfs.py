# DFS and BFS with User Input Graph and Target Node Search

graph = {}

# Input number of nodes
n = int(input("Enter number of nodes: "))

# Input graph
for i in range(n):

    node = input("Enter node: ")

    neighbours = input(
        f"Enter neighbours of {node} separated by space: "
    ).split()

    graph[node] = neighbours

# Display graph
print("\nGraph is:")
print(graph)

# Input starting node
start = input("\nEnter starting node: ")

# Input target node
target = input("Enter target node to search: ")

# ---------------- DFS ----------------

visited_dfs = set()

found_dfs = False

def dfs(node):

    global found_dfs

    if node not in visited_dfs and not found_dfs:

        print(node, end=" ")

        visited_dfs.add(node)

        # Check target node
        if node == target:

            print("\nTarget node found in DFS!")

            found_dfs = True

            return

        # Visit neighbours
        for neighbour in graph[node]:

            dfs(neighbour)

# ---------------- BFS ----------------

def bfs(start):

    visited_bfs = []

    queue = []

    visited_bfs.append(start)

    queue.append(start)

    while queue:

        node = queue.pop(0)

        print(node, end=" ")

        # Check target node
        if node == target:

            print("\nTarget node found in BFS!")

            return

        # Visit neighbours
        for neighbour in graph[node]:

            if neighbour not in visited_bfs:

                visited_bfs.append(neighbour)

                queue.append(neighbour)

    print("\nTarget node not found in BFS")

# ---------------- OUTPUT ----------------

print("\nDFS Traversal:")

dfs(start)

if not found_dfs:

    print("\nTarget node not found in DFS")

print("\nBFS Traversal:")

bfs(start)
