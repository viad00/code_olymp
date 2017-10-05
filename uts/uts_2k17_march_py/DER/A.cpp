#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;
#define MAXN 100007

int a[MAXN], tree[4 * MAXN], upd[4 * MAXN], n;

void build_tree(int v, int tl, int tr)
{
    if(tl == tr) tree[v] = a[tl];
    else
    {
        int tm = (tl + tr) >> 1;
        build_tree(v + v, tl, tm);
        build_tree(v + v + 1, tm + 1, tr);
        tree[v] = tree[v + v] + tree[v + v + 1];
    }
}

int query_tree(int v, int tl, int tr, int l, int r)
{
    if(l > r) return 0;
    if(upd[v] != -1) return upd[v] * (r - l + 1);
    if(l == tl && r == tr) return tree[v];
    int tm = (tl + tr) >> 1;
    return query_tree(v + v, tl, tm, l, min(r, tm)) + query_tree(v + v + 1, tm + 1, tr, max(l, tm + 1), r);
}

void update_tree(int v, int tl, int tr, int l, int r, int color)
{
    if(l > r) return;
    if(l == tl && tr == r)
    {
        upd[v] = color;
        tree[v] = color * (r - l + 1);
    }
    else
    {
        upd[v] = -1;
        int tm = (tl + tr) >> 1;
        update_tree(v + v, tl, tm, l, min(r, tm), color);
        update_tree(v + v + 1, tm + 1, tr, max(l, tm + 1), r, color);
        tree[v] = tree[v + v] + tree[v + v + 1];
    }
}

int main()
{
    ifstream cin("sum.in");
    ofstream cout("sum.out");
    int k;
    cin >> n >> k;
    for(int i = 0; i < 4 * MAXN; i++) upd[i] = -1; //Изначально все отрезки(вершины) не обновлены
    build_tree(1, 0, n-1);
    int q, x, l, r;
    char type;
    scanf("%d", &q);
    for(int i = 0; i < k; i++)
    {
        cin >> type;
        cin >> l;
        cin >> r;
        if(type == 'Q')
        {
            printf("%d\n", query_tree(1, 0, n - 1, l, r));
        }
        else if(type == 'A')
        {
            update_tree(1, 0, n - 1, l, l, r);
        }
    }

    return 0;
}
