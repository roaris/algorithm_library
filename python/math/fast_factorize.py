class Fast_factorize:
    def __init__(self, n):
        self.p = [-1]*(n+1)
        
        for i in range(2, n+1):
            if self.p[i]==-1:
                for j in range(i, n+1, i):
                    if self.p[j]==-1:
                        self.p[j] = i
    
    def factorize(self, n):
        res = []
        
        while n>1:
            res.append(self.p[n])
            n //= self.p[n]
        
        return res
