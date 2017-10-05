#include <iostream>
#include <bits/stdc++.h>

using namespace std;
const int MAXN = 1e6;
vector<int> tree[MAXN];
int lel[MAXN];
int in[MAXN];
int out[MAXN];
int timer = 0;

bool is_anc(int a, int b) {
    return (in[a] <= in[b]) && (out[b] <= out[a]);
}

void dfs(int v, int p, int h) {
    lel[v] = h;
    in[v] = timer++;
    for (int u : tree[v]) {
        if (u == p) {
            continue;
        }
        dfs(u, v, h + 1);
    }
    out[v] = timer++;
}

int main() {
    //assert(freopen("../4/A.txt", "r", stdin));
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n, m, k;

    cin >> n >> m >> k;

    for (int i = 1; i < n; i++) {
        int v;
        cin >> v;
        tree[i].push_back(--v);
        tree[v].push_back(i);
    }

    dfs(0, -1, 0);

    for (int i = 0; i < m; i++) {
        int vi, ui;
        cin >> vi >> ui;
        --vi;
        --ui;

        if (!is_anc(vi, ui)){
            cout << "no\n";
            continue;
        }

        if (lel[ui] - lel[vi] > k) {
            cout << "no\n";
        } else {
            cout << "yes\n";
        }
    }
}
