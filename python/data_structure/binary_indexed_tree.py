#AOJ DSL_2_B
class BIT:
    #n:要素数
    def __init__(self, n):
        self.n = n
        self.bit = [0]*(n+1)
    
    #i番目(0-indexed)の値にxを足す
    def add(self, i, x):
        i += 1
        
        while i<=self.n:
            self.bit[i] += x
            i += i&(-i)
    
    #0からi番目までの値の和を求める
    def acc(self, i):
        i += 1
        s = 0
        
        while i>0:
            s += self.bit[i]
            i -= i&(-i)
        
        return s

n, q = map(int, input().split())
bit = BIT(n)

for _ in range(q):
    c, x, y = map(int, input().split())
    
    if c==0:
        bit.add(x-1, y)
    else:
        print(bit.acc(y-1)-bit.acc(x-2))
