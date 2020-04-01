import sys
sys.setrecursionlimit(10**5)

def dfs(v, pv):
    global c
    
    begin[v] = c
    euler_tour.append(v)
    c += 1
    
    for nv in G[v]:
        if nv!=pv:
            dfs(nv, v)
            euler_tour.append(v)
            c += 1
    
    end[v] = c

N = int(input())
G = [[] for _ in range(N)]

for _ in range(N-1):
    u, v = map(int, input().split())
    G[u-1].append(v-1)
    G[v-1].append(u-1)

c = 0
begin = [-1]*N
end = [-1]*N
euler_tour = []
dfs(0, -1)

print(begin)
print(end)
print(euler_tour)
