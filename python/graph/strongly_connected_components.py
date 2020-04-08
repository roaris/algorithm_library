#scc: 強連結成分分解を行う
#G: 順方向グラフ
#RG: 逆方向グラフ
#label: ラベル数
#group: 各頂点のラベル
#---------------------------------------------------
#construct: 縮約したグラフを構築する
#belong: ラベルiに属する頂点のリスト
#G2: ラベル間のグラフ
#---------------------------------------------------
#縮約後のグラフはDAGになる→DPが可能になる!
#強連結成分毎に前処理して、DAGに潰してDPするのは典型
#---------------------------------------------------

import sys
sys.setrecursionlimit(10**6+100)

def scc():
    order = []
    visited = [False]*N
    
    def dfs(v):
        visited[v] = True
        
        for nv in G[v]:
            if not visited[nv]:
                dfs(nv)
        
        order.append(v)
    
    for v in range(N):
        if not visited[v]:
            dfs(v)
    
    visited = [False]*N
    group = [-1]*N
    label = 0
    
    def rdfs(v, label):
        group[v] = label
        visited[v] = True
        
        for nv in RG[v]:
            if not visited[nv]:
                rdfs(nv, label)
    
    for v in reversed(order):
        if not visited[v]:
            rdfs(v, label)
            label += 1
            
    return label, group
    
def construct():
    belong = [[] for _ in range(label)]
    G2 = [set() for _ in range(label)]
    
    for v in range(N):
        l1 = group[v]
        
        for nv in G[v]:
            l2 = group[nv]
            
            if l1==l2:
                continue
            
            G2[l1].add(l2)
        
        belong[l1].append(v)
    
    return belong, G2
