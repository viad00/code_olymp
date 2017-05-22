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
        if (s[i]>='a' && s[i]<='z') s[i]=toupper(s[i]);
        else if (s[i]>='A' && s[i]<='Z') s[i]=tolower(s[i]);
        i++;
    }
    cout <<"Результат: "<<s<<endl;
    system ("pause");
    return 0;
}
