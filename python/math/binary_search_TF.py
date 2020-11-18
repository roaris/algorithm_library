def binary_search():
    #0除算に注意！！！
    l, r = 0, N-1
    
    while l<=r:
        m = (l+r)//2
        
        if judge(m):
            l = m+1
        else:
            r = m-1
    
    return r
