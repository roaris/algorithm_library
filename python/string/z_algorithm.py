def z_algo(s): #空文字列に注意!
    c = 0
    n = len(s)
    z = [0]*n
    
    for i in range(1, n):
        l = i-c
        
        if i+z[l]<c+z[c]:
            z[i] = z[l]
        else:
            j = max(0, c+z[c]-i)
            
            while i+j<n and s[j]==s[i+j]:
                j += 1
            
            z[i] = j
            c = i
    
    z[0] = n
    return z