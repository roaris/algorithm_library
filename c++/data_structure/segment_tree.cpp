//AOJ DSL_2_A
#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i=0; i<n; i++)
typedef long long ll;
//const ll INF = 10000000000;
//const ll MOD = 1000000007;

//二項演算は結合法則が成り立てばOK
struct segtree {
    int size;
    vector<ll> node;
    
    segtree(int n) {
        size = 1;
        while (size<n) size *= 2;
        node.resize(2*size-1);
        //ここ初期値にする
        fill(node.begin(), node.end(), 2147483647);
    }
    
    //k番目(0-indexed)の値をaにする
    void update(int k, int a) {
        k += size-1;
        node[k] = a;
        while (k>0) {
            k = (k-1)/2;
            //ここ変える
            node[k] = min(node[2*k+1], node[2*k+2]);
        }
    }
    
    ll query(int a, int b, int k, int l, int r) {
        //ここ単位元にする
        if (r<=a || b<=l) return 2147483647;
        if (a<=l && r<=b) return node[k];
        else {
            ll vl = query(a, b, 2*k+1, l, (l+r)/2);
            ll vr = query(a, b, 2*k+2, (l+r)/2, r);
            //ここ変える
            return min(vl, vr);
        }
    }
    
    //[a, b)に対するクエリ
    ll get(int a, int b) {
        return query(a, b, 0, 0, size);
    }
};

int main() {
    int n, q; cin >> n >> q;
    segtree st(n);
    
    rep(i, q) {
        int f; cin >> f;
        if (f==0) {
            int x, y; cin >> x >> y;
            st.update(x, y);
        }
        else {
            int x, y; cin >> x >> y;
            cout << st.get(x, y+1) << endl;
        }
    }
}
