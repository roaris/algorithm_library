//ATC001 B
#include <bits/stdc++.h>
using namespace std;

int N, Q;

struct Unionfind {
    vector<int> par, rank;
    
    Unionfind(int n) {
        par.resize(n);
        fill(par.begin(), par.end(), -1);
        rank.resize(n);
    }
    
    int root(int x) {
        int r = x;
        while (!(par[r]<0)) r = par[r];
        int t = x;
        
        while (t!=r) {
            int tmp = t;
            t = par[t];
            par[tmp] = r;
        }
        
        return r;
    }
    
    void unite(int x, int y) {
        int rx = root(x);
        int ry = root(y);
        
        if (rx==ry) return;
        
        if (rank[rx]<=rank[ry]) {
            par[ry] += par[rx];
            par[rx] = ry;
            
            if (rank[rx]==rank[ry]) rank[ry]++;
        }
        else {
            par[rx] += par[ry];
            par[ry] = rx;
        }
    }
    
    bool is_same(int x, int y) {
        return root(x)==root(y);
    }
    
    int count(int x) {
        return -par[root(x)];
    }
};

int main() {
    cin.tie(0); ios::sync_with_stdio(false);
    
    cin >> N >> Q;
    Unionfind uf = Unionfind(N);
    
    for (int q=0; q<Q; q++) {
        int P, A, B; cin >> P >> A >> B;
        
        if (P==0) uf.unite(A, B);
        else {
            if (uf.is_same(A, B)) cout << "Yes" << endl;
            else cout << "No" << endl;
        }
    }
}
