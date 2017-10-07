
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
#define log(x) cout << #x << " = " << x << endl;

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
template <class T> T fact(T n) {if (n == 1) return 1; return n * fact(n - 1);}
////////////////////////////////////////////////////////////////////////////////////////////////

const int MAXN = 105;
ll n, k;
ll dp[MAXN][MAXN]; // dp[sum][first_digit]
vector <int> res;

int main() {
    cin >> n >> k;

    for (int i = 1; i < 105; ++i) { // sum
        for (int j = 1; j < i; ++j) { // first digit
            for (int k = j; k < 105; ++k) { // second digit
                dp[i][j] += dp[i - j][k];
            }
        }
        dp[i][i] = 1;
    }

    if (n == 0 && k != 0) {
        cout << "N/A" << endl;
        return 0;
    }

    ll sm = 0;
    for (int i = 1; i <= n; ++i) {
        sm += dp[n][i];
    }
    if (k >= sm && n != 0) {
        cout << "N/A" << endl;
        return 0;
    }

    ll last = 1;

    while (n) {
        for (int i = last; i <= n; ++i) {
            // cout << "dp[" << n << "][" << i << "] = " << dp[n][i] << endl;
            if (k < dp[n][i]) {
                n -= i;
                res.push_back(i);
                last = i;
                break;
            } else {
                k -= dp[n][i];
            }
        }
    }
    cout << sz(res) << endl;
    rep(i, sz(res)) {
        cout << res[i] << " ";
    }
    cout << endl;
    return 0;
}