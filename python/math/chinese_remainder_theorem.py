# https://yukicoder.me/problems/no/187
import sys
input = sys.stdin.readline
from math import gcd

def ext_gcd(a, b):
    if b==0:
        return 1, 0
    
    s, t = ext_gcd(b, a%b)
    return t, s-a//b*t

def crt(rs, ms):
    r, m = 0, 1
    
    for ri, mi in zip(rs, ms):
        p, q = ext_gcd(m, mi)
        g = gcd(m, mi)
        
        if (ri-r)%g!=0:
            return -1, -1
        
        r += m*(ri-r)//g*p
        m *= mi//g
        r %= m
    
    return r, m

N = int(input())
rs, ms = [], []

for _ in range(N):
    r, m = map(int, input().split())
    rs.append(r)
    ms.append(m)

r, m = crt(rs, ms)

if r==-1:
    print(r)
else:
    if r==0:
        print(m%(10**9+7))
    else:
        print(r%(10**9+7))
