# https://yukicoder.me/problems/no/913
import sys
input = sys.stdin.readline
from collections import *

class CHT: # 傾きの単調減少と最小値クエリのxの単調性を仮定
    def __init__(self):
        self.q = deque([]) # 直線群
        
    def f(self, f1, x): # 直線f1のxの値
        return f1[0]*x+f1[1]
    
    def check(self, f1, f2, f3): # f2を削除しても良いかの判定
        return (f2[0]-f1[0])*(f3[1]-f2[1])>=(f2[1]-f1[1])*(f3[0]-f2[0])
    
    def add_line(self, a, b): # 傾きa, 切片bの直線を追加
        while len(self.q)>=2 and self.check(self.q[-2], self.q[-1], (a, b)):
            self.q.pop()
        
        self.q.append((a, b))
    
    def get_inc(self, x): # xでの最小値(xは単調増加)
        while len(self.q)>=2 and self.f(self.q[0], x)>=self.f(self.q[1], x):
            self.q.popleft()
        
        return self.f(self.q[0], x)
    
    def get_dec(self, x): # xでの最小値(xは単調減少)
        while len(self.q)>=2 and self.f(self.q[-1], x)>=self.f(self.q[-2], x):
            self.q.pop()
        
        return self.f(self.q[-1], x)

def dfs(l, r): # [l, r)
    global ans
    
    if l>=r:
        return

    m = (l+r)//2
    # [l, m)
    cht = CHT()
    
    for i in range(m+1, r+1):
        cht.add_line(-2*i, i*i+acc[i])
    
    res = 10**18
    
    for i in range(l, m):
        res = min(res, cht.get_inc(i)+i*i-acc[i])
        ans[i] = min(ans[i], res)
    
    # [m, r)
    cht = CHT()
    
    for i in range(l, m+1):
        cht.add_line(-2*i, i*i-acc[i])
    
    res = 10**18
    
    for i in range(r, m, -1):
        res = min(res, cht.get_dec(i)+i*i+acc[i])
        ans[i-1] = min(ans[i-1], res)
    
    dfs(l, m)
    dfs(m+1, r)
    
N = int(input())
A = list(map(int, input().split()))
acc = [0]

for Ai in A:
    acc.append(acc[-1]+Ai)

ans = [10**18]*N
dfs(0, N)

for i in range(N):
    print(ans[i])
