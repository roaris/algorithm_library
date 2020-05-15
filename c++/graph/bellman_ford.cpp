int bellman_ford() {
    rep(i, N) dist[i] = 1000000000000000;
    dist[0] = 0;
    rep(i, N) rep(j, M) {
        int a = get<0>(edges[j]), b = get<1>(edges[j]), c = get<2>(edges[j]);
        if (flag1[a] && flag2[b] && dist[b]>dist[a]+c) {
            dist[b] = dist[a]+c;
            if (i==N-1) return -1000000000000000;
        }
    }
    return dist[N-1];
}
