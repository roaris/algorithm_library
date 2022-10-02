# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bd
import sys
input = sys.stdin.readline
from collections import *

class RollingHash:
    def __init__(self, a):
        self.base = 31
        self.mod = 10**9+7
        self.acc = [0]
        self.power = [1]
        
        for i in range(len(a)):
            self.acc.append((self.acc[-1]*self.base%self.mod+a[i])%self.mod)
            self.power.append(self.power[-1]*self.base%self.mod)
    
    def get(self, l, r):
        return (self.acc[r]-self.acc[l]*self.power[r-l])%self.mod
    
N, Q = map(int, input().split())
S = input()[:-1]
rh = RollingHash([ord(c)-ord('a') for c in S])

for _ in range(Q):
    a, b, c, d = map(int, input().split())
    
    if rh.get(a-1, b)==rh.get(c-1, d):
        print('Yes')
    else:
        print('No')
