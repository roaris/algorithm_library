//ARC039 C
#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i=0; i<n; i++)
#define pb push_back
typedef pair<int, int> P;
typedef tuple<int, int, int> T;
map<char, int> dir = {make_pair('U', 0), make_pair('R', 1), make_pair('D', 2), make_pair('L', 3)};

struct dancinglinks {
    int dx[4] = {0, 1, 0, -1};
    int dy[4] = {1, 0, -1, 0};
    map<T, P> links;
    
    P query(int x, int y, int i) { //(x, y)から見てi方向にある未訪問の近傍点を返す
        return links[make_tuple(x, y, i)];
    }
    
    void update(int x, int y) { //(x, y)を訪問した時に実行
        rep(i, 4) { //ノード生成
            if (links.find(make_tuple(x, y, i))==links.end()) {
                links[make_tuple(x, y, i)] = P(x+dx[i], y+dy[i]);
            }
        }
        rep(i, 4) { //リンク張り替え
            P p = query(x, y, i);
            links[make_tuple(p.first, p.second, (2+i)%4)] = links[make_tuple(x, y, (2+i)%4)];
        }
    }
};

int main() {
    cin.tie(0); ios::sync_with_stdio(false);
    int K; cin >> K;
    string S; cin >> S;
    int x = 0, y = 0;
    dancinglinks dl;
    dl.update(x, y);
    
    rep(i, K) {
        P p = dl.query(x, y, dir[S[i]]);
        x = p.first, y = p.second;
        dl.update(x, y);
    }
    
    cout << x << " " << y << endl;
}
