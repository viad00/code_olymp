#include <iostream>
#include <graphics.h>
#include <conio.h>
#include <fstream>
#include <cstring>
#include <cctype>
#include <cstdio>

using namespace std;

int main() {
    ifstream f; f.open("Strin.txt");
    ofstream d; d.open("Strout.txt");
    char s1[80]; int j, N;
    f>>N;
    for (j=0; j<=N; j++) {
    f.getline(s1, sizeof(s1));
    cout <<"Str "<<j<<" - "<<strlen(s1)<<" symbols\n";
    d <<"Str "<<j<<" - "<<strlen(s1)<<" symbols\n";
    }
    d<<'\0';
    f.close(); d.close();
    system ("pause");
    return 0;
}
