#include <iostream>
#include <graphics.h>
#include <conio.h>
#include <fstream>
#include <cstring>
#include <cctype>
#include <cstdio>

using namespace std;

int main() {
    ifstream f; f.open("TEXT.txt");
    ofstream d; d.open("NEWTEXT.txt");
    char s1[80], s2[80]; int i, j, N, len, k=0;
    f>>N;
    for (j=0; j<=N; j++) {
    k=0;
    f.getline(s1, sizeof(s1));
    cout <<s1<<" - ";
    d<<s1<<" - ";
    //main code here:
    len=strlen(s1);
    for (i=len-1; i>=0; i--) {
        s2[k]=s1[i]; k++;
    }
    s2[k]='\0';
    if (strcmp(s2,s1)==0) {
         cout<<"Палиндром!"<<endl;
         d<<"Palindrom!"<<endl;
    } else {
        cout<<"Не палиндром!"<<endl;
        d<<"Ne palindrom!"<<endl;
    }
    //end of main code
    }
    d<<'\0';
    f.close(); d.close();
    system ("pause");
    return 0;
}
