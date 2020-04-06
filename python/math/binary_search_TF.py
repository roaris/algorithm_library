def binary_search():
    #ここ変える
    l, r = 0, N-1
    
    while l<=r:
        m = (l+r)//2
        
        if judge(m):
            l = m+1
        else:
            r = m-1
    
    return r
