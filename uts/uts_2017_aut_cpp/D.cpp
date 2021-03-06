
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
template <class T> T binpow(T n, T k) {if (k == 1) return n; if (k & 1) return binpow(n, k - 1) * n; T a = binpow(n, k / 2); return a * a;}
////////////////////////////////////////////////////////////////////////////////////////////////

const int MAXN = 100;

ll n, k, bal;
ll dp[MAXN][MAXN];
string res;

int main() {
    cin >> n >> k;
    n *= 2;

    dp[0][0] = 1;
    for (int i = 1; i < 100; ++i) {
        for (int j = 1; j < 100; ++j) {
            dp[i][j] += dp[i - 1][j - 1];
        }
        for (int j = 0; j < 99; ++j) {
            dp[i][j] += dp[i - 1][j + 1];
        }
    }

    rep(i, n) {
        if (k < dp[n - i - 1][bal + 1]) {
            bal++;
            res.push_back('(');
        } else {
            k -= dp[n - i - 1][bal + 1];
            bal--;
            res.push_back(')');
        }
    }
    cout << res << endl;
    return 0;
}