#ATC001 B
import sys
input = sys.stdin.readline

class Unionfind:
    def __init__(self, n):
        self.par = [-1]*n
        self.rank = [1]*n
    
    def root(self, x):
        r = x
        
        while not self.par[r]<0:
            r = self.par[r]
        
        t = x
        
        while t!=r:
            tmp = t
            t = self.par[t]
            self.par[tmp] = r
        
        return r
    
    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        
        if rx==ry:
            return
        
        if self.rank[rx]<=self.rank[ry]:
            self.par[ry] += self.par[rx]
            self.par[rx] = ry
            
            if self.rank[rx]==self.rank[ry]:
                self.rank[ry] += 1
        else:
            self.par[rx] += self.par[ry]
            self.par[ry] = rx
    
    def is_same(self, x, y):
        return self.root(x)==self.root(y)
    
    def count(self, x):
        return -self.par[self.root(x)]
        
N, Q = map(int, input().split())
uf = Unionfind(N)

for _ in range(Q):
    P, A, B = map(int, input().split())
    
    if P==0:
        uf.unite(A, B)
    else:
        if uf.is_same(A, B):
            print('Yes')
        else:
            print('No')
