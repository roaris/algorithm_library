//AOJ NTL_1_B
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll m, n;

ll mod_pow(ll x, ll n, ll mod) {
    ll res = 1;
    
    while (n>0) {
        if (n&1) res = res*x%mod;
        x = x*x%mod;
        n >>= 1;
    }
    
    return res;
}

int main() {
    cin >> m >> n;
    cout << mod_pow(m, n, 1000000007) << endl;
}
