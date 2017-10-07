#include <algorithm>
#include <iostream>
#include <string>
#include <cmath>
#include <vector>

using namespace std;

void comb(unsigned int N, unsigned int K, unsigned int stp)
{
    string bitmask(K, 1);
    bitmask.resize((unsigned long)N, 0);
    unsigned int carl = 0;
    do {
        for (int i = 0; i < N; ++i)
        {
            if (bitmask[i]) { cout << " " << i; }
        }
        cout << endl;
        carl++;
    } while (prev_permutation(bitmask.begin(), bitmask.end()));
}

int compare(const void * x1, const void * x2)
{
    return ( *(int*)x1 - *(int*)x2 );
}

int main() {
    unsigned long long n, na;
    //cin >> n;
    for (na = 1; na < 101; na++) {
        n = na;
        cout << na << ':' << '\n';
    if(n==1){
        cout << 1;
        //return 0;
    }
    for (unsigned long long i = 2; i*i <= n; i++) {
        while (n % i == 0) {
            cout << i << ' ';
            n = n / i;
        }
    }
    if (n != 1) {
        cout << n << ' ';
    } cout << '\n'; }
    return 0;
}
