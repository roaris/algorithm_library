// https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bd
#include <bits/stdc++.h>
using namespace std;

struct RollingHash {
    vector<long long> acc = {0};
    vector<long long> power = {1};
    int base = 17;
    int mod = 1000000007;
    
    RollingHash(string s) {
        for (int i=0; i<s.size(); i++) {
            acc.push_back((acc.back()*base+(s[i]-'a'+1))%mod);
            power.push_back(power.back()*base%mod);
        }
    }
    
    long long get(int l, int r) {
        long long h = (acc[r]-acc[l]*power[r-l])%mod;
        if (h<0) h += mod;
        return h;
    }
};

int main() {
    cin.tie(0); ios::sync_with_stdio(false);
    
    int N, Q; cin >> N >> Q;
    string s; cin >> s;
    RollingHash rh(s);
    
    while (Q--) {
        int a, b, c, d; cin >> a >> b >> c >> d;
        if (rh.get(a-1, b)==rh.get(c-1, d)) cout << "Yes" << endl;
        else cout << "No" << endl;
    }
}
