//
// Created by vlad on 30.06.17.
//

#include <iostream>
#include <cassert>

using namespace std;

int main() {
    assert(freopen("../5/A.txt", "r", stdin));
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int len;
        cin >> len;
        if (len > 437) {
            continue;
        } else {
            cout << "Crash " << ++i << "\n";
            return 0;
        }
    }
    cout << "No crash\n";
    return 0;
}
