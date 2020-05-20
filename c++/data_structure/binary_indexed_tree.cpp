struct BIT {
    int size;
    vector<int> node;
    
    BIT(int n) {
        size = n;
        node.resize(n+1);
    }
    
    void add(int i, int x) {
        i++;
        while (i<=size) {
            node[i] += x;
            i += i&(-i);
        }
    }
    
    int acc(int i) {
        int s = 0;
        while (i>0) {
            s += node[i];
            i -= i&(-i);
        }
        return s;
    }
    
    //小さい方からk番目(1-indexed)
    int get(int k) {
        int res = 0;
        int N = 1; while (N<size) N *= 2;
        for (int i=N/2; i>0; i/=2) {
            if (res+i<size && node[res+i]<k) {
                k = k-node[res+i];
                res = res+i;
            }
        }
        return res;
    }
};
