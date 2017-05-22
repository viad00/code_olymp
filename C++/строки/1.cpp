#include <iostream>
#include <cstring>
#include <cctype>
#include <cstdio>

using namespace std;

int main() {
    char s[80];
    cout <<"Введите:\n>";
    gets (s);
    int i=0;
    while (s[i]!='\0') {
        if (s[i]=='a') s[i]='b';
        else if (s[i]=='b') s[i]='a';
        if (s[i]=='A') s[i]='B';
        else if (s[i]=='B') s[i]='A';
        i++;
    }
    cout <<"Результат: "<<s<<endl;
    system ("pause");
    return 0;
}
