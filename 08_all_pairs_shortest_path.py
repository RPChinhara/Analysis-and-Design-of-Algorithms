import sys

INF = sys.maxsize

def shortest_path(V, E, edges):
    graph = [[INF for i in range(V)] for j in range(V)]

    for i in range(E):
        # Get source and destination
        # with weight
        u = edges[i][0]
        v = edges[i][1]
        w = edges[i][2]

        # Add the edges
        graph[u][v] = w
        graph[v][u] = w

    for i in range(V):
        for j in range(V):
            graph[i][j] = graph[i][j]

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if graph[i][k] != INF and graph[k][j] != INF:
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    sum = 0

    for i in range(V):
        for j in range(i + 1, V):
            sum += graph[i][j]

    return sum


# Number of Vertices
V = 4
# Number of Edges
E = 3
# Given Edges with weight
Edges = [[0, 1, 1], [1, 2, 2], [2, 3, 3]]

print(shortest_path(V, E, Edges))