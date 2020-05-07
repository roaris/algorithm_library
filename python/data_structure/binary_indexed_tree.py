#AOJ DSL_2_B
#クエリが区間の和だったらセグ木よりもBITの方が高速!

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

    #sum[0:i)
    def acc(self, i):
        s = 0
        
        while i>0:
            s += self.bit[i]
            i -= i&(-i)
        
        return s
    
    #[l:r]の和を求める
    def get(self, l, r):
        return self.acc(r)-self.acc(l-1)
    
    #i番目(0-indexed)の値をxに変更する
    def update(self, i, x):
        bit.add(i, -self.get(i, i)+x)

n, q = map(int, input().split())
bit = BIT(n)

for _ in range(q):
    c, x, y = map(int, input().split())
    
    if c==0:
        bit.add(x-1, y)
    else:
        print(bit.acc(y-1)-bit.acc(x-2))
