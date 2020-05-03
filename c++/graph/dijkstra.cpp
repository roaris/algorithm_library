vector<int> dijkstra() {
    priority_queue<P, vector<P>, greater<P>> q;
    vector<int> d(N);
    rep(i, N) d[i] = 1000000000000000;
    d[0] = 0;
    q.push(P(0, 0));
    while (!q.empty()) {
        P p = q.top(); q.pop();
        int v = p.second;
        if (d[v]<p.first) continue;
        rep(i, G[v].size()) {
            int nv = G[v][i].first, w = G[v][i].second;
            if (d[nv]>d[v]+w) {
                d[nv] = d[v]+w;
                q.push(P(d[nv], nv));
            }
        }
    }
    return d;
}
