def hakidashi(A): #mod2の掃き出し法 O(NM^2) 戻り値は(rank, 変換後の行列)
    N, M = len(A), len(A[0])
    pos = 0
    
    for i in range(M):
        found = False
        
        for j in range(pos, N):
            if A[j][i]==1:
                A[pos], A[j] = A[j], A[pos]
                found = True
                break
        
        if found:
            for j in range(N):
                if j!=pos and A[j][i]==1:
                    for k in range(i, M):
                        A[j][k] ^= A[pos][k]
            
            pos += 1
    
    return pos, A
