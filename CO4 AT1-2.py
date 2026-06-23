# Atchaya Vharsne S (192524185)
# Time Complexity : O(n^3)
# Space Complexity : O(n^2)
def kruskals(graph):
    n = len(graph)
    parent = list(range(n))
    def find(i):
        while parent[i] != i:
            i = parent[i]
        return i
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            if graph[i][j] != 0:
                edges.append((graph[i][j], i, j))
    edges.sort()
    cost = 0
    for weight, u, v in edges:
        if find(u) != find(v):
            parent[find(u)] = find(v)
            cost += weight
    return cost
graph = [[0, 2, 3, 0],[2, 0, 1, 4], [3, 1, 0, 5],[0, 4, 5, 0]]
print("Total Minimum Cost:", kruskals(graph))
