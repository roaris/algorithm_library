#ABC061 D Score Attack
#ベルマンフォード法を使う時は、グラフが連結でない場合に注意する。
from collections import deque

def bfs(s, graph):
    visited = [False]*N
    visited[s] = True
    q = deque([s])
    
    while q:
        v = q.popleft()
        
        for nv in graph[v]:
            if not visited[nv]:
                visited[nv] = True
                q.append(nv)
    
    return visited

def bellmanford():
    dist = [10**18]*N
    dist[0] = 0
    
    for i in range(N):
        for s, t, c in edges:
            if not visited1[s] or not visited2[t]:
                continue
            
            if dist[t]>dist[s]+c:
                dist[t] = dist[s]+c
                
                if i==N-1:
                    print('inf')
                    exit()

    return dist[-1]

N, M = map(int, input().split())
edges = []
G = [[] for _ in range(N)]
rG = [[] for _ in range(N)]

for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((a-1, b-1, -c))
    G[a-1].append(b-1)
    rG[b-1].append(a-1)

visited1 = bfs(0, G)
visited2 = bfs(N-1, rG)

print(-bellmanford())
