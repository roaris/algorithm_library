vector<P> factorize(int n) {
    vector<P> res;
    for (int i=2; i*i<=n; i++) {
        int cnt = 0;
        while (n%i==0) {
            cnt++;
            n /= i;
        }
        if (cnt>0) res.pb(P(i, cnt));
    }
    if (n!=1) res.pb(P(n, 1));
    return res;
}
