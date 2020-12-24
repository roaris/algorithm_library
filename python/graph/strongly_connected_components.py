#縮約後のグラフはDAGになる→DPが可能になる!
#強連結成分毎に前処理して、DAGに潰してDPするのは典型
import sys
input = sys.stdin.readline
sys.setrecursionlimit(5*10**5+10)

class Scc:
    def __init__(self, N, G):
        self.N = N
        self.G = G
        self.RG = [[] for _ in range(N)]
        
        for v in range(N):
            for nv in G[v]:
                self.RG[nv].append(v)
    
    def decomp(self):
        order = []
        visited = [False]*self.N
        
        def dfs(v):
            visited[v] = True
            
            for nv in self.G[v]:
                if not visited[nv]:
                    dfs(nv)
            
            order.append(v)
            
        for v in range(self.N):
            if not visited[v]:
                dfs(v)
        
        visited = [False]*self.N
        comp = [-1]*self.N
        label = 0
        
        def rdfs(v, label):
            comp[v] = label
            visited[v] = True
            
            for nv in self.RG[v]:
                if not visited[nv]:
                    rdfs(nv, label)
            
        for v in reversed(order):
            if not visited[v]:
                rdfs(v, label)
                label += 1
        
        return label, comp
    
    def construct(self):
        label, comp = self.decomp()
        belong = [[] for _ in range(label)]
        nG = [set() for _ in range(label)]
        
        for v in range(self.N):
            for nv in self.G[v]:
                if comp[v]!=comp[nv]:
                    nG[comp[v]].add(comp[nv])
            
            belong[comp[v]].append(v)
        
        return belong, nG
