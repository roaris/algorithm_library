#AOJ GRL_1_A
import sys
input = sys.stdin.readline
from heapq import *

def dijkstra(sta):
    dist = [10**18]*V
    dist[sta] = 0
    pq = []
    heappush(pq, (dist[sta], sta))
    
    while pq:
        d, v = heappop(pq)
        
        if dist[v]<d:
            continue
        
        for nv, w in G[v]:
            if dist[nv]>dist[v]+w:
                dist[nv] = dist[v]+w
                heappush(pq, (dist[nv], nv))
    
    return dist

V, E, r = map(int, input().split())
G = [[] for _ in range(V)]

for _ in range(E):
    s, t, d = map(int, input().split())
    G[s].append((t, d))

dist = dijkstra(r)

for di in dist:
    if di==10**18:
        print('INF')
    else:
        print(di)
