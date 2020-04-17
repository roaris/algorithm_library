class LowestCommonAncestor:
    def __init__(self, N, G):
        self.N = N
        self.G = G
        self.log_size = 22
        self.parent = [[-1]*self.N for _ in range(self.log_size)]
        q = deque([0])
        self.depth = [-1]*self.N
        self.depth[0] = 0
        
        while q:
            v = q.popleft()
            
            for nv in self.G[v]:
                if self.depth[nv]==-1:
                    self.parent[0][nv] = v
                    self.depth[nv] = self.depth[v]+1
                    q.append(nv)
                    
        for i in range(1, self.log_size):
            for v in range(self.N):
                if self.parent[i-1][v]>=0:
                    self.parent[i][v] = self.parent[i-1][self.parent[i-1][v]]
    
    def lca(self, u, v):
        if self.depth[u]>self.depth[v]:
            u, v = v, u
        
        for i in range(self.log_size):
            if ((self.depth[v]-self.depth[u])>>i)&1:
                v = self.parent[i][v]
        
        if u==v:
            return u
        
        for i in range(self.log_size-1, -1, -1):
            if self.parent[i][u]!=self.parent[i][v]:
                u, v = self.parent[i][u], self.parent[i][v]
        
        return self.parent[0][u]
    
    def dist(self, u, v):
        return self.depth[u]+self.depth[v]-2*self.depth[self.lca(u, v)]
