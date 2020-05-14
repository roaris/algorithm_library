def mat_mul(A, B):
    C = [[0]*len(B[0]) for _ in range(len(A))]
    
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(A[0])):
                C[i][j] += A[i][k]*B[k][j]
                C[i][j] %= MOD
    
    return C

def mat_pow(A, n):
    res = [[0]*len(A) for _ in range(len(A))]
    
    for i in range(len(A)):
        res[i][i] = 1
    
    while n>0:
        if n&1:
            res = mat_mul(res, A)
        
        n >>= 1
        A = mat_mul(A, A)
    
    return res
