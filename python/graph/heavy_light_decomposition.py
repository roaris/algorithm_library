class HLD:
    def __init__(self, N, G):
        self.G = G
        self.par = [-1]*N #親ノード
        self.size = [1]*N #部分木のサイズ
        self.depth = [-1]*N #深さ
        self.dfs1(0, -1, 0)
        self.in_order = [-1]*N #行きがけ順
        self.in_order_now = 0
        self.top = [-1]*N #分解後の連結成分の中で最も浅い頂点
        self.dfs2(0, -1, 0)
    
    def dfs1(self, v, pv, d):
        self.depth[v] = d
        
        for nv in self.G[v]:
            if nv==pv:
                continue
            
            self.dfs1(nv, v, d+1)
            self.par[nv] = v
            self.size[v] += self.size[nv]
    
    def dfs2(self, v, pv, top_node):
        self.in_order[v] = self.in_order_now
        self.in_order_now += 1
        self.top[v] = top_node
        
        if self.size[v]==1:
            return
        
        M = 0
        heavy_node = -1
        
        for nv in self.G[v]:
            if nv==pv:
                continue
            
            if self.size[nv]>M:
                M = self.size[nv]
                heavy_node = nv
        
        self.dfs2(heavy_node, v, top_node)
        
        for nv in self.G[v]:
            if nv==pv:
                continue
            
            if nv!=heavy_node:
                self.dfs2(nv, v, nv)
    
    def query(self, u, v):
        res = []
        
        while self.top[u]!=self.top[v]:
            if self.depth[self.top[u]]<=self.depth[self.top[v]]:
                res.append((self.in_order[self.top[v]], self.in_order[v]))
                v = self.par[self.top[v]]
            else:
                res.append((self.in_order[self.top[u]], self.in_order[u]))
                u = self.par[self.top[u]]
        
        res.append((min(self.in_order[u], self.in_order[v]), max(self.in_order[u], self.in_order[v])))
        return res

N = 12
edges = [[0, 1], [1, 2], [2, 3], [2, 4], [1, 5], [0, 6], [6, 7], [7, 8], [7, 9], [0, 10], [10, 11]]
G = [[] for _ in range(N)]

for u, v in edges:
    G[u].append(v)
    G[v].append(u)

hld = HLD(N, G)
print(hld.par)
print(hld.size)
print(hld.depth)
print(hld.in_order)
print(hld.top)
print(hld.query(4, 9))
