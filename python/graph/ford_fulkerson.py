import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5+100)
from collections import *

#最大流: sからtに流すことのできる最大のデータ量
#最小カット: sからtへのパスが存在しなくなるために、除去しなければならない辺の容量の和の最小値
#最大流=最小カット
class FordFulkerson:
    def __init__(self, N, edges): #edges: (s, t, c) sからtに向かう容量cの有向辺
        self.N = N
        self.G = defaultdict(lambda : defaultdict(int))
        
        for s, t, cap in edges:
            self.G[s][t] += cap
        
    def dfs(self, v, t, f):
        if v==t:
            return f
        
        self.used[v] = True
        
        for nv, cap in self.G[v].items():
            if not self.used[nv] and self.G[v][nv]>0:
                d = self.dfs(nv, t, min(f, self.G[v][nv]))
                
                if d>0:
                    self.G[v][nv] -= d
                    self.G[nv][v] += d
                    
                    return d
        
        return 0
    
    def max_flow(self, s, t):
        flow = 0
        
        while True:
            self.used = [False]*self.N
            f = self.dfs(s, t, 10**18)
        
            if f==0:
                return flow
        
            flow += f
