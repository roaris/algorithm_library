#EDPC Z
import sys
input = sys.stdin.readline
from collections import *

class CHT: #傾きの単調性と最小値クエリのxの単調性を仮定
    def __init__(self):
        self.q = deque([]) #直線群
        
    def f(self, f1, x): #直線f1のxの値
        return f1[0]*x+f1[1]
    
    def check(self, f1, f2, f3): #f2を削除しても良いかの判定
        return (f2[0]-f1[0])*(f3[1]-f2[1])>=(f2[1]-f1[1])*(f3[0]-f2[0])
    
    def add_line(self, a, b): #傾きa, 切片bの直線を追加
        while len(self.q)>=2 and self.check(self.q[-2], self.q[-1], (a, b)):
            self.q.pop()
        
        self.q.append((a, b))
    
    def get(self, x): #xでの最小値
        while len(self.q)>=2 and self.f(self.q[0], x)>=self.f(self.q[1], x):
            self.q.popleft()
        
        return self.f(self.q[0], x)
    
N, C = map(int, input().split())
h = list(map(int, input().split()))
dp = [0]*N
cht = CHT()
cht.add_line(-2*h[0], h[0]**2)

for i in range(1, N):
    dp[i] = h[i]**2+C+cht.get(h[i])
    cht.add_line(-2*h[i], dp[i]+h[i]**2)

print(dp[N-1])
