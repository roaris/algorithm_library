// https://atcoder.jp/contests/abc242/tasks/abc242_g
// O(N√Q)
#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i=0; i<n; i++)
#define pb push_back
typedef long long ll;

struct Mo {
    int N;
    vector<pair<int, int>> lr;
    
    Mo(int N) : N(N) {}
    
    void add(int l, int r) { // 0-indexed, [l, r]
        lr.emplace_back(l, r);
    }
    
    void run(auto& add_left, auto& add_right, auto& erase_left, auto& erase_right, auto& out) {
        int Q = lr.size();
        int W = N/min(N, (int)sqrt(Q)); // ブロック幅
        vector<int> ord(Q);
        iota(ord.begin(), ord.end(), 0);
        sort(ord.begin(), ord.end(), [&](int x, int y) {
            int x_block = lr[x].first/W;
            int y_block = lr[y].first/W;
            if (x_block!=y_block) return x_block<y_block;
            return (x_block&1) ? lr[x].second>lr[y].second : lr[x].second<lr[y].second;
        });
        
        int l = 0;
        int r = -1;

        for (int i : ord) {
            while (l>lr[i].first) add_left(--l);
            while (r<lr[i].second) add_right(++r);
            while (l<lr[i].first) erase_left(l++);
            while (r>lr[i].second) erase_right(r--);
            out(i);
        }
    }
};

int main() {
    cin.tie(0); ios::sync_with_stdio(false);
    
    int N; cin >> N;
    int A[N];
    rep(i, N) {
        cin >> A[i];
        A[i]--;
    }
    
    Mo mo(N);
    int Q; cin >> Q;
    rep(i, Q) {
        int l, r; cin >> l >> r;
        mo.add(l-1, r-1);
    }
    
    int cnt[N]; rep(i, N) cnt[i] = 0;
    int pair = 0;
    int ans[Q];
    
    auto add_left = [&](int i) { // iを左端に追加
        cnt[A[i]]++;
        if (cnt[A[i]]%2==0) pair++;
    };
    
    auto add_right = [&](int i) { // iを右端に追加
        cnt[A[i]]++;
        if (cnt[A[i]]%2==0) pair++;
    };
    
    auto erase_left = [&](int i) { // iを左端から削除
        cnt[A[i]]--;
        if (cnt[A[i]]%2==1) pair--;
    };
    
    auto erase_right = [&](int i) { // iを右端から削除
        cnt[A[i]]--;
        if (cnt[A[i]]%2==1) pair--;
    };
    
    auto out = [&](int q) { // q個目のクエリに答える
        ans[q] = pair;
    };
    
    mo.run(add_left, add_right, erase_left, erase_right, out);
    rep(i, Q) cout << ans[i] << endl;
}
