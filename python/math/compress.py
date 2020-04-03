from collections import defaultdict
 
def compress(l):
    l = list(set(l))
    l.sort()
    idx = defaultdict(int)
    c = 0
    
    for li in l:
        idx[li] = c
        c += 1
    
    return idx
