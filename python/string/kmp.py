def make_table(s):
    n = len(s)
    res = [-1]*(n+1)
    j = -1
    
    for i in range(n):
        while j>=0 and s[i]!=s[j]:
            j = res[j]
        
        j += 1
        res[i+1] = j
    
    return res

def kmp(s, w): #s中のwと一致する箇所の先頭インデックスのリストを作成
    table = make_table(w)
    res = []
    m, i, n = 0, 0, len(s)
    
    while m+i<n:
        if w[i]==s[m+i]:
            i += 1
            
            if i==len(w):
                res.append(m)
                m = m+i-table[i]
                i = table[i]
        else:
            m = m+i-table[i]
            
            if i>0:
                i = table[i]
    
    return res
