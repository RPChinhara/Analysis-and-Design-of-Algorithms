import sys

INF = sys.maxsize

def shortest_path(costMat, V):
    graph = [[INF for i in range(V)] for j in range(V)]

    for i in range(V):
        for j in range(V):
            graph[i][j] = costMat[i][j]

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if graph[i][k] != INF and graph[k][j] != INF:
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    return graph


# Number of Vertices
V = 7

# Cost Matrix
cost_matrix = [ [0, 3, 6, INF, INF, INF, INF],
                [3, 0, 2, 1, INF, INF, INF],
                [6, 2, 0, 1, 4, 2, INF],
                [INF, 1, 1, 0, 2, INF, 4],
                [INF, INF, 4, 2, 0, 2, 1],
                [INF, INF, 2, INF, 2, 0, 1],
                [INF, INF, INF, 4, 1, 1, 0]]


output = shortest_path(cost_matrix, V)

print("Output Matrix:")
for i in range(V):
    print(output[i])

sum = 0
for i in range(V):
    for j in range(i + 1, V):
        sum += output[i][j]

print("Sum of shortest path is: ", sum)