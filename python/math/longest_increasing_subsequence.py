from bisect import *

#a1<a2<...
def lis(l):
    dp = [10**18]*(len(l)+1)
    dp[0] = -10**18
    
    for i in range(len(l)):
        j = bisect_left(dp, l[i])
        dp[j] = l[i]
    
    return bisect_left(dp, 10**18)-1
