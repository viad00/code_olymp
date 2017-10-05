//
// Created by vlad on 29.06.17.
//

#include <iostream>
#include <vector>
#include <cassert>

using namespace std;
const int MAXN = 1e6;
const int MAXLOG = 25;
vector<int> tree[MAXN];
int lel[MAXN];
int in[MAXN];
int out[MAXN];
int timer = 0;
int up[MAXN][MAXLOG];

bool is_anc(int a, int b) {
    return (in[a] <= in[b]) && (out[b] <= out[a]);
}

void add(int a, int p) {
    up[a][0] = p;
    for (int i = 1; i < MAXLOG; i++) up[a][i] = up[up[a][i - 1]][i - 1];
}

void dfs(int v, int p, int h) {
    lel[v] = h;
    in[v] = timer++;
    for (int u : tree[v]) {
        if (u == p) continue;
        add(u, v);
        dfs(u, v, h + 1);
    }
    out[v] = timer++;
}

int lca(int a, int b){
    if (is_anc(a, b)) return a;
    if (is_anc(b, a)) return b;
    for(int i = MAXLOG-1; i>=0; --i){
        int v = up[a][i];
        if (!is_anc(v, b)) a = v;
    }
    return up[a][0];
}

int main() {
    //assert(freopen("../4/B.txt", "r", stdin));
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int n, m;
    cin >> n;
    for (int i = 1; i < n; i++) {
        int pi, qi;
        cin >> pi >> qi;
        tree[--pi].push_back(--qi);
        tree[qi].push_back(pi);
    }
    cin >> m;
    dfs(0, -1, 0);
    for (int i = 0; i < m; i++) {
        int ai, bi;
        cin >> ai >> bi;
        ai--;
        bi--;
        cout << lca(ai, bi) + 1 << endl;
    }
    return 0;
}
