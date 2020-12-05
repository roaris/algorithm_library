def manacher(s):
    res = [0]*len(s)
    i, j = 0, 0
    
    while i<len(s):
        while i-j>=0 and i+j<len(s) and s[i-j]==s[i+j]:
            j += 1
        
        res[i] = j
        k = 1
        
        while i-k>=0 and k+res[i-k]<j:
            res[i+k] = res[i-k]
            k += 1
            
        i += k
        j -= k

    return res
