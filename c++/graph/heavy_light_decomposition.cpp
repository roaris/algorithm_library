//https://atcoder.jp/contests/past202010-open/submissions/18410107
int N, Q;
vector<P> G[100010];
int rel[100010];

//辺の更新クエリの時はこれを実行
void dfs(int v, int pv) {
    rep(i, G[v].size()) {
        int serial = G[v][i].first;
        int nv = G[v][i].second;
        if (nv==pv) continue;
        rel[serial] = nv;
        dfs(nv, v);
    }
}

int par[100010], siz[100010], depth[100010];

int dfs1(int v, int pv, int d) {
    par[v] = pv;
    siz[v] = 1;
    depth[v] = d;
    rep(i, G[v].size()) {
        int nv = G[v][i].second;
        if (nv==pv) continue;
        siz[v] += dfs1(nv, v, d+1);
    }
    return siz[v];
}

int in_order[100010], top[100010];
int in_order_now;

void dfs2(int v, int pv, int top_node) {
    in_order[v] = in_order_now;
    in_order_now++;
    top[v] = top_node;
    if (siz[v]==1) return;
    int M = 0;
    int heavy_node = -1;
    rep(i, G[v].size()) {
        int nv = G[v][i].second;
        if (nv==pv) continue;
        if (siz[nv]>M) {
            M = siz[nv];
            heavy_node = nv;
        }
    }
    dfs2(heavy_node, v, top_node);
    rep(i, G[v].size()) {
        int nv = G[v][i].second;
        if (nv==pv) continue;
        if (nv!=heavy_node) dfs2(nv, v, nv);
    }
}

//辺の更新クエリの場合は、resの最後の区間だけ、左端を+1して扱う(LCAを更新しないようにするため)
vector<P> query(int u, int v) {
    vector<P> res;
    while (top[u]!=top[v]) {
        if (depth[top[u]]<=depth[top[v]]) {
            res.pb(P(in_order[top[v]], in_order[v]));
            v = par[top[v]];
        }
        else {
            res.pb(P(in_order[top[u]], in_order[u]));
            u = par[top[u]];
        }
    }
    res.pb(P(min(in_order[u], in_order[v]), max(in_order[u], in_order[v])));
    return res;
}