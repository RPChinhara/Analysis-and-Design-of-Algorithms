import sys

INF = sys.maxsize

def shortest_path(costMat, V):
    for k in range(V):
        for i in range(V):
            for j in range(V):
                costMat[i][j] = min(costMat[i][j], costMat[i][k] + costMat[k][j])

    return costMat

V = 7
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