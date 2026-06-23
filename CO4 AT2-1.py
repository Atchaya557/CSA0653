# Atchaya Vharsne S (192524185)
def kruskal(graph):
    n = len(graph)

    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x

    def union(x, y):
        px = find(x)
        py = find(y)

        if px != py:
            parent[py] = px
            return True

        return False

    edges = []

    # Convert adjacency matrix to edge list
    for i in range(n):
        for j in range(i + 1, n):
            if graph[i][j] != 0:
                edges.append((graph[i][j], i, j))

    edges.sort()

    mst = []
    total_cost = 0

    for cost, u, v in edges:
        if union(u, v):
            mst.append((u, v, cost))
            total_cost += cost

    return mst, total_cost


graph = [
    [0, 2, 4, 0],
    [2, 0, 1, 7],
    [4, 1, 0, 3],
    [0, 7, 3, 0]
]

mst, total = kruskal(graph)

print("Selected Routes:")
for u, v, cost in mst:
    print(u, "-", v, ":", cost)

print("Minimum Transportation Cost =", total)
