def era(n): #n以下の素数を列挙
    is_prime = [True]*(n+1)
    is_prime[0] = False
    is_prime[1] = False
    
    for i in range(2, int(n**0.5)+1):
        if not is_prime[i]:
            continue
        
        for j in range(2*i, n+1, i):
            is_prime[j] = False
    
    return [i for i in range(n+1) if is_prime[i]]
