def multiply(A, B, C, n):
    for i in range(n):
        for j in range(len(B[0])):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C            
    
