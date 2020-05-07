from collections import defaultdict
 
def compress(l):
    l = list(set(l))
    l.sort()
    idx = defaultdict(int)

    for i in range(len(l)):
        idx[l[i]] = i
    
    return idx
