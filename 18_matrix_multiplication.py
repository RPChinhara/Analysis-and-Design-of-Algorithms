def multiply(A, B, N):
    C = [[0 for i in range(N)] for j in range(N)]
	
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i][j] += A[i][k]*B[k][j]
    
    return C

A = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [2, 2, 2, 2]]
B = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [2, 2, 2, 2]]

print(multiply(A, B, 4))