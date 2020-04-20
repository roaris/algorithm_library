//AOJ GRL_3_C
#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i=0; i<n; i++)
#define pb push_back

int N, M;
vector<int> G[10100];
vector<int> rG[10100];
bool used[10100];
vector<int> vs;
int cmp[10100];

void dfs(int v) {
    used[v] = true;
    rep(i, G[v].size()) {
        if (!used[G[v][i]]) dfs(G[v][i]);
    }
    vs.pb(v);
}

void rdfs(int v, int k) {
    used[v] = true;
    cmp[v] = k;
    rep(i, rG[v].size()) {
        if (!used[rG[v][i]]) rdfs(rG[v][i], k);
    }
}

int scc() {
    memset(used, 0, sizeof(used));
    vs.clear();
    rep(v, N) if (!used[v]) dfs(v);
    memset(used, 0, sizeof(used));
    int k = 0;
    for (int i=vs.size()-1; i>=0; i--) {
        if (!used[vs[i]]) rdfs(vs[i], k++);
    }
    return k;
}

int main() {
    cin.tie(0); ios::sync_with_stdio(false);
    cin >> N >> M;
    rep(i, M) {
        int s, t; cin >> s >> t;
        G[s].pb(t);
        rG[t].pb(s);
    }
    
    scc();
    int Q; cin >> Q;
    rep(i, Q) {
        int u, v; cin >> u >> v;
        if (cmp[u]==cmp[v]) cout << 1 << endl;
        else cout << 0 << endl;
    }
}
