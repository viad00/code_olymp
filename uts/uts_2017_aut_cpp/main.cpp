#include <iostream>
#include <cmath>

using namespace std;

int compare(const void * x1, const void * x2)
{
    return ( *(int*)x1 - *(int*)x2 );
}

int main() {
    unsigned long long n, b, p;
    cin >> n >> b >> p;
    unsigned long long a[n];
    for (long i = 0; i < n; i++) {
        a[i] = (unsigned long long)pow(b, i+1) % p;
    }
    unsigned long long ma;
    unsigned long long mi;
    long lastclean;
    for (long j = 0; j < n-1; j++) {
        mi = 10000000000;
        ma = 0;
        for (long i = 0; i < n; i++) {
            bool change = false;
            if (a[i] >= ma && a[i] != 10000000000) {
                ma = a[i];
                change = true;
                lastclean = i;
            }
            if (a[i] <= mi && a[i] != 10000000000) {
                mi = a[i];
                change = true;
                lastclean = i;
            }
            if (change) {
                a[i] = 10000000000;
            }
        }
        a[lastclean] = (mi + ma) % p;
        cout << a[lastclean] << ' ';
    }
    //cout << '\n';
    //for (long i = 0; i < n; i++) {
    //    cout << a[i] << ' ';
    //}
    return 0;
}
