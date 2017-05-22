#include <iostream>
#include <cstring>
#include <cstdio>
#include <cctype>

using namespace std;

int main() {
    char s[80], j;
    int c[28], i;
    for (i='A'; i<='Z'; i++) {
        c[i]=0;
    }
    cout <<"¬ведите строку заканчивающуюс€ на точку:\n>";
    gets (s);
    i=0;
    while (s[i]!='.') {
          if ('a'<=s[i] && s[i]<='z') s[i]=toupper(s[i]);
          c[s[i]]=c[s[i]]+1;
          i++;
    }
    for (i='A'; i<='Z'; i++) {
        if (c[i]>0) {
                    j=i+32;
                    cout <<j<<"-"<<c[i]<<endl;
        }
    }
    system ("pause");
    return 0;
}
