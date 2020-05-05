const int MAX = 101000;
const int MOD = 1000000007;
int fact[MAX], finv[MAX], inv[MAX];

void Cinit() {
    fact[0] = fact[1] = 1;
    finv[0] = finv[1] = 1;
    inv[1] = 1;
    for (int i=2; i<MAX; i++) {
        fact[i] = fact[i-1]*i%MOD;
        inv[i] = MOD-inv[MOD%i]*(MOD/i)%MOD;
        finv[i] = finv[i-1]*inv[i]%MOD;
    }
}

int C(int n, int k) {
    if (n<k) return 0;
    if (n<0 || k<0) return 0;
    return fact[n]*(finv[k]*finv[n-k]%MOD)%MOD;
}
