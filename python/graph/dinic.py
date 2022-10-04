# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_6_A&lang=ja
import sys
sys.setrecursionlimit(1000)
from collections import *

class Dinic:
    def __init__(self, N):
        self.N = N
        self.G = defaultdict(lambda: defaultdict(int))
        self.dist = [-1]*self.N
    
    def add_edge(self, u, v, cap):
        self.G[u][v] += cap
    
    def bfs(self, s):
        q = deque([s])
        self.dist = [-1]*self.N
        self.dist[s] = 0
        
        while q:
            v = q.popleft()
            
            for nv, cap in self.G[v].items():
                if cap>0 and self.dist[nv]==-1:
                    self.dist[nv] = self.dist[v]+1
                    q.append(nv)
    
    def dfs(self, v, t, f):
        if v==t:
            return f
        
        for nv, cap in self.G[v].items():
            if cap>0 and self.dist[v]<self.dist[nv]:
                d = self.dfs(nv, t, min(f, cap))
                
                if d>0:
                    self.G[v][nv] -= d
                    self.G[nv][v] += d
                    return d
                
        return 0
    
    def max_flow(self, s, t):
        flow = 0
        
        while True:
            self.bfs(s)
            
            if self.dist[t]==-1:
                return flow
            
            while True:
                f = self.dfs(s, t, 10**18)
                
                if f>0:
                    flow += f
                else:
                    break

N, M = map(int, input().split())
din = Dinic(N)

for _ in range(M):
    u, v, cap = map(int, input().split())
    din.add_edge(u, v, cap)

print(din.max_flow(0, N-1))
