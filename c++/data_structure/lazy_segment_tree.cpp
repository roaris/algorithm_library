//AOJ DSL_2_H RMQ and RAQ

#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i=0; i<n; i++)
typedef long long ll;
const ll INF=1000000000;

struct lazysegtree {
    int size;
    //初期値0
    vector<ll> node, lazy;
    
    lazysegtree(int n) {
        size = 1;
        while (size<n) size *= 2;
        node.resize(2*size-1);
        lazy.resize(2*size-1);
    }
    
    void eval(int k) {
        node[k] += lazy[k];
        
        if (k<size-1) {
            lazy[2*k+1] += lazy[k];
            lazy[2*k+2] += lazy[k];
        }
        
        lazy[k] = 0;
    }
    
    void update(int a, int b, ll x, int k, int l, int r) {
        eval(k);
        
        if (b<=l || r<=a) return;
        
        if (a<=l && r<=b) {
            lazy[k] += x;
            eval(k);
        }
        else {
            update(a, b, x, 2*k+1, l, (l+r)/2);
            update(a, b, x, 2*k+2, (l+r)/2, r);
            //ここ変える
            node[k] = min(node[2*k+1], node[2*k+2]);
        }
    }
    
    ll query(int a, int b, int k, int l, int r) {
        eval(k);
        
        //ここ単位元にする
        if (b<=l || r<=a) return INF;
        if (a<=l && r<=b) return node[k];
        ll vl = query(a, b, 2*k+1, l, (l+r)/2);
        ll vr = query(a, b, 2*k+2, (l+r)/2, r);
        //ここ変える
        return min(vl, vr);
    }
    
    //[a, b)にxを足す
    void add(int a, int b, ll x) {
        update(a, b, x, 0, 0, size);
    }
    
    //[a, b)に対するクエリ
    ll get(int a, int b) {
        return query(a, b, 0, 0, size);
    }
};

int main() {
    int n, q; cin >> n >> q;
    lazysegtree lst(n);
    
    rep(i, q) {
        int f; cin >> f;
        
        if (f==0) {
            int s, t, x; cin >> s >> t >> x;
            lst.add(s, t+1, x);
        }
        else {
            int s, t; cin >> s >> t;
            cout << lst.get(s, t+1) << endl;
        }
    }
}
