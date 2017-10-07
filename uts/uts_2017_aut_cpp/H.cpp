
////////////////////////////////////////////////////////////////////////////////////////////////
// Andrey Odintsov
#include <bits/stdc++.h>
using namespace std;

#define mp make_pair
#define pb push_back
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(0)
#define FILE_IO(x) freopen((string(x) + ".in").c_str(), "r", stdin); freopen((string(x) + ".out").c_str(), "w", stdout)
#define sz(x) ((int)((x).size()))
#define len(x) ((int)((x).length()))
#define x first
#define y second
#define foreach(it, v) for (auto it : v)
#define rep(it, n) for (int it = 0; it < n; ++it)
#define forin(it, l, r) for (int it = l; it < r; ++it)
#define all(x) x.begin(), x.end()

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
const int INF = (1 << 31) - 1;
const ll LINF = (1ll << 63) - 1;
const double DINF = numeric_limits<double>::infinity();
const int MOD = 1e9 + 7;
const double EPS = 1e-7;
ll gcd(ll a, ll b) { return b ? gcd(b, a % b) : a; }
mt19937 mmtw(MOD);
ll rnd(ll x, ll y) { static uniform_int_distribution<ll> d; return d(mmtw) % (y - x + 1) + x; }
template <class T> T arr_max(T a[], int n) { T res = a[0]; for (int i = 1; i < n; ++i) if (a[i] > res) res = a[i]; return res; }
template <class T> T arr_min(T a[], int n) { T res = a[0]; for (int i = 1; i < n; ++i) if (a[i] < res) res = a[i]; return res; }
template <class T> T binpow(T n, T k) { if (k == 1) return n; if (k & 1) return binpow(n, k - 1) * n; T a = binpow(n, k / 2); return a * a; }
template <class T> T fact(T n) { if (n == 1) return 1; return n * fact(n - 1); }
////////////////////////////////////////////////////////////////////////////////////////////////

const int MAXN = 25;
ll n;
ll a[MAXN];
ll res;
vector <ll> not_used;

int main() {
    cin >> n;
    rep(i, n) {
        cin >> a[i];
    }

    if (n == 1) {
        cout << 1 << endl;
        return 0;
    }

    for (int i = 1; i <= n; ++i) {
        not_used.push_back(i);
    }

    ll size = fact(n - 1);
    rep(i, n) {
        auto it = find(all(not_used), a[i]);
        res += size * (it - not_used.begin());
        not_used.erase(it);
        if (i != n - 1) {
            size = size / (n - i - 1);
        }
    }

    cout << res + 1 << endl;
    return 0;
}