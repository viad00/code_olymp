#include <iostream>

using namespace std;
//#define DEBUG
int main() {
#ifndef DEBUG
    freopen("count.in", "r", stdin);
    freopen("count.out", "w", stdout);
#else
    freopen("../count.in", "r", stdin);
#endif
    long long x[31][31];
    long long m = 0;
    long long n = 0;
    long long s = 0;
    for (int i = 0; i <= 31; i++) {
        for (int j = 0; i <= 31; i++) {
            x[i][j] = 0;
        }
    }
    for (int i = 0; i <= 30; i++) {
        x[1][i] = 1;
    }

    cin >> m >> n;

    for (int i = 2; i <= m; i++) {
        for (int j = 0; j <= n; j++) {
            for (int k = 0; k <= j; k++) {
                x[i][j] += x[i-1][k];
            }
        }
    }
    for (int i = 0; i <= n; i++) {
        s += x[m][i];
    }
    cout << s;
    fclose(stdout);
    return 0;
}
