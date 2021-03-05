from math import gcd
 
def extGCD(a, b): #ax+by=gcd(a,b)となる(x,y)を1つ求める
    if b==0:
        return 1, 0
    
    s, t = extGCD(b, a%b)
    return t, s-a//b*t
 
def crt(rs, ms): #x≡rs[0](mod ms[0]),...となるxについてx≡r(mod lcm(ms))となるrを求める
    r, m = 0, 1
    
    for i in range(len(rs)):
        p, q = extGCD(m, ms[i])
        g = gcd(m, ms[i])
        
        if (rs[i]-r)%g!=0:
            return -1
        
        t = (rs[i]-r)//g*p%(ms[i]//g)
        r += m*t
        m *= ms[i]//g
    
    return r%m