//O(n^2)
int shortest_cycle() {
    int res = 10000;
    rep(i, n) {
        vector<int> dist(n, -1);
        vector<int> par(n, -1);
        dist[i] = 0;
        queue<int> q;
        q.push(i);
        while (q.size()) {
            int v = q.front(); q.pop();
            rep(j, G[v].size()) {
                int nv = G[v][j];
                if (dist[nv]==-1) {
                    dist[nv] = dist[v]+1;
                    q.push(nv);
                    par[nv] = v;
                }
                else if (par[nv]!=v && par[v]!=nv) {
                    res = min(res, dist[v]+dist[nv]+1);
                }
            }
        }
    }
    return res;
}
