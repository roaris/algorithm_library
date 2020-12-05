from heapq import *

class Mincostflow:
    def __init__(self, N):
        self.N = N
        self.G = [[] for _ in range(N)]
        
    def add_edge(self, u, v, cap, cost):
        self.G[u].append([v, cap, cost, len(self.G[v])])
        self.G[v].append([u, 0, -cost, len(self.G[u])-1])
    
    def min_cost_flow(self, s, t, f):
        res = 0
        h = [0]*self.N
        
        while f>0:
            dist = [10**18]*self.N
            dist[s] = 0
            pq = [(0, s)]
            prev_v = [-1]*self.N
            prev_e = [-1]*self.N
            
            while pq:
                d, v = heappop(pq)
                
                if dist[v]<d:
                    continue
                
                for i in range(len(self.G[v])):
                    nv, cap, cost, _  = self.G[v][i]
                    
                    if cap>0 and dist[nv]>dist[v]+cost+h[v]-h[nv]:
                        dist[nv] = dist[v]+cost+h[v]-h[nv]
                        prev_v[nv] = v
                        prev_e[nv] = i
                        heappush(pq, (dist[nv], nv))
            
            if dist[t]==10**18:
                return -1
            
            for i in range(self.N):
                h[i] += dist[i]
                
            d = f
            v = t
            
            while v!=s:
                d = min(d, self.G[prev_v[v]][prev_e[v]][1])
                v = prev_v[v]
            
            f -= d
            res += d*h[t]
            v = t
            
            while v!=s:
                self.G[prev_v[v]][prev_e[v]][1] -= d
                rev = self.G[prev_v[v]][prev_e[v]][3]
                self.G[v][rev][1] += d
                v = prev_v[v]
        
        return res
