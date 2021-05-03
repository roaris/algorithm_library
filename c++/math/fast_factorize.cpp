struct Fast_factorize {
    vector<int> p;
    
    Fast_factorize(int n) {
        p.resize(n+1);
        fill(p.begin(), p.end(), -1);
        for (int i=2; i<=n; i++) if (p[i]==-1) {
            for (int j=i; j<=n; j+=i) {
                if (p[j]==-1) p[j] = i;
            }
        }
    }
    
    vector<int> factorize(int n) {
        vector<int> res;
        while (n>1) {
            res.pb(p[n]);
            n /= p[n];
        }
        return res;
    }
};
