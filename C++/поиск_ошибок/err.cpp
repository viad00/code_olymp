#include <iostream>
#include <graphics.h>
#include <conio.h>
#include <fstream>
#include <cstring>
#include <cctype>
#include <cstdio>
using namespace std;

int main() {
    ifstream f;
    ofstream d;
    f.open("input.txt");
    d.open("output.txt");
    int N, a[50], err=0, sum=0;
    double rest;
    f>>N;
    for (int i=1; i<=N; i++) {
        f>>a[i];
    }
    for (int i=1; i<=N; i++) {
        sum=sum+a[i];
    }
    rest=(double)sum/N;
    if (rest<=3.5) {
        d<<err; 
        f.close();
        d.close();
        return 0;         
    }
    int stop=1, j=1;
    while (stop) {
        a[j]=1;
        err++;
        sum=0;
    for (int i=1; i<=N; i++) {
        sum=sum+a[i];
    }
    rest=(double)sum/N;
    if (rest<=3.5) stop=0;
        j++;
    }
    d<<err;
    cout<<err<<endl;
    f.close();
    d.close();
    system ("pause");
    return 0;
}
